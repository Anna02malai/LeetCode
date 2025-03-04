class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res
    
    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1 +length

        return res 

def main():
    s = ["leet","code","love","you"]
    res = Solution()
    e_res = res.encode(s)
    d_res = res.decode(e_res)
    print(d_res)

if __name__ == "__main__":
    main()