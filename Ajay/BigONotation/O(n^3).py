def cube(num):
    for i in range(num):
        for j in range(num):
            for k in range(num):
                print(f"({i} {j} {k}) ",end=" ")
            print()
            
cube(4)

#function depends on n , it executes n cube times 
# n=4 means it'll run n^3 times which is 64