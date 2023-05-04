import time
import sys
import random
import pprint
import pyperclip
import re
import requests as requests
import json
import cowsay as cowsay
import re
import pyinputplus as pyip
from pathlib import Path
import shelve
import os

# print(22 // 8)
"""i = 0
print("I am thinking of a number between 1 and 20")
while True:
    x = int(input("Guess the number "))
    if x < 16:
        print("Guess is too low")
        i += 1
        continue
    elif x > 16:
        print("Guess is too high")
        i += 1
        continue
    else:
        print(f"You're correct, you guessed my number in {i} trials")
        break"""
"""v = 0
increasing = True
try:
    while True:
        if increasing:
            print(" " * v, "########", sep='')
            time.sleep(0.1)
            v += 1
            if v == 20:
                increasing = False
        else:
            print(" " * v, "########", sep='')
            v -= 1
            if v == 0:
                increasing = True
except KeyboardInterrupt:
    sys.exit()"""

"""def collartz(x):
        if x % 2 == 0:
            return x // 2
        elif x % 2 == 1:
            return (x * 3) + 1

def main():
    while True:
        y = random.randint(1, 20)
        x = collartz(y)
        print(y, x)
        if x == 1:
            break

main()"""

"""name = ['victor', 'titus', 'sunday', 'peter']
for i, x in enumerate(name):
    print(f"The index of {x} in name is {i}")"""

"""num = [1,2,3,4,5,6,7,8,9,0]
for i in num:
    i %= 2
    print(i)"""

"""x = ['name', 'class', 'subject']
x.append("topic")
print(x)
x.insert(2,'date')
print(x)
del x[2]
print(x)
x.remove('name')
print(x)"""
'''spam = ['victor', 'titus', 'sunday', 'peter', 'chukwuma', 'irighogbe', 'musa', 'sarah', 'mercy']
for i, v in enumerate(spam):
    if i == len(spam) - 1:
        v = f'and {v}.'
    else:
        v = f"{v},"
    print(v, end=' ')'''
"""y = []
numberofstreaks = 0
for i in range(10000):
    x = random.randint(0, 1)
    if x == 0:
        y.append('H')
    else:
        y.append('T')
print(y)
for i in range(10000):
    if ['H'] * 6 == y[i:i+6] or ['T'] * 6 == y[i:i+6]:
        numberofstreaks += 1
    else:
        pass
print(numberofstreaks)
c = round((numberofstreaks / 10000) * 100, 1)
print(f"percentage of streaks: {c}%")"""

"""grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
v = ''
for c in range(6):
    for i in grid:
        v += (i[c])
for t in range(0, 54, 9):
    print(f"{v[t:t + 9]}")"""

# Building tic-tac-toe (imperative style)
"""def printboard():
    print(theboard['top-L'] + '|' + theboard['top-M'] + '|' + theboard['top-R'])
    print('_+_+_')
    print(theboard['mid-L'] + '|' + theboard['mid-M'] + '|' + theboard['mid-R'])
    print('_+_+_')
    print(theboard['low-L'] + '|' + theboard['low-M'] + '|' + theboard['low-R'])


theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': '', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
                    'low-M': ' ', 'low-R': ' '}

turn = 'X'
x = 0
o = 0
try:
    while True:
        theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': '', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
                    'low-M': ' ', 'low-R': ' '}
        for i in range(9):
            printboard()
            print("turn for " + turn + ".Which move")
            move = input()
            theboard[move] = turn
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            if theboard['top-L'] == theboard['top-M'] == theboard['top-R'] == "X":
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['mid-L'] == theboard['mid-M'] == theboard['mid-R'] == 'X':
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['low-L'] == theboard['low-M'] == theboard['low-R'] == "X":
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['top-L'] == theboard['mid-M'] == theboard['low-R'] == 'X':
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['low-L'] == theboard['mid-M'] == theboard['top-R'] == 'X':
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['top-R'] == theboard['low-R'] == theboard['mid-R'] == 'X':
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['mid-M'] == theboard['low-M'] == theboard['top-M'] == 'X':
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['low-L'] == theboard['top-L'] == theboard['mid-L'] == "X":
                print("Player X is the winner")
                x += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                continue
            elif theboard['top-L'] == theboard['top-M'] == theboard['top-R'] == "O":
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['mid-L'] == theboard['mid-M'] == theboard['mid-R'] == 'O':
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['low-L'] == theboard['low-M'] == theboard['low-R'] == "O":
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['top-L'] == theboard['mid-M'] == theboard['low-R'] == 'O':
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['low-L'] == theboard['mid-M'] == theboard['top-R'] == 'O':
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['top-R'] == theboard['low-R'] == theboard['mid-R'] == 'O':
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['mid-M'] == theboard['low-M'] == theboard['top-M'] == 'O':
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            elif theboard['low-L'] == theboard['top-L'] == theboard['mid-L'] == "O":
                print("Player O is the winner")
                o += 1
                print(f"Player_X_(wins) = {x}, Player_O_(wins) = {o} ")
                break
            else:
                print("It's a tie)
                break    

except KeyboardInterrupt:
    print("You have exited the game")
    sys.exit()"""

"""stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print(f"Total items = {item_total}")


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(addedItems[addedItems.index(i)], 1)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)"""

"""message = input("Enter an English sentence\n")
print("The pig latin format is given as :")
x = message.split()
y = ''
for i in x:
    if i[0].lower() in ('a', 'e', 'i', 'o', 'u'):
        if i.isupper():
            i += 'YAY'
        else:
            i += 'yay'
    elif i[0].lower() not in ('a', 'e', 'i', 'o', 'u'):
        if i.isupper():
            i = i[1:] + i[0] + "AY"
        else:
            i = i[1:] + i[0] + "ay"
    else:
        i = i
    y += " " + i
print(y)"""
"""tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

v = []
for c in range(0, 4):
    for i in tableData:
        v.append(i[c])
for b in range(0, 12, 3):
    y = v[b] + " " + v[b + 1] + " " + v[b + 2]
    print(y.rjust(20))"""

# grouping searches
"""phoneregx = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneregx.search("my number is 123-456-7899")
# print("Found a phone number " + mo.group())
areacode, cellnumber = mo.groups()
print(areacode)
print(cellnumber)"""

# optional searching using ? and |(pipe)
"""heroregex = re.compile(r"Bat(wo)?man|Superman")
v = heroregex.search("My favourite hero is Superman")
print(v.group())
v1 = heroregex.search("My favourite hero is Batman")
print(v1.group())
v2 = heroregex.search("My favourite hero is Batwoman")
print(v2.group())"""

"""wholestringisnum = re.compile(r'^\d+$')
x = wholestringisnum.findall("234212563456443")
print(x)"""

"""agent = re.compile(r"victor", re.I)
x = agent.sub('V*****', "victor is stupid, Victor is unserious, VICTOR is mad, VIcToR has not achieve anything this year")
print(x)"""

"""encode = re.compile(r"agent (\w)\w*", re.I)
x = encode.sub(r"\1******", "Agent Victor is determined to succeed, AGENT VICTOR has promised change his ways, AgENt VIctoR is going to succeed")
print(x)"""

# phone number and email address extractor
'''message = ''
matches = []
phoneregex = re.compile(r"(\d{3})?|(\(\d{3}\))(\s|-|\.)?(\d{3})(\s|\.|-)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,4}))?")
emailregex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+([\.a-zA-Z]{2, 4})")
for groups in phoneregex.findall(message):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum += 'x' + groups[8]
    matches.append(phonenum)
for i in emailregex.findall(message):
    matches.append(i[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("copied to clipboard: ")
    print('\n'.join(matches))
else:
    print("No phone number or email was found")'''

# date detection
"""text = ''
matches = []
dateregex = re.compile(r"(\d{2})(\\)(\d{2})(\\)(\d{4})")
for groups in dateregex.findall(text):
    date = "\\".join([groups[1], groups[3], groups[5]])
    day = groups[1]
    month = groups[3]
    year = groups[5]
    if 1 >= day or day >= 31:
        date += ' invalid day format'
    if month > 12 or month < 1:
        date += ' invalid month format'
    if year < 1000 or year > 2999:
        date += ' invalid year format'
    if str(month) in ['04', '06', '09', '11']:
        if day > 30:
            date += ' invalid day format'
    elif str(month) not in ['04', '06', '09', '11', '02']:
        if day > 31:
            date += ' invalid day number'
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if str(month) == '02':
            if day > 29:
                date += ' invalid day number'
    else:
        if str(month) == '02':
            if day > 28:
                date += ' invalid day number'

    matches.append(date)"""
# x = pyip.inputNum('Enter a number: ', limit=3, timeout=5, default='no response')
# print(x)


"""def addsuptoten(numbers):
    x = list(numbers)
    for i, digit in enumerate(x):
        x[i] = int(digit)
    if sum(x) != 10:
        raise Exception("The numbers ust add up to 10 not %s." % (sum(x)))"""

# multiplication quiz
"""questionnumber = 10
correctanswers = 0
for i in range(questionnumber):
    try:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        prompt = '#%s: %s x %s = ' % (i + 1 , num1, num2)
        x = pyip.inputInt(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=['.*', 'Incorrect'], limit=3, timeout=8)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        print("Correct!")
        correctanswers += 1
        time.sleep(1)
        print("%s / %s" % (correctanswers, questionnumber))"""

"""n = int(input("Number of rows "))
k = 0
for i in range(n):
    k += i
    m = n + k
for i in range(n):
    for j in range(i + 1):
        print(format(m, '<3'), end=' ')
        m -= 1
    print()"""

"""n = int(input("Number of rows "))
for i in range(n):
    m = i + 1
    for j in range(n-i-1):
        print(format(" ", '<3'), end='')
    for j in range(i+1):
        print(format("*", '<3'), end='')
    print(end=' ')
    for j in range(i+1):
        print(format(m, '<3'), end='')
        m += 1
    print()
for i in range(0, 2*n, 2):
    k = i//2
    for j in range(k):
        print(format(" ", '<3'), end='')
    for j in range(n-k):
        print(format(n-j, '<3'), end='')
    print(end=' ')
    for j in range(i, 2*n, 2):
        print(format(j+1, '<3'), end='')

    print()"""

# print(Path('spam', 'house', 'knife'))
# print(Path(r'C:\Users\al')/'bread'/'people')
# print(Path.cwd())
# os.chdir('C:/barrelrider')
# print(Path.cwd())
# print(Path.home())
# os.makedirs('C:\\Users\\victor\\stupidity')
# Path('C:\\victor\\stupidity').mkdir
# print(os.path.abspath("."))
# print(os.path.isabs(os.path.abspath(".")))
# print(os.path.abspath("victor"))
# print(os.getcwd())
x = Path.home()
# print(x.anchor, x.drive, x.parent, x.name, x.stem, x.suffix, sep='//')
# print(os.path.basename(x))
# print(os.path.dirname(x))
# parent, name = os.path.split(x)
# print(parent, name, sep='???')
# print(os.path.getsize(x))
"""print(x)
b = 0
for file in os.listdir(x):
    b += os.path.getsize(os.path.join('C:\\Users\\USER', file))
print(b, 'Bytes')
print(f"Size in kilobytes {round(b / 1024)}")
# print(os.listdir(x))"""
# y = Path('C:/Users/USER/Downloads')
# print(x.glob('*'))
# print(list(x.glob('*')))
"""print(list(y.glob('*.pdf')))
t = 0
for i in list(y.glob('*.pdf')):
    t += 1
print("You have %s pdf files in your download folder" % t)"""
# print(x.exists())
# print(x.is_file())
# print(x.is_dir())
"""c = Path('spam.txt')
c.write_text("Hello, world. My name is victor")
print(c.read_text())"""
# hellofile = open(Path.home() / "hello.txt")
# hellocontent = hellofile.read()
# print(hellocontent)
"""name = open('name.txt', 'w')
name.write("Victor Obiezue\n")
name.close()
name = open('name.txt', 'a')
name.write("Sunday Emmanuel\n")
name.write("Peter Isreal\n")
name.write("Victor Iri\n")
name.close()
name = open('name.txt')
p = name.read()
name.close()
print(p)"""
"""shelvfile = shelve.open('df')
cats = ['big', 'small', 'large']
shelvfile['cats'] = cats
shelvfile.close()
shelvfile = shelve.open('df')
print(shelvfile['cats'])
shelvfile.close()"""

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

"""for quiznumber in range(30):
    p = quiznumber + 1
    quizfile = open(f'capitalsquiz{p}.txt', 'w')
    answerfile = open(f'capitalsquiz_answers{p}.txt', 'w')
    quizfile.write('Name:\n\nDate:\n\nForm\n\n')
    quizfile.write((' ' * 20) + f'State Capitals Quiz(Form{p})')
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(50):
        correctanswers = capitals[states[questionnum]]
        wronganswers = list(capitals.values())
        del wronganswers[wronganswers.index(correctanswers)]
        wronganswers = random.sample(wronganswers, 3)
        answersoptions = wronganswers + [correctanswers]
        random.shuffle(answersoptions)

        quizfile.write(f"{questionnum + 1}. What's the capital of {states[questionnum]}?\n")
        for i in range(4):
            quizfile.write(f"    {'ABCD'[i]}. {answersoptions[i]}\n")
        quizfile.write('\n')

        answerfile.write(f"{qu  estionnum + 1}. {'ABCD'[answersoptions.index(correctanswers)]}\n")
    quizfile.close()
    answerfile.close() """
pprint.pformat(capitals)
print(capitals)













