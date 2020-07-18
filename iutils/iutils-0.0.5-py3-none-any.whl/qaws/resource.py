import click
import subprocess


class Resource:
    def __init__(self, *args, **kwargs):
        self.limit = kwargs["limit"]

    def get_known_attributes(self):
        return []

    def get_cmd(self):
        return ""

    def run(self):
        if self.known_attributes:
            for attrib in self.get_known_attributes():
                click.echo(attrib)
            return

        cmd = self.get_cmd()

        res = subprocess.run(cmd, capture_output=True, encoding="utf-8")

        if res.returncode != 0:
            raise Exception(res.stderr)

        # No error, thus we print lines.
        if self.limit == 0:
            print(res.stdout.strip())
        else:
            n = 0
            for line in res.stdout.split("\n"):
                print(line)
                n += 1
                if n >= self.limit:
                    break
