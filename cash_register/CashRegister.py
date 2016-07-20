import re
import json
from collections import Counter
class CashRegister():

    def isRightBarcode(self, barCode):

        result = re.match(r'^ITEM\d{6}(-\d)?$', barCode)
        if result is not None:
            return True
        else:
            return False

    def produce_discount_good_list(self):
        with open('../discount95.json', 'r+', encoding='utf-8') as f:
            discount_good_list = json.load(f)
            return discount_good_list

    def produce_buy2send1_good_list(self):
        with open('../buy2send1.json', 'r+', encoding='utf-8') as f:
            buy2send1_good_list = json.load(f)
            return buy2send1_good_list

    def produce_good_information_list(self):
        with open('../good_information.json', 'r+', encoding='utf-8') as f:
            good_information_list = json.load(f)
            return good_information_list

    def produce_shopping_good_list(self, input_file):
        tmp_dict = {}
        with open(input_file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                tmp = item.split('-')
                if len(tmp) == 2:
                    tmp_dict[tmp[0]] = float(tmp[1])
                    data.remove(item)
            count_dict = Counter(data)
            shopping_dict = dict(count_dict, **tmp_dict) # 存放商品编码和购买数量
            return shopping_dict



    def print_ticket(self):
        shopping_dict = self.produce_shopping_good_list('../input.json')
        total_cost = 0.0
        name = ''
        unit = ''
        price = 0.0
        single_total = 0.0
        for key in shopping_dict:
            result = self.isRightBarcode(key)
            if not result:
                msg = key + '不是一个正确的条形码,请检查'
                print(msg)
                return

        print('***<没钱赚商店>购物清单***')
        for key in shopping_dict:
            count = shopping_dict[key]
            good_list = self.produce_good_information_list()
            for item in good_list:
                if item['barcode'] == key:
                    name = item['name']
                    unit = item['unit']
                    price = item['price']

            single_total = price * count
            total_cost += single_total
            print('\n')
            single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(price) + '(元)' + ',' + ' 小计: ' + str(single_total) + '(元)'
            print(single_info)

        print('\n')
        print('----------------------')
        print('\n')
        print('总计: ' + str(total_cost) + '(元)')
        print('\n')
        print('**********************')


