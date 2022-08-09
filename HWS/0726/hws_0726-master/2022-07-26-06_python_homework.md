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
a=[1,3,45,2,77]

print(sorted(a))# 값을 sort 된 리스트로 뱉는다. 

print(a.sort())# 값을 None을 뱉는다.a 리스트를 확인해야 바뀐 것을 볼 수 있다. 
print(a)
```

<pre>
[1, 2, 3, 45, 77]
None
[1, 2, 3, 45, 77]
</pre>

```python
a=[1,3,45,2,77]

a.extend([2,3])#추가 할때 리스트 안의 값들을 추가한다. 
print(a)
a.append([2,3])#리스트 자체를 추가한다.(원형 그대로 요소로 추가한다.)
print(a)
```

<pre>
[1, 3, 45, 2, 77, 2, 3]
[1, 3, 45, 2, 77, 2, 3, [2, 3]]
</pre>

```python
a=[1,2,3,4,5]
b=a
a[2]=5
print(a)
print(b)
print(id(a)==id(b))
# 할당을 해주는 방식으로, 같은 객체를 보기 떄문에 리스트의 요소는 같고 이에 
#id 값도 같게 출력 되는것을 확인 할 수 있다. 
```

<pre>
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]
True
</pre>

```python
```
