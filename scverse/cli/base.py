from click import group, option
from tiledb.cloud import client


@group
def cli():
    """TileDB-Cloud CLI for the scverse project."""
    pass


NAMESPACE = 'scverse-ml-workshop-2024'
DEFAULT_CREDENTIAL_NAME = 'scverse-ml-workshop-2024'
DEFAULT_CLOUD_TOKEN_PATH = '.tiledb-cloud-token'
TILEDB_REST_TOKEN_VAR = 'TILEDB_REST_TOKEN'


credential_opt = option('-c', '--credential-name', default=DEFAULT_CREDENTIAL_NAME, help=f'Storage credential name; default: {DEFAULT_CREDENTIAL_NAME}')
compact_opt = option('-C', '--compact', is_flag=True, help="Print compact JSON")
dry_run_opt = option('-n', '--dry-run', is_flag=True, help="Print commands that would be run, but don't run them")
namespace_opt = option('-N', '--namespace', default=NAMESPACE, help=f'TileDB-Cloud namespace to work in; default: {NAMESPACE}')
cloud_token_opt = option('-t', '--cloud-token-path', default=DEFAULT_CLOUD_TOKEN_PATH, help=f'Path to file containing TileDB-Cloud auth token; default: {DEFAULT_CLOUD_TOKEN_PATH}. ${TILEDB_REST_TOKEN_VAR} takes precedence, if set.')


def get_arrays(namespace: str):
    return client.list_arrays(namespace=namespace).arrays

