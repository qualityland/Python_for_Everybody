import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# data = '''<?xml version="1.0" encoding="UTF-8"?>
# <commentinfo>
#   <note>This file contains the sample data for testing</note>
#
#   <comments>
#     <comment>
#        <name>Romina</name>
#        <count>97</count>
#     </comment>
#     <comment>
#        <name>Laurie</name>
#        <count>97</count>
#     </comment>
#     <comment>
#        <name>Bayli</name>
#        <count>90</count>
#     </comment>
#     <comment>
#        <name>Siyona</name>
#        <count>90</count>
#     </comment>
#     <comment>
#        <name>Taisha</name>
#        <count>88</count>
#     </comment>
#     <comment>
#        <name>Alanda</name>
#        <count>87</count>
#     </comment>
#     <comment>
#        <name>Ameelia</name>
#        <count>87</count>
#     </comment>
#     <comment>
#        <name>Prasheeta</name>
#        <count>80</count>
#     </comment>
#     <comment>
#        <name>Asif</name>
#        <count>79</count>
#     </comment>
#     <comment>
#        <name>Risa</name>
#        <count>79</count>
#     </comment>
#     <comment>
#        <name>Zi</name>
#        <count>78</count>
#     </comment>
#     <comment>
#        <name>Danyil</name>
#        <count>76</count>
#     </comment>
#     <comment>
#        <name>Ediomi</name>
#        <count>76</count>
#     </comment>
#     <comment>
#        <name>Barry</name>
#        <count>72</count>
#     </comment>
#     <comment>
#        <name>Lance</name>
#        <count>72</count>
#     </comment>
#     <comment>
#        <name>Hattie</name>
#        <count>66</count>
#     </comment>
#     <comment>
#        <name>Mathu</name>
#        <count>66</count>
#     </comment>
#     <comment>
#        <name>Bowie</name>
#        <count>65</count>
#     </comment>
#     <comment>
#        <name>Samara</name>
#        <count>65</count>
#     </comment>
#     <comment>
#        <name>Uchenna</name>
#        <count>64</count>
#     </comment>
#     <comment>
#        <name>Shauni</name>
#        <count>61</count>
#     </comment>
#     <comment>
#        <name>Georgia</name>
#        <count>61</count>
#     </comment>
#     <comment>
#        <name>Rivan</name>
#        <count>59</count>
#     </comment>
#     <comment>
#        <name>Kenan</name>
#        <count>58</count>
#     </comment>
#     <comment>
#        <name>Hassan</name>
#        <count>57</count>
#     </comment>
#     <comment>
#        <name>Isma</name>
#        <count>57</count>
#     </comment>
#     <comment>
#        <name>Samanthalee</name>
#        <count>54</count>
#     </comment>
#     <comment>
#        <name>Alexa</name>
#        <count>51</count>
#     </comment>
#     <comment>
#        <name>Caine</name>
#        <count>49</count>
#     </comment>
#     <comment>
#        <name>Grady</name>
#        <count>47</count>
#     </comment>
#     <comment>
#        <name>Anne</name>
#        <count>40</count>
#     </comment>
#     <comment>
#        <name>Rihan</name>
#        <count>38</count>
#     </comment>
#     <comment>
#        <name>Alexei</name>
#        <count>37</count>
#     </comment>
#     <comment>
#        <name>Indie</name>
#        <count>36</count>
#     </comment>
#     <comment>
#        <name>Rhuairidh</name>
#        <count>36</count>
#     </comment>
#     <comment>
#        <name>Annoushka</name>
#        <count>32</count>
#     </comment>
#     <comment>
#        <name>Kenzi</name>
#        <count>25</count>
#     </comment>
#     <comment>
#        <name>Shahd</name>
#        <count>24</count>
#     </comment>
#     <comment>
#        <name>Irvine</name>
#        <count>22</count>
#     </comment>
#     <comment>
#        <name>Carys</name>
#        <count>21</count>
#     </comment>
#     <comment>
#        <name>Skye</name>
#        <count>19</count>
#     </comment>
#     <comment>
#        <name>Atiya</name>
#        <count>18</count>
#     </comment>
#     <comment>
#        <name>Rohan</name>
#        <count>18</count>
#     </comment>
#     <comment>
#        <name>Nuala</name>
#        <count>14</count>
#     </comment>
#     <comment>
#        <name>Maram</name>
#        <count>12</count>
#     </comment>
#     <comment>
#        <name>Carlo</name>
#        <count>12</count>
#     </comment>
#     <comment>
#        <name>Japleen</name>
#        <count>9</count>
#     </comment>
#     <comment>
#        <name>Breeanna</name>
#        <count>7</count>
#     </comment>
#     <comment>
#        <name>Zaaine</name>
#        <count>3</count>
#     </comment>
#     <comment>
#        <name>Inika</name>
#        <count>2</count>
#     </comment>
#   </comments>
# </commentinfo>'''
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
stuff = ET.fromstring(data)
# list of trees (tags)
lst = stuff.findall('comments/comment')
print('comments count:', len(lst))
total = 0
for item in lst:
    count = int(item.find('count').text)
    total += count
    # print('Id', item.find('id').text)
    # print('Attribute', item.get("x"))
print('total:', total)
