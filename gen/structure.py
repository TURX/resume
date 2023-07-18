import type
import env
import typing

def translate(text: type.Translatable):
    if isinstance(text, str):
        return text
    else:
        return text[env.lang]

def _subheading_item(item: type.ResumeSubHeadingDict, tag: type.ResumeTags):
    try:
        if tag is not None:
            if "tag" not in item.keys() or item["tag"] is None:
                return ""  # no tag to match
            if list(set(item["tag"]) & set(tag)) == []:
                return ""  # tag not match
        code = r"""
        \resumeSubheading
        """ + "{" + translate(item["title"]) + "}" + "{" + translate(item["date"]) + "}" + """
        """ + "{" + translate(item["subtitle"]) + "}" + "{" + translate(item["place"]) + "}" + """
        """ + translate(item["body"])
        return code
    except KeyError:  # not defined for this language
        return ""

def subheading_list(list: type.ResumeSubHeadingList):
    code = r"""
    \resumeSubHeadingListStart
    """

    for item in list:
        code += _subheading_item(item, env.tag)

    code += r"""
    \resumeSubHeadingListEnd
    """

    return code

def _projectheading_item(item: type.ResumeProjectHeadingDict, tag: type.ResumeTags):
    try:
        if tag is not None:
            if "tag" not in item.keys() or item["tag"] is None:
                return ""  # no tag to match
            if list(set(item["tag"]) & set(tag)) == []:
                return ""  # tag not match
        code = r"""
        \resumeProjectHeading
        """ + "{" + translate(item["title"]) + "}" + "{" + translate(item["date"]) + "}" + """
        """ + translate(item["body"])
        return code
    except KeyError:  # not defined for this language
        return ""

def projectheading_list(list: type.ResumeProjectHeadingList):
    code = r"""
    \resumeSubHeadingListStart
    """

    for item in list:
        code += _projectheading_item(item, env.tag)

    code += r"""
    \resumeSubHeadingListEnd
    """

    return code

def _item_list_item(item: type.Translatable, prop: typing.Optional[str] = None):
    if prop is not None:
        raise Exception("unsupported")
    try:
        return r"\resumeItem{" + translate(item)+ "}\n"
    except KeyError:  # not defined for this language
        return ""

def item_list(list: type.ResumeItemList, item_parser: type.ItemParser = _item_list_item):
    code = r"""
    \resumeItemListStart
    """

    for item in list:
        if isinstance(item, int):
            code += r"\vspace{" + str(item) + "pt}\n"
        else:
            code += item_parser(item, None)

    code += r"""
    \resumeItemListEnd
    """

    return code

def _itemize_item(item: type.Translatable, prop: typing.Optional[str] = None):
    try:
        if prop is None:
            return r"\item " + translate(item)+ "\n"
        else:
            return r"\item[" + prop + "] " + translate(item)+ "\n"
    except KeyError:  # not defined for this language
        return ""

def itemize(list: type.ResumePropableItemList, prop: typing.Optional[str] = None, item_parser: type.ItemParser = _itemize_item):
    if prop is None:
        code = r"""
        \begin{itemize}
        """
    else:
        code = r"""
        \begin{itemize}[""" + prop + "]\n"

    for item in list:
        if isinstance(item, int):
            code += r"\vspace{" + str(item) + "pt}\n"
        elif isinstance(item, type.PropItem):
            code += item_parser(item.item, item.prop)
        else:
            code += item_parser(item, None)

    code += r"""
    \end{itemize}
    """

    return code
