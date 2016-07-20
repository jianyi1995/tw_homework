import re
import json
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

