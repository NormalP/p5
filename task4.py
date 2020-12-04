out_f = open("text4.txt", "r",encoding='utf-8')
my_f = open("text4,1.txt", "w",encoding='utf-8')
for line in out_f:
    my_list = list(line.split())
    a = (my_list[0])
    if a == "One":
        my_list[0] = "один"
    elif a == "Two":
        my_list[0] = "два"
    elif a == "Three":
        my_list[0] = "три"
    elif a == "Four":
        my_list[0] = "четыре"
    else:
        a = "Я ордынский воин и знаю только 1 2 3 4"
    my_string = ''.join(my_list)
    my_f.writelines(f"{my_string}\n")
out_f.close()
