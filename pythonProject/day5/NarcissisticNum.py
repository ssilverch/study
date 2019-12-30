"""
寻找水仙花数
"""
#function1
"""
for num in range(100,1000):
    a = int(num/100)
    b = int(num%100/10)
    c = int(num%10)
    if pow(a,3) + pow(b,3) + pow(c,3) == num:
        print(num)
"""


#function2
def narcissistic_number_1(num):
    length = len(str(num))
    count = length
    num_sum = 0
    while count:
        num_sum += ((num // 10 ** (count-1)) % 10) ** length
        count -= 1
    else:
        if num_sum == num:
            print('%d is %d bit narcissistic_number' % (num, length))
        else:
            print('%d is not a narcissistic_number' % num)

#function3
def narcissistic_number_2(num):
    original_num = num
    s = str(original_num)
    length = len(s)
    count = length
    sum_num = 0
    while count:
        sum_num += int(s[count - 1]) ** length
        count -= 1
    else:
        if sum_num == num:
            print('%d is %d bit narcissistic_number' % (num, length))
        else:
            print('%d is not a narcissistic_number' % num)

max_num = int(input('请输入最大范围：'))
#获取小于制定数的阿姆斯特朗数
for num in range(0,max_num):
    narcissistic_number_2(num)
