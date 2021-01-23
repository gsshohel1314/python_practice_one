#String Literals:
#Python e string single quotation '' or double quotation "" er majhe likhte hoy.like_ 'Hello' or "Hello"
print('Hello')
print("Hello")

#Assign string to a variable:
a='Shohel'
b="Rana"
print(a)
print(b)

#Multiline Strings:
#Multiline string ke three single quotation or three double quotation dara variable er majhe rakha jay. Like_
a='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

b="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor           incididunt
ut labore et dolore magna aliqua."""
print(b)
#Note: a khetre code e je vabe line break dibo result e sei vabei line break show korbe.

#Strings are Arrays:
#Python e string array hisabe kaj kore.Ekhane string er firat charecter index 0 theke suru hoy. Like_
a="Hello, World!"
print(a[0])
print(a[3])
print(a[5])
print(a[6])
print(a[7])
print(a[12])
#print(a[13]) ->IndexError: string index out of range. Karon ekhane 13 ta charecter nai.

#Slicing:
#Eta dara amra charecter er range orthat akta slic er modddhe koyta charecter ace ta print korte parbo.
#Ekhetre start index and end index er range set kore deya hoy. Start index theke end index porjonto joto gula charecter ace sob show korbe sudhu matro end index er charecte bade. Jodi range 2 theke 5 dei tahole 3 ta charecter print korbe karon 5 no index er charecter ta bad jabe.Like_
a='Hello, World!'
print(a[2:5])
print(a[2:7])
print(a[2:8])

#Negative Indexing:
#Eta dara string ta ulta dik theke slic korbe orthat string er last charecter hobe index 1. Like_
a="Hello, World"
print(a[-5:-2])
print(a[-6:-2])
print(a[-7:-2])

#String Length:
#len() function dara akta string er length porimap kora jay. Like_
a='Hello, World!'
print(len(a))
b=len("Shohel Rana")
print(b)

#Check String
txt='The rain in Spain stays mainly in the plain'
x='ain' in txt
z='ain' not in txt
y='w' in txt
a='shohel' not in txt
print(x)
print(z)
print(y)
print(a)

#String Concatenation
a='Hello'
b='world!'
c=a + b
d=a + ' ' + b
print(c)
print(d)

#String Format
# we cannot combine strings and numbers. But we can combine strings and numbers by using the format() method!
age=25
txt='I am shohel, and I am {} years old'
print(txt.format(age))

#The format() method takes unlimited number of arguments.
quantity=3  #index 0
item=50     #index 1
price=1000  #index 2
order='I want {} pieces of item {} for {} taka'
pay='I want to pay {2} taka for {0} pieces of item {1}.'
print(order.format(quantity,item,price))
print(pay.format(quantity,item,price))

#Escape Character
#Akti string er majhe oboidho character babohar korar jonno escape character use kora hoy.
# amra double quote er majhe " quote and single quote er majhe ' quote dite parina.jodi diye chai tahole ' ba " er age \ dite hoy.
a="We are the so-called \"Vikings\" from the north"
b='My name is \'shohle\'. I am a programmer'
print(a)
print(b)

# \' single quote
c='It\'s alright'
print(c)

# \\ blackslash
d='This will insert one \\ blackslash'
e='This will insert two \\\\ blackslash'
f='This will insert three \\\\\\ blackslash'
print(d)
print(e)
print(f)

# \n new line
g='Hello,\nworld!'
print(g)

# \r carriage return. je koyta character er age \r dibo sei koyta character dara string er first er thik oi koyta character replace korbe.
h='Javaaa is a best programming language \rPython'
print(h)

# \t tab
i='I am\tshohel'
print(i)

# \b Backspace.ata dare akta space remove kore pichone back kore.
j='I am \bshohel'
print(j)

# \f Form Feed
#output:
'''
I am
    shohel
'''
h='I am \fshohel'
print(h)

# String Methods
#strip()-> ei method surur abong sesh er sob space gula remove kore.
a = "   Hello, World!   "
print(a.strip())

# lower(), casefold()-> ei method string ke lower case e rupantor kore.
a = "HELLO, WORLD!"
print(a.lower())
b='SHOHEL RANA'
print(b.casefold())

# upper()-> ei method string ke upper case e rupantor kore.
a = "hello, world!"
print(a.upper())

#replace()-> ei method akta string ke onno akta string dara replace kore.
a ="Hello, World!"
print(a.replace('H', 'J').replace('W', 'X'))

#split()-> akta string ke sub string e prinoto kore.
a ="Hello World Hello World"
print(a.split())

# capitalize()->string er first letter ke capital letter e prinoto kore.
a = "hello, and welcome to my world."
print(a.capitalize())

#center()-> ei method string ke center e niye jay.
a="Shohel"
print(a.center(50))

#

