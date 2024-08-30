from click import group, option
from tiledb.cloud import client


@group
def cli():
    """TileDB-Cloud CLI for the scverse project."""
    pass


NAMESPACE = 'scverse-ml-workshop-2024'
DEFAULT_CREDENTIAL_NAME = 'rw-test'
DEFAULT_CLOUD_TOKEN_PATH = '.tiledb-cloud-token'


credential_opt = option('-c', '--credential-name', default=DEFAULT_CREDENTIAL_NAME, help=f'Storage credential name; default: {DEFAULT_CREDENTIAL_NAME}')
namespace_opt = option('-N', '--namespace', default=NAMESPACE, help=f'TileDB-Cloud namespace to work in; default: {NAMESPACE}')
cloud_token_opt = option('-t', '--cloud-token-path', default=DEFAULT_CLOUD_TOKEN_PATH, help=f'Path to file containing TileDB-Cloud auth token; default: {DEFAULT_CLOUD_TOKEN_PATH}')


def get_arrays(namespace: str):
    return client.list_arrays(namespace=namespace).arrays

