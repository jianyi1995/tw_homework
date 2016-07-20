from unittest import TestCase
from cash_register.CashRegister import CashRegister

class TestCashRegister(TestCase):

    def test_legal_barcode(self):

        cash_register = CashRegister()
        self.assertEqual(cash_register.isRightBarcode('ITEM000001'), True)
        self.assertEqual(cash_register.isRightBarcode('ITEM000002-2'), True)
        self.assertEqual(cash_register.isRightBarcode('ITEM000003-'), False)
        self.assertEqual(cash_register.isRightBarcode('ITEM'), False)

    def test_discount_list(self):
        cash_register = CashRegister()
        self.assertIsNotNone(cash_register.produce_discount_good_list())

    def test_buy2send1_list(self):
        cash_register = CashRegister()
        self.assertIsNotNone(cash_register.produce_buy2send1_good_list())

    def test_good_information(self):
        cash_register = CashRegister()
        self.assertIsNotNone(cash_register.produce_good_information_list())