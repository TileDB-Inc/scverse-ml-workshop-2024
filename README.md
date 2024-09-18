# Training models on atlas-scale single-cell datasets

Workshop at [scverse Conference 2024]:

- **Conference page:** [Training models on atlas-scale single-cell datasets]
- **Slides:** [Google Slides][slides], [PDF]
- **Notebook:** [workshop.ipynb] is synced to the TileDB-Cloud namespace, and a copy created for each workshop participant (by [GitHub Action]).

[![](img/title-slide.png)][slides]

---

## `scverse`: TileDB-Cloud CLI
We used this command-line tool to manage signups to the TileDB-Cloud namespace where live notebooks were hosted during the workshop, especially `scverse user add [emails...]` which:
- Invites a user to the TileDB-Cloud namespace used in the workshop (`scverse invite send [emails...]`)
- Creates a copy of [workshop.ipynb] in the namespace, renamed after the user's email address (`scverse nb cp [emails...]`)
- Sets relevant defaults on their copy of the notebook ("Genomics" image, "Large" size, "us-west-2" region; `scverse nb set-defaults [notebook names...]`)

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
#   user    Manage a scverse TileDB-Cloud user.
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
```

<!-- `bmdfff -- scverse org show --help` -->
<details><summary><code>scverse org show --help</code></summary>

```
Usage: scverse org show [OPTIONS]

  Print a TileDB-Cloud organization.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
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
#   do (send)  Invite a user to a TileDB-Cloud namespace.
#   ls (list)  List a TileDB-Cloud namespace's outstanding invitations
#   rm         Revoke one or more outstanding invitations to a TileDB-Cloud
#              namespace
```

<!-- `bmdfff -- scverse invite send --help` -->
<details><summary><code>scverse invite send --help</code></summary>

```
Usage: scverse invite send [OPTIONS] [EMAILS]...

  Invite a user to a TileDB-Cloud namespace.

Options:
  -t, --cloud-token-path TEXT     Path to file containing TileDB-Cloud auth
                                  token; default: ".tiledb-cloud-token".
                                  $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT            TileDB-Cloud namespace to work in; default:
                                  "scverse-ml-workshop-2024"
  -R, --role [owner|admin|read_write|read_only]
                                  Role to invite new user as (options:
                                  ['owner', 'admin', 'read_write',
                                  'read_only']; default: "read_write")
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
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
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
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
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
#   cp (copy)          Create one or more copies of a "template" notebook, with
#                      names...
#   get (download)     Download a TileDB-Cloud notebook; [DST] of "-" prints to
#                      stdout.
#   ls (list)          List TileDB-Cloud notebooks.
#   md (metadata)      Show a TileDB-Cloud notebook's metadata.
#   put (upload)       Upload a notebook to TileDB-Cloud.
#   rm (delete)        Delete a notebook from TileDB-Cloud, by namespace and
#                      name.
#   sd (set-defaults)  Set default image, region, and size for a notebook.
```

<!-- `bmdfff -- scverse nb ls --help` -->
<details><summary><code>scverse nb ls --help</code></summary>

```
Usage: scverse nb ls [OPTIONS]

  List TileDB-Cloud notebooks.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse nb cp` -->
<details><summary><code>scverse nb cp</code></summary>

```
Usage: scverse nb cp [OPTIONS] [EMAILS]...

  Create one or more copies of a "template" notebook, with names corresponding
  to provided email addresses.

Options:
  -t, --cloud-token-path TEXT   Path to file containing TileDB-Cloud auth
                                token; default: ".tiledb-cloud-token".
                                $TILEDB_REST_TOKEN takes precedence, if set.
  -c, --credential-name TEXT    Storage credential name; default: "scverse-ml-
                                workshop-2024"
  -N, --namespace TEXT          TileDB-Cloud namespace to work in; default:
                                "scverse-ml-workshop-2024"
  -n, --dry-run                 Print commands that would be run, but don't
                                run them
  -s, --src-notebook-name TEXT  "Read-only" notebook name, to be copied and
                                renamed for each user (default:
                                "instructor_scverse-ml-workshop-2024").
  --help                        Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse nb get` -->
<details><summary><code>scverse nb get</code></summary>

```
Usage: scverse nb get [OPTIONS] NB_NAME [DST]

  Download a TileDB-Cloud notebook; [DST] of "-" prints to stdout.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse nb md` -->
<details><summary><code>scverse nb md</code></summary>

```
Usage: scverse nb md [OPTIONS] NB_NAME

  Show a TileDB-Cloud notebook's metadata.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
  -C, --compact                Print compact JSON
  --help                       Show this message and exit.
