"""
This is ported from the original PHP version here:
https://gist.github.com/jbroadway/2836900
"""
import re

class Slimdown(object):
    def __init__(self):
        self.rules = [
            (r'\n\*(.*)' ,  self.ul_list),
            (r'````([^`]*)````' ,  r'<pre><code>\1</code></pre>'),
            (r'>(.*)\n\n' ,  r'<blockquote>\1</blockquote>'),
            (r'`([^`]*)`' ,  r'<code>\1</code>'),
            (r'\[([^\[]+)\]\(([^\)]+)\)' ,  r'<a href=\2>\1</a>'),
            (r'\n(#+)(.*)',  self.header),
            (r'(\*\*|__)(.*?)\1' ,  r'<strong>\2</strong>'),
            #(r'(\*|_)(.*?)\1' ,  r'<em>\2</em>'),
            (r'\~\~(.*?)\~\~' ,  r'<del>\1</del>'),
            (r'\, \"(.*?)\"\, ' ,  r'<q>\1</q>'),
            (r'\n[0-9]+\.(.*)' ,  self.ol_list),
            (r'\n-{5,}/' ,  r"\n<hr />"),
            (r'<\/ul>\s?<ul>' ,  ''),
            (r'<\/ol>\s?<ol>' ,  ''),
        ]

    def para(self, match):
        line = match.group(0)
        stripped = line.strip()
        regex = re.compile(r'/^<\/?(ul|ol|li|h|p|bl)/')

        if regex.match(stripped):
            return stripped
        return "<p>{}</p>".format(stripped)

    def ul_list(self, match):
        item = match.groups()[0]
        return "\n<ul><li>{}</li></ul>".format(item.strip())

    def ol_list(self, match):
        item = match.group(0)
        return "\n<ol><li>{}</li></ol>".format(item.strip())

    def header(self, match):
        item = match.groups()
        level = len(item[0])
        return '<h{level}>{header}</h{level}>'.format(level=level,
                header=item[1].strip())

    def render(self, text):
        text = "\n{text}\n".format(text=text)
        for rule, output in self.rules:
            regex = re.compile(rule)
            text = regex.sub(output, text)
        text = "".join(["<p>{}</p>".format(x.strip()) for x in text.split("\n\n")])

        return text.strip()
