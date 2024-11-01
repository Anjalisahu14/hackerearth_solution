n = int(input())                
lst = list(map(int,input().split()))        

from collections import Counter

singer_count= Counter(lst)

max_number = max(singer_count.values())

number = sum(1 for count in singer_count.values() if count==max_number)

print(number)
