from xml.etree.ElementTree import parse, Element
doc = parse(r'main.xml')
root = doc.getroot()
theEmt =root.find('part')
newEmt =Element('part')
newEmt.attrib = {"id":"P1"}

#删除连接线等
for theMea in theEmt:
    for theNode in theMea:
        for theDel in theNode.findall('notations'):
            theNode.remove(theDel)
        for theDel in theNode.findall('beam'):
            theNode.remove(theDel)

for index in range(len(theEmt)):
    newMea =Element('measure')
    newMea.attrib = {"number":"1"}
    newEmt.append(newMea)

    theMea =theEmt[-1 -index]
    for idx in range(len(theMea)):
        newMea.append(theMea[-1 -idx])

root.remove(theEmt)
root.append(newEmt)
doc.write('updown.xml', encoding = "utf-8" ,xml_declaration=True)
