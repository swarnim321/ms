def find_missing(input):
    final_sum = sum(input)
    n = len(input) +1
    actual_sum = (n*(n+1)/2)
    return final_sum - actual_sum



def test(n):
  missing_element = random.randint(1, n)
  v = []
  for i in range(1, n):
    if i != missing_element:
      v.append(i)

  actual_missing = find_missing(v)
  print("Expected Missing = ", missing_element, " Actual Missing = ", actual_missing)
  assert missing_element == actual_missing


def main():
  for n in range(1, 10):
    test(1000000)

main()