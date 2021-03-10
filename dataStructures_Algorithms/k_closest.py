def find_closest_element(arr, K, X):
  result = []
  # TODO: Write you
  index = arr.index(X)
  print(index)
  if index >= K:
    result.append(arr[index-K+1:index+1])
  else:
    result.append(arr[0:K])
  print( result)

find_closest_element([2, 4, 5, 6, 9], 3,6)