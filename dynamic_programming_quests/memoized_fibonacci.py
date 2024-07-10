"""
Author: Sai Sundeep Rayidi
Date: 7/10/2024

Description:
Demonstrates the efficiency of memoization in a simple problem - calculating fibonacci numbers.

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

import time


def simple_fibonacci(n):
    if n == 0 or n == 1:
        return n
    return simple_fibonacci(n - 1) + simple_fibonacci(n - 2)


# Dictionary to store Fibonacci Values already computed
memoized_fibonacci_values = {}


def memoized_fibonacci(n):
    if n == 0 or n == 1:
        return n
    if n in memoized_fibonacci_values.keys():
        return memoized_fibonacci_values[n]
    else:
        memoized_fibonacci_values[n] = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
        return memoized_fibonacci_values[n]


def run_test_client():
    print("*" * 100)
    t1 = time.time()
    for i in range(1, 25):
        print(simple_fibonacci(i))
    print(f"Elapsed Time: {(time.time() - t1):.5f}")
    print("*" * 100)

    t1 = time.time()
    for i in range(1, 25):
        print(memoized_fibonacci(i))
    print(f"Elapsed Time: {(time.time() - t1):.5f}")
    print("*" * 100)

    print(f"Calculating Fibonacci numbers between 35 and 40 using non-memoized process...")
    t1 = time.time()
    for i in range(35, 40):
        print(simple_fibonacci(i))
    print(f"Elapsed Time: {(time.time() - t1):.5f}")
    print("*" * 100)

    print(f"Calculating Fibonacci numbers between 35 and 40 using Memoized process...")
    t1 = time.time()
    for i in range(35, 40):
        print(memoized_fibonacci(i))
    print(f"Elapsed Time: {(time.time() - t1):.5f}")
    print("*" * 100)

    print(f"Calculating Fibonacci numbers between 250 and 300 using Memoized process...")
    t1 = time.time()
    for i in range(250, 300):
        print(memoized_fibonacci(i))
    print(f"Elapsed Time: {(time.time() - t1):.5f}")
    print("*" * 100)


if __name__ == "__main__":
    run_test_client()