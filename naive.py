
# Input: 
#  integers = [i_0, i_1, ..., i_n]
#  The set of n integers.
#
#  target = integer
#
# Output:
#  subset_exists = boolean representing the answer to the question
#   "Does there exist a subset of integers that sums to the target?"
#  subset_indices = [p_0, p_1, ..., p_k]
#   Each element in this array corresponds to the index of the element
#   in the array of integers that is included in the subset that sums
#   to the target.

class subset_decorator(object):
  def __init__(self, f):
    self.f = f

  def __call__(self, integers, target):
    print("Set of integers: {0}".format(integers))
    subset_exists, subset_indices = self.f(integers, target=0)
    if subset_exists:
      print("Subset: {0}".format([integers[i] for i in subset_indices]))
    else:
      print("No subset exists")
    return subset_exists, subset_indices


@subset_decorator
def solve(integers, target=0):
  n = len(integers)
  for subset_binary in range(1, 2**n):
    subset_indices = construct_subset_indices(subset_binary)
    sum_of_subset = sum([integers[i] for i in subset_indices])
    if sum_of_subset == target:
      return True, subset_indices

  return False, None


def construct_subset_indices(subset_binary):
  subset_indices = []
  index = 0
  current_binary = subset_binary
  while current_binary:
    # Extract least significant bit
    bit_of_interest = current_binary & 1
    # Check if that bit is a 1
    if bit_of_interest:
      # If it is a 1, append its index in the subset of indices
      subset_indices.append(index)

    # Shift to the next bit
    current_binary = current_binary >> 1
    index += 1
  
  return subset_indices


if __name__ == "__main__":
  test_binary = '1010000101'
  test_number = 645
  expected_subset_indices = [0, 2, 7, 9]
  assert expected_subset_indices == construct_subset_indices(test_number)

  sample_integers = [4, 2, 8, 3, -9, -5]
  actual_result, actual_subset_indices = solve(sample_integers)
  assert actual_result, "False negative"

  sample_integers = [-12, 13, 18, 19]
  actual_result, actual_subset_indices = solve(sample_integers)
  assert not actual_result, "False positive"
