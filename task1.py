my_f = open("text.txt", "w")
a=[]
i=True
while i:
   i=input()
   if i: a.append(f'{i}\n')
my_f.writelines(a)
my_f.close()