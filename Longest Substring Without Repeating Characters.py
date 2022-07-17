# from itertools import count

from cv2 import sort


a=list('asdasfasfamsgasdalsd')

# print(a[0:4])
# seen=set()
# uniq=[ x for x in a if x not in seen and not seen.add(x)]
# print(uniq)
# list_1=[]
# for i in uniq:
#     b=0
#     for j in a:
#         # print(j)
#         if i==j:
#             # list_1.append(b)
#             # print(i, list_1)
#             b=0
#         if i!=j:
#             b+=1
#         list_1.append(b)
# print(list_1)

    
# a=list('asdasfasfamsgasdalsd')
a=list('asdqwertyasddas')
seen=set()
uniq=[ x for x in a if x not in seen and not seen.add(x)]
print(uniq)
list_1=[]
for i in uniq:
    #b=0
    for j in range(len(a)):
        try:
            if i==a[j] and i!=a[j+1]:
                b=j
                l=[]
        except:
            qq=1
        if i!=a[j-1] and i!=a[j]:
            l=a[b:j+1]    
   
    list_1.append(l)
    
print(list_1)




















# a=list('qqsq')

# b=0

# li=[]
# seen=set()
# uniq=[ x for x in a if x not in seen and not seen.add(x)]
# print(uniq)
# for i in uniq:
#     list_of_l=[]
#     for j in range(len(a)-1):
#         try:
#             if i==a[j] and i!=a[j+1]:
#                 list_of_l.append(j)
#                 print('list_of_l',list_of_l, 'len:', len(list_of_l))
#                 output_l=[]
#                 range_1=len(list_of_l)-1
#                 if len(list_of_l)==1:
#                     range_1=1
                
#                 for o in range(range_1):
#                     e= (list_of_l[o]-list_of_l[o+1]+1)*-1
#                     output_l.append(e)
#                     print(output_l)
                
#                 li.append(max(output_l))
#                 print(li)
        
#         except:
#             pass        
# #print(max(li))


# seen=set()
# uniq=[ x for x in a if x not in seen and not seen.add(x)]
# print(uniq)
# print(a.index(uniq[1]))
# di={}
# cou=-1
# list_ind=[]
# for i in uniq:
#     for j in a:
#         if cou==len(a)-1:
#             cou=-1
#         cou+=1
#         if i==j:
#             list_ind.append(a.index(j,cou))
#             di['{}'.format(i)]=list_ind
#             print(di)
# print(di)            


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         for letter in s:
#             1

