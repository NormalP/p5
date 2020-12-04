out_f = open("text2.txt", "r")
i = 0
for line in out_f:
    i += 1
    my_list = list(line.split())
    num = len(my_list)
    print(f"Количество слов = {num}")
print(f"Количество строк = {i}")

out_f.close()