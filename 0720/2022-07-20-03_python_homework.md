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
abs()
all()
any()
ascii()
bin()
bool()
breakpoint()
bytearray()
bytes()
callable()
```




```python
a=list(range(1,50,2))
print(a)
```

<pre>
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
</pre>

```python
n=5
m=9
k='*'*5
i=0
while(i<9):
    print(k)
    i+=1
```

<pre>
*****
*****
*****
*****
*****
*****
*****
*****
*****
</pre>

```python
temp =36.5 

if temp >=37.5:
    print('입실 불가')
else:
    print('입실 가능')
```

<pre>
입실 가능
</pre>

```python
def get_middle_char(a) :
    lst=list(a)
    aa=len(lst)
    
    if (aa%2==0):
        k_1=int(aa/2)
        k_2=int(aa/2+1)
        return(lst[k_1],lst[k_2])
        
    else:
        k_3=int((aa)/2)
        return(lst[k_3])
                
a='fffdg'

get_middle_char(a)
```

<pre>
'f'
</pre>

```python
```
