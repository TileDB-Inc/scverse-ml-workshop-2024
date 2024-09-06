from click import argument
from tiledb import cloud
from utz import err

from . import cmd
from ..base import get_arrays, dry_run_opt


@cmd('delete')
@dry_run_opt
@argument('nb-names', nargs=-1)
def rm(namespace, dry_run, nb_names):
    """Delete a notebook from TileDB-Cloud, by namespace and name."""
    arrs1 = get_arrays(namespace)
    err("Arrays before deleting:")
    err('\t' + '\n\t'.join([ arr.name for arr in arrs1 ]))

    for arr in arrs1:
        if arr.name in nb_names:
            if dry_run:
                err(f"Would delete {arr.tiledb_uri}")
            else:
                err("Deleting", arr.tiledb_uri)
                cloud.array.delete_array(arr.tiledb_uri)

    if not dry_run:
        arrs2 = get_arrays(namespace)
        err("Arrays after deleting:")
        err('\t' + '\n\t'.join([ arr.name for arr in arrs2 ]))
