import csv

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['1', 'csv_test'])

data = [
    ('2', 'csv_test'),
    ('3', 'csv_test'),
    ('4', 'csv_test'),
]

with open('test.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
