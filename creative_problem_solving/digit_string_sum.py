"""
Author: Sai Sundeep Rayidi
Date: 1/24/2025

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


def calc_sum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    n1 = len(str1)
    n2 = len(str2)
    str1 = str1[::-1]
    str2 = str2[::-1]

    res_str = ""
    carry = 0

    for i in range(n1):
        sum = (ord(str1[i]) - 48) + (ord(str2[i]) - 48) + carry
        res_str += chr(sum % 10 + 48)
        carry = sum // 10

    for i in range(n1, n2):
        sum = (ord(str2[i]) - 48) + carry
        res_str += chr(sum % 10 + 48)
        carry = sum // 10

    if carry:
        res_str += chr(carry + 48)

    res_str = res_str[::-1]
    return res_str


if __name__ == "__main__":
    digit_string1 = "100"
    digit_string2 = "10"
    res_sum = calc_sum(digit_string1, digit_string2)
    print(res_sum)