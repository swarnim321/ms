from heapq import *

class KthLargestNumberInStream:
    minheap = []
    def __init__(self, nums,k):
        self.k =k
        for num in nums:
            self.add(num)

    def add(self, num):
        heappush(self.minheap, num)
        if len(self.minheap)> self.k:
            heappop(self.minheap)
        return self.minheap[0]

def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))

main()