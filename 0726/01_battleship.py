import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    sea[index]=1
    sea[index+1]=1
    sea[index-1]=1
    return sea


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    a=int(input('배를 위치시킬 시작점을 고르세요.:'))
    if a<=0 or a>=14:
        print('-----해당 위치에는 배를 둘 수 없습니다.-----')
        continue
    else:
        player_sea=set_ship(a,player_sea)

        lst=list(range(1,14))
        lst.remove(a)
        lst.remove(a+1)
        lst.remove(a-1)
        a=random.choice(lst)
        computer_sea=set_ship(a,computer_sea)
        break
    


n=1 #라운드
A=0  
while True:
    while True:
        a=int(input('공격할 위치를 선택하세요: '))
        A=a

        if 0>a or a>15 :
            print('해역의 범위에서 벗어난 위치를 선택하셨습니다.다시 선택하세요')
            continue
            
        else:
            if computer_attacked[a]==True:
                print('이미 공격한 위치를 선택하셨습니다. 다시 선택하세요')
                continue
                
            else:
                if computer_sea[a]==1:

                    print('<1라운드 결과!>')
                    print('컴퓨터의 해역:',computer_sea)
                    print(f'플레이어는 컴퓨터의 해역{a}칸을 공격 하였고 컴퓨터 배는 피격되었습니다.')
                    print(f'게임이 종료되었습니다! {n}라운드 만에 플레이어의 승리 입니다!')
                    break

                else : 
                    computer_attacked[a]=True
                    break
 
    while True:

        lst=list(range(0,15))
        a=random.choice(lst)

        
        if player_attacked[a]==True:
            continue
                
        else:
            if player_sea[a]==1:

                print(f'<{n}라운드 결과!>')
                print(f'플레이어는 컴퓨터의 해역{A}칸을 공격 하였으나 공격 실패')
                print(f'컴퓨터는 컴퓨터의 해역{a}칸을 공격 하였고 플레이어의 배는 피격되었습니다.')
                print(f'게임이 종료되었습니다! {n}라운드 만에 컴퓨터의 승리 입니다!')
                n+=1
                break

            else : 
                player_attacked[a]=True
                print(f'<{n}라운드 결과!>')
                print(f'플레이어는 컴퓨터의 해역{A}칸을 공격하였으나, 공격에 실패 하였습니다!.')
                print(f'컴퓨터는 플레이어의 해역{a}칸을 공격하였으나, 공격에 실패 하였습니다!.')
                n+=1 
                break
    continue
        