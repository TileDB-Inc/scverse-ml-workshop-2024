from .base import cli as main
from .nb.upload import upload
from .nb.delete import delete
from .nb.ls import ls


if __name__ == '__main__':
    main()
