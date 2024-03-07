while True:
    number = 5
    user_input = input("Guess the number: ")
    user_input = int(user_input)
    if user_input == number:
        print("Congratulations! You got it!")
        break
    else:
        print('Try again')
