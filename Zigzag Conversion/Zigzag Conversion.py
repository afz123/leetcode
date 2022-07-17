class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=list(s)
        matix_num=len(l)//(numRows+numRows-2)
        for i in range(numRows):
            for j in range(matix_num):
                output=l[i*(numRows+2)]+' '+' '
                if j==matix_num:
                    output+='\n'
        print(output)


s='dsfisdkfjsdf'
numRows=4

l=list(s)
print(l)
output=str()
matix_num=len(l)//(numRows+numRows-2)
#print(matix_num)
for i in range(numRows):
    for j in range(matix_num):
        raw=l[i]+' '*(numRows-2)


        #raw=l[i]+l[i+1]+l[i+1]
        i+=(numRows+2)
        print(j)
        if j+1==matix_num:
            raw+='\n'
        output+=raw
print(output)        