for num_cock in range(0,100):
    for num_hen in range(0,100):
        if 14*num_cock + 8*num_hen - 200 == 0 and 100 - num_hen-num_cock >=0:
            print('公鸡{0}只，母鸡{1}只，雏鸡{2}只'.format(num_cock,num_hen,(100-num_cock-num_hen)))
