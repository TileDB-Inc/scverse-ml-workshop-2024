from os import getenv
from typing import Optional

from functools import wraps
from inspect import getfullargspec
from tiledb import cloud
from utz import decos

from .aliased_group import AliasedGroup
from .base import cloud_token_opt, credential_opt, namespace_opt


def _get_token(
    cloud_token_path: str= ".tiledb-cloud-token",
    env_var: str = "TILEDB_REST_TOKEN",
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
            token = _get_token(cloud_token_path)
            cloud.login(token=token)
            return fn(**{ k: v for k, v in kwargs.items() if k in spec.args })

        for alias in aliases:
            if alias in parent.aliases:
                raise ValueError(f'Alias already in use: {alias} -> {parent.aliases[alias]}; refusing to overwrite with {_fn.name}')
            parent.aliases[alias] = _fn.name
        return _fn

    return _command