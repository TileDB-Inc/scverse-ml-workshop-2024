from click import argument
from tiledb.cloud.client import client
from tiledb.cloud.rest_api.api.array_api import ArrayApi
from tiledb.cloud.rest_api.models.array_info_update import ArrayInfoUpdate
from utz import decos

from . import cmd
from ..base import image_opt, region_opt, size_opt


def set_defaults(namespace, image, region, size, nb_name):
    """Set default image, region, and size for a notebook."""
    array_api = client.build(ArrayApi)

    array_api.update_array_metadata(
        namespace=namespace,
        array=nb_name,
        array_metadata=ArrayInfoUpdate(
            file_properties=dict(
                image=image,
                region=region,
                size=size,
            )
        )
    )


_set_defaults = decos(
    cmd('set-defaults', name='sd'),
    image_opt,
    region_opt,
    size_opt,
    argument('nb-name'),
)(set_defaults)
