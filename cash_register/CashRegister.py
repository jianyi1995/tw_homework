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

    def produce_shopping_good_list(self):
        tmp_dict = {}  # 存放商品编码和数量
        with open('../input.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                tmp = item.split('-')
                if len(tmp) == 2:
                    tmp_dict[tmp[0]] = float(tmp[1])
                    data.remove(item)
            count_dict = Counter(data)
            shopping_dict = dict(count_dict, **tmp_dict)
            return shopping_dict


