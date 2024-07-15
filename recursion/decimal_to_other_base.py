"""
Author: Sai Sundeep Rayidi
Date: 7/10/2024

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


def decimal_to_binary(n):
    if n == 0 or n == 1:
        return n
    rem = n % 2
    return str(decimal_to_binary(n // 2)) + str(rem)


hex_chars = "0123456789ABCDEF"


def decimal_to_hexadecimal(n):
    if n == 0:
        return "0x"
    rem = n % 16
    return decimal_to_hexadecimal(n // 16) + hex_chars[rem]


octal_characters = "01234567"


def decimal_to_octal(n):
    if n == 0:
        return "0o"
    rem = n % 8
    return decimal_to_octal(n // 8) + hex_chars[rem]


def run_test_client():
    print(f"Running Decimal to Binary Test Cases ...")
    test_numbers = np.random.randint(2, 10000, 10)
    for test_i in test_numbers:
        print(f"{test_i}: {decimal_to_binary(test_i)}")
    print("=" * 100)

    print(f"Running Decimal to Hexadecimal Test Cases ...")
    test_numbers = np.random.randint(2, 10000, 10)
    for test_i in test_numbers:
        print(f"{test_i}: {decimal_to_hexadecimal(test_i)}")
    print("=" * 100)

    print(f"Running Decimal to Octal Test Cases ...")
    test_numbers = np.random.randint(2, 10000, 10)
    for test_i in test_numbers:
        print(f"{test_i}: {decimal_to_octal(test_i)}")
    print("=" * 100)


if __name__ == "__main__":
    run_test_client()
