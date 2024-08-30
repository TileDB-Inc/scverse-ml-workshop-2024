[cloud.ipynb] contains an example adding and deleting a notebook from the `scverse-ml-workshop-2024` TileDB-Cloud namespace. To execute with [Papermill]:

```bash
papermill cloud.ipynb cloud-out.ipynb && \
juq papermill-clean cloud-out.ipynb -o cloud.ipynb && \
rm cloud-out.ipynb
```

[cloud.ipynb]: cloud.ipynb
