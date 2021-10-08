import re
class PhoneNumber:
    def __init__(self, number):
        try:
            number = re.sub(r'\D', '', number)
            self.number = re.match(r'(1)?([2-9]\d{2}[2-9]\d{6})$', number).group(2)
            self.area_code = re.match(r'(1)?([2-9]\d\d)', number).group(2)
        except:
            raise ValueError('Entrada invalida')
    def pretty(self):
        return f'({self.area_code})-{self.number[-7:-4]}-{self.number[-4:]}'
