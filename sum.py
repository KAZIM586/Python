class Solution(object):
    def totalMoney(self, n):
        sum=0
        for i in range(1,n+1,1):
            sum=sum+i
        # print(sum)
        return sum
s=Solution()
print(s.totalMoney(4))
        