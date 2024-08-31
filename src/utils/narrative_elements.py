"""Functions for selecting narrative elements (tropes and themes)"""
import os
import csv
import random

from src.trope import Trope


def create_tropes(rows) -> list[Trope]:
    """Creates a list of Trope objects from a row"""
    trope_objects = []
    for row in rows:
        trope = Trope(int(row["id"]), row["name"], row["description"])
        conflicts = row["conflicts"]
        if conflicts:
            conflicts = conflicts.strip("[]").split(",")
            trope.conflicts = [int(s) for s in conflicts]
        trope_objects.append(trope)
    return trope_objects


def read_csv_file(file_name) -> list[dict]:
    """Reads a csv file and returns a list of the rows as dictionaries"""
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"path {file_name} does not exist!")
    rows = []
    with open(file_name, encoding="unicode_escape") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


def get_random_tropes(tropes_list, num_tropes) -> list[Trope]:
    """Returns a list of with the requested amount of
    randomly chosen tropes which do not conflict"""
    random_tropes = []

    while len(random_tropes) < num_tropes:
        trope = random.choice(tropes_list)
        if trope not in random_tropes:
            if trope.conflicts is None:
                random_tropes.append(trope)
            elif len({r.id_ for r in random_tropes}.intersection(set(trope.conflicts))) == 0:
                random_tropes.append(trope)
    return random_tropes


def get_random_theme(themes_file) -> str:
    if not os.path.exists(themes_file):
        raise FileNotFoundError(f"path {themes_file} does not exist!")
    with open(themes_file) as file:
        themes = [line.rstrip() for line in file]
    return random.choice(themes)


def select_narrative_elements(
        themes_file,
        plot_tropes_csv_file,
        protagonist_tropes_csv_file,
        antagonist_tropes_csv_file,
        num_plot_tropes,
        num_prot_tropes,
        num_ant_tropes
) -> tuple[str, list[Trope]]:
    """Selects and returns a list of one theme, three plot
    tropes, one protagonist trope and one antagonist trope
    from the theme txt file and the trope csv files"""
    chosen_theme = get_random_theme(themes_file)
    chosen_tropes = get_random_tropes(create_tropes(read_csv_file(plot_tropes_csv_file)), num_plot_tropes)
    chosen_tropes.extend(get_random_tropes(create_tropes(read_csv_file(protagonist_tropes_csv_file)), num_prot_tropes))
    chosen_tropes.extend(get_random_tropes(create_tropes(read_csv_file(antagonist_tropes_csv_file)), num_ant_tropes))
    return chosen_theme, chosen_tropes
