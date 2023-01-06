from fractions import Fraction
while True:
    request_sign = input('''
Choose sign:
1.+
2.-
3.*
4./
    ''')
    if request_sign != "break":
        match int(request_sign):
            case 1:
                numerator_first = int(input('Input first numerator: \n'))
                denominator_first = int(input('Input first denomerator: \n'))
                x = Fraction(numerator=numerator_first, denominator=denominator_first)
                numerator_second = int(input('Input second numerator: \n'))
                denominator_second = int(input('Input second denomerator: \n'))
                y = Fraction(numerator=numerator_second, denominator=denominator_second)
                print(x + y)
            case 2:
                numerator_first = int(input('Input first numerator: \n'))
                denominator_first = int(input('Input first denomerator: \n'))
                x = Fraction(numerator=numerator_first, denominator=denominator_first)
                numerator_second = int(input('Input second numerator: \n'))
                denominator_second = int(input('Input second denomerator: \n'))
                y = Fraction(numerator=numerator_second, denominator=denominator_second)
                print(x - y)
            case 3:
                numerator_first = int(input('Input first numerator: \n'))
                denominator_first = int(input('Input first denomerator: \n'))
                x = Fraction(numerator=numerator_first, denominator=denominator_first)
                numerator_second = int(input('Input second numerator: \n'))
                denominator_second = int(input('Input second denomerator: \n'))
                y = Fraction(numerator=numerator_second, denominator=denominator_second)
                print(x * y)
            case 4:
                numerator_first = int(input('Input first numerator: \n'))
                denominator_first = int(input('Input first denomerator: \n'))
                x = Fraction(numerator=numerator_first, denominator=denominator_first)
                numerator_second = int(input('Input second numerator: \n'))
                denominator_second = int(input('Input second denomerator: \n'))
                y = Fraction(numerator=numerator_second, denominator=denominator_second)
                print(x / y)
    else:
        break