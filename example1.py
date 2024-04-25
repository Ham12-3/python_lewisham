# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# sum = num1 + num2
# print("The sum of the two numbers is", sum)


# # IF ELSE STATEMENT 

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")

# elif age == 16:
#     print("You will be eligible to vote next 2 year.")

# elif age == 17:
#     print("You will be eligible to vote next year.")

# else:
#     print("You are not eligible to vote.")


# NESTED FOR LOOPS 

for i in range(6):
    for j in range(i):
        print("#", end="")
    print()


print("---------------------")


for i in range(3):
    for j in range(i):
        print("#", end="")
    print()
for i in range(3):
    for j in range(3-i):
        print("#", end="")
    print()



# Check vowel or consonant alphabets 

char = input("Enter a character: ")

if char in ('a', 'e', 'i', 'o', 'u'):
    print(char + " is a vowel")

else:
    print(char + " is a consonant")



for i in range(1,10,2):
    print(i)
 