import unittest
from datetime import datetime
from pdc_calculator import PdcCalculator

class TestPdcCalculator(unittest.TestCase):

    def setUp(self):
        self.start_date = datetime(2022, 1, 1)
        self.end_date = datetime(2022, 12, 31)

    def test_user_1(self):
        valid_users_data = {1: [(datetime.strptime(date, '%d/%m/%Y'), 30) for date in [
            "04/01/2022", "02/02/2022", "05/03/2022", "04/04/2022", "04/05/2022",
            "03/06/2022", "03/07/2022", "02/08/2022", "01/09/2022", "01/10/2022",
            "31/10/2022", "30/11/2022", "30/12/2022"]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 1.0
        pdc_results = calculator.calculate_PDC()
        self.assertIn(1, pdc_results)
        self.assertAlmostEqual(pdc_results[1], expected_pdc, places=1)

    def test_user_2(self):
        valid_users_data = {2: [(datetime.strptime(date, '%d/%m/%Y'), 30) for date in [
            "04/01/2022", "04/02/2022", "07/03/2022", "07/04/2022", "08/05/2022",
            "08/06/2022", "09/07/2022", "09/08/2022", "09/09/2022", "10/10/2022",
            "10/11/2022", "11/12/2022"]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 0.966
        pdc_results = calculator.calculate_PDC()
        self.assertIn(2, pdc_results)
        self.assertAlmostEqual(pdc_results[2], expected_pdc, places=1)

    def test_user_3(self):
        valid_users_data = {3: [(datetime.strptime(date, '%d/%m/%Y'), quantity) for date, quantity in [
            ("04/01/2022", 20), ("02/02/2022", 30), ("05/03/2022", 30), ("04/04/2022", 30),
            ("04/05/2022", 30), ("03/06/2022", 30), ("03/07/2022", 30), ("02/08/2022", 30),
            ("01/09/2022", 30), ("01/10/2022", 30), ("31/10/2022", 30), ("30/11/2022", 30),
            ("30/12/2022", 30)]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 0.97
        pdc_results = calculator.calculate_PDC()
        self.assertIn(3, pdc_results)
        self.assertAlmostEqual(pdc_results[3], expected_pdc, places=1)

    def test_user_4(self):
        valid_users_data = {4: [(datetime.strptime(date, '%d/%m/%Y'), 60) for date in [
            "04/01/2022", "05/03/2022", "04/05/2022", "03/06/2022", "01/09/2022",
            "31/10/2022", "30/12/2022"]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 1.0
        pdc_results = calculator.calculate_PDC()
        self.assertIn(4, pdc_results)
        self.assertAlmostEqual(pdc_results[4], expected_pdc, places=1)

    def test_user_5(self):
        valid_users_data = {5: [(datetime.strptime(date, '%d/%m/%Y'), quantity) for date, quantity in [
            ("04/01/2022", 120), ("05/03/2022", 60), ("04/05/2022", 60), ("03/06/2022", 60),
            ("31/10/2022", 60), ("30/12/2022", 60)]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 1.0
        pdc_results = calculator.calculate_PDC()
        self.assertIn(5, pdc_results)
        self.assertAlmostEqual(pdc_results[5], expected_pdc, places=1)

    def test_user_6(self):
        valid_users_data = {6: [(datetime.strptime(date, '%d/%m/%Y'), 60) for date in [
            "04/01/2022", "05/03/2022", "04/05/2022", "31/10/2022", "30/12/2022"]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 0.666
        pdc_results = calculator.calculate_PDC()
        self.assertIn(6, pdc_results)
        self.assertAlmostEqual(pdc_results[6], expected_pdc, places=1)

    def test_user_7(self):
        valid_users_data = {7: [(datetime.strptime(date, '%d/%m/%Y'), 60) for date in [
            "04/01/2022", "31/10/2022", "30/12/2022"]]}
        calculator = PdcCalculator(self.start_date, self.end_date, valid_users_data)
        expected_pdc = 0.333
        pdc_results = calculator.calculate_PDC()
        self.assertIn(7, pdc_results)
        self.assertAlmostEqual(pdc_results[7], expected_pdc, places=1)

if __name__ == '__main__':
    unittest.main()
