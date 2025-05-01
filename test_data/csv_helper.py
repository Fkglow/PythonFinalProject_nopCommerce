import csv

class CsvDataManager:

    @staticmethod
    def save_credentials_in_csv_file(filename, email, password):
        with open(filename, 'a', newline='') as data_file:
            writer = csv.writer(data_file, delimiter=',')
            writer.writerow([email, password])

    @staticmethod
    def get_credentials_from_csv_file(filename):
        rows = []
        data_file = open(filename, 'r')
        reader = csv.reader(data_file)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows

