# python3 ./migrate.py ./tests/export.csv ./tests/import.csv
# python3 ./migrate.py ./avira.csv ./nomatter.csv ./failed.csv

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


def csv_writer(data, path):
    with open(path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)


# print(sys.argv)
if len(sys.argv) != 4:
    raise ValueError('Wrong number of arguments received (expecting 3)')

input_file = sys.argv[1]
output_file = sys.argv[2]
failed_file = sys.argv[3]

input_data = csv.DictReader(open(input_file))
output_data = []
failed_data = []

for input_entry in input_data:
    if validentry(input_entry):
        full_url = formaturl(input_entry['website'])
        # print(full_url)
        output_entry = {
            'url': full_url,
            'username': input_entry['username'],
            'password': input_entry['password'],
        }
        output_data.append(output_entry)
    else:
        failed_data.append(input_entry)

csv_writer(output_data, output_file)
csv_writer(failed_data, failed_file)
