"""Game Loop"""
import os
import csv
import random

from src.trope import Trope


def create_tropes(rows):
    """Creates a list of Trope objects from a row"""
    tropes = []
    for row in rows:
        trope = Trope(int(row["id"]), row["title"], row["description"])
        conflicts = row["conflicts"]
        if conflicts:
            conflicts = conflicts.strip("[]").split(",")
            trope.conflicts = [int(s) for s in conflicts]
        tropes.append(trope)
    return tropes


def read_csv_file(file_name):
    """Reads a csv file and returns a list of the rows as dictionaries"""
    if not os.path.exists(file_name):
        print(f"path {file_name} does not exist!")
        return
    rows = []
    with open(file_name, encoding="unicode_escape") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


def get_random_tropes(tropes_list, num_tropes):
    """Returns a list of with the requested amount of randomly chosen tropes which do not conflict"""
    random_tropes = []
    conflicts = set([])

    while len(tropes_list) < num_tropes:
        trope = random.choice(tropes_list)
        if trope not in tropes_list and not bool(set(trope.conflicts) & conflicts):
            random_tropes.append(trope)
            if trope.conflicts:
                conflicts.update(trope.conflicts)

    return random_tropes


def select_tropes(plot_tropes_csv_file, protagonist_tropes_csv_file, antagonist_tropes_csv_file):
    """Selects and returns a list of three plot tropes, a protagonist trope and an antagonist trope from the
    trope csv files"""
    plot_tropes = create_tropes(read_csv_file(plot_tropes_csv_file))
    protagonist_tropes = create_tropes(read_csv_file(protagonist_tropes_csv_file))
    antagonist_tropes = create_tropes(read_csv_file(antagonist_tropes_csv_file))

    tropes = get_random_tropes(plot_tropes, 3)
    tropes.extend(get_random_tropes(protagonist_tropes, 1))
    tropes.extend(get_random_tropes(antagonist_tropes, 1))

    return tropes
