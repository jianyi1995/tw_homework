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

        self.assertEqual(expected_out, cash_register.print_all_ticket('../no_discount_with_1_good_with_only_barcood.json'))
        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 苹果, 数量: 5(斤), 单价: 5.5(元), 小计: 27.5(元)\n' + \
            '----------------------\n' + \
            '总计: 27.5(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_all_ticket('../no_discount_with_1_good_with_barcood_with_number.json'))

        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 可口可乐, 数量: 2(瓶), 单价: 3.0(元), 小计: 6.0(元)\n' + \
            '名称: 苹果, 数量: 5(斤), 单价: 5.5(元), 小计: 27.5(元)\n' + \
            '----------------------\n' + \
            '总计: 33.5(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_all_ticket('../no_discount.json'))

    def test_print_with_95_discount(self):
        cash_register = CashRegister()
        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 雪碧, 数量: 2(瓶), 单价: 3.0(元), 小计: 5.7(元), 节省 0.3(元)\n' + \
            '----------------------\n' + \
            '总计: 5.7(元)\n' + \
            '节省: 0.3(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_all_ticket('../discount_95_with_only_one_good.json'))

        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 雪碧, 数量: 2(瓶), 单价: 3.0(元), 小计: 5.7(元), 节省 0.3(元)\n' + \
            '名称: 网球, 数量: 2(个), 单价: 3.0(元), 小计: 5.7(元), 节省 0.3(元)\n' + \
            '----------------------\n' + \
            '总计: 11.4(元)\n' + \
            '节省: 0.6(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_all_ticket('../discount_95_with_more_goods.json'))

        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 雪碧, 数量: 2(瓶), 单价: 3.0(元), 小计: 5.7(元), 节省 0.3(元)\n' + \
            '名称: 可口可乐, 数量: 2(瓶), 单价: 3.0(元), 小计: 6.0(元)\n' + \
            '----------------------\n' + \
            '总计: 11.7(元)\n' + \
            '节省: 0.3(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_all_ticket('../one_discount_95_good_and_one_no_discount_good.json'))

    def test_print_with_but2send1(self):
        cash_register = CashRegister()
        expected_out = \
            '***<没钱赚商店>购物清单***\n' + \
            '名称: 可口可乐, 数量: 3(瓶), 单价: 3.0(元), 小计: 6.0(元)\n' + \
            '----------------------\n' + \
            '买二赠一商品: \n' + \
            '名称：可口可乐，数量：1瓶 \n' + \
            '----------------------\n' + \
            '总计: 6.0(元)\n' + \
            '**********************'
        self.assertEqual(expected_out, cash_register.print_all_ticket('../discount_buy2send1_with_1_good.json'))
