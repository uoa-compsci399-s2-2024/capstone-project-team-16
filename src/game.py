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

    while len(random_tropes) < num_tropes and not len(random_tropes) == len(tropes_list):
        trope = random.choice(tropes_list)
        if trope not in random_tropes:
            if trope.conflicts is None:
                random_tropes.append(trope)
            elif len(conflicts.intersection(set(trope.conflicts))) == 0:
                random_tropes.append(trope)
                conflicts.update(trope.conflicts)
    return random_tropes


def select_tropes(plot_tropes_csv_file, protagonist_tropes_csv_file, antagonist_tropes_csv_file):
    """Selects and returns a list of three plot tropes, a protagonist trope and an antagonist trope from the
    trope csv files"""
    plot_tropes = create_tropes(read_csv_file(plot_tropes_csv_file))
    protagonist_tropes = create_tropes(read_csv_file(protagonist_tropes_csv_file))
    antagonist_tropes = create_tropes(read_csv_file(antagonist_tropes_csv_file))

    chosen_tropes = get_random_tropes(plot_tropes, 3)
    chosen_tropes.extend(get_random_tropes(protagonist_tropes, 1))
    chosen_tropes.extend(get_random_tropes(antagonist_tropes, 1))

    return chosen_tropes


dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tropes = select_tropes(os.path.join(dirname, 'src/story/plot_tropes.csv'),
                       os.path.join(dirname, 'src/story/protagonist_tropes.csv'),
                       os.path.join(dirname, 'src/story/antagonist_tropes.csv'))
