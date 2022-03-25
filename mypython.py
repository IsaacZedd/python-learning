"""
       **********************************************
       *        Python Explanation in Coding !      *
       **********************************************
"""



"""
    output operations
"""
print('Hello World')#string output with ''
print("Hello Ethiopia")#string output with ""
print(1+4+6+19)#maths operation
print('12'+"34")#concatenating a string
print(2*2.0)#floating operation
print(2**3)#power of a number
print(20//7)#quotient
print(12%5)#remainder

print("He\'s \nSo \tgenius.\n")#escape characters
print(r"Hello\tGuys")#r used \t to be printed as txt
print("\\")
"""
    input operations
"""
input("Enter something :")#accept any type
input("Enter \nYour name :\nYour age :\nYour grade :\n")#accept any type
"""
  string operarions
"""
print("Hi"+","+'There')#3 strings concatenated to be printed
print("2"+'2')
print("Galuak"*3)
print('4'*3,"\n")
"""
    Type conversion
"""
print(int('12'))#string '12' will be converted & printed as an integer 12.
print(int('4')+int("6"))#the sum of 6 & 4 will be printed.
print(str(123))
print(float(32))
int(input("Enter an integer not another type :"))#inputs integer type only.
float(input('Enter a floating point number :'))
str(input("Enter some string word :\n"))
"""
   Variables operation
"""
fname="Isaac" #declaration
lname="Zed"
x=9.0#declaration

name="Isaac"#assigning(initialization)
num=7258#assigning(initialization)
print("Name: ",name)
print("ID: ",num,"\n")
"""
   Operators
"""
a=(1==2)
print(a)
b=(4>7)
print(b)
c=2**4#power of a number
print(c)
d=7
d+=10
print(d)
#e= c>d ? print("Nice Job.") : print("Lazy Work.")#ternary operator
print()
"""
   Control Statements
"""
ui='GUI'
print("This is my gui." if ui=='GUI' else "This is not my gui.")

mynum=10
grin=rot='Isaac' if mynum==10 else 'Zed'
print(grin)

q=5
if q%2==0:
    print(q,"is even number.")
else:
    print(q,"is odd number.")

s=5
f=7
o=6
if s>f:
    if s>o:
        print(s,"is greater.")
elif f>s:
    if f>o:
        print(f,"is greater.")
else:
    print(o,"is greater\n")
"""
  Boolean Logic
"""
r= True and False
print(r)

l=False or True
print(l)

p=not True
print(p,"\n")
"""
   Loops (while & for)
"""
#while loops
i=1
while i<5:
    print(i)
    i=i+1

j=0
while j<=6:
    print("Asgardia")
    j=j+1
#for loops

for ii in range(5):
    print(ii)

for jj in range(5,0,-2):
    print(jj)
    
worded="Hi ma nigga"
for wor in worded:
    print(wor)

for rr in range(7):
    print(rr)
    if rr==3:
        continue
    if rr==5:
        break

#break statement
u=1
while 1==1:
    print(u)
    u=u+1
    if u==4:
        print("Breaking the loop at 4\n")
        break

#continue statement
y=0
while True:
    print(y)
    y=y+1
    if y==4:
        print("Skipping 4")
        continue
    if y==8:
        print("Breaking the loop at 8\n")
        break
"""
   Lists in python(arrays in other prog. languages)
"""
numof=[]#empty List
num=[12,56,89.87,32]
print(num)
print(type(num))
name=["Python","is","Fun","!"]#declaration of list
for li1 in name:
    print(li1)
print(name)
print(name[3])
print(name[-3])#Indexing from right starts from -1
print(name[-4])
name1=['Hi','man']#initialization
print(name1)
print(name1[1])

#Mixed(Nested) List

mixed=['Hi',[12,4,2],76.45,"My name"]
print(mixed)
print(mixed[1])

#lists in strings

str1="Asgradia Spaceship"
print(str1[7])
"""
   List Operations
"""
n=[10,4,7,2,8]
n[2]=6
print(n)

n1=[1,2,3]
add=n1+[4,5,6]
print(add)
mult=n1*3
print(mult)

#keywords in & not in list operations(output is boolean value)
word=["I","am","asgardian","of","ethiopia","!"]
check1="asgard" in word
print(check1)
check2="ethiopia" in word
print(check2)

num21=[12,7,45,32,98]
c1=not 12 in num21
print(c1)
c2=not 34 in num21
print(c2)
"""
   List Functions
"""
nim=[10,20,30]
nim.append(40)#adds value to the end of list
print(nim)

nom=[1,4,6,8,3,9,4,2,8]
count=len(nom)#get number of items in a list
print(count)

nam=['My','is','Isaac']
ins=nam.insert(1,'name')#add an item at any position using index
print(nam)

chars=['w','u','r']
ind1=chars.index('u')
print(ind1)
ind2=chars.index('r')
print(ind2)

sunof=[23,98.2,2,8.21]
sumup=sum(sunof)#adds items in a list and give the sum
print(sumup)

sort=[23,87,1,43,92]
sorted1=sorted(sort)#sorts the items in a list
print(sorted1)

any1=[True,12,"Galuak",False]
anyc=any(any1)#return True if any boolean True value exist in the list
print(anyc)

any2=[True,False,12,'wer']
anyc1=all(any2)
print(anyc1)

#for more methods type dir(list) in the pyhton shell.
#max(name)->give the item with max value
#min(name)->give the item with min value
#name.count(item)->gives an item in which how many times it occur
#name.remove(item)->removes the item from the list

#range() funcion
nym=list(range(5))#creates sequential list of items with the given range
print(nym)
ano=list(range(3,10))#creates list start from 3 upto 9
print(ano)
print(range(10)==range(0,10))#boolean value is printed

nhm=list(range(5,15,2))#2 indicates the interval b/n the list to be created
print(nhm)

#list() function

lis1_str="How are ya brada?"
str_to_list=list(lis1_str)
print(str_to_list)
"""
  Tuples
"""
myf=()#empty tuple
mytuple=('Green','Red',123,56.67)
for tr in mytuple:
    print(tr)
print(mytuple)
print(mytuple[1])
print(mytuple[3])
print(mytuple[-2])#Indexing from right starts from -1
print(mytuple[-4])
single=('Hello',)
print(single)

#Tuple operations

tup1=("Hi","Ma","Nigga")
mul=(tup1*3)
print(mul)
adder=tup1+("Are","Ya","Fine","?")
print(adder)

#Tuple Booleans

tup=(2,12,78,89)
chu=2 in tup
chu2=not 78 in tup
print(chu)
print(chu2)

#Nested Tuples

numss=(12,6,87)
lette=('q','y','u')
nested=(numss,lette)
print(nested)

#tuple() function, for more methods type dir(tuple) in the python shell

conv=("The Last Ship")
covid=tuple(conv)
print(covid)
conv2=("is Fantastic Movie")
covid2=covid+tuple(conv2)
print(covid2)
