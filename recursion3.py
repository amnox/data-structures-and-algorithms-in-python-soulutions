def binary_search(data,number, low, high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if number == data[mid]
            return True
        elif number < data[mid]:
            return binary_search(data, number, low, mid - 1)
        elif number > data[mid]:
            return binary_search(data, number, mid+1, high)