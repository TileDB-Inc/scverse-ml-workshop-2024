from click import argument
from tiledb import cloud
from utz import err

from .command import command
from ..base import get_arrays


@command('rm')
@argument('nb-name')
def delete(namespace, nb_name):
    """Delete a notebook from TileDB-Cloud, by namespace and name."""
    arrs1 = get_arrays(namespace)
    err("Arrays before deleting:")
    err('\t' + '\n\t'.join([ arr.name for arr in arrs1 ]))
    [arr] = [arr for arr in arrs1 if arr.name == nb_name]

    cloud.array.delete_array(arr.tiledb_uri)
    arrs2 = get_arrays(namespace)
    err("Arrays after deleting:")
    err('\t' + '\n\t'.join([ arr.name for arr in arrs2 ]))
