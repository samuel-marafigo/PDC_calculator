import csv


class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def read_csv_to_list(file_name, delimiter):
        try:
            with open(file_name, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=delimiter)
                return list(reader)
        except (csv.Error, UnicodeDecodeError) as e:
            print(f"Error reading file {file_name}: {e}")
            return None
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            return None


    @staticmethod
    def write_csv_from_list(data, output_filename, header):
        try:
            with open(output_filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        except csv.Error as e:
            print(f"Error writing file {output_filename}: {e}")

# Usage example
# file_manager = FileManager()
# processed_data = file_manager.process_user_data('input.csv', PDC)
# if processed_data is not None:
#     file_manager.write_csv_from_list(processed_data, 'output.csv', header)
