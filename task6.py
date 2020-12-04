
out_f = open("text6.txt", "r", encoding='utf-8')
for line in out_f:
    s = (line)
    my_l = len(s)
    integ = []
    final = []
    i = 0
    sbg_name = list(line.split())
    final.append(sbg_name[0])
    while i < my_l:

        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < my_l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))

    final.append(sum(integ))
    print(final)
