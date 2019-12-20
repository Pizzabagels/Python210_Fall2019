#Thomas Aguilu
#Python 220
#Fall 2019

class Element:
    Tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.Content = []
        self.Content.append(content);
        self.attributes = {**kwargs}

    def append(self, new_content):
        self.Content.append(new_content);

    def render(self, out_file=None):
        Content = ''
        for i in self.Content:
            if i is None:
                pass
            else:
                try:
                    Content += i.render()
                except AttributeError:
                    Content += i
        if self.attributes is None:
            pass
        elif self.attributes is not None:
            #get this working
            values = ""
            for k,v in self.attributes.items():
                values += (str(k)+"="+ str(v))
        String = '<' + self.Tag + '>\n' + Content + '\n' + \
                 '</' + self.Tag + '>\n'
        if out_file is None:
            pass
        else:
            out_file.write(String)
            #writes outfile of formatted String value

        return String


class Body(Element):
    Tag = 'body'


class Html(Element):
    Tag = 'html'


class P(Element):
    Tag = 'p'

class Head(Element):
    Tag = 'head'
class OnelineTag(Element):
    def render(self, out_file=None):
        Content = ''
        for i in self.Content:
            if i is None:
                pass
            else:
                try:
                    Content += i.render()  # more or less. But, what it would return??? If outfile is not specified, it will NOT
                except AttributeError:  # This is VERY UGLY, to detect base case
                    Content += i
                # write to file, right, just return
                # We also need specify base case for recursion!
        String = '<' + self.Tag + '> ' + Content + ' </' + self.Tag + '>'

        if out_file is None:
            pass
        else:
            out_file.write(String)
            # writes outfile of formatted String value

        return String  # we need to return. When we call recursively, we will have file argument just for first

class Title(OnelineTag):
    Tag = "title"

page = Html()
body = Body()
head = Head()
title = Title()
body.append(P("a very small paragraph"))
head.append(Title("PythonClass - Session 6 example"))
page.append(head)
page.append(body)
print(body.Content)
with open("test.html", 'w') as outfile:
    page.render(outfile)

page = Body("Some content")
page.append("Some more contenet")