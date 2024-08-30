"""Game Loop"""
import os
import csv
import random

from src.trope import Trope


def create_tropes(rows):
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


def read_csv_file(file_name):
    """Reads a csv file and returns a list of the rows as dictionaries"""
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"path {file_name} does not exist!")
    rows = []
    with open(file_name, encoding="unicode_escape") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


def get_random_tropes(tropes_list, num_tropes):
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


def select_tropes(
    plot_tropes_csv_file,
    protagonist_tropes_csv_file,
    antagonist_tropes_csv_file,
    num_plot_tropes,
    num_prot_tropes,
    num_ant_tropes
    ):
    """Selects and returns a list of three plot tropes,
    one protagonist trope and one antagonist trope from the
    trope csv files"""
    chosen_tropes = get_random_tropes(create_tropes(read_csv_file(plot_tropes_csv_file)), num_plot_tropes)
    chosen_tropes.extend(get_random_tropes(create_tropes(read_csv_file(protagonist_tropes_csv_file)), num_prot_tropes))
    chosen_tropes.extend(get_random_tropes(create_tropes(read_csv_file(antagonist_tropes_csv_file)), num_ant_tropes))

    return chosen_tropes