```
</details>

<!-- `bmdfff -- scverse nb sd` -->
<details><summary><code>scverse nb sd</code></summary>

```
Usage: scverse nb sd [OPTIONS] NB_NAME

  Set default image, region, and size for a notebook.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
  -i, --image TEXT             Default image
  -r, --region TEXT            Default region
  -z, --size TEXT              Default server size
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
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -c, --credential-name TEXT   Storage credential name; default: "scverse-ml-
                               workshop-2024"
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
  -S, --storage-path TEXT      Storage path; default: "s3://tiledb-
                               conferences-us-west-2/scverse-ml-workshop-2024"
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
                               token; default: ".tiledb-cloud-token".
                               $TILEDB_REST_TOKEN takes precedence, if set.
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               "scverse-ml-workshop-2024"
  -n, --dry-run                Print commands that would be run, but don't run
                               them
  --help                       Show this message and exit.
```
</details>

### `scverse user`: Add/Show/List organization users
<!-- `bmdf scverse user` -->
```bash
scverse user
# Usage: scverse user [OPTIONS] COMMAND [ARGS]...
#
#   Manage a scverse TileDB-Cloud user.
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   add   Add and initialize (notebook copy + defaults) one or more users...
#   ls    List users in a TileDB-Cloud organization.
#   show  Show a TileDB-Cloud user.
```

<!-- `bmdf -- scverse user show --help` -->
```bash
scverse user show --help
# Usage: scverse user show [OPTIONS] [USERNAME]
#
#   Show a TileDB-Cloud user.
#
# Options:
#   -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
#                                token; default: ".tiledb-cloud-token".
#                                $TILEDB_REST_TOKEN takes precedence, if set.
#   -C, --compact                Print compact JSON
#   --help                       Show this message and exit.
```

<!-- `bmdf -- scverse user ls --help` -->
```bash
scverse user ls --help
# Usage: scverse user ls [OPTIONS]
#
#   List users in a TileDB-Cloud organization.
#
# Options:
#   -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
#                                token; default: ".tiledb-cloud-token".
#                                $TILEDB_REST_TOKEN takes precedence, if set.
#   -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
#                                "scverse-ml-workshop-2024"
#   -C, --compact                Print compact JSON
#   --help                       Show this message and exit.
```

<!-- `bmdf scverse user add` -->
```bash
scverse user add
# Usage: scverse user add [OPTIONS] [EMAILS]...
#
#   Add and initialize (notebook copy + defaults) one or more users to a TileDB-
#   Cloud namespace.
#
# Options:
#   -t, --cloud-token-path TEXT     Path to file containing TileDB-Cloud auth
#                                   token; default: ".tiledb-cloud-token".
#                                   $TILEDB_REST_TOKEN takes precedence, if set.
#   -c, --credential-name TEXT      Storage credential name; default: "scverse-
#                                   ml-workshop-2024"
#   -N, --namespace TEXT            TileDB-Cloud namespace to work in; default:
#                                   "scverse-ml-workshop-2024"
#   -R, --role [owner|admin|read_write|read_only]
#                                   Role to invite new user as (options:
#                                   ['owner', 'admin', 'read_write',
#                                   'read_only']; default: "read_write")
#   -s, --src-notebook-name TEXT    "Read-only" notebook name, to be copied and
#                                   renamed for each user (default:
#                                   "instructor_scverse-ml-workshop-2024").
#   -i, --image TEXT                Default image
#   -r, --region TEXT               Default region
#   -z, --size TEXT                 Default server size
#   --help                          Show this message and exit.
```

## Example notebooks/tutorials
See [examples/](examples/):
- [pytorch.ipynb]: copy of [Training a PyTorch Model][pytorch.html] (CELLxGENE Census tutorial)
- [cshl.ipynb]: copy of [CELLxGENE Discover Census Workshop - CSHL Single-Cell Analysis 2023][cshl-2023] (Python)
- [cshl-R.ipynb]: copy of [CELLxGENE Discover Census Workshop - CSHL Single-Cell Analysis 2023][cshl-2023 R] (R)


[Training models on atlas-scale single-cell datasets]: https://cfp.scverse.org/2024/talk/GQHNYE/
[scverse Conference 2024]: https://scverse.org/conference2024
[slides]: https://docs.google.com/presentation/d/1VnAKyOUUdzTZkgcYjoavtDU5_drFu5flC5oG6I7RnP0/edit
[PDF]: census-tiledb-atlas-scale-models_r1.pdf
[workshop.ipynb]: workshop.ipynb
[pytorch.ipynb]: examples/pytorch.ipynb
[pytorch.html]: https://chanzuckerberg.github.io/cellxgene-census/notebooks/experimental/pytorch.html
[cshl.ipynb]: examples/cshl.ipynb
[cshl-R.ipynb]: examples/cshl-R.ipynb
[Papermill]: https://papermill.readthedocs.io/en/latest/
[cshl-2023]: https://colab.research.google.com/drive/1QgZQRF_ZM9q5oKbynnD9ToklVFdui7pq
[cshl-2023 R]: https://colab.research.google.com/drive/158f6Ggl5MRxtnxC9Q01TjJMbkIPQxcim
[GitHub Action]: .github/workflows/cp-template.yml
