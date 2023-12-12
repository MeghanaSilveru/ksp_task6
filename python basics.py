print("hello world")
#this is a print statement
number=10
if number==100:
    print("this is correct")
else:
    print("this is incorrect")
number1=20
number1=30
print("number1=",number1)
number2=30 #integer type
name="megna"#string type
age=21
print(name)
print(age)

# if else 
score=50
if score>=75:
    print("Distinction marks")
elif score>=65:
    print("first class marks")
elif score>=50:
    print("second class marks")
elif score>=40:
    print("just pass")
else:
    print("not qualified")
    
    
# arithmetic operators
result=number+number2
print("result:", result)
result1=number-number2
print("result1:", result1)
result2=number2/number
print("result2:", result2)
result3=number*number2
print("result3:", result3)

#assignment operators
number += 10     # number=number+10
print(number)
number2 -= 5     # number2=number2-5
print(number2)
number *= 10     #at number is updated to 20 that means number=20*10
print(number)
number /= 10     # number=200/10
print(number)

#comparision operators
A=10
B=20
C=20
equal = A == B
print("A equal to B:", equal)
notequal = A != B
print("A not equal to B:", notequal)
greaterthan = B > C
print("B greaterthan C:", greaterthan)
lesserthan = A <= B
print("A lesserthan and equal to B:", lesserthan)

# logical operators
X = A == B and B == C # false + true = false
print(X)
X = A == B and A == B # false + false = false
print(X)
X = A < B and B > A  # true + true = true
print(X)
X = B == C and A == B # true + false = false
print(X)
X = A == B or B == C # false + true = true
print(X)
X = A == B or A == B # false + false = false
print(X)
X = A < B or B > A  # true + true = true
print(X)
X = B == C or A == B # true + false = true
print(X)
X = not (A == B or B == C) # !(false + true) = false
print(X)
X = not (A == B or A == B) # !(false + false) = true
print(X)


count=0
while count < 10:
    print("meghana")
    count += 1
    
count1=0
for number in range(0,6):
    print(count1)
    count1 += 1
    
count2=10
for number in range(-1,10):
    print(count2)
    count2 -= 1
    

def HELLO():
    print("I LOVE YOU")
HELLO()

    




