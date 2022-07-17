# # целочисленное деление
# print(4321//1000)
# print(4321//100)
# print(4321//10)
# #остаток от деления
# print(4321%10000)
# print(4321%1000)
# print(4321%100)
# print(4321%10)

# print('d'*2)



def qwe123(input_num):
    thouthend=input_num//1000
    hundred=(input_num//100)%10
    ten=(input_num//10)%10
    one=input_num%10
    output=''
    if thouthend>0:
        output+='M'*thouthend
    if hundred==9:
        output+='CM'
    if hundred==4:
        output+='CD'
    if hundred==5:
       output+='D'
    if 5<hundred<9:
        output+='D'+'C'*(hundred-5)
    if hundred<4:
        output+='C'*hundred
   
    if ten==9:
        output+='XC'
    if ten==4:
        output+='XL'
    if ten==5:
       output+='L'
    if 5<ten<9:
        output+='L'+'X'*(ten-5)
    if ten<4:
        output+='X'*ten
    
    if one==9:
        output+='IX'
    if one==4:
        output+='IV'
    if one==5:
       output+='V'
    if 5<one<9:
        output+='V'+'I'*(one-5)
    if one<4:
        output+='I'*one
    
    return output

print(qwe123(3999))
