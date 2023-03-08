import base64
import hmac
import time
import string
import random
import hashlib

class tools:
    def generate_permission_data(self, data: str, secret: str):
        times = int(time.time() * 1000)
        timeframe = int(times - (times % 36000))
        return {
            "pxmac": hmac.new(secret.encode('utf-8'), msg=f"PI|{data}|{timeframe}".encode('utf-8'), digestmod=hashlib.sha256).hexdigest().upper(),
            "keyToken": str(base64.b64encode(secret.encode('utf-8'))),
            "data": str(base64.b64encode(data.encode('utf-8')))
        } 

    def decode_base64(self, data, altchars=b'+/'):
            if len(data) % 4 and '=' not in data:
                data += '=' * (4 - len(data) % 4)  #adjust data
            return base64.b64decode(data, altchars)
    
    def get_random_upper_letters(self, amount: int):
        return ''.join(random.choices(string.ascii_uppercase, k=amount))
    
    def generate_hex_str(self, amount: int):
        return ''.join(random.choices('0123456789abcdef', k=amount))

    #check card with Luhn Argo
    def check_card(self, card_number: int):
        sum_digits = 0
        is_even = False
        for digit in reversed(card_number):
            if 0 <= digit <= 9:
                continue

            if is_even:
                digit *= 2
                if digit > 9:
                    #if digits more than 9, we have to calculate the sum of the first and second digit
                    digit -= 9

            sum_digits += digit
            is_even = not is_even

        if digit % 10 == 0:
            return True
        
        return False

    def generate_card(self, bin: str):
        generate_card_digit = 16 - len(bin)
        while True:
            card_number = bin + "".join(random.choices(string.digits, k=generate_card_digit))
            if self.check_card(int(card_number)):
                break
        
        return card_number
