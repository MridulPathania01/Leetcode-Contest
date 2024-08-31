class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        a1=str(num1).zfill(4)
        a2=str(num2).zfill(4)
        a3=str(num3).zfill(4)
        k=""
        for i in range(4):
            k+=min(a1[i],a2[i],a3[i])
        k=k.lstrip('0')
        return 0 if k==""else int(k)