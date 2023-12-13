import csv
with open("archivos\\datos.csv")as archivito:
    reader = csv.reader(archivito)
    for row in reader:
        print(row)