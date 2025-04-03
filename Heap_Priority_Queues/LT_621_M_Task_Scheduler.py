from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [int(-c) for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        t = 0

        while maxHeap or q:
            t += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t

def main():
    tasks = ["A","A","A","B","B","B"]
    n = 2
    res = Solution()
    print(res.leastInterval(tasks, n))

if __name__ == "__main__":
    main()