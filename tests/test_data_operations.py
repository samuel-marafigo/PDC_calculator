import unittest
from data_operations import DataOperations

class TestDataOperations(unittest.TestCase):
    def setUp(self):
        # Data for testing standard functionality
        self.csv_data = [
            {'user_id': '1', 'date': '01/01/2020', 'quantity': '2,5'},
            {'user_id': '2', 'date': '02/01/2020', 'quantity': '3,0'},
            # Add more test data as needed
        ]

        # Data for testing the new method
        self.csv_data_for_conditions = [
            {'Usuário': '1', 'Idade': '30', 'Sexo': 'M', 'Farmacêutico': 'A', 'Cenário': 'X', 'Date': '01/01/2020', 'Quantity': '2,5'},
            {'Usuário': '1', 'Idade': '32', 'Sexo': 'M', 'Farmacêutico': 'A', 'Cenário': 'X', 'Date': '02/01/2020', 'Quantity': '3,0'},
            {'Usuário': '2', 'Idade': '25', 'Sexo': 'F', 'Farmacêutico': 'B', 'Cenário': 'Y', 'Date': '03/01/2020', 'Quantity': '1,5'},
            # Additional test data as needed
        ]
        self.PDC = {'1': 'PDC1', '2': 'PDC2'}

        # Initialize DataOperations instances for different tests
        self.data_ops = DataOperations(self.csv_data, 'user_id', 'date', 'quantity', 'age', 'sex', 'pharmacist', 'scenario', self.PDC, 1)
        self.data_ops_with_conditions = DataOperations(
            self.csv_data_for_conditions, 'Usuário', 'Date', 'Quantity', 'Idade', 'Sexo', 'Farmacêutico', 'Cenário', self.PDC, 1)

    def test_initialization(self):
        self.assertEqual(self.data_ops.user_id_col, 'user_id')
        self.assertEqual(self.data_ops.date_col, 'date')
        self.assertEqual(self.data_ops.quantity_col, 'quantity')
        self.assertEqual(self.data_ops.min_dispensations, 1)

    def test_parse_user_id(self):
        row = {'user_id': '123', 'date': '01/01/2020', 'quantity': '2,5'}
        self.assertEqual(self.data_ops._parse_user_id(row), '123')

    def test_convert_date(self):
        self.assertEqual(self.data_ops._convert_date('01/01/2020').isoformat(), '2020-01-01')

    def test_convert_quantity_to_float(self):
        self.assertEqual(self.data_ops._convert_quantity_to_float('2,5'), 2.5)

    def test_aggregate_records(self):
        self.data_ops._aggregate_records()
        self.assertIn('1', self.data_ops._user_medication)
        self.assertIn('2', self.data_ops._user_medication)

    def test_create_valid_users(self):
        valid_users = self.data_ops.create_valid_users()
        self.assertIn('1', valid_users)
        self.assertIn('2', valid_users)

    def test_process_user_data_with_conditions(self):
        processed_data = self.data_ops_with_conditions.process_user_data_with_conditions()

        expected_output = [
            {'Usuário': '1', 'Idade': 32, 'Sexo': 'M', 'Farmacêutico': 'A', 'Cenário': 'X', 'PDC': 'PDC1'},
            {'Usuário': '2', 'Idade': 25, 'Sexo': 'F', 'Farmacêutico': 'B', 'Cenário': 'Y', 'PDC': 'PDC2'},
            # Add expected output for other test scenarios
        ]

        self.assertEqual(processed_data, expected_output)

if __name__ == '__main__':
    unittest.main()
