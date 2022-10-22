student = ["Labid", "Asim", "Muhsin", "Antara", "Salim"]
student.append("alim")
student[1] = "Basit"
print(student)

"""
immutable 
"""
stuff = [{"name":  "Amin", "age" : "25", "selary" : "40000"},
    {"name" : "Tuhin", "age" : "35", "selary" : "60000"},
    {"name" : "Saleh", "age" : "45", "selary" : "50000"}]
print(stuff)

for i in stuff:
    print(i["name"])
    print(i ["age"])

print(((300 + 200) - 250) * 12 / 2)

lines = '''Allah is our Khaliq.
Muhammad is the Masenger.
Abdullah is his father.
Amena is his mother,
and Baytullah is our Qibla'''
print(lines)

print(10 * ' Allah ')
rab = ' Allah '
print(rab * 10)

name1 = 'Amin'
name2 = 'Bashir'
tahiya = '''Assalamu yalaikum, my brother %s and %s, How are you? 
My students %s all are good'''


print(tahiya % (name1, name2, students))

list1 = 'a', 'b', 'c'
list2 = 1, 2, 3 
mylist = list1 + list2 
print(mylist)

age = '10'
converted_age = int(age)
age = 10
converted_age = str(age)

sl = 1
for x in range(1, 6):
    for y in range(101, 106):
        print(sl)
        print('Reg : %s' % x + ' Roll : %s' % y)
        sl = sl + 1

for i in range(1, 6):
    print('Reg : %s ' % i)

for s in students:
    print(s)
"""
students = ['Labib', 'Shahid', 'Salam', 'Nayem', 'Tuhin']
reg = 1
roll = 101
while(reg < 6 and roll < 116):
    print (students[reg - 1], reg, roll)
    reg = reg + 1
    roll = roll + 1

basic = 34000
incriment = (34000 / 100) * 5
Jeshdha = ((basic + incriment) / 100) * 10
Mul = basic + incriment + Jeshdha

"""
    