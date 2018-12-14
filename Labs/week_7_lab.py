i = 1

def counting(i):
    print(i)
    i=i+1
    if i == 100: return
    counting(i)

counting()
