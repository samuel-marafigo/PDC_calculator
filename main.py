from datetime import datetime

from file_manager import FileManager
from pdc_calculator import PdcCalculator
from data_operations import DataOperations

# Constants
INPUT_CSV = 'Known values.csv'
OUTPUT_CSV = 'Processed values.csv'
USER_ID_COLUMN = 'Usuário'
DATE_COLUMN = 'Data da Saída'
QUANTITY_COLUMN = 'Quantidade'
AGE_COLUMN = 'Idade'
SEX_COLUMN = 'Sexo'
PHARMACIST_COLUMN = 'Farmacêutico'
SCENARIO_COLUMN = 'Cenário'
MIN_DISPENSATIONS = 2

# Read the CSV file
file_manager = FileManager()
csv_data = file_manager.read_csv_to_list(INPUT_CSV, ';')

# Process data to find valid users
data_operations = DataOperations(csv_data, USER_ID_COLUMN, DATE_COLUMN, QUANTITY_COLUMN, AGE_COLUMN, SEX_COLUMN, PHARMACIST_COLUMN, SCENARIO_COLUMN, None, MIN_DISPENSATIONS)
valid_users_data = data_operations.create_valid_users()

# Calculate PDC
pdc_calculator = PdcCalculator(datetime(2022, 1, 1).date(), datetime(2022, 12, 31).date(), valid_users_data)
PDC = pdc_calculator.calculate_PDC()

# Update DataOperations with PDC values
data_operations.PDC = PDC
processed_data = data_operations.process_user_data_with_conditions()

# Write the processed data to a new CSV file
file_manager.write_csv_from_list(processed_data, OUTPUT_CSV, ['Usuário', 'Idade', 'Sexo', 'Farmacêutico', 'Cenário', 'PDC'])

print("Data processing complete. Check the output file.")
