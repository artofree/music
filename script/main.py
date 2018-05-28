from xml.etree.ElementTree import parse, Element
doc = parse(r'1.xml')
root = doc.getroot()
theEmt =root.find('part')

for theMea in theEmt:
    if theMea.find('backup'):
        index =theMea.getchildren().index(theMea.find('backup'))
        while len(theMea) >index:
            theMea.remove(theMea[index])

doc.write('main.xml', encoding = "utf-8" ,xml_declaration=True)
