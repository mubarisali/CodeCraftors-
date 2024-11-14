def extract_numbers(str):
    num = []
    current_num = ""
    for ele in str:
        if ele.isdigit():  
            current_num += ele
        else:
            if current_num:
                num.append(int(current_num))
                current_num = ""
    if current_num:
        num.append(int(current_num))

    return num

print(extract_numbers("abc334v44d"))
print(extract_numbers("abv345fjjf123tyir45jf6th"))
print(extract_numbers("12jgskjh3shjy355ghgf2673ygs001ghhg9876"))