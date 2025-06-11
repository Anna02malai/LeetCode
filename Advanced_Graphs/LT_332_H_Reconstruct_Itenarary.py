class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        adj = {src : [] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)
                
                if dfs(v): 
                    return True
                
                adj[src].insert(i, v)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res

def main():
    tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
    res = Solution()
    print(res.findItinerary(tickets))

if __name__ == "__main__":
     main()   