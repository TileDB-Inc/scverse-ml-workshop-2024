import json
from os import getenv

from click import get_current_context
from typing import Optional

from functools import wraps
from inspect import getfullargspec, signature
from tiledb import cloud
from utz import decos

from .aliased_group import AliasedGroup
from .base import cloud_token_opt, credential_opt, namespace_opt, DEFAULT_CLOUD_TOKEN_PATH, TILEDB_REST_TOKEN_VAR, \
    storage_path_opt, compact_opt
from ..util.json import DateTimeEncoder


def _get_token(
    cloud_token_path: str = DEFAULT_CLOUD_TOKEN_PATH,
    env_var: str = TILEDB_REST_TOKEN_VAR,
) -> str:
    """Get a TileDB Cloud API token.
    
    Prioritizes a dotfile.
    Args:
        cloud_token_path:
            Path to dotfile having API token
        env_var:
            Environment variable key name.
    
    Returns:
        TileDB Cloud API token.
    """
    
    try: 
        with open(cloud_token_path, 'r') as f:
            token = f.read().strip()
    except FileNotFoundError:
        token = getenv(env_var)
        if not token:
            raise ValueError(f"No token specified in {cloud_token_path} or ${env_var}.")

    return token


def command(
    parent: AliasedGroup,
    *aliases: str,
    name: Optional[str] = None,
    no_args_is_help: bool = True,
    **kwargs
):
    """Define a subcommand of a ``parent`` group, add namespace and credential-parsing options."""
    def _command(fn):
        spec = getfullargspec(fn)
        args = spec.args

        @parent.command(name=name or fn.__name__, no_args_is_help=no_args_is_help, **kwargs)
        @cloud_token_opt
        @decos([
            *([credential_opt] if 'credential_name' in args else []),
            *([namespace_opt] if 'namespace' in args else []),
            *([storage_path_opt] if 'storage_path' in args else []),
        ])
        @wraps(fn)
        def _fn(cloud_token_path, **kwargs):
            token = _get_token(cloud_token_path)
            cloud.login(token=token)
            return fn(**{ k: v for k, v in kwargs.items() if k in args or k in getattr(fn, 'include_kwargs', []) })

        for alias in aliases:
            if alias in parent.aliases:
                raise ValueError(f'Alias already in use: {alias} -> {parent.aliases[alias]}; refusing to overwrite with {_fn.name}')
            parent.aliases[alias] = _fn.name
        return _fn

    return _command


def json_output(f):
    """Wrap a function to take a ``-C/--compact`` option, and print its return value as JSON.

    Also registers ``DateTimeEncoder`` during JSON serialization.
    """
    @compact_opt
    @wraps(f)
    def wrapper(*args, compact, **kwargs):
        response = f(*args, **kwargs)
        json_kwargs = dict(cls=DateTimeEncoder)
        if not compact:
            json_kwargs.update(indent=2)

        print(json.dumps(response, **json_kwargs))

    wrapper.__signature__ = signature(f)
    wrapper.include_kwargs = ['compact']
    return wrapper
