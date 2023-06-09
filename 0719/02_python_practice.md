# Python Practice 02





## Practice 1 : 자판기 메뉴 표현하기

### 목표 : Python 기초 문법 익히기 (변수, 할당,  연산자, 연산자 우선순위)

> (1) 다음과 같은 자판기 메뉴를 변수의 할당을 사용하여 표현합니다. <br> (HINT) 가격은 계산하기 편한 자료형을 사용합니다.

1. 콜라 500원
2. 사이다 700원
3. 레모네이드 4500원
4. 오렌지주스 2000원
5. 초코우유 1200원
6. 아메리카노 3600원


```python
# 아래에 답안을 작성해 주세요.

'콜라'= 500
'사이다'=700
'레모네이드'=4500
'오렌지주스'=2000
'초코우유'=1200
'아메리카노'=3600


```

> (2) 김싸피의 현재 소지 금액은 30,000원입니다. <br>
김싸피는 콜라와 사이다는 2개씩, 나머지 메뉴는 모두 1개씩 구매하려고 합니다. <br>
(1)의 결과를 활용하여 거스름돈을 계산한 후 출력합니다.

[변수 설명]

* money : 김싸피의 현재 소지 금액
* change : 거스름돈


```python
# 아래에 답안을 작성해 주세요.
money =30000
콜라= 500
사이다=700
레모네이드=4500
오렌지주스=2000
초코우유=1200
아메리카노=3600

change= money- (콜라*2 + 사이다*2 + 레모네이드+ 오렌지주스 + 초코우유+ 아메리카노) 
print(change)

```

    16300
    

## Practice 2 : 항구의 배 표시하기

### 목표 : 리스트 익히기(생성과 접근, 인덱싱, 슬라이싱)

> (1) 리스트를 사용하여 다음의 상황을 표현한 후 항구 정보를 출력합니다.

싸피국의 항구는 가로로 긴 모양을 하고 있으며, 총 15대의 배가 동시에 입항할 수 있습니다.
선착장 번호는 왼쪽 끝인 1번부터 오른쪽 끝인 15번까지 존재합니다.
현재 4번, 8번, 9번, 15번 선착장에 배가 들어와 있습니다.

[변수 설명]

* ports : 항구

[요구 사항]

1. 항구 정보를 리스트로 표현합니다.
2. 배가 있으면 True, 없으면 False로 표기합니다.
3. 4번, 8번, 9번, 15번 선착장은 배가 있음을 표기합니다.
4. 모든 배에 대해서 항구 정보를 출력합니다.


```python
imfor= int (input( '번호입력하세요:' ))

           
list_ports ={'1': 'False', '2': 'False' ,'3': 'False','4': 'True','5': 'False','6': 'False','7': 'False','8':' True','9':'True','10': 'False','11':' False','12': 'False','13':' False','14': 'False','15':'True'}
k=str(imfor)
print(list_ports[k])


```

    번호입력하세요:4
    True
    


```python
> (2) 항구를 관리하는 김싸피는, 홀수 선착장의 현황만 따로 추려서 보고자 합니다. <br> (1)의 결과를 활용하여, 홀수 선착장의 번호를 갖는 리스트를 만들어서 출력합니다.

[변수 설명]

* odd_ports : 홀수 선착장 정보
```


      File "<ipython-input-33-4956d6448cdf>", line 1
        > (2) 항구를 관리하는 김싸피는, 홀수 선착장의 현황만 따로 추려서 보고자 합니다. <br> (1)의 결과를 활용하여, 홀수 선착장의 번호를 갖는 리스트를 만들어서 출력합니다.
        ^
    SyntaxError: invalid syntax
    



```python
# 아래에 답안을 작성해 주세요.
list_ports ={'1': 'False', '2': 'False' ,'3': 'False','4': 'True','5': 'False','6': 'False','7': 'False','8':' True','9':'True','10': 'False','11':' False','12': 'False','13':' False','14': 'False','15':'True'}


print({'1':list_ports['1'],'3':list_ports['3'],'5':list_ports['5'],'7':list_ports['7'],'9':list_ports['9'],'11':list_ports['11'],'13':list_ports['13'],'15':list_ports['15']})
```

    {'5': 'False', '3': 'False', '7': 'False', '15': 'True', '13': ' False', '11': ' False', '1': 'False', '9': 'True'}
    

## Practice 3 : 로또 당첨 여부 확인하기

### 목표 : Set 자료구조 활용 및 연산자 숙달

> 김싸피가 수동으로 구매한 로또 번호는 1, 12, 27, 33, 38, 42입니다. <br>
해당 회차의 로또 당첨 번호는 7, 15, 27, 33, 37, 42입니다. <br>
김싸피가 고른 번호들과 로또 당첨 번호를 Set을 활용해 표현하고, 몇 개의 번호가 맞았는지 출력합니다.

[변수 설명]

* ssafy_choice : 김싸피가 고른 번호 목록
* lucky_numbers : 해당 회차의 로또 당첨 번호 목록
* count : 몇 개의 번호가 맞았는지 세는 변수


```python
# 아래에 답안을 작성해 주세요.
ssafy_choice = [ 1, 12, 27, 33, 38, 42 ]
lucky_numbers = [ 7, 15, 27, 33, 37, 42 ]
se= (ssafy_choice+lucky_numbers)
my_se= set(se)
count= 12 - len(my_se)
print(count)

```

    3
    

## Practice 4 : 도시 정보 구조화하기

### 목표 : 리스트, 딕셔너리 컨테이너 숙달

> (1) 싸피국은 수도인 A 도시와 일반 도시인 B 도시가 있습니다. <br>
싸피국은 매일 두 도시의 이산화탄소 및 산소 농도를 조사하는데, <br>
김싸피는 분석기로부터 얻은 데이터를 리스트 및 딕셔너리를 활용해 구조화하려 합니다. <br>
자세한 구조는 변수 설명과 딕셔너리 키 설명을 참고합니다.

[변수 설명]

* air_info
    - 두 도시의 정보를 담는 리스트입니다.
    - 두 도시의 정보는 각각 딕셔너리 형태입니다.

[각 도시의 정보]

* name : 도시 이름
* capital : 수도 여부
* air_status : 대기 정보 (딕셔너리)
    * O2 : 산소 농도
    * CO2 : 이산화탄소 농도
    
[요구 사항]
1. A 도시 : 도시 이름은 A이며, 수도입니다. 산소 농도는 3이며, 이산화탄소 농도는 2입니다.
2. B 도시 : 도시 이름은 B이며, 수도가 아닙니다. 산소 농도는 5이며, 이산화탄소 농도는 3입니다.



```python
# 아래에 답안을 작성해 주세요.

A=['이름': A, '수도': 1, '산소농도': 3, '이산화탄소농도': 2 ]
B=['이름': B, '수도': 0, '산소농도': 5, '이산화탄소농도': 3 ]

air_info=[A,B]

```

> (2) 김싸피는 두 도시의 산소 농도 정보만을 모아서 정리하고자 합니다. 변수 설명을 참고하여 정리된 정보를 출력합니다.

[변수 설명]

O2_info : 두 도시의 산소 농도 값을 모은 리스트


```python
# 아래에 답안을 작성해 주세요.

A_im ={'이름': 'A', '수도': 1, '산소농도': 3, '이산화탄소농도': 2 }
B_im ={'이름': 'B', '수도': 0, '산소농도': 5, '이산화탄소농도': 3 }

air_info=[A_im,B_im]


O2_info=[ A_im['이산화탄소농도'],B_im['이산화탄소농도']]


print(O2_info)



```

    [2, 3]
    


```python

```


```python

```


```python

```
