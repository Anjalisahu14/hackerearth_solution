N = int(input())        

def fact_cal(n):
    result =1
    for i in range (2, n+1):
        result = result * i
    print(result)

# def fact_cal(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* fact_cal(n-1)
print(fact_cal(N))
