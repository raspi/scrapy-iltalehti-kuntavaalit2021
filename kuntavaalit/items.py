from dataclasses import dataclass


@dataclass
class Item:
    url: str
    data: dict


@dataclass
class Municipality(Item):
    pass


@dataclass
class Party(Item):
    pass


@dataclass
class ItemWithMunicipality(Item):
    municipality: str


@dataclass
class Answer(ItemWithMunicipality):
    candidateid: int


@dataclass
class Question(ItemWithMunicipality):
    pass
