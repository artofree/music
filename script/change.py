# 升1度
step = -6
dList = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
sList = ['c', 'd', 'f', 'g', 'a']

from xml.etree.ElementTree import parse, Element

doc = parse('main.xml')
root = doc.getroot()
theEmt = root.find('part')

for theMea in theEmt:
    for theNode in theMea:
        if theNode.find('pitch') is not None:
            thePitch = theNode.find('pitch')
            isShift = 0
            theStep = thePitch.find('step')
            theOct = thePitch.find('octave')
            iOct = int(theOct.text)
            iAlter = 0
            if thePitch.find('alter') is not None:
                iAlter = int(thePitch.find('alter').text)

            index = dList.index(theStep.text) + iAlter
            index += step
            if index > 11:
                index -= 12
                isShift = 1
            if index < 0:
                index += 12
                isShift = -1

            theStep.text = dList[index]
            theOct.text = str(iOct + isShift)
            if dList[index] in sList:
                theStep.text = dList[index].upper()
                if thePitch.find('alter') is not None:
                    thePitch.find('alter').text = '1'
                else:
                    e = Element('alter')
                    e.text = '1'
                    thePitch.insert(1, e)
            else:
                if thePitch.find('alter') is not None:
                    thePitch.find('alter').text = '0'


doc.write('change.xml', encoding="utf-8", xml_declaration=True)
