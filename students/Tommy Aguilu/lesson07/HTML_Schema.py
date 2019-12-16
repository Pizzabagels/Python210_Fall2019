class Element:
    Tag='html'
    def __init__(self,content=None):
        self.Content=[] #Content will, ultimately, be a list of elements
        self.Content.append(content);

    def append(self,new_content):
        self.Content.append(new_content);


    def render(self, out_file=None): #OK, it should generate string and write to file
        Content=''
        for _ in self.Content:
            if _ is None:
                pass
            else:
                try:
                    Content+=_.render() #more or less. But, what it would return??? If outfile is not specified, it will NOT
                except AttributeError: #This is VERY UGLY, to detect base case
                    Content+=_
                #write to file, right, just return
                #We also need specify base case for recursion!

        String='<'+self.Tag+'>\n'+Content+'\n'+ \
         '</'+self.Tag+'>'

        if out_file is None:
            pass
        else:
            pass #
            #HEre we will write in outfile

        return String #we need to return. When we call recursively, we will have file argument just for first

class Body(Element):
        Tag='body'

class Html(Element):
        Tag='html'

class P(Element):
        Tag='p'


page = Html()
body = Body()
body.append(P("a very small paragraph"))
body.append(P("another small paragraph"))
page.append(body)
print(page.render())


page = Body("Some content")
page.append("Some more contenet")