from xml.etree.ElementTree import parse, Element
doc = parse(r'main.xml')
root = doc.getroot()
theEmt =root.find('part')

#删除连接线等
for theMea in theEmt:
    for theNode in theMea:
        for theDel in theNode.findall('notations'):
            theNode.remove(theDel)
        for theDel in theNode.findall('beam'):
            theNode.remove(theDel)

doc.write('clean.xml', encoding = "utf-8" ,xml_declaration=True)
