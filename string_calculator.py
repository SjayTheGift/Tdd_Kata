import re


class StringCalculator:

    def add(self, numbers):
        if numbers == '':
            return 0

        digits = list(map(int, re.findall(r'-?\d+\.?\d*', numbers)))
        digits_less_than_thousand = list(filter(lambda x: x < 1000, digits))
        negative_numbers = list(filter(lambda x: x < 0, digits))
        listToStr = ' '.join([str(elem) for elem in negative_numbers])

        if negative_numbers:
            raise Exception(f'negatives not allowed {listToStr}')

        return sum(digits_less_than_thousand)


if __name__ == '__main__':
    calculate = StringCalculator()
    calculate.add('5,4,100')
