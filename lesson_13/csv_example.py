import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'New York'],
    ['Bob', None, 'Chicago']
]

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('output.csv', 'r') as read_csv_file:
    reader = list(csv.reader(read_csv_file))

    header = reader[0]
    row_data = reader[1:]

    print('Header is', header)
    for index, row in enumerate(row_data, start=1):
        print(f'{index+1} row is: {row}')