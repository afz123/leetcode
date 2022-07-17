class Solution:
    def romanToInt(self, roman):
        save_lat_one=0
        save_lat_ten=0
        save_lat_h=0

        save_lat_one_2=0
        save_lat_ten_2=0
        save_lat_h_2=0

        output=0

        for latter in roman:
            # with 1
            if latter=='I':
                save_lat_one+=1
                output+=1
            
            if latter=='X' and save_lat_one==1:
                output+=8
                save_lat_one=0
                save_lat_one_2=1
            if latter=='V' and save_lat_one==1:
                output+=3
                save_lat_one=0
                save_lat_one_2=1
    
            #with 10
            if latter=='X' and save_lat_one_2==0:
                save_lat_ten+=10
                output+=10
            if latter=='L' and save_lat_ten==10:
                output+=30
                save_lat_ten=0
                save_lat_ten_2=1
            if latter=='C' and save_lat_ten==10:
                output+=80
                save_lat_ten=0
                save_lat_ten_2=1
                
            #with 100
            if latter=='C' and save_lat_ten_2==0:
                save_lat_h+=100
                output+=100
            if latter=='M' and save_lat_h==100:
                output+=800
                save_lat_h=0
                save_lat_h_2=1
            if latter=='D' and save_lat_h==100:
                output+=300
                save_lat_h=0
                save_lat_h_2=1
                
            if latter=='V' and save_lat_one_2==0:
                output+=5
            if latter=='L' and save_lat_ten_2==0:
                output+=50
            if latter=='D' and save_lat_h_2==0:
                output+=500
            if latter=='M' and save_lat_h_2==0:
                output+=1000
        print (output)

a=Solution()
d=input()
a.romanToInt(d)

'''
"III"
"LVIII"
"MCMXCIV"
'''

'''
class Solution:
    def romanToInt(self, s: str) -> int:
        save_lat_one=0
        save_lat_ten=0
        save_lat_h=0

        save_lat_one_2=0
        save_lat_ten_2=0
        save_lat_h_2=0

        output=0

        for latter in s:
            # with 1
            if latter=='I':
                save_lat_one+=1
                output+=1
            
            if latter=='X' and save_lat_one==1:
                output+=8
                save_lat_one=0
                save_lat_one_2=1
            if latter=='V' and save_lat_one==1:
                output+=3
                save_lat_one=0
                save_lat_one_2=1
    
            #with 10
            if latter=='X' and save_lat_one_2==0:
                save_lat_ten+=10
                output+=10
            if latter=='L' and save_lat_ten==10:
                output+=30
                save_lat_ten=0
                save_lat_ten_2=1
            if latter=='C' and save_lat_ten==10:
                output+=80
                save_lat_ten=0
                save_lat_ten_2=1
                
            #with 100
            if latter=='C' and save_lat_ten_2==0:
                save_lat_h+=100
                output+=100
            if latter=='M' and save_lat_h==100:
                output+=800
                save_lat_h=0
                save_lat_h_2=1
            if latter=='D' and save_lat_h==100:
                output+=300
                save_lat_h=0
                save_lat_h_2=1
                
            if latter=='V' and save_lat_one_2==0:
                output+=5     
            if latter=='L' and save_lat_ten_2==0:
                output+=50
            if latter=='D' and save_lat_h_2==0:
                output+=500
            if latter=='M' and save_lat_h_2==0:
                output+=1000
        return output
'''