# TASK1
# t=input()
# for i in t:
#     if(i=='W'):
#         i='M'
#     if(i=='M'):
#         i='W'
#     print(i,end='')


#task2
# t=input()
# ls=[]
# for i in t:
#     ls.append(i)
# ln=len(ls)
# if(ln%2==0):
#     print('Even')
# else:
#     print('Odd')

# #task3
# def is_only_one_case(s: str) -> bool:
#     return s.isalpha() and (s.islower() or s.isupper())
# print(is_only_one_case("hello"))     
# print(is_only_one_case("HELLO"))     

#task4
# def num(n):
#     ls=[]
#     a=n/2
#     b=a/2
#     c=b/2
#     ls.append(a)
#     ls.append(b)
#     ls.append(c)
#     return ls
# print(num(6))

#task5
# def n(a):
#     return 'Ed'+'a'*a+'bit'
# print(n(0))

#task6
# def fun(n):
#     for i in n:
#         if (',' in n) or ('.' in n) or('/' in n) or('!' in n) or('@' in n)  or('#' in n) :
#             return False
#         else :
#             return True
# print(fun('helo,'))
#task7
# def lis(ls):
#      ls1=[]
#      mx=-999999999
#      mn=9999999999
#      for i in ls:
#           if i>mx:
#                mx=i
#           if i<mn:
#                mn=i
#      ls1.append(mn)
#      ls1.append(mx)
#      return ls1
# print(lis([1,2,3,4,5]))
    
#task8
# def st(s):
#     cnt=0
#     for i in s:
#         if (i=='D') or (i=='d'):
#             cnt+=1
#     return cnt
# print(st('Doctor'))
#task9
# def fun(n,s):
#     if n>=15:
#         return True
#     else:
#         if s==True:
#             return True
#         else :
#             return False
# print(fun(14,True))
#task10
# def funn(a,b):
#     ls=[]
#     cnt1=0
#     for i in a:
#         if cnt1==1:
#             break
#         else:ls.append(i)
#     cnt2=0
#     for i in b:
#         if cnt2==3:
#             break
#         else: ls.append
#     return ls
# print(funn('john','Smith'))

# task11

