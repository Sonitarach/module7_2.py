from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'w')
    strings_positions = {}
    string_num = 0
    start_byte = file.seek(0)
    for i in strings:
        file.write(i+'\n')
        string_num += 1
        key = (string_num, start_byte)
        strings_positions[key] = i
        start_byte = file.tell()
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



