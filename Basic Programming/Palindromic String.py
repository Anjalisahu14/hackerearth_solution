str1= input().lower()              

def palindrom_ckeck(str1):
    return {str1==str1[::-1] : 'YES'}.get(True, 'NO')
print(palindrom_ckeck(str1))
