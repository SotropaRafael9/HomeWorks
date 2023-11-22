from sys import maxsize
def two_subsets_with_minimal_differance_naive(sequence_of_numbers, number_of_elements)
    result_1 = []
    result_2 = []
    minimal_difference = maxsize
    for i in range (0, 2 ** number_of_elements):
        subset_1 = []
        subset_2 = []
        subset_difference = 0
        for j in range (number_of_elements):
            if (i & (1 << j))
                subset_1.appent(sequence_of_numbers_[j])
                subsets_difference -= sequence_of_numbers[j]
            else:
                subset_2.append(sequence_of_numbers[j])
                subsets_difference -= 
