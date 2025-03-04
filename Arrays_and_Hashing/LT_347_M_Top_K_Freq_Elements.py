class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count_d = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count_d[n] = 1 + count_d.get(n, 0)

        for num, count in count_d.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res        

def main():
    nums = [1,2,2,3,3,3]
    k = 2
    res = Solution()
    print(res.topKFrequent(nums, k))

if __name__ == "__main__":
    main()