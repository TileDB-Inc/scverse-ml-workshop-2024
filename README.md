# scverse workshop

Scripts associated with the [Training models on atlas-scale single-cell datasets] workshop at [scverse Conference 2024].

## `scverse`: TileDB-Cloud CLI

### Install
```bash
git clone https://github.com/ryan-williams/scverse-workshop
pip install -e scverse-workshop
```

#### Auth
Put a TileDB-Cloud auth token in `.tiledb-cloud-token`, and it will be picked up automatically by the CLI commands below.

### `scverse nb`: Upload, list, and delete notebooks
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
#   delete (rm)   Delete a notebook from TileDB-Cloud, by namespace and name.
#   list (ls)     Delete a notebook from TileDB-Cloud, by namespace and name.
#   upload (put)  Upload a notebook to TileDB-Cloud.
```

<details><summary><code>scverse nb put</code></summary>

```
Usage: scverse nb put [OPTIONS] SRC

  Upload a notebook to TileDB-Cloud.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token
  -c, --credential-name TEXT   Storage credential name; default: rw-test
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  -d, --delete                 If True, delete the notebook after uploading
  -n, --dst-name TEXT          Destination notebook name
  --help                       Show this message and exit.
```
</details>

<details><summary><code>scverse nb ls</code></summary>

```
Usage: scverse nb ls [OPTIONS]

  List TileDB-Cloud notebooks.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  --help                       Show this message and exit.
```
</details>

<details><summary><code>scverse nb rm</code></summary>

```
Usage: scverse nb rm [OPTIONS] NB_NAME

  Delete a notebook from TileDB-Cloud, by namespace and name.

Options:
  -t, --cloud-token-path TEXT  Path to file containing TileDB-Cloud auth
                               token; default: .tiledb-cloud-token
  -N, --namespace TEXT         TileDB-Cloud namespace to work in; default:
                               scverse-ml-workshop-2024
  --help                       Show this message and exit.
```
</details>

## Related tutorials
See [examples/](examples/):
- [pytorch.ipynb]: copy of [Training a PyTorch Model][pytorch.html] (CELLxGENE Census tutorial)
- [cshl.ipynb]: copy of [CELLxGENE Discover Census Workshop - CSHL Single-Cell Analysis 2023][cshl-2023]


[Training models on atlas-scale single-cell datasets]: https://cfp.scverse.org/2024/talk/GQHNYE/
[schedule]: https://scverse.org/conference2024/schedule#2024-09-12
[scverse Conference 2024]: https://scverse.org/conference2024
[pytorch.ipynb]: examples/pytorch.ipynb
[pytorch.html]: https://chanzuckerberg.github.io/cellxgene-census/notebooks/experimental/pytorch.html
[cshl.ipynb]: examples/cshl.ipynb
[Papermill]: https://papermill.readthedocs.io/en/latest/
[cshl-2023]: https://colab.research.google.com/drive/1QgZQRF_ZM9q5oKbynnD9ToklVFdui7pq
