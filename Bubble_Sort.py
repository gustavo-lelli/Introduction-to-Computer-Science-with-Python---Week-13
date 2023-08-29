def bubble_sort(vector):
    for i in range(len(vector) - 1, 0, -1):
        for j in range(i):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                print(vector)

    return vector
