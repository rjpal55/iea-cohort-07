conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]

num = 47
roman = ''
i = 0 #initiate i = 0
while num > 0:
    while conv[i][0] > num: i+=1 #increments i to largest value greater than current num
    roman += conv[i][1] #adds the roman numeral equivalent to string
    num -= conv[i][0] #decrements your num

print(roman)