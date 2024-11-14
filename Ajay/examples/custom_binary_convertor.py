num = int (input("Enter a psoitive number : "))

def num_to_binary(num):
    binary = ""
    if num < 0:
        print("Wrong input")
    if num == 0:
        return 0
    else:
        while num > 0 :
            bit = num % 2
            binary =str(bit) + binary
            num = num // 2
        return binary
    

binary_digit = num_to_binary(num)

print(binary_digit)