import heapq
from heapq import heappop, heappush

def sort_k_sorted_arr(list,k):
    pq=list[0:k+1]
    heapq.heapify(pq)
    index =0
    for i in range (k+1, len(list)):
        list[index]=heappop(pq)
        index+=1
        heappush(pq,list[i])
    while pq:
        list[index]=heappop(pq)
        index+=1


if __name__ == '__main__':
    list = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2

    sort_k_sorted_arr(list, k)
    print(list)
