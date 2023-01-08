word_list = []
marks_list = []
list_of_symbols = [',', '!', '.', '?']

test_string1 = 'Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и схватит пулю. ' \
               'Думаешь, им буду я? Нет. Это я постучу в дверь.'


def funct_to_fill_lists(my_string):
    for i in my_string.split(' '):
        if i[-1] in list_of_symbols:
            if i[-1] not in marks_list:
                marks_list.append(i[-1])
            if i[:-1] not in word_list:
                word_list.append(i[:-1])
        else:
            if i not in word_list:
                word_list.append(i)


funct_to_fill_lists(test_string1)
print(word_list)
print(marks_list)
