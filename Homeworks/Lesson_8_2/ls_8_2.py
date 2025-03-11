
import string

my_string_punctuation = ' ' + string.punctuation  # Додаємо пробіл до списку заборонених символів

def is_palindrome(text):

    for char in my_string_punctuation:
        text = text.replace(char, '')

    return text.lower() == text[::-1].lower()



assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

