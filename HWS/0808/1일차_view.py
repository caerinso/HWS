for case in range(10):
    block=input()
    blocks=list(map(int,input().split()))+[0,0]
    n=0
    for i in range(len(blocks)):
        for j in range(1,blocks[i]+1):
            if not(j<=blocks[i+1] or j<=blocks[i-1] or j<=blocks[i+2]or j<=blocks[i-2]):
                n+=1
    print(f'#{case+1}: {n}')