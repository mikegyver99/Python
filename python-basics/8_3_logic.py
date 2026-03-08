# word = str(input("Enter a word: "))

# if len(word) == 5:
#     print("Your input is 5 characters long")
# elif len(word) > 5:
#     print("Your input is greater than 5 characters long")
# else:
#     print("Your input is less than 5 characters long")

num = int(input("I'm thinking of a number between 1 and 10. Guess which one.: "))
# if num in range(1, 11):
# if 1 <= num <= 10:
if num >= 1 and num <=10:
    if num == 3:
        print("You win!")
    else:
        print("You lose")
else:
    print("Enter a number between 1 and 10")