# str data type:
x="Hello World " # x=str('shohel')
y=type(x)
print(x , y) 

# int data type:
x=20            # x=int(20)
y=type(x)
print(x , y)

# float data type:
x=20.5            # x=float(20.5)
y=type(x)
print(x , y)

# complex data type:
x=1j                # x=complex(1j)
y=type(x)
print(x , y)

# list data type:
x=['apple','banaba','mango']   # x=list(('apple','banana','mango'))
y=type(x)
print(x , y)

# tuple data type:
x=('apple','banana','mango')   # x=tuple(('apple','banana','mengo'))
y=type(x)
print(x , y)

# range data type:
x=range(6)
y=type(x)
print(x , y)

# dict data type:
x={'name' : 'shohel','age' : 25}   # x=dict(('name' : 'shohel', 'age' : 25))
y=type(x)
print(x , y)

# set data type:
x={"apple",'banana',"mango"}   # x=set(('apple','banana','mango'))
y=type(x)
print(x , y)

# froxenset data type:
x=frozenset({'apple','banana','mango'})  # x=frozenset(('apple','banana','mango'))
y=type(x)
print(x , y)

# bool data type:
x=True            # x=bool(5)
y=type(x)
print(x , y)

# bytes data type:
x=b'Hello'         # x=bytes(5)
y=type(x)
print(x , y)

# bytearray data type:
x=bytearray(6)
y=type(x)
print(x , y)

# memoryview data type:
x=memoryview(bytes(10))
y=type(x)
print(x , y)