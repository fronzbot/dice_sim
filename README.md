# DICE SIM

A dumb little command-line dice simulator for calculting averages and such

### Installation

```bash
git clone git@github.com:fronzbot/dice_sim.git
cd dice_sim
pip install .
```

### Usage

```bash
dice-sim --help
```

### Examples

Take average of 1000 d20 rolls with advantage
```bash
dice-sim roll d20 1000 -m --adv
```

Roll 6 stat blocks for dnd character creation (rolling 4 d6, taking sum of top 3)
```bash
dice-sim roll d6 6 -s
```
