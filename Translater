from googletrans import Translator

translater = Translator()

file = open('<path>\\file.txt', encoding='utf-8')

list = []
for line in file:
    list.append(line)
file.close()

listfile = open('<path>\\file.txt', 'a', encoding='utf-8')

for i in range(len(list)):
    text = list[i]
    transtext = translater.translate(text, src='<lang>', dest='<lang>')
    str_text = str(transtext)
    listfile.write(str_text)

listfile.close()
