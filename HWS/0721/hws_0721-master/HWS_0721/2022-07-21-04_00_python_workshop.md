---
layout: single
title:  "jupyter notebook 변환하기!"
categories: coding
tag: [python, blog, jekyll]
toc: true
author_profile: false
---

<head>
  <style>
    table.dataframe {
      white-space: normal;
      width: 100%;
      height: 240px;
      display: block;
      overflow: auto;
      font-family: Arial, sans-serif;
      font-size: 0.9rem;
      line-height: 20px;
      text-align: center;
      border: 0px !important;
    }

    table.dataframe th {
      text-align: center;
      font-weight: bold;
      padding: 8px;
    }

    table.dataframe td {
      text-align: center;
      padding: 8px;
    }

    table.dataframe tr:hover {
      background: #b8d1f3; 
    }

    .output_prompt {
      overflow: auto;
      font-size: 0.9rem;
      line-height: 1.45;
      border-radius: 0.3rem;
      -webkit-overflow-scrolling: touch;
      padding: 0.8rem;
      margin-top: 0;
      margin-bottom: 15px;
      font: 1rem Consolas, "Liberation Mono", Menlo, Courier, monospace;
      color: $code-text-color;
      border: solid 1px $border-color;
      border-radius: 0.3rem;
      word-break: normal;
      white-space: pre;
    }

  .dataframe tbody tr th:only-of-type {
      vertical-align: middle;
  }

  .dataframe tbody tr th {
      vertical-align: top;
  }

  .dataframe thead th {
      text-align: center !important;
      padding: 8px;
  }

  .page__content p {
      margin: 0 0 0px !important;
  }

  .page__content p > strong {
    font-size: 0.8rem !important;
  }

  </style>
</head>



```python
N=int(input())
lst=[]
for i in range(1,N+1):
    
    if N%i==0:
        lst.append(i)
    else :
        continue 
        
lst.sort()        
result=' '.join(str(s)for s in lst)
print(result)

#sorted() 와 .sort(리턴 밸류가 없다 !!! 헷갈리지 말자.)는 방식이 다르다. 
```

<pre>
10
1 2 5 10
</pre>

```python
def list_sum (a) :
    k=len(a)
    sum=0
    num=0
    for i in range(0,k):
        num = a[i]
        sum=sum+num
    
    return sum 

list_sum([1,2,3,4,5])  
```

<pre>
15
</pre>

```python
def dic_list_sum(a):
    
    k=len(a)
    sum=0
    num=0

    for i in range(0,k):
        A=a[i]
        num=A['age']
        sum=sum+num
        
    return sum
    

dic_list_sum([{'name':'kim','age':12},{'name':'lee','age':4}])
```

<pre>
16
</pre>

```python
def list_sum (a) :
    k=len(a)
    sum=0
    num=0
    for i in range(0,k):
        num = a[i]
        sum=sum+num
    
    return sum 


def all_list_sum(a):
     
    k=len(a)
    sum=0
    num=0
    for i in range(0,k):
        A=a[i]
        
        sum_1=list_sum(A)
        
        num=num+sum_1
    return num 


all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]])        
       
```

<pre>
55
</pre>

```python
def get_secret_word(a):
    
    k=list(map(str,a))
    
    A={'83':'S','115':'s','65':'a','102':'f','89':'y'}
    lst=[]
    s=len(k)
    for i in range(0,s):
        
        lst.append(A[k[i]])
        
    lst_T=''.join(lst)
    return lst_T
    

    
get_secret_word([83,115,65,102,89])
```

<pre>
'Ssafy'
</pre>

```python
def list_sum (a) :
    k=len(a)
    sum=0
    num=0
    for i in range(0,k):
        num = a[i]
        sum=sum+num
    
    return sum 
    

def get_secret_number(a):
    
    lst= list(a)
    
    A={'h':'104','a':'97','p':'112','y':'121'}
    list_1=[]
    s=len(lst)
    
    for i in range(0,s):
        
        list_1.append(A[lst[i]])
        
    
    list_2 =list(map(int,list_1))
    
    return list_sum(list_2)
    


get_secret_number('happy')
```

<pre>
546
</pre>

```python
def list_sum (a) :
    k=len(a)
    sum=0
    num=0
    for i in range(0,k):
        num = a[i]
        sum=sum+num
    
    return sum 
    

def get_secret_number(a):
    
    lst= list(a)
    
    A={'z':'122','a':'97','d':'100','e':'101',
   'l':'75','i':'105','a':'97','n':'110','h':'104','x':'120','o':'111','n':'110'}

    list_1=[]
    s=len(lst)
    
    for i in range(0,s):
        
        list_1.append(A[lst[i]])
        
    
    list_2 =list(map(int,list_1))
    
    return list_sum(list_2)


def get_strong_word(a,b):
    
    A=get_secret_number(a)
    
    B=get_secret_number(b)
    
    if A > B:
        return a
    elif A<B:
        return b
    else:
        return a,b





get_strong_word('z','a')

get_strong_word('delilah','dixon')
```

<pre>
'delilah'
</pre>

```python
```


```python
```
