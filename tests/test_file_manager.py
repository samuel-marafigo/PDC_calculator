import unittest
from unittest.mock import mock_open, patch, MagicMock, call
import csv
from file_manager import FileManager  # Replace 'your_module' with the name of your module


class TestFileManager(unittest.TestCase):

    def test_read_csv_to_list_success(self):
        # Mock data for a CSV file
        mock_file_data = "name,age\nJohn,30\nJane,25"

        # Mock the open function and the CSV reader
        with patch("builtins.open", mock_open(read_data=mock_file_data)):
            with patch("csv.DictReader", return_value=[{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]):
                # Call the method
                result = FileManager.read_csv_to_list("dummy.csv", ',')

                # Check if the result is as expected
                self.assertEqual(result, [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}])

    def test_read_csv_to_list_file_not_found(self):
        # Simulate file not found error
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = FileManager.read_csv_to_list("nonexistent.csv", ',')
            self.assertIsNone(result)

    def test_read_csv_to_list_csv_error(self):
        # Simulate CSV error
        with patch("builtins.open", mock_open(read_data="some,invalid,data")):
            with patch("csv.DictReader", side_effect=csv.Error):
                result = FileManager.read_csv_to_list("invalid.csv", ',')
                self.assertIsNone(result)


    def test_write_csv_from_list_success(self):
        data_to_write = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
        header = ['name', 'age']

        m = mock_open()
        with patch("builtins.open", m):
            FileManager.write_csv_from_list(data_to_write, "dummy_output.csv", header)

            # Retrieve the actual write calls made to the mock
            actual_write_calls = m().write.call_args_list

            # Check if the header is written correctly
            self.assertIn(call("name,age\r\n"), actual_write_calls)

            # Check if each data row is written (order may vary)
            self.assertIn(call("John,30\r\n"), actual_write_calls)
            self.assertIn(call("Jane,25\r\n"), actual_write_calls)

if __name__ == '__main__':
    unittest.main()