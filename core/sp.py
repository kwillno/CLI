import time

import click
import speedtest


def checkDown(sp):
    down = sp.download() / 10 ** 6  # in Mbit/s
    print("Download speed: {0:.2f} Mbit/s".format(down))


def checkUp(sp):
    up = sp.upload() / 10 ** 6  # in Mbit/s
    print("Upload speed: {0:.2f} Mbit/s".format(up))


def checkPing(sp):
    ping = sp.results.ping
    print("Ping: {0:.3f} ms".format(ping))


@click.command()
@click.option("--verbose", "-v", "verb", count=True, help="Show full output")
@click.option("--download", "-d", "down", default=True, help="Test download speed")
@click.option("--upload", "-u", "up", default=True, help="Test upload speed")
@click.option("--ping", "-p", "ping", count=True, help="Check ping")
def process(verb, down, up, ping):

    servers = []
    try:
        sp = speedtest.Speedtest()
        sp.get_servers(servers)
        if verb:
            print("Servers found, searching for best server")
        sp.get_best_server()
        if verb:
            print("Best server found!")
    except speedtest.ConfigRetrievalError:
        print("Could not connect.")
        exit()
    if verb:
        print("Running speedtest")
    if down == True:
        checkDown(sp)
    if up == True:
        checkUp(sp)
    if ping == True:
        checkPing(sp)
    if verb:
        print("Speedtest completed!")


if __name__ == "__main__":
    process()
