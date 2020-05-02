import subprocess
import chardet

"""1"""
names = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430',
    '\u0441\u043E\u043A\u0435\u0442',
    '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440']
for i in names:
    print(i)
    print(type(i))

"""2"""
byte_list = [b'class', b'function', b'method']
for i in byte_list:
    print(i)
    print(type(i))
    print(len(i))

"""3"""
# names = [b'class', b'функция', b'attribute',b'type']
# for i in names:
#     print(i)


"""4"""
words = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words:
    encoded = i.encode('utf-16')
    print(encoded)

encoded = [
    b'\xff\xfe@\x040\x047\x04@\x040\x041\x04>\x04B\x04:\x040\x04',
    b'\xff\xfe0\x044\x04<\x048\x04=\x048\x04A\x04B\x04@\x048\x04@\x04>\x042\x040\x04=\x048\x045\x04',
    b'\xff\xfep\x00r\x00o\x00t\x00o\x00c\x00o\x00l\x00',
    b'\xff\xfes\x00t\x00a\x00n\x00d\x00a\x00r\x00d\x00']
for i in encoded:
    decoded = i.decode('utf-16')
    print(decoded)

"""5"""

#
# ARGS = ['ping', 'yandex.ru']
# YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
# for line in YA_PING.stdout:
#     result = chardet.detect(line)
#     line = line.decode(result['encoding']).encode('utf-8')
#     print(line.decode('utf-8'))

# ARGS = ['ping', 'youtube.com']
# YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
# for lines in YA_PING.stdout:
#     results = chardet.detect(lines)
#     lines = lines.decode(results['encoding']).encode('utf-8')
#     print(lines.decode('utf-8'))

"""6"""

file = open('test_file.txt', 'w', encoding='utf-8')
stroki = ['сетевое программирование ', 'сокет ', 'декоратор ']
for i in stroki:
    file.write(i)
file.close()
print(type(file))

with open('test_file.txt', encoding='utf-8') as f_n:
    for str_el in f_n:
        print(str_el+" ", end=' ')
