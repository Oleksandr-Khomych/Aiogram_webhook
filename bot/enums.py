import enum


class StartType(enum.Enum):
    webhook = enum.auto()
    polling = enum.auto()
