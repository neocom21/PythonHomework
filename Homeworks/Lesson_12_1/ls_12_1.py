

import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):

      with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()
          matches = re.findall(r'<(title|h[1-6]|p)>(.*?)</\1>', html)
          #print(matches)


          # Записуємо очищений текст у файл
          with codecs.open(result_file, 'w', 'utf-8')  as f:

              for match in matches:
                  #print(match[1])
                  f.write(match[1]+"\n")


delete_html_tags("draft.html")