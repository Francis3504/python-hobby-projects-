def raise_pow(base_num,base_pow):
    result=1
    for i in range(base_pow):
        result *=base_num
    return result
a=raise_pow(2,3)
print(a)