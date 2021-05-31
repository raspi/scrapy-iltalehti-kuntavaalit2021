from dataclasses import dataclass


@dataclass
class Item:
    url: str
    data: dict


class Candidate(Item):
    pass


class Party(Item):
    pass


class Question(Item):
    pass
