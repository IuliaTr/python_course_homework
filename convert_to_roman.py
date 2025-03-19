def integer_to_roman(num_string):
  num = int(num_string)
  roman_symbol_list = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
  to_string_result = ""
  for val, roman_symbol in roman_symbol_list:
    while num >= val:
        to_string_result += roman_symbol
        num -= val
 
  return to_string_result
 
num_string = input("Introdu un numar integer: ")  
print(f"Varianta romana este: {integer_to_roman(num_string)}")
