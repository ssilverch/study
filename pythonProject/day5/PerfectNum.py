"""
完全数
"""

#print("请输入所选范围上限：")
n = int(input('请输入所选范围上限：'))
for i in range(1,n):
    s=0
    for j in range(1,i):
        if i %j ==0:
            s += j
    if s == i:
        print("It's a perfect number:%d\n" % i)



