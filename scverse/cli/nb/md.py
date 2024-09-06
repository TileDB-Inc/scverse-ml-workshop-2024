from click import argument
from tiledb.cloud.client import client
from tiledb.cloud.rest_api.api.array_api import ArrayApi

from . import cmd
from ..command import json_output


@cmd('metadata')
@argument('nb-name')
@json_output
def md(namespace, nb_name):
    """Show a TileDB-Cloud notebook's metadata."""
    api = client.build(ArrayApi)
    response = api.get_array_metadata(namespace, nb_name)
    return response.to_dict()
