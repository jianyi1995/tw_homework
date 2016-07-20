from unittest import TestCase
from cash_register.CashRegister import CashRegister

class TestCashRegister(TestCase):

    def test_legal_barcode(self):

        cash_register = CashRegister()
        self.assertEqual(cash_register.isRightBarcode('ITEM000001'), True)
        self.assertEqual(cash_register.isRightBarcode('ITEM000002-2'), True)
        self.assertEqual(cash_register.isRightBarcode('ITEM000003-'), False)
        self.assertEqual(cash_register.isRightBarcode('ITEM'), False)

