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

    carry = 0
    res_sum = ""

    for i in range(n1):
        sum = (ord(str1[i]) - 48) + (ord(str2[i]) - 48) + carry
        res_sum += chr(sum % 10 + 48)
        carry = sum // 10

    for i in range(n1, n2):
        sum = (ord(str2[i]) - 48) + carry
        res_sum += chr(sum % 10 + 48)
        carry = sum // 10

    if carry:
        res_sum += chr(carry + 48)

    res_sum = res_sum [::-1]
    return res_sum


def check_sum_string_util(digit_string, beg, len1, len2):
    str1 = digit_string[beg: beg+len1]
    str2 = digit_string[beg+len1: beg+len1+len2]
    str3 = calc_sum(str1, str2)

    str3_len = len(str3)
    if str3_len > (len(digit_string) - (beg+len1+len2)):
        return False

    if str3 == digit_string[beg+len1+len2: beg+len1+len2+str3_len]:
        if len(digit_string) == (beg+len1+len2+str3_len):
            return True
        return check_sum_string_util(digit_string, beg+len1, len2, str3_len)
    return False


def is_sum_string(digit_string):
    n = len(digit_string)
    if n >= 3:
        for i in range(1, n):
            for j in range(1, n-i):
                if check_sum_string_util(digit_string, 0, i, j):
                    return True
    return False


if __name__ == "__main__":
    print(is_sum_string("1212243660"))
    print(is_sum_string("111112223335"))
    print(is_sum_string("1235"))
    print(is_sum_string("1267"))