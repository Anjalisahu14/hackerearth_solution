name = str(input() ).lower()          

def name_zoo(name):
    countz = sum(1 for char in name if char=='z')
    counto = sum(1 for char in name if char =='o')
    if 2* countz == counto:
      print('Yes')
    else:
        print('No')
    
name_zoo(name)
