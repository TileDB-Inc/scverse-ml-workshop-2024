from .base import cli as main

# Register subcommands
from . import invite, nb, org, user


if __name__ == '__main__':
    main()
