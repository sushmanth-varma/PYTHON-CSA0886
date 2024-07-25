import os
def prefix(strs):
    if not strs:
        return ""
    return os.path.commonprefix(strs)
print(prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(prefix(["dog", "racecar", "car"]))     # Output: ""
