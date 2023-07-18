import typing

class TranslatedDict(typing.TypedDict):
    zh: str
    en: str
    ja: str

ResumeTags = typing.Optional[typing.List[str]]

Translatable = str | TranslatedDict

class ResumeSubHeadingDict(typing.TypedDict):
    title: Translatable
    date: Translatable
    subtitle: Translatable
    place: Translatable
    body: Translatable
    tag: typing.NotRequired[ResumeTags]

class ResumeProjectHeadingDict(typing.TypedDict):
    title: Translatable
    date: Translatable
    body: Translatable
    tag: typing.NotRequired[ResumeTags]

ResumeSubHeadingList = typing.List[ResumeSubHeadingDict]

ResumeProjectHeadingList = typing.List[ResumeProjectHeadingDict]

class PropItem():
    item: Translatable
    prop: str

    def __init__(self, item: Translatable, prop: str) -> None:
        self.item = item
        self.prop = prop

ResumeItemList = typing.List[Translatable | int]

ResumePropableItemList = typing.List[Translatable | int | PropItem]

ItemParser = typing.Callable[[Translatable, typing.Optional[str]], str]
