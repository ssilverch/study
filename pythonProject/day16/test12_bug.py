"""
分治法例子：快速排序
快速排序 - 选择枢轴对元素进行划分左边都比枢轴小右边都比枢轴大
"""

def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)

def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)

def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i+1], items[end] = items[end], items[i+1]
    return i+1

def main():
    array = [23,45,64,75,76,43,6,3,41,34,2,4,53,]
    print(array)
    a = quick_sort(array)
    print(a)

if __name__ == '__main__':
    main()
