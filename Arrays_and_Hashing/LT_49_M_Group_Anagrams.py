from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h_map = defaultdict(list)

        for s in strs:
            count = [0] *26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            h_map[tuple(count)].append(s)
        
        return h_map.values()

def main():
    strs = ["act","pots","tops","cat","stop","hat"]
    res = Solution()
    print(res.groupAnagrams(strs))

if __name__ == "__main__":
    main()