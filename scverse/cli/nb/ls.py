from .command import command
from ..base import get_arrays


@command('ls', name='list')
def ls(namespace):
    """List TileDB-Cloud notebooks."""
    arrs = get_arrays(namespace)
    print('\n'.join([ arr.name for arr in arrs ]))
