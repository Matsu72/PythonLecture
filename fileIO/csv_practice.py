import os
import csv

file_path = os.path.dirname(os.path.abspath(__file__)) + "/"
file_name = file_path + "example.csv"

# with open(file_name) as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line[1])

# with open(file_name) as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line["Country"])

# with open(file_path + "sample.csv", mode="w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Country"])
#     writer.writerow(["Yamada", "Japan"])
#     writer.writerow(["Smith", "USA"])

with open(file_path + "sample.csv", mode="w") as f:
    writer = csv.DictWriter(f, ["Name", "Country"])
    writer.writeheader()
    writer.writerow({"Name": "Yamada", "Country": "Japan"})
    writer.writerow({"Name": "Smith", "Country": "USA"})