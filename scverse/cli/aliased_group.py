from gettext import gettext

from click import Group, Context, HelpFormatter


class AliasedGroup(Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aliases = {}

    def get_command(self, ctx, cmd_name):
        rv = Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv

        if cmd_name in self.aliases:
            return self.get_command(ctx, self.aliases[cmd_name])

    def get_usage(self, ctx: Context) -> str:
        usage = super().get_usage(ctx)
        if self.aliases:
            usage += '\nAliases: ' + ', '.join(self.aliases)

    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None:
        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)
            # What is this, the tool lied about a command.  Ignore it
            if cmd is None:
                continue
            if cmd.hidden:
                continue

            commands.append((subcommand, cmd))

        # allow for 3 times the default spacing
        if len(commands):
            limit = formatter.width - 6 - max(len(cmd[0]) for cmd in commands)

            rows = []
            for subcommand, cmd in commands:
                help = cmd.get_short_help_str(limit)
                aliases = { k for k, v in self.aliases.items() if v == subcommand }
                if aliases:
                    subcommand = f"{subcommand} ({', '.join(aliases)})"
                rows.append((subcommand, help))

            if rows:
                with formatter.section(gettext("Commands")):
                    formatter.write_dl(rows)

