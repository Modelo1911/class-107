print("hello world")

# let variable = 21
variable = 21 # in python nothing more is needed to add
name = "Guillermo"
last_name = "Escobar"
total = "99.99"
age = 25
found = True

# if/else statment
# if(var==var2){
# logic
# }
if age< 100:
    print("be not afraid")# here a space is required before "print", else an error will occur.
elif age == 100:
    print("congratulations you are a century")
else:
    print("Sorry, seems you are too old")

#functions
    
def say_hello():
    print("hello there")

def say_goodbye(name):
    print("Goodbye " + name)

# call a function
say_hello()
say_goodbye(" Guillermo")

# concatination
print(" Hello my name is "+ name + " and I am "+ str (age) +" years old")

