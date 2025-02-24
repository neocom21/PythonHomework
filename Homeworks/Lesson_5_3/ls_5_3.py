#'Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes


#ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
#підсумкова довжина hashtag має бути не більше 140 символів.
#кожне слово починається з великої літери.
#якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string

my_string_punctuation = ' ' + string.punctuation  # Додаємо пробіл до списку заборонених символів

my_variable = input("Введіть фразу для створення хештегу: ")

my_variable = my_variable.title() #кожне слово починається з великої літери.

# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів
for char in my_string_punctuation:
    my_variable=my_variable.replace(char,'')

short_string = "#"+my_variable[:139] #підсумкова довжина hashtag має бути не більше 140 символів.

print (short_string)

