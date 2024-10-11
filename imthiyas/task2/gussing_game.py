number = int(input("guess a number between 1-100: "))
guess_number= 0


while guess_number==number:
    print("right answer")
    if number > guess_number:
        print("its too high")
    else:
        print("the number is too low")