import click
import subprocess


def commandHelp(name):
    with open("CLI/core/aliases.txt", "r") as f:
        data = f.readlines()
        f.close()

    names, coms = [], []
    for i in range(len(data)):
        data[i] = data[i].split('"')
        name = data[i].pop(0)
        name = name[6:-1]
        data[i].pop(1)
        names.append(name)
        coms.append(data[i][0])

    print(names, coms)

    if name in coms:
        print("Wee")
        command = name + " --help"
        print(command)
        process = subprocess.run(command)


@click.command()
@click.option("-c", "--command", "com", type=str, help="Command you need help with")
def process(com):
    commandHelp("integrate")


if __name__ == "__main__":
    process()
