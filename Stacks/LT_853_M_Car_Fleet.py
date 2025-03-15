class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        pair = [[p, s] for p, s in zip(position, speed)]

        stk = []
        for p, s in sorted(pair)[::-1]:
            stk.append((target - p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()      
        return len(stk)

def main():
    tgt = 10
    pos = [6,8]
    spd = [3,2]
    res = Solution()
    print(res.carFleet(tgt, pos, spd))

if __name__ == "__main__":
    main()