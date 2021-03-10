def max_sub_array_of_size_k(k, arr):
    window_sum =0
    global_sum =0
    for i in range (len(arr)- k +1):
        window_sum =0
        for j in range(i,i+k):
            window_sum+=arr[j]
        global_sum =max(global_sum,window_sum)
    print(global_sum)
    return global_sum

print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
