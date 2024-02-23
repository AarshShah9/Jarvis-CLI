import click
import speedtest
import time
import webbrowser
import subprocess
from app import application


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    ctx.obj = application.Application()


@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}!')


def help(self):
    click.echo("Welcome to Jarvis CLI. Here are the available commands:")


@cli.command()
def startday():
    # Open D2L in the default web browser (or specify Chrome if necessary)
    d2l_url = 'https://d2l.ucalgary.ca/d2l/home'
    webbrowser.open(d2l_url)

    click.echo("Started your day!")


@cli.command()
@click.pass_context
@click.option('--work-time', default=25, help='Duration of work time in minutes.')
@click.option('--break-time', default=5, help='Duration of break time in minutes.')
@click.option('--cycles', default=4, help='Number of work/break cycles.')
def pomodoro(ctx, work_time, break_time, cycles):
    """
    Start a Pomodoro timer with specified work and break durations.
    """
    app = ctx.obj

    for cycle in range(cycles):
        click.echo(f"Cycle {cycle + 1} of {cycles}")
        click.echo("Work time! Let's focus.")
        app.start_timer(work_time)

        if cycle == cycles - 1:
            click.echo("All cycles complete! Great work.")
        else:
            click.echo("Time for a break! Relax :)")
            app.start_timer(break_time)

    click.echo("Pomodoro session complete! Ready to go again?")


@cli.command()
def chatgpt():
    click.echo('Opening ChatGPT in your default web browser...')
    webbrowser.open('https://chat.openai.com/')


@cli.command()
def speedtester():
    click.echo('Running speed test...')

    with click.progressbar(length=100, label='Selecting Best Server') as bar:
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            for i in range(100):
                time.sleep(0.01)  # Simulate time taken to select server
                bar.update(1)
        except Exception as e:
            click.echo(f"Failed to select server: {e}")
            return

    with click.progressbar(length=100, label='Measuring Download Speed') as bar:
        try:
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            for i in range(100):
                time.sleep(0.01)  # Simulate time taken for download test
                bar.update(1)
            click.echo(f"Download speed: {download_speed:.2f} Mbps")
        except Exception as e:
            click.echo(f"Failed to measure download speed: {e}")
            return

    with click.progressbar(length=100, label='Measuring Upload Speed') as bar:
        try:
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            for i in range(100):
                time.sleep(0.01)  # Simulate time taken for upload test
                bar.update(1)
            click.echo(f"Upload speed: {upload_speed:.2f} Mbps")
        except Exception as e:
            click.echo(f"Failed to measure upload speed: {e}")
            return

    try:
        ping = st.results.ping
        click.echo(f"Ping: {ping} ms")
    except Exception as e:
        click.echo(f"Failed to measure ping: {e}")


if __name__ == '__main__':
    cli()
