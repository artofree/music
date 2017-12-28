from xml.etree.ElementTree import parse, Element
doc = parse(r'../2.xml')
root = doc.getroot()
theEmt =root.find('part')
print(len(theEmt))
theMea =theEmt[3]
print(len(theMea))
print(theMea.getchildren().index(theMea.find('backup')))
index =theMea.getchildren().index(theMea.find('backup'))
while len(theMea) >index:
    theMea.remove(theMea[index])
print(len(theMea))
for theMea in theEmt:
    if theMea.find('backup'):
        index =theMea.getchildren().index(theMea.find('backup'))
        while len(theMea) >index:
            theMea.remove(theMea[index])
doc.write('new.xml', encoding = "utf-8" ,xml_declaration=True)
