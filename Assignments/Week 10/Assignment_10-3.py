def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s_to_t = {}
    map_t_to_s = {}

    for char_s, char_t in zip(s, t):
        if (char_s in map_s_to_t and map_s_to_t[char_s] != char_t) or (char_t in map_t_to_s and map_t_to_s[char_t] != char_s):
            return False
        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s

    return True

s = input()
t = input()
print(isIsomorphic(s, t))