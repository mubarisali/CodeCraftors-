def square(num):
    for i in range(num):
        for j in range(num):
            print(f"({i} {j}) " , end=" ")
        print()

square(10)

#function depends on num , it executes n square times.