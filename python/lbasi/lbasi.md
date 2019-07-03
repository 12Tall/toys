# Let's Build a Simple Interpreter  

本来想翻译一下来着，但是发现无论是英文还是中文水品都不咋地，挖个坑先  

- [x] [一个简单的加法器](f01_addition.py)  
- [x] [加减法](f02_calc.py)
- [x] [多项运算](f03_calc_2.py)
- [x] [语法-语言](f04_grammar.py)
- [x] [运算优先级](f05_precedence.py)

## 语法图(铁路图)  

1 一张用来表示一个语法规则的图  
2 沿箭头指向的路线前进：顺序、选择、循环  
3 沿途会有`操作符` 和`字面量`

## 上下文无关语法  

- Token 词素  
- lexer 返回词素
- grammar 利用词素求值
