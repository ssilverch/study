def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) -1 
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def main():
    array = [x for x in range(0,1000)]
    print(seq_search(array,1002))

    print(bin_search(array,999))
    print(bin_search(array,2000))
if __name__ == '__main__':
    main()
