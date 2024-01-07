"""Dice simulator tool."""
import click
import random

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group()
def top():
    """CLI for dice simulator."""


@top.command(context_settings=CONTEXT_SETTINGS)
@click.argument("die", type=str, required=True)
@click.argument("count", type=int, required=True)
@click.option("--adv", "-a", is_flag=True, default=False, help="Roll with advantage.")
@click.option(
    "--dis", "-d", is_flag=True, default=False, help="Roll with disadvantage."
)
@click.option(
    "--avg", "-m", is_flag=True, default=False, help="Report average of result."
)
@click.option("--top", "-t", default=0, help="Take top 'N' values.")
@click.option(
    "--dnd_stat", "-s", is_flag=True, default=False, help="Roll 4, take sum of top 3"
)
def roll(die, count, adv, dis, avg, top, dnd_stat):
    """Roll a die a certain number of times.

    DIE can be d4, d6, d8, d10, d12, d20, d100.

    Order of operations: top > avg
    """

    vals = _roll(die, count, adv, dis, dnd_stat)

    if top > 0:
        vals = sorted(vals, reverse=True)[:top]

    if avg:
        vals = round(sum(vals) / len(vals), 2)

    click.echo(vals)


def _roll(die, count, adv=False, dis=False, dnd=False):
    """Return list of rolls for a given die."""
    lookup = {
        "d4": [1, 4],
        "d6": [1, 6],
        "d8": [1, 8],
        "d10": [0, 9],
        "d12": [1, 12],
        "d20": [1, 20],
        "d100": [0, 99],
    }
    try:
        die_faces = range(lookup[die][0], lookup[die][1] + 1)
        vals = [random.choice(die_faces) for x in range(count)]
    except KeyError:
        click.secho(f"ERROR: Invalid die choice {die}!", fg="red")

    if adv or dis:
        v1 = vals
        v2 = [random.choice(die_faces) for x in range(count)]

        _vals = []
        for i, val in enumerate(v1):
            if adv:
                _vals.append(max(v1[i], v2[i]))
            else:
                _vals.append(min(v1[i], v2[i]))
        vals = _vals

    if dnd:
        vals = [
            sum(sorted([random.choice(die_faces) for x in range(4)], reverse=True)[:3])
            for _ in range(count)
        ]

    return vals


cli = click.CommandCollection(sources=[top], help="Die simulator.")

if __name__ == "__main__":
    cli()
