from enum import Enum

class TextType(Enum):
    Normal = 1
    Bold = 2
    Italic = 3
    Code = 4
    Links = 5
    Images = 6


class BlockType(Enum):
    Paragraph = 1
    Heading = 2
    Code = 3
    Quote = 4
    UnorderedList = 5
    OrderedList = 6