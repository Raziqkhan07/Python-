import json
import xmltodict
# import csv
# import string
import csv
with open('c:\\Users\\Raziq.Khan\\PycharmProjects\\pythonProject\\data2.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))


f = open('data.json','r')

# returns JSON object as
# a dictionary
data = json.load(f)
#

# # Iterating through the json
# # list
for i in data['employee']:
 print(i)

with open("data.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read()) #XML TO DICT
    #xml_file.close()

    # generate the object using json.dumps()
    # corresponding to json data

    json_data = json.dumps(data_dict)