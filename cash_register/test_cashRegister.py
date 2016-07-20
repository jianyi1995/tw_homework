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

    def test_shopping_good_list(self):
        cash_register = CashRegister()
        self.assertIsNotNone(cash_register.produce_shopping_good_list('../input.json'))

    def test_print_without_discount(self):
        cash_register = CashRegister()
        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 可口可乐, 数量: 2(瓶), 单价: 3.0(元), 小计: 6.0(元)\n' + \
            '----------------------\n' + \
            '总计: 6.0(元)\n' + \
            '**********************'

        self.assertEqual(expected_out, cash_register.print_ticket('../no_discount_with_1_good_with_only_barcood.json'))
        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 苹果, 数量: 5(斤), 单价: 5.5(元), 小计: 27.5(元)\n' + \
            '----------------------\n' + \
            '总计: 27.5(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_ticket('../no_discount_with_1_good_with_barcood_with_number.json'))


