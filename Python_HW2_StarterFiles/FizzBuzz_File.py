import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    # If dtype not specified, can return error for below codes
    out_list = np.array(nums, dtype=object)

    # Create masks for conditions
    fizz_mask = (nums % 3 == 0)
    buzz_mask = (nums % 5 == 0)

    # Apply condition
    out_list[fizz_mask] = "fizz"
    out_list[buzz_mask] = "buzz"
    out_list[fizz_mask & buzz_mask] = "fizzbuzz"

    # Use tolist() return a Python list, otherwise a numpy array
    return out_list.tolist()
