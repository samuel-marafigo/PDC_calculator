from collections import defaultdict
from datetime import datetime

class DataOperations:
    def __init__(self, csv_data, user_id_column, date_column, quantity_column, age_column, sex_column, pharmacist_column, scenario_column, PDC, min_dispensations):
        self.csv_data = csv_data
        self.user_id_col = user_id_column
        self.date_col = date_column
        self.quantity_col = quantity_column
        self.age_col = age_column
        self.sex_col = sex_column
        self.pharmacist_col = pharmacist_column
        self.scenario_col = scenario_column
        self.PDC = PDC
        self.min_dispensations = min_dispensations
        self._user_medication = None

    def _parse_user_id(self, row):
        return row[self.user_id_col]

    def _convert_date(self, date_str):
        return datetime.strptime(date_str, '%d/%m/%Y').date()

    def _convert_quantity_to_float(self, quantity_str):
        return float(quantity_str.replace(',', '.'))

    def _aggregate_records(self):
        user_medication = defaultdict(list)
        for row in self.csv_data:
            user_id = self._parse_user_id(row)
            date = self._convert_date(row[self.date_col])
            quantity = self._convert_quantity_to_float(row[self.quantity_col])
            user_medication[user_id].append((date, quantity))
        self._user_medication = user_medication

    def create_valid_users(self):
        if self._user_medication is None:
            self._aggregate_records()

        valid_users_info = {}
        for user_id, dispensing_data in self._user_medication.items():
            if len(dispensing_data) >= self.min_dispensations:
                valid_users_info[user_id] = dispensing_data
        return valid_users_info

    def process_user_data_with_conditions(self):
        user_data = {}
        for row in self.csv_data:
            user_id = row[self.user_id_col]
            if user_id in self.PDC:
                age = int(row[self.age_col])
                sex = row[self.sex_col]
                pharmacist = row[self.pharmacist_col]
                scenario = row[self.scenario_col]

                if user_id in user_data:
                    if user_data[user_id]['Farmacêutico'] != pharmacist or \
                       user_data[user_id]['Cenário'] != scenario or \
                       user_data[user_id]['Sexo'] != sex:
                        del user_data[user_id]
                        continue
                    user_data[user_id]['Idade'] = max(user_data[user_id]['Idade'], age)
                else:
                    user_data[user_id] = {'Usuário': user_id, 'Idade': age, 'Sexo': sex,
                                          'Farmacêutico': pharmacist, 'Cenário': scenario, 'PDC': self.PDC[user_id]}
        return list(user_data.values())