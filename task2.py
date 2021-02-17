"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

poem = open('space oddity.txt')
poem_text = poem.readlines()
num_of_lines = len(poem_text)
print(f'\nThe number of lines in this text is: {num_of_lines}\n')
poem.close()

poem_lines = open('space oddity.txt')
for each_line in poem_text:
    each_line_elements = poem_lines.readline().split(' ')
    each_line_length = len([word for word in each_line_elements if word != '-'])
    if each_line_elements[0] == '\n':
        print("%-70s %s %3s" % (' ', 'The number of words in this line is:', 0))
    else:
        print("%-70s %s %3s" % (
            " ".join(each_line_elements).rstrip(), 'The number of words in this line is:', each_line_length))
poem.close()
