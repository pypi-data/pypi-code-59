from .._internals import IterableConstants


class FixtureType(metaclass=IterableConstants):
    SCRAPED = 'Scraped'
    MANUAL = 'Manual'
    IMPLIED = 'Implied'
