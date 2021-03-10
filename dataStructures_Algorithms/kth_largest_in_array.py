import heapq

def find_kth_largest(ints,k):
    pq=ints[0:k]
    print(pq)
    heapq.heapify(pq)
    print(pq)
    for i in range(k,len(ints)):
        if ints[i]>pq[0]:
            heapq.heapreplace(pq,int[i])
    return pq[0]

if __name__ == '__main__':

    ints = [7, 4, 6, 3, 9, 1]
    k = 2

    print("K'th largest element in the list is", find_kth_largest(ints, k))