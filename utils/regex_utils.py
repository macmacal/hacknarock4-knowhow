import re


def format_youtube_link(text):
    ends = []
    for m in re.finditer('\[/ref\]', text):
        ends.append(m.start())
    ends.reverse()

    starts = []
    for m in re.finditer('www.youtube.com', text):
        starts.append(m.start())
        starts.reverse()

    for start in starts:
        closest_end = min(i for i in ends if i > start)
        text = text[:closest_end] + ' (Youtube)' + text[closest_end:]

    return text


def format_link(text):

    ends = []
    for m in re.finditer('\[/ref\]', text):
        ends.append(m.end())
    ends.reverse()

    for end in ends:
        text = text[:end] + '[/color][/u]' + text[end:]

    starts = []
    for m in re.finditer('\[ref=', text):
        starts.append(m.start())
        starts.reverse()

    for start in starts:
        text = text[:start] + '[u][color=#0000FF]' + text[start:]

    return text


