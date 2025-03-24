def nums(n):
    if(n==0):
        return
    nums(n-1)+n
    print(n)
nums(6)


