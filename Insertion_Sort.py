def insertion_sort(vector):
    for i in range(1, len(vector)):
        element = vector[i]
        j = i

        while(j > 0 and vector[j - 1] > element):
            vector[j] = vector[j - 1]
            j -= 1
        vector[j] = element

    return vector
