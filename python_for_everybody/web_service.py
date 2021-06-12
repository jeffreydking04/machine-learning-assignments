import xml.etree.ElementTree as ET

data = '''<person>
    <name>jeff</name>
    <name>cassie</name>
    <phone type="intl">
    +1 555 555 5555
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.findall('name')[1].text)
print('Attr:', tree.find('email').get('hide'))