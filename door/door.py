from hashlib import md5

id = 'reyedfim'
index = 0
password = [''] * 8
lenght = 0

while lenght < 8:
    hash = md5(f'{id}{index}'.encode()).hexdigest()
    order = int(hash[5]) if hash[5].isdigit() else 8

    if hash[:5] == '00000' and order < 8 and not password[order]:
        password[order] = hash[6]
        lenght += 1

    index += 1

print(''.join(password))
