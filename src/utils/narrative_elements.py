"""
Functions for selecting narrative elements (tropes and themes)
"""
import os
import csv
import random

from trope import Trope


def create_tropes(rows: list[dict]) -> list[Trope]:
    """
    Creates a list of Trope objects from a list of rows

    :param list[dict] rows: List of rows
    :return: A list of Trope objects
    :rtype: list[Trope]
    """
    trope_objects = []
    for row in rows:
        trope = Trope(int(row["id"]), row["name"], row["description"])
        conflicts = row["conflicts"]
        if conflicts:
            conflicts = conflicts.strip("[]").split(",")
            trope.conflicts = [int(s) for s in conflicts]
        trope_objects.append(trope)
    return trope_objects


def read_csv_file(file_name: str) -> list:
    """
    Reads a csv file and returns a list of the rows as dictionaries

    :param str file_name: Name of the csv file
    :return: A list of rows as dictionaries
    :rtype: list[dict]
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"path {file_name} does not exist!")
    rows = []
    with open(file_name, encoding="unicode_escape") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


def get_random_tropes(tropes_list: list[Trope], num_tropes: int) -> list[Trope]:
    """
    Returns a list of with the requested amount of randomly chosen tropes which do not conflict

    :param list[Trope] tropes_list: A list of Trope objects
    :param int num_tropes: The number of tropes to be selected
    :return: A list of the requested number of Trope objects
    :rtype: list[Trope]
    """
    random_tropes = []

    while len(random_tropes) < num_tropes:
        trope = random.choice(tropes_list)
        if trope not in random_tropes:
            if trope.conflicts is None:
                random_tropes.append(trope)
            elif len({r.id_ for r in random_tropes}.intersection(set(trope.conflicts))) == 0:
                random_tropes.append(trope)
    return random_tropes


def get_random_theme(themes_file: str) -> str:
    """
    Returns a randomly chosen theme

    :param str themes_file: The name of the themes file
    :return: A randomly chosen theme
    :rtype: str
    """
    if not os.path.exists(themes_file):
        raise FileNotFoundError(f"path {themes_file} does not exist!")
    with open(themes_file) as file:
        themes = [line.rstrip() for line in file]
    return random.choice(themes)


def select_narrative_elements(
        themes_file: str,
        plot_tropes_csv_file: str,
        protagonist_tropes_csv_file: str,
        antagonist_tropes_csv_file: str,
        num_plot_tropes: int,
        num_prot_tropes: int,
        num_ant_tropes: int
) -> tuple[str, list[Trope]]:
    """
    Selects and returns a list of one theme and the requested amount of each type of trope from the theme txt file and
    the trope csv files

    :param str themes_file: The name of the themes file
    :param str plot_tropes_csv_file: The name of the plot tropes file
    :param str protagonist_tropes_csv_file: The name of the protagonist tropes file
    :param str antagonist_tropes_csv_file: The name of the antagonist tropes file
    :param int num_plot_tropes: The number of plot tropes to be selected
    :param int num_prot_tropes: The number of protagonist tropes to be selected
    :param int num_ant_tropes: TThe number of antagonist tropes to be selected
    :return: A tuple of the theme and a list of the requested amount of Trope objects
    :rtype: tuple[str, list[Trope]]
    """
    chosen_theme = get_random_theme(themes_file)
    chosen_tropes = get_random_tropes(create_tropes(read_csv_file(plot_tropes_csv_file)), num_plot_tropes)
    chosen_tropes.extend(get_random_tropes(create_tropes(read_csv_file(protagonist_tropes_csv_file)), num_prot_tropes))
    chosen_tropes.extend(get_random_tropes(create_tropes(read_csv_file(antagonist_tropes_csv_file)), num_ant_tropes))
    return chosen_theme, chosen_tropes
