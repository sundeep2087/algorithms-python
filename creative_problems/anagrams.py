# Created by Sai at 7/7/2024

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
