"""排序算法(选择、冒泡和归并)和查找算法(顺序和折半)"""
def select_sort(origin_items, comp=lambda x, y : x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def main():
    array = [3,4,6,5,4,3,2,6,8,98,65,44,23,13]
    a = select_sort(array)
    print(a)

if __name__ == '__main__':
    main()
