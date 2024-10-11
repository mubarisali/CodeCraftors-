limit = int(input("Enter the limt of fibonnacci series : "))

f1 = 0
f2 = 1

if limit <= 0:
    print("Wrong entry for limit,Enter a positve number!")
elif limit == 1 :
    print(f1)
else:
    print(f1 , f2 , end=" ")  
    for i in range(2, limit):
        # f3 = f1 + f2
        # f1 = f2
        # f2 = f3       
        f1, f2 = f2, f1 + f2  
        print(f2, end=" ")  
    
