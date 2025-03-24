import codecs


def remove_tags(s):
    tags = ('</title>', '<title>', '</h1>', '<h1>', '</p>', '<p>')
    for tag in tags:
        s = s.replace(tag, '')  # Видаляємо всі теги зі списку

    return s.strip()  # Очищаємо пробіли на початку та в кінці



def delete_html_tags(html_file, result_file='cleaned.txt'):

      with codecs.open(html_file, 'r', 'utf-8') as file:

          lines = file.read().split("\n")

          #print(lines)

          filtered_lines = []  # Створюємо порожній список

          # Перебираємо рядки
          for s in lines:
              # Перевіряємо, чи містить рядок один із потрібних тегів
              if any(tag in s for tag in ('</title>', '</h1>', '</p>')):
                  filtered_lines.append(remove_tags(s))



          # Записуємо очищений текст у файл
          with codecs.open(result_file, 'w')  as f:

              for match in filtered_lines:
                  f.write(match+"\n")



delete_html_tags("draft.html")
