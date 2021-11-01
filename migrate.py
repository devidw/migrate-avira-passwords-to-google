import sys
import csv
import re
# from urllib.parse import urlparse


def formaturl(url):
    """https://stackoverflow.com/a/55766564"""
    if not re.match('(?:http|ftp|https)://', url):
        url = 'http://{}'.format(url)
    # url = url.encode('idna')
    # url = url.decode()
    # print(url)
    return url


def validentry(entry):
    keys = ['website', 'username', 'password']
    for key in keys:
        if key not in entry or entry[key] == '':
            return False
    return True


# print(sys.argv)
if len(sys.argv) != 3:
    raise ValueError('Not enough arguments received')

input_file = sys.argv[1]
output_file = sys.argv[2]

input_data = csv.DictReader(open(input_file))
output_data = []

for input_entry in input_data:
    if not validentry(input_entry):
        continue
    full_url = formaturl(input_entry['website'])
    # print(full_url)
    output_entry = {
        'url': full_url,
        'username': input_entry['username'],
        'password': input_entry['password'],
    }
    output_data.append(output_entry)

# print(output_data)
output_keys = output_data[0].keys()
with open(output_file, 'w', newline='') as output_csv:
    dict_writer = csv.DictWriter(output_csv, output_keys)
    dict_writer.writeheader()
    dict_writer.writerows(output_data)
