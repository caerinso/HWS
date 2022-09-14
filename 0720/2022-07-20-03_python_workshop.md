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
a=1
while a<=10 :
    print(a)
    a+=1
```

<pre>
1
2
3
4
5
6
7
8
9
10
</pre>

```python
n=1
while n<=10:
    a=[]
    a.append(n)
    n=1+n
    
print(a)
??
```

<pre>
[10]
</pre>

```python
a=5
while a>0 :
    print(a)
    a+=-1
```

<pre>
5
4
3
2
1
</pre>

```python
n=1
while n<=10:
    a=[]
    a.append(n)
    n=1+n
    
print(a)
??
```

<pre>
[10]
</pre>

```python
sum=0
k=10
for i in range(1,1+k):
    sum=sum+i
    
print(sum)
```

<pre>
55
</pre>

```python
k=7

for i in range(1,1+k):
    d='*'*i
    print(d)
```

<pre>
*
**
***
****
*****
******
*******
</pre>

```python
```
