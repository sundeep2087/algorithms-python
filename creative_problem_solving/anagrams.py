"""
Author: Sai Sundeep Rayidi
Date: 7/7/2024

Description:
Given a String. Return the minimum number of elemsnts to change in
the first half of the string to make the two half anagrams.

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

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    string1, string2 = s[:len(s) // 2], s[len(s) // 2:]
    if (string1 == string2) or (string1 == string2[::-1]) or (string2 == string1[::-1]):
        return 0
    else:
        print(string1, string2)
        counter = 0
        charac_seen_list = []
        for charac in string2:
            if charac not in charac_seen_list:
                charac_seen_list.append(charac)
                ch_count1 = string1.count(charac)
                ch_count2 = string2.count(charac)
                if ch_count2 > ch_count1:
                    counter += abs(ch_count2 - ch_count1)
        return counter


if __name__ == "__main__":
    res = anagram("fdhlvosfpafhalll")
    print(res)

    res = anagram("abbabbbb")
    print(res)

    res = anagram("superdupef")
    print(res)

    res = anagram("moldinboldofl")
    print(res)



# 1335