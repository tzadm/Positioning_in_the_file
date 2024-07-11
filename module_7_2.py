def  custom_write(file_name, strings):
    num_string = []
    num_string_2 = []
    num_ = 0
    for i in strings:
        num_ += 1
        num_string.append(num_)
        open_file_2 = open(file_name, 'a', encoding='utf')
        num_string.append(open_file_2.tell())
        open_file_2.write(f'{i}\n')
        num_string_2.append(tuple(num_string))
        open_file_2.close()
        num_string.clear()

    return dict(zip(num_string_2, strings))

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('1234567.txt', info)
for elem in result.items():
  print(elem)
