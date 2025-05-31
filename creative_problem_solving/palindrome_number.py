"""
Author: Sai Sundeep Rayidi
Date: 1/30/2025

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

def palindrome(num):
    if (num < 0) or (num % 10 == 0 and num != 0):
        return False

    reversed_half = 0
    while num > reversed_half:
        reversed_half = (reversed_half * 10) + (num % 10)
        num = num // 10

    return num == reversed_half or num == reversed_half // 10


if __name__ == "__main__":
    print(f"Num: 121 | Palindrome: {palindrome(121)}")
    print(f"Num: 12321 | Palindrome: {palindrome(12321)}")
    print(f"Num: 1231 | Palindrome: {palindrome(1231)}")
    print(f"Num: 000 | Palindrome: {palindrome(000)}")
    print(f"Num: 1210 | Palindrome: {palindrome(1210)}")
    print(f"Num: -121 | Palindrome: {palindrome(-121)}")
    print(f"Num: 11111111 | Palindrome: {palindrome(11111111)}")