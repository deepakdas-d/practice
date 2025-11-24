
# s="abcabcbb"
def longest_substring(s):
    char=set()
    lft=0
    max_len=0
    for rgt in range(len(s)):
        while s[rgt] in char:
            char.remove(s[lft])
            lft+=1
        else:
             char.add(s[rgt])
             max_len=max(max_len,rgt-lft+1)
    return max_len
 

print(longest_substring("abcabcbb"))