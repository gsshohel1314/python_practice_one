# local variable function er vetor create kora hoy.
# local variable sudhu matro function er vetor ei use kora jay.
# local variable and global variable er name same holeo problem nai.
x='Shohel Rana' # global variable 
def myFunction():
    x='awesome' # local variable 
    print("Python is " + x) # local variable print
myFunction()
print("My name is " + x) # global variable print