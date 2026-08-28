from __future__ import annotations

class ContentBlock:
    pass


class Paragraph(ContentBlock):
    def __init__(
        self,
        children: list[InlineContent],
        is_attribution: bool = False
    ):
        self.children = children
        self.is_attribution = is_attribution


class Heading(ContentBlock):
    def __init__(self, text: str, level: int):
        self.text = text
        self.level = level


class ListItem:
    def __init__(self, children: list[InlineContent]):
        self.children = children      


class ListBlock(ContentBlock):
    def __init__(self, items: list[ListItem], ordered: bool = False):
        self.items = items
        self.ordered = ordered


class Document:
    def __init__(self, blocks: list[ContentBlock]):
        self.blocks = blocks  


class InlineContent:
    pass


class Text(InlineContent):
    def __init__(self, value: str):
        self.value = value


class Strong(InlineContent):
    def __init__(self, children: list[InlineContent]):
        self.children = children


class Emphasis(InlineContent):
    def __init__(self, children: list[InlineContent]):
        self.children = children


class ExternalLink(InlineContent):
    def __init__(self, children: list[InlineContent], href: str):
        self.children = children
        self.href = href


class InternalLinkRequest(InlineContent):
    def __init__(
        self,
        anchor_text: str,
        target_topic: str | None = None,
        source_number: int | None = None,
        tid: str | None = None
    ):
        self.anchor_text = anchor_text
        self.target_topic = target_topic
        self.source_number = source_number
        self.tid = tid


class TableCell:
    def __init__(
        self,
        children: list[InlineContent],
        is_header: bool = False
    ):
        self.children = children
        self.is_header = is_header


class TableRow:
    def __init__(self, cells: list[TableCell]):
        self.cells = cells


class Table(ContentBlock):
    def __init__(
        self,
        header_rows: list[TableRow],
        body_rows: list[TableRow]
    ):
        self.header_rows = header_rows
        self.body_rows = body_rows


class LineBreak(InlineContent):
    pass        