import json 
import csv

with open ("file.json", "r") as json_file:
    data = json.load(json_file)

with open ("file.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("Conversion complete!")