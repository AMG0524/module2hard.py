def get_pass(n):
    pass_list_ = ''
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pass_list_ += str(i) + str(j)
    return pass_list_
for n in range(3, 21):
    pass_list_ = get_pass(n)
    print(f'{n} - {pass_list_}')




