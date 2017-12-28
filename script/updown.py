from xml.etree.ElementTree import parse, Element
doc = parse(r'../3.xml')
root = doc.getroot()
theEmt =root.find('part')
newEmt =Element('part')
newEmt.attrib = {"id":"P1"}

for index in range(len(theEmt)):
    newMea =Element('measure')
    newMea.attrib = {"number":"1"}
    newEmt.append(newMea)

    theMea =theEmt[-1 -index]
    for idx in range(len(theMea)):
        newMea.append(theMea[-1 -idx])

root.remove(theEmt)
root.append(newEmt)
doc.write('dao.xml', encoding = "utf-8" ,xml_declaration=True)
