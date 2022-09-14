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
def duplicated_letters(a) :
    lst=[]

    a_1=list(set(a)) #aple
    a_2=list(a) #apple 

    for i in a_1:
        if a_2.count(i)>1:
            lst.append(i)
        else:
            continue

    return lst

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
```

<pre>
['p']
['n', 'a']
</pre>

```python
def low_and_up(a):

    a=list(a)
    a_1=a[0:len(a):2]
    a__1=[]
    for i in a_1:
        a__1.append(i.lower())
    a_2=a[1:len(a):2]
    a__2=[]
    for i in a_2:
        i.upper()
        a__2.append(i.upper())

    n=0
    for i in a__2: 
        a__1.insert(2*n+1,i)
        n+=1

    return ''.join(a__1)

print(low_and_up('apple'))
print(low_and_up('banan'))
```

<pre>
aPpLe
bAnAn
</pre>

```python
def lonely(lst):
    lst_1=[]
    for i in range(0,len(lst)):

        if i==len(lst)-1:
            lst_1.append(lst[i])
            
        else:             
            if lst[i]!=lst[i+1]:
                lst_1.append(lst[i])
            elif lst[i]==lst[i+1]:
                continue

    return lst_1

print(lonely([1,1,3,3,0,1,1]))
print(lonely([4,4,4,3,3]))
```

<pre>
[1, 3, 0, 1]
[4, 3]
</pre>

```python
```
