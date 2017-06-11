'''
Created on 10 Jun 2017

@author: fgurkov1
'''

class NumberWord(object):
    
    digits = [
        0,
        len('one'),
        len('two'),
        len('three'),
        len('four'),
        len('five'),
        len('six'),
        len('seven'),
        len('eight'),
        len('nine'),
        len('ten'),
        len('eleven'),
        len('twelve'),
        len('thirteen'),
        len('fourteen'),
        len('fifteen'),
        len('sixteen'),
        len('seventeen'),
        len('eighteen'),
        len('nineteen'),
        ]
    
    tens = [
        0,
        0,
        len('twenty'),
        len('thirty'),
        len('forty'),
        len('fifty'),
        len('sixty'),
        len('seventy'),
        len('eighty'),
        len('ninety'),
        ]
    
    hundred = len('hundred')
    thousand = len('thousand')
    
    union = len('and')
    
    def to_word(self, number:int):
        word = 0
        if number >= 1000:
            thousands = number // 1000
            number %= 1000
            word += self.to_word(thousands) + self.thousand
        if number >= 100:
            hundreds = number // 100
            number %= 100
            word += self.digits[hundreds] + self.hundred
            if number > 0:
                word += self.union
        if number >= 20:
            ten, digit = number // 10, number % 10
            word += self.tens[ten] + self.digits[digit]
        else:
            word += self.digits[number]
        return word
            
def count_sums(limit:int):
    converter = NumberWord()
    count = 0
    for i in range (1, limit + 1):
        count += converter.to_word(i)
    return count

if __name__ == '__main__':
    print(count_sums(1000))