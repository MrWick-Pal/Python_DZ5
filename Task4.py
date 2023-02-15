# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def encode(code):
    encoding = ''
    i = 0
    while i < len(code):
        count = 1
        while i + 1 < len(code) and code[i] == code[i + 1]:
                count = count + 1
                i = i + 1
        encoding += str(count) + code[i]
        i = i + 1
    return encoding

def decoding(code): 
    decode = '' 
    count = '' 
    for char in code:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count) 
            count = '' 
    return decode 

code = 'AAAAABBAAABBBKKKCAADD'
code1 = (encode(code))

print(f'Изначальный вид: {code}')
print(f'Зашифрованный вид: {code1}')
print(f'Расшифрованный вид: {decoding(code1)}')

