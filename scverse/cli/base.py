from click import group, option, Choice
from tiledb.cloud import client
from tiledb.cloud.rest_api import OrganizationRoles


@group
def cli():
    """TileDB-Cloud CLI for the scverse project."""
    pass


NAMESPACE = 'scverse-ml-workshop-2024'
PARTICIPANTS_NB_DIR = "participants"
DEFAULT_IMAGE = 'genomics'  # TODO
DEFAULT_REGION = 'us-west-2'
DEFAULT_STORAGE_PATH = 's3://tiledb-conferences-us-west-2/scverse-ml-workshop-2024'
DEFAULT_CREDENTIAL_NAME = 'scverse-ml-workshop-2024'
DEFAULT_CLOUD_TOKEN_PATH = '.tiledb-cloud-token'
TILEDB_REST_TOKEN_VAR = 'TILEDB_REST_TOKEN'
TEMPLATE_NAME = 'instructor_scverse-ml-workshop-2024'  # "Read-only" notebook, to be copied and renamed for each user.
DEFAULT_SERVER_SIZE = 'large'  # TODO

READ_WRITE = OrganizationRoles.READ_WRITE
ROLES = OrganizationRoles.allowable_values

credential_opt = option('-c', '--credential-name', default=DEFAULT_CREDENTIAL_NAME, help=f'Storage credential name; default: "{DEFAULT_CREDENTIAL_NAME}"')
compact_opt = option('-C', '--compact', is_flag=True, help="Print compact JSON")
image_opt = option('-i', '--image', default=DEFAULT_IMAGE, help='Default image')
dry_run_opt = option('-n', '--dry-run', is_flag=True, help="Print commands that would be run, but don't run them")
namespace_opt = option('-N', '--namespace', default=NAMESPACE, help=f'TileDB-Cloud namespace to work in; default: "{NAMESPACE}"')
cloud_token_opt = option('-t', '--cloud-token-path', default=DEFAULT_CLOUD_TOKEN_PATH, help=f'Path to file containing TileDB-Cloud auth token; default: "{DEFAULT_CLOUD_TOKEN_PATH}". ${TILEDB_REST_TOKEN_VAR} takes precedence, if set.')
storage_path_opt = option('-S', '--storage-path', default=DEFAULT_STORAGE_PATH, help=f'Storage path; default: "{DEFAULT_STORAGE_PATH}"')
region_opt = option('-r', '--region', default=DEFAULT_REGION, help='Default region')
role_opt = option('-R', '--role', type=Choice(ROLES), default=READ_WRITE, help=f'Role to invite new user as (options: {ROLES}; default: "{READ_WRITE}")')
src_nb_opt = option('-s', '--src-notebook-name', default=TEMPLATE_NAME, help=f'"Read-only" notebook name, to be copied and renamed for each user (default: "{TEMPLATE_NAME}").')
size_opt = option('-z', '--size', default=DEFAULT_SERVER_SIZE, help='Default server size')


def get_arrays(namespace: str, per_page: int = 100):
    return client.list_arrays(namespace=namespace, per_page=per_page).arrays
