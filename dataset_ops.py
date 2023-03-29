import csv

source_file = open('source.csv', 'r', encoding='utf-8', errors='ignore')
destination_file = open('destination_file.csv', 'a', encoding='utf-8', errors='ignore')

with source_file as sf:
    cursor = csv.DictReader(sf)
    writer = csv.DictWriter(destination_file)
    for row in cursor:
        writer.writerow(rowdict)

    