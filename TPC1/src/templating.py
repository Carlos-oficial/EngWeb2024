import sys

import jinja2
import parse

if __name__=="__main__":
    
    
    ruas = parse.parse_folder(sys.argv[1])
    
    templateLoader = jinja2.FileSystemLoader(searchpath="../templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("rua.jinja.html")
    ruas_pages = []
    for rua,cenas in ruas.items():
        print(cenas.keys())
        figuras = cenas.get("figuras")
        for f in figuras.values():
            f['img'] = '../'+f['img'].split('tpc1/')[1]
        outputText = template.render(
            **cenas
        )  # this is where to put args to the template renderer
        path = '../pages/'+rua+'.html'
        ruas_pages.append(path)
        with open(path,'w+') as f: f.write(outputText)
    
    template = templateEnv.get_template("index.jinja.html")
    outputText = template.render(
        ruas = ruas_pages
    )
    with open('../pages/index.html','w+') as f: f.write(outputText)
