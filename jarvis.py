import click
import speedtest
import time


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}!')


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
