def busca(vector, element):
    first = 0
    last = len(vector) - 1

    while(first <= last):
        middle = (last + first) // 2
        print(middle)
        if vector[middle] == element:
            return middle
        else:
            if vector[middle] < element:
                first = middle + 1
            else:
                last = middle - 1

    return False
