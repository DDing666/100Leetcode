#https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         mp = collections.defaultdict(list)

#         for st in strs:
#             key = "".join(sorted(st))
#             mp[key].append(st)
        
#         return list(mp.values())
import collections
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
mp = collections.defaultdict(list)

for st in strs:
    
    key = "".join(sorted(st))
    mp[key].append(st)
    print(st, mp, key, "".join(sorted(st)))

print(list(mp.values())) 
