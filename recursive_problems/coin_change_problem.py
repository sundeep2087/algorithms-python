"""
Author: Sai Sundeep Rayidi
Date: 7/16/2024

Description:
[Description of what the file does, its purpose, etc.]

Additional Notes:
[Any additional notes or information you want to include.]

License: 
MIT License

Copyright (c) 2024 Sai Sundeep Rayidi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contact:
[Optional: How to reach you for questions or collaboration.]

"""
import numpy as np
np.random.seed(10)


def count_ways(coins, num_coins, amount):
    if amount == 0:
        return 1

    if amount < 0 or num_coins <= 0:
        return 0

    return count_ways(coins, num_coins - 1, amount) + count_ways(coins, num_coins, amount - coins[num_coins - 1])


def run_test_client():
    test_coins = [
        [1, 2, 3, 4, 5],
        [1, 2, 5],
        [10, 20, 50, 100, 200],
        [1, 5, 10]
    ]
    test_amounts = [20, 5, 2500, 50]
    for coins, amount in zip(test_coins, test_amounts):
        print(f"coins: {coins}\n"
              f"Amount: {amount}\n"
              f"Number of Ways: {count_ways(coins, len(coins), amount)}")
        print("=" * 100)


if __name__ == "__main__":
    run_test_client()