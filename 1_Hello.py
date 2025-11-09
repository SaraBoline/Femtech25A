#Print statements
print ("Hello world")

#Use input and a variable 
print ("What is your name?")
myName = input()
print ("It is good to meet you," + myName)

#use a variable and a number OBS strings (always input) and integers
print ("The length of your name is: " + str(len(myName)))
print ("What is your age?")
myAge = input()
print ("On your next birthday you will be " + str(int(myAge) + 1) + ".")



#IF and ELSE 
print ("Do you want me to sing you a birthday song? please write Yes or No")
answer1 = input()

if answer1 == "Yes":
    print ("Happy birthday to you, happy birthday to you, happy birthday dear " + myName + " happy birthday to you")
else:
    print ("Okay")


#FOR LOOP 
print ("Do you want me to say Hurra the number of years?")
answer2 = input()

if answer2 == "Yes":
    for i in range(int(myAge)):
        print ("hurra")
else:
    print ("Okay")

print("HUUUUUURAAAAAAAA")
