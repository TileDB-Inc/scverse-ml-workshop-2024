# scverse workshop

Scripts associated with the [Training models on atlas-scale single-cell datasets] workshop at [scverse Conference 2024].

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
[Papermill]: https://papermill.readthedocs.io/en/latest/