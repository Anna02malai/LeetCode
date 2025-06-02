import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card = {}
        for n in hand:
            card[n] = 1 + card.get(n, 0)
        
        minH = list(card.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in card:
                    return False
                
                card[i] -= 1
                if card[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
                
        return True

def main():
    hand = [1,2,4,2,3,5,3,4]
    groupSize = 4
    res = Solution()
    print(res.isNStraightHand(hand, groupSize))

if __name__ == "__main__":
    main()