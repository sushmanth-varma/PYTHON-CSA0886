from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(["a"]))




