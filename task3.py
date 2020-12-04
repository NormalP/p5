out_f = open("text3.txt", "r")
foodless = []
i = 0
f_sum = 0
for line in out_f:
    i += 1
    my_list = list(line.split())
    a = int(my_list[1])
    d_name = (my_list[0])
    f_sum = f_sum + a
    if a < 20000:
        foodless.append(d_name)
print(foodless)
print(f_sum//i)
out_f.close()