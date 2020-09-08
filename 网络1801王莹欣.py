import random
check=''
for num in range(4):
    i= random.randrange(1,3)
    if i%2==0:
        check_num = random.randrange(65,91)
        check_str = chr(check_num)
        check=check +check_str
    else:
        check_num = random.randrange(49,58)
        check_str = chr(check_num)
        check=check + check_str
print(check)
