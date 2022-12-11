import xml.etree.ElementTree as ET
str = """<?xml version="1.0" encoding="utf-8"?>\n<root><version>1.29</version><code>0</code><count>1</count><pageCount>1</pageCount><currentPage>1</currentPage><data><item><id>4579675</id><name>Post Malone</name><ipi/><type>Person</type><url>http://data.music-story.com/post-malone</url><firstname> Malone</firstname><lastname>Post</lastname><coeff_actu>16</coeff_actu><update_date>2022-06-23 09:07:04.107123</update_date><creation_date>2015-09-03 10:21:50</creation_date><search_scores><name>0</name></search_scores></item></data></root>"""

tree = ET.fromstring(str)
print(tree[5][0].find("type").text)