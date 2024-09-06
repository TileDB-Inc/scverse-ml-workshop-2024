# scverse-ml-workshop-2024

Scripts/Notebooks associated with the [Training models on atlas-scale single-cell datasets] workshop at [scverse Conference 2024].

## `scverse`: TileDB-Cloud CLI

### Install
```bash
git clone https://github.com/ryan-williams/scverse-workshop
pip install -e scverse-workshop
```

<!-- `bmdf scverse` -->
```bash
scverse
# Usage: scverse [OPTIONS] COMMAND [ARGS]...
#
#   TileDB-Cloud CLI for the scverse project.
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   invite  Create/List invitations to a TileDB-Cloud namespace.
#   nb      Notebook-CRUD TileDB-Cloud commands for the...
#   org     Manage a TileDB-Cloud organization / namespace.
```

#### Auth
Put a TileDB-Cloud auth token in `.tiledb-cloud-token`, and it will be picked up automatically by the CLI commands below.

### `scverse org`: Show organization/user info
<!-- `bmdf scverse org` -->
```bash
scverse org
# Usage: scverse org [OPTIONS] COMMAND [ARGS]...
#
#   Manage a TileDB-Cloud organization / namespace.
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   show (info)  Print a TileDB-Cloud organization.
#   user         Show a TileDB-Cloud user.
#   users        List users in a TileDB-Cloud organization.
```

<!-- `bmdfff -- scverse org show --help` -->
<details><summary><code>scverse org show --help</code></summary>

```
Usage: scverse org show [OPTIONS]

  Print a TileDB-Cloud organization.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse org users --help` -->
<details><summary><code>scverse org users --help</code></summary>

```
Usage: scverse org users [OPTIONS]

  List users in a TileDB-Cloud organization.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  -C, --compact                Print compact JSON
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse org user --help` -->
<details><summary><code>scverse org user --help</code></summary>

```
Usage: scverse org user [OPTIONS] [USERNAME]

  Show a TileDB-Cloud user.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -C, --compact                Print compact JSON
  --help                       Show this message and exit.
```
</details>

### `scverse invite`: Send/List/Revoke TileDB-Cloud workspace invitations
<!-- `bmdf scverse invite` -->
```bash
scverse invite
# Usage: scverse invite [OPTIONS] COMMAND [ARGS]...
#
#   Create/List invitations to a TileDB-Cloud namespace.
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   do (send)  Invite a user to a TileDB-Cloud namespace
#   ls (list)  List a TileDB-Cloud namespace's outstanding invitations
#   rm         Revoke one or more outstanding invitations to a TileDB-Cloud
#              namespace
```

<!-- `bmdfff -- scverse invite send --help` -->
<details><summary><code>scverse invite send --help</code></summary>

```
Usage: scverse invite send [OPTIONS] [EMAILS]...

  Invite a user to a TileDB-Cloud namespace

Options:
  -t, --cloud-token-path TEXT     Path to file containing TileDB-Cloud auth
                                  token; default: .tiledb-cloud-token.
                                  $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT            TileDB-Cloud namespace to work in; default:
                                  scverse-ml-workshop-2024
  -r, --role [owner|admin|read_write|read_only]
                                  Role to invite new user as (options:
                                  ['owner', 'admin', 'read_write',
                                  'read_only']; default: read_write)
  --help                          Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse invite list --help` -->
<details><summary><code>scverse invite list --help</code></summary>

```
Usage: scverse invite list [OPTIONS]

  List a TileDB-Cloud namespace's outstanding invitations

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  -C, --compact                Print compact JSON
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse invite rm --help` -->
<details><summary><code>scverse invite rm --help</code></summary>

```
Usage: scverse invite rm [OPTIONS] [EMAILS]...

  Revoke one or more outstanding invitations to a TileDB-Cloud namespace

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  -n, --dry-run                Print commands that would be run, but don't run
                               them
  -S, --no-strict              Raise and exit if any email is not found,
                               without revoking any invites
  --help                       Show this message and exit.
```
</details>

### `scverse nb`: Upload, list, and delete notebooks
<!-- `bmdf scverse nb` -->
```bash
scverse nb
# Usage: scverse nb [OPTIONS] COMMAND [ARGS]...
#
#   Notebook-CRUD TileDB-Cloud commands for the `scverse-ml-workshop-2024`
#   namespace.
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   cp (copy)       Create copies of a "template" notebook, with names
#                   corresponding...
#   get (download)  Download a TileDB-Cloud notebook; [DST] of "-" prints to
#                   stdout.
#   ls (list)       List TileDB-Cloud notebooks.
#   put (upload)    Upload a notebook to TileDB-Cloud.
#   rm (delete)     Delete a notebook from TileDB-Cloud, by namespace and name.
```

<!-- `bmdfff -- scverse nb ls --help` -->
<details><summary><code>scverse nb ls --help</code></summary>

```
Usage: scverse nb ls [OPTIONS]

  List TileDB-Cloud notebooks.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse nb cp --help` -->
<details><summary><code>scverse nb cp --help</code></summary>

```
Usage: scverse nb cp [OPTIONS] [EMAILS]...

  Create copies of a "template" notebook, with names corresponding to provided
  email addresses.

Options:
  -t, --cloud-token-path TEXT   Path to file containing TileDB-Cloud auth
                                token; default: .tiledb-cloud-token.
                                $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT          TileDB-Cloud namespace to work in; default:
                                scverse-ml-workshop-2024
  -n, --dry-run                 Print commands that would be run, but don't
                                run them
  -s, --src-notebook-name TEXT  "Read-only" notebook name, to be copied and
                                renamed for each user.
  --help                        Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse nb get --help` -->
<details><summary><code>scverse nb get --help</code></summary>

```
Usage: scverse nb get [OPTIONS] NB_NAME [DST]

  Download a TileDB-Cloud notebook; [DST] of "-" prints to stdout.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff scverse nb put` -->
<details><summary><code>scverse nb put</code></summary>

```
Usage: scverse nb put [OPTIONS] SRC [DST_NAME]

  Upload a notebook to TileDB-Cloud.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -c, --credential-name TEXT   Storage credential name; default: scverse-ml-
                               workshop-2024
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  -S, --storage-path TEXT      Storage path; default: s3://tiledb-conferences-
                               us-west-2/scverse-ml-workshop-2024
  -d, --delete                 If True, delete the notebook after uploading
                               (e.g. for testing uploading/deleting)
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff scverse nb rm` -->
<details><summary><code>scverse nb rm</code></summary>

```
Usage: scverse nb rm [OPTIONS] [NB_NAMES]...

  Delete a notebook from TileDB-Cloud, by namespace and name.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token.
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  -n, --dry-run                Print commands that would be run, but don't run
                               them
  --help                       Show this message and exit.
```
</details>

## Example notebooks/tutorials
See [examples/](examples/):
- [pytorch.ipynb]: copy of [Training a PyTorch Model][pytorch.html] (CELLxGENE Census tutorial)
- [cshl.ipynb]: copy of [CELLxGENE Discover Census Workshop - CSHL Single-Cell Analysis 2023][cshl-2023] (Python)
- [cshl-R.ipynb]: copy of [CELLxGENE Discover Census Workshop - CSHL Single-Cell Analysis 2023][cshl-2023 R] (R)


[Training models on atlas-scale single-cell datasets]: https://cfp.scverse.org/2024/talk/GQHNYE/
[schedule]: https://scverse.org/conference2024/schedule#2024-09-12
[scverse Conference 2024]: https://scverse.org/conference2024
[pytorch.ipynb]: examples/pytorch.ipynb
[pytorch.html]: https://chanzuckerberg.github.io/cellxgene-census/notebooks/experimental/pytorch.html
[cshl.ipynb]: examples/cshl.ipynb
[cshl-R.ipynb]: examples/cshl-R.ipynb
[Papermill]: https://papermill.readthedocs.io/en/latest/
[cshl-2023]: https://colab.research.google.com/drive/1QgZQRF_ZM9q5oKbynnD9ToklVFdui7pq
[cshl-2023 R]: https://colab.research.google.com/drive/158f6Ggl5MRxtnxC9Q01TjJMbkIPQxcim
