'''
_ => True
__ => False
___ => False
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True
assert => False
assert_exception => True '''

my_test = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
        'get_Value', 'getValue', '3m', 'm3', 'assert', 'assert_exception']

import keyword
import string

my_string_punctuation = ' ' + string.punctuation.replace('_','')  # Додаємо пробіл до списку заборонених символів та виключаємо '_'

for my_variable in my_test:
    rez = 'True'

    if my_variable[0].isdigit():
        rez = 'False'
    elif any(c.isupper() for c in my_variable):
        rez = 'False'
    elif my_variable in keyword.kwlist:
        rez = 'False'
    elif my_variable.count("_")>1:
        rez = 'False'
    else:
        '''for char in my_variable:
            if char in my_string_punctuation:
                rez='False'
                break'''

    print(f"'{my_variable}' => {rez}")

