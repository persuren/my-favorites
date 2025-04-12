import sys
import csv

# CSV alan sınırını artır
csv.field_size_limit(sys.maxsize)

file_path = '/Users/persuren/Downloads/'
input_name = input('Enter the file name without extension: ')
oldname = file_path + input_name + '.tsv'
newname = file_path + input_name + '.csv'

with open(oldname, 'r', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    with open(newname, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in reader:
            writer.writerow(row)