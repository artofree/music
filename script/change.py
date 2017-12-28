#升1度
step =-1
dList =['C','D','E','F','G','A','B']

from xml.etree.ElementTree import parse, Element
doc = parse('zhu.xml')
root = doc.getroot()
theEmt =root.find('part')

for theMea in theEmt:
    for theNode in theMea:
        if theNode.find('pitch'):
            thePitch =theNode.find('pitch')
            isShift =0
            theStep =thePitch.find('step')
            theOct =thePitch.find('octave')
            iOct =int(theOct.text)
            index =dList.index(theStep.text)
            index +=step
            if index >6:
                index -=7
                isShift =1
            if index <0:
                index +=7
                isShift =-1
            theStep.text =dList[index]
            theOct.text =str(iOct +isShift)

doc.write('change.xml', encoding = "utf-8" ,xml_declaration=True)
