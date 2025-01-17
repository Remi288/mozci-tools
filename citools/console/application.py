import sys

from cleo import Application

from citools.console.commands.migration import MigrationCommands
from citools.console.commands.push import PushCommands


def cli():
    application = Application()
    application.add(PushCommands())
    application.add(MigrationCommands())
    application.run()


if __name__ == "__main__":
    sys.exit(cli())
