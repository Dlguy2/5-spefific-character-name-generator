from operator import truediv
import requests
import string
import random
import time
print('this is made on version python 23.2.1')
print('may not work on other versions')
print('custom generator(1.0) made by dsploiter')
print('')
print('')
print('1 : false (recomended for collecting )')
print('2 : true (for knowing whats wrong and recomended for people who only need 1 username)')
print('')
uvu = int(input('do you allow errors showcase : '))
print('')
print('')
print('1 : random letter (A)')
print('2 : random digit (1)')
print('3 : _')
print('')
print('')
chc1 = int(input('what do you want as the first character : '))
print('')
print('')
chc2 = int(input('what do you want as the second character : '))
print('')
print('')
chc3 = int(input('what do you want as the third character : '))
print('')
print('')
print('1 : random letter (A)')
print('2 : random digit (B)')
print('3 : _')
print('4 : same letter as first')
print('5 : same letter as second')
print('')
print('')
chc4 = int(input('what do you want as the fourth character : '))
print('')
print('')
chc5 = int(input('what do you want as the fifth character : '))
print('')
c11 = ''
c22 = ''
c33 = ''
c44 = ''
c55 = ''
if chc1 == 1:
    c11 = 'A'
elif chc1 == 2:
    c11 = '1'
elif chc1 == 3:
    c11 = '_'
if chc2 == 1:
    c22 = 'B'
elif chc2 == 2:
    c22 = '2'
elif chc2 == 3:
    c22 = '_'
if chc3 == 1:
    c33 = 'C'
elif chc3 == 2:
    c33 = '3'
elif chc3 == 3:
    c33 = '_'
if chc4 == 1:
    c44 = 'D'
elif chc4 == 2:
    c44 = '4'
elif chc4 == 3:
    c44 = '_'
elif chc4 == 4:
    c44 = c11
elif chc4 == 5:
    c44 = c22
if chc5 == 1:
    c55 = 'E'
elif chc5 == 2:
    c55 = '5'
elif chc5 == 3:
    c55 = '_'
elif chc5 == 4:
    c55 = c11
elif chc5 == 5:
    c55 = c22
choises = [c11,c22,c33,c44,c55]
usernamee = ''
for words in choises:
    usernamee += words + '' ''
print('')
print('code : ',chc1,chc2,chc3,chc4,chc5)
print('usernames are like :')
print(usernamee)
print('')
print('')
def generate():
    c1 = ''
    c2 = ''
    c3 = ''
    c4 = ''
    c5 = ''
    if chc1 == 1:
        c1 = random.choice(string.ascii_letters)
    elif chc1 == 2:
        c1 = random.choice(string.digits)
    elif chc1 == 3:
        c1 = '_'
    if chc2 == 1:
        c2 = random.choice(string.ascii_letters)
    elif chc2 == 2:
        c2 = random.choice(string.digits)
    elif chc2 == 3:
        c2 = '_'
    if chc3 == 1:
        c3 = random.choice(string.ascii_letters)
    elif chc3 == 2:
        c3 = random.choice(string.digits)
    elif chc3 == 3:
         c3 = '_'
    if chc4 == 1:
        c4 = random.choice(string.ascii_letters)
    elif chc4 == 2:
        c4 = random.choice(string.digits)
    elif chc4 == 3:
        c4 = '_'
    elif chc4 == 4:
        c4 = c1
    elif chc4 == 5:
        c4 = c2
    if chc5 == 1:
        c5 = random.choice(string.ascii_letters)
    elif chc5 == 2:
        c5 = random.choice(string.digits)
    elif chc5 == 3:
         c5 = '_'
    elif chc5 == 4:
        c5 = c1
    elif chc5 == 5:
        c5 = c2
    words = [c1,c2,c3,c4,c5]
    username = ''
    for words in words:
        username += words + '' ''
    api = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=1999-7-7&Context=0"
    r = requests.get(api).json()
    if r['code'] == 0:
        print(username)
    elif r['code'] >= 2: 
        if uvu == 2:
            print('we tried :')
            print(username)
            print('and we got :')
            print(r)
            time.sleep(3.8)
            print('restarting')
            time.sleep(0.2)
while True:
    generate()
