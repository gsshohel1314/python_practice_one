# Global variable function er bahire create kora hoy.
# Gobal variable function er vetor and bahir theke je keou e use korte pare. 
x='awesome' # Global variable.
def myfunction():
    print('Python is ' + x)

myfunction() # Jehetu python e {} nai sehetu function create line and function call line same position theke hobe.
print('Also python is ' + x)

# global keyword use kore function er majhe global variable create kora jay.like,
def myfunction1():
    global x
    x='Beautiful'
    print(x)

myfunction1()
print(x)

# global keyword dara function er majhe globar variable er value change kora jay.like,
x='awesome'
def myfunction2():
    global x
    x='awesome chnaged by fantastic'
    print(x)

myfunction2()


