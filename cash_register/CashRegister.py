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
        try:
            with open('../discount95.json', 'r+', encoding='utf-8') as f:
                discount_good_list = json.load(f)
                return discount_good_list
        except:
            return []

    def produce_buy2send1_good_list(self):
        try:
            with open('../buy2send1.json', 'r+', encoding='utf-8') as f:
                buy2send1_good_list = json.load(f)
                return buy2send1_good_list
        except:
            return []

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
                    tmp_dict[tmp[0]] = int(tmp[1])
                    data.remove(item)
            count_dict = Counter(data)
            shopping_dict = dict(count_dict, **tmp_dict) # 存放商品编码和购买数量
            return shopping_dict



    def print_ticket(self, input_file):
        shopping_dict = self.produce_shopping_good_list(input_file)
        total_cost = 0.0
        name = ''
        unit = ''
        price = 0.0
        res = ''
        single_total = 0.0

        res += '***<没钱赚商店>购物清单***\n'
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
            single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)'
            print(single_info)
            res += single_info + '\n'

        print('----------------------')
        res += '----------------------\n'
        print('总计: ' + '%.2f' % total_cost + '(元)')
        res += '总计: ' + '%.2f' %total_cost + '(元)\n'
        print('**********************')
        res += '**********************\n'
        return res

    def print_buy2send1_ticket(self, input_file):

        good_list = self.produce_good_information_list()
        shopping_dict = self.produce_shopping_good_list(input_file)
        buy2send1_good_list = self.produce_buy2send1_good_list()
        saved_cost = 0.0
        total_cost = 0.0
        name = ''
        unit = ''
        price = 0.0
        buy2send1_good = []
        res = ''

        print('***<没钱赚商店>购物清单***')
        res += '***<没钱赚商店>购物清单***\n'
        for key in shopping_dict:
            count = shopping_dict[key]
            if key in buy2send1_good_list and float(count) >= 3.0:
                new_count = int(count - count // 3)
                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']
                        tmp = {}
                        tmp['name'] = name
                        tmp['count'] = count - new_count
                        tmp['unit'] = unit
                        saved_cost += (count - new_count) * price
                        buy2send1_good.append(tmp)

                single_total = price * new_count
                total_cost += single_total
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)'
                print(single_info)
                res += single_info + '\n'

            else:

                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']

                single_total = price * count
                total_cost += single_total
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)'
                print(single_info)
                res += single_info + '\n'

        print('----------------------')
        res += '----------------------\n'
        print('----------------------')
        res += '----------------------\n'
        print('买二赠一商品:\n')
        res += '买二赠一商品:\n'

        for item in buy2send1_good:
            print('名称: ' + item['name'] + ',' + ' 数量: ' + str(item['count']) + item['unit'])
            res += '名称: ' + item['name'] + ',' + ' 数量: ' + str(item['count']) + item['unit'] + '\n'

        print('----------------------')
        res += '----------------------\n'
        print('总计: ' + '%.2f' % total_cost + '(元)')
        res += '总计: ' + '%.2f' % total_cost + '(元)' + '\n'
        print('节省: ' + '%.2f' % saved_cost + '(元)')
        res += '节省: ' + '%.2f' % saved_cost + '(元)' + '\n'
        print('**********************')
        res += '**********************\n'
        return res


    def print_95discount_ticket(self, input_file):
        good_list = self.produce_good_information_list()
        shopping_dict = self.produce_shopping_good_list(input_file)
        discount95_good_list = self.produce_discount_good_list()
        saved_cost = 0.0
        total_cost = 0.0
        name = ''
        unit = ''
        price = 0.0
        res =''

        print('***<没钱赚商店>购物清单***')
        res += '***<没钱赚商店>购物清单***\n'
        for key in shopping_dict:
            count = shopping_dict[key]
            if key in discount95_good_list:
                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']

                single_total = price * count * 0.95
                saved_single = price * count - single_total
                saved_single = float('%.2f' % saved_single)
                total_cost += single_total
                saved_cost += saved_single
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)' + ',' + ' 节省: ' + '%.2f' % saved_single + '(元)'
                print(single_info)
                res += single_info + '\n'

            else:
                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']

                single_total = price * count
                total_cost += single_total
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)'
                print(single_info)
                res += single_info + '\n'


        print('----------------------')
        res += '----------------------\n'
        print('总计: ' + '%.2f' % total_cost + '(元)')
        res += '总计: ' + '%.2f' % total_cost + '(元)' + '\n'
        print('节省: ' + '%.2f' %saved_cost + '(元)')
        res += '节省: ' + '%.2f' % saved_cost + '(元)' + '\n'
        print('**********************')
        res += '**********************\n'
        return res


    def print_two_benefit_ticket(self, input_file):
        good_list = self.produce_good_information_list()
        shopping_dict = self.produce_shopping_good_list(input_file)
        discount95_good_list = self.produce_discount_good_list()
        buy2send1_good_list = self.produce_buy2send1_good_list()
        buy2send1_good = []
        saved_cost = 0.0
        total_cost = 0.0
        name = ''
        unit = ''
        price = 0.0
        res =''

        print('***<没钱赚商店>购物清单***')
        res += '***<没钱赚商店>购物清单***\n'
        for key in shopping_dict:
            count = shopping_dict[key]
            if key in buy2send1_good_list and float(count) >= 3.0:
                new_count = int(count - count // 3)
                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']
                        tmp = {}
                        tmp['name'] = name
                        tmp['count'] = count - new_count
                        tmp['unit'] = unit
                        saved_cost += (count - new_count) * price
                        buy2send1_good.append(tmp)

                single_total = price * new_count
                total_cost += single_total
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)'
                print(single_info)
                res += single_info + '\n'

            elif (key in buy2send1_good_list and key in discount95_good_list and float(count) < 3.0) or (key  not in buy2send1_good_list and key  in discount95_good_list):
                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']

                single_total = price * count * 0.95
                saved_single = price * count - single_total
                saved_single = float('%.2f' % saved_single)
                total_cost += single_total
                saved_cost += saved_single
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)' + ',' + ' 节省: ' + '%.2f' % saved_single + '(元)'
                print(single_info)
                res += single_info + '\n'

            else:
                for item in good_list:
                    if item['barcode'] == key:
                        name = item['name']
                        unit = item['unit']
                        price = item['price']

                single_total = price * count
                total_cost += single_total
                single_info = '名称: ' + name + ',' + ' 数量: ' + str(count) + '(' + unit + ')' + ',' + ' 单价: ' + str(
                    price) + '(元)' + ',' + ' 小计: ' + '%.2f' % single_total + '(元)'
                print(single_info)
                res += single_info + '\n'

        print('----------------------')
        res += '----------------------\n'
        print('买二赠一商品:\n')
        res += '买二赠一商品:\n'

        for item in buy2send1_good:
            print('名称: ' + item['name'] + ',' + ' 数量: ' + str(item['count']) + item['unit'])
            res += '名称: ' + item['name'] + ',' + ' 数量: ' + str(item['count']) + item['unit'] + '\n'

        print('----------------------')
        res += '----------------------\n'
        print('总计: ' + '%.2f' % total_cost + '(元)')
        res += '总计: ' + '%.2f' % total_cost + '(元)' + '\n'
        print('节省: ' + '%.2f' % saved_cost + '(元)')
        res += '节省: ' + '%.2f' % saved_cost + '(元)' + '\n'
        print('**********************')
        res += '**********************\n'
        return res


    def print_all_ticket(self, input_file):

        shopping_dict = self.produce_shopping_good_list(input_file)
        discount95_good_list = self.produce_discount_good_list()
        buy2send1_good_list = self.produce_buy2send1_good_list()
        discount95_good = []
        buy2send1_good = []

        for key in shopping_dict:
            result = self.isRightBarcode(key)
            if not result:
                msg = key + '不是一个正确的条形码,请检查'
                print(msg)
                return

        for key in shopping_dict:
            count = shopping_dict[key]
            if key in (buy2send1_good_list) and (float(count) >= 3.0):
                buy2send1_good.append(key)

            if (key in buy2send1_good_list) and (float(count) < 3.0) and (key in discount95_good_list):
                discount95_good.append(key)

            if (key not in buy2send1_good_list) and (key in discount95_good_list):
                discount95_good.append(key)

        if (not discount95_good) and (not buy2send1_good):
            return self.print_ticket(input_file)

        elif (not discount95_good) and buy2send1_good:
            return self.print_buy2send1_ticket(input_file)

        elif discount95_good and (not buy2send1_good):
            return self.print_95discount_ticket(input_file)

        elif set(discount95_good) == set(buy2send1_good):
            return self.print_buy2send1_ticket(input_file)

        elif discount95_good and buy2send1_good:
            return self.print_two_benefit_ticket(input_file)

        else:
            print('输入文件有误,请检查')




if __name__ == '__main__':
    s = CashRegister()
    s.print_all_ticket('../no_discount_with_1_good_with_only_barcood.json')





