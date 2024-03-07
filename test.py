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

# how to show arrays
#  how list are organized, as below. its starts with zero. Zero = white
colorList = ["white","red","black","blue"]
numberList = [1,2,3]

# to add ot the list
colorList.append("pink")

#to travel the list
for temp in colorList:
    print(temp)

print(colorList[0])

# for(i=0;color.len;i++) the above is equivilant to JS
    # let temp = color[i]
        # console.log(temp)
#dictionary
me={
    "first_name":"Guillermo",
    "lasT_name":"Escobar",
    "month":"june",
    "age":"25",
}
print(me["first_name"])

me["age"] = 54
me["color"]="green"
print(me)
