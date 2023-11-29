from datetime import datetime, timedelta

class PdcCalculator:
    def __init__(self, start_date, end_date, valid_users_data):
        self.start_date = start_date
        self.end_date = end_date
        self.valid_users_data = valid_users_data

    def calculate_PDC(self):
        PDC = {}
        for user, dispensing_data in self.valid_users_data.items():
            dispensing_data.sort(key=lambda x: x[0])
            user_start_date = dispensing_data[0][0]
            if user_start_date > self.end_date:
                continue
            covered_days = 0
            current_date = max(self.start_date, user_start_date)
            current_quantity = 0
            surplus = 0
            for dispensing in dispensing_data:
                if dispensing[1] == 0:
                    continue
                if current_quantity == 0:
                    current_date = max(current_date, dispensing[0])
                while current_quantity < dispensing[1]:
                    current_quantity += 1
                    if current_date > self.end_date:
                        break
                    if current_quantity > dispensing[1]:
                        surplus = current_quantity - dispensing[1]
                        current_quantity = dispensing[1]
                    covered_days += 1
                    current_date += timedelta(days=1)
                current_quantity -= dispensing[1]
                if surplus > 0:
                    current_quantity = surplus
                    surplus = 0
                if current_date > self.end_date:
                    break

            total_days = (min(self.end_date, dispensing_data[-1][0]) - user_start_date).days + 1
            PDC[user] = min(covered_days / total_days, 1.0)

        return PDC