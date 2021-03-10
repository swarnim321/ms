def merge(first_array, second_array, m, n):
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n - 1, -1, -1):

        last = first_array[m - 1]
        j=m-2
        while j>=0 and first_array[j] > second_array[i]:
                ar1[j + 1] = ar1[j]
                j -= 1

        # If there was a greater element
        if (j != m - 2 or last > second_array[i]):
            first_array[j + 1] = second_array[i]
            second_array[i] = last


# Driver program

ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)

merge(ar1, ar2, m, n)

print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(ar1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i], " ", end="")