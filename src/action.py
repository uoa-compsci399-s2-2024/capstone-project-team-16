import string


class Action:
    def __init__(self, description: string):
        self.__description = description
        self.__stats = dict()

    def use(self, item):
        pass
