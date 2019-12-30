"""
 计算指定的年月日是这一年的第几天
"""

def is_leap_year(year):
    """
    判断指定的年份是不是润年

    :param year: 年份
    :return : 润年返回True 平年返回Flase
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,data):
    """
    计算传入的如期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return :第几天
    """

    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + data

def main():
    print(which_day(1980,11,28))
    print(which_day(1981,12,31))
    print(which_day(2018,1,1))
    print(which_day(2016,3,1))

if __name__ == '__main__':
    main()

