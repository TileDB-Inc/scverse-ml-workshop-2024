from . import cmd
from ..base import get_arrays


@cmd('list', no_args_is_help=False)
def ls(namespace):
    """List TileDB-Cloud notebooks."""
    arrs = get_arrays(namespace)
    print('\n'.join([ arr.name for arr in arrs ]))
