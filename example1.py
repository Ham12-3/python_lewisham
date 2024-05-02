import re

# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the second number: "))
# # sum = num1 + num2
# # print("The sum of the two numbers is", sum)


# # # IF ELSE STATEMENT 

# # age = int(input("Enter your age: "))
# # if age >= 18:
# #     print("You are eligible to vote.")

# # elif age == 16:
# #     print("You will be eligible to vote next 2 year.")

# # elif age == 17:
# #     print("You will be eligible to vote next year.")

# # else:
# #     print("You are not eligible to vote.")


# # ## Challenge 1

# # # NESTED FOR LOOPS 

# # for i in range(6):
# #     for j in range(i):
# #         print("#", end="")
# #     print()


# # print("---------------------")


# # for i in range(3):
# #     for j in range(i):
# #         print("#", end="")
# #     print()
# # for i in range(3):
# #     for j in range(3-i):
# #         print("#", end="")
# #     print()


# # ### Challenge 2

# # # Check vowel or consonant alphabets 

# # char = input("Enter a character: ")

# # if char in ('a', 'e', 'i', 'o', 'u'):
# #     print(char + " is a vowel")

# # else:
# #     print(char + " is a consonant")



# # for i in range(1,10,2):
# #     print(i)
 

# # nums = int(input("Enter a number: "))
# # sums =0
# # for i in range(nums):
# #   sums += i
# # print("The sum of the numbers is", sums)



# # ### Challenge 3


# # num_3 = int(input("Enter a nnumber"))

# # for i in range(2,num_3+2,2):
# #     print(i)



# ### Challenge 4
    

# num_4 = int(input("Enter a number"))

# factorial = 1
# for i in range(1,num_4 +1):
#     factorial*=i

# print(factorial)


# ### Challenege 5



def validate_password(password):
    # define our regex pattern for validation
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

    # We use the re.match function to test the password against the pattern
    match = re.match(pattern, password)

    # return True if the password matches the pattern, False otherwise
    print(bool(match))



validate_password("mideswgvetugbeoltgiuyeg")
