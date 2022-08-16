# time: O(n) | space: O(n) (n is the length of s or t if they are the same length)
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # make a dictionary from s ( O(n) )
    dict_s = {}
    for i in range(len(s)):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1

    # O(n)
    for i in range(len(t)):
        key = t[i]
        if key in dict_s:
            if dict_s[key] == 1:
                dict_s.pop(key)
            elif dict_s[key] > 1:
                dict_s[key] -= 1
            else:
                return False

    return True

# time: O(nlogn) | space: O(1)
def isAnagram2(s: str, t: str) -> bool:
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))
    return s == t

isAnagram("car", "rat")