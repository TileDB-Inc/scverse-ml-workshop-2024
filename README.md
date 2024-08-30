# scverse workshop

Scripts associated with the [Training models on atlas-scale single-cell datasets] workshop at [scverse Conference 2024].

## TileDB-Cloud CLI
Install `scverse` CLI:
```bash
git clone https://github.com/ryan-williams/scverse-workshop
pip install -e scverse-workshop
```

### Upload, list, and delete notebooks
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

## Notebooks
- [pytorch.ipynb]: PyTorch model training and evaluation.
- [cshl.ipynb]: CSHL dataset exploration.

[cloud.ipynb] contains an example adding and deleting a notebook from the `scverse-ml-workshop-2024` TileDB-Cloud namespace. To execute with [Papermill]:

```bash
papermill cloud.ipynb cloud-out.ipynb && \
juq papermill-clean cloud-out.ipynb -o cloud.ipynb && \
rm cloud-out.ipynb
```

[Training models on atlas-scale single-cell datasets]: https://cfp.scverse.org/2024/talk/GQHNYE/
[schedule]: https://scverse.org/conference2024/schedule#2024-09-12
[scverse Conference 2024]: https://scverse.org/conference2024
[cloud.ipynb]: cloud.ipynb
[pytorch.ipynb]: pytorch.ipynb
[cshl.ipynb]: cshl.ipynb
[Papermill]: https://papermill.readthedocs.io/en/latest/
