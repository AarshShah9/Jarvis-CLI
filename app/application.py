import platform
import click
import time


class Application:
    def __init__(self):
        pass

    def getSystemType(self):
        return platform.system()

    def start_timer(self, minutes):
        """
        A simple countdown timer that prints the time remaining.
        """
        for i in range(minutes * 60, 0, -1):
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            click.echo(f"\r{timer}", nl=False)
            time.sleep(1)
        click.echo("\rTimer done!")
