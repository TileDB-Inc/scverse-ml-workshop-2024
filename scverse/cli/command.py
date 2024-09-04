from os.path import exists

from functools import wraps
from inspect import getfullargspec
from tiledb import cloud
from utz import decos

from .aliased_group import AliasedGroup
from .base import cloud_token_opt, credential_opt, namespace_opt


def command(
    parent: AliasedGroup,
    *aliases: str,
    name: str | None = None,
    no_args_is_help: bool = True,
    **kwargs
):
    def _command(fn):
        spec = getfullargspec(fn)

        @parent.command(name=name or fn.__name__, no_args_is_help=no_args_is_help, **kwargs)
        @cloud_token_opt
        @decos([
            *([credential_opt] if 'credential_name' in spec.args else []),
            *([namespace_opt] if 'namespace' in spec.args else []),
        ])
        @wraps(fn)
        def _fn(cloud_token_path, **kwargs):
            if not exists(cloud_token_path):
                raise ValueError(f'Cloud token file not found: {cloud_token_path}')
            with open(cloud_token_path, 'r') as f:
                token = f.read().strip()
            cloud.login(token=token)
            return fn(**{ k: v for k, v in kwargs.items() if k in spec.args })

        for alias in aliases:
            if alias in parent.aliases:
                raise ValueError(f'Alias already in use: {alias} -> {parent.aliases[alias]}; refusing to overwrite with {_fn.name}')
            parent.aliases[alias] = _fn.name
        return _fn

    return _command
