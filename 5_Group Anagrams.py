from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    strs_dict = defaultdict(list)
    strs_lst = []

    for i in range(len(strs)):
        strs_dict[''.join(sorted(strs[i]))].append(strs[i])

    for i in strs_dict:
        strs_lst.append(strs_dict[i])

    return strs_lst





