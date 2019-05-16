# 正则语言预正则表达式  

[原文地址](https://www.cnblogs.com/Ninputer/archive/2011/06/08/2075714.html) 有个人理解，可能会和原文有出入，关于状态机这一块，可以学习下计算理论，虽然比较晦涩  

## what_basic  

```csharp
string str = "hello world";
```  

对于上面这行`C#` 代码，有以下需要注意，不做严格定义，但要明确意思：  

- `词素(lexeme)` 具有明确含义的字符串片段  
- 词素具有不同的类型，类型有确定的规则描述  

类型|规则|例子
---|---|---
`关键字`|由特定的字符按指定顺序组成|`string`
`标识符`|由字母开头，后面可以跟`零个或多个`字母、下划线或者数字 <br/> 但不能和关键字重复|`str`
`等号`|符号|`=`
`字符串`|由双引号开始和结束，中间包括任意不是双引号的字符|"hello 12tall!"
`分号`|`;`|`;`

- `单词(token)` 一般长这个样子`<词素,类型>`  

## what_regex  

- `语言` 字符串的集合，其中的字符来源于一个`有限`的字符集合。简单来说，包含好多甚至无限多的字符串，但是字的数量是有限的  
- `ε` 表示一个语言，仅包含一个长度为`0` 的字符串，读作`epsilon`  
- 对于字符集中任意字符`a`，表达式**a** 表示仅有一个字符串*a* 的语言，即`{a}`

### 运算规则  

- A`∪`B 或者 A`|`B，并。表示语言的并集。  
- AB，连接。表示语言A 的每一个字符串连接上B 的每一种字符串，类似于`笛卡尔积`。A=a|b，B=c|d，则AB={ac,ad,bc,bd}  
- A*，克林闭包。表示分别将`0个或多个`A 分别与自己连接的结果的并集。  
- 无论那种运算，不要忘记`ε`  
- **优先级** `克林闭包` > `连接` > `并`，有括号先算括号里的  

### 运算规则扩展  

- 方括号内的元素取并运算[abc]=a|b|c  
- 方括号内以^ 开头表示取`补集`[^abc]={x∈字符集|x≠a且x≠b且x≠c}  
- . 表示所有字符的并  
- A? 表示A|ε  
- A+ 表示 AA*  

要学会根据规则推演规则  

能用`正则表达式` 表示的语言，称为`正则语言`(手工doge)。常见的编程语言几乎都不是正则语言能描述的(doge)，所以才会引入文法分析、语义分析等一大堆更难理解的东西吧。但是正则表达式用来进行词法分析却是极适合的，大部分编程语言的词素都可以用简单的正则表达式来表示。  

类型|正则表达式|内容
---|---|---
`关键字`|string|`string`
`标识符`|[a-z][a-z0-9]*|`str`
`等号`|=|`=`
`字符串`|"[^"]*"|"hello 12tall!"
`分号`|;|`;`  

然后，作者提供了几个类，`通过循环调用.toString()`，来生成常见的正则表达式：  

## how  

这里不将代码复制过来了，后面照着实现一下，其中里面几个委托方法没有看懂，对这一块一直是弱项  

- [x] [RegularExpression](https://github.com/Ninputer/VBF/blob/master/src/Compilers/Compilers.Scanners/RegularExpression.cs)  
    - [x] [AlternationExpression](https://github.com/Ninputer/VBF/blob/master/src/Compilers/Compilers.Scanners/AlternationExpression.cs) 或运算  
    - [x] [ConcatenationExpression](https://github.com/Ninputer/VBF/blob/master/src/Compilers/Compilers.Scanners/ConcatenationExpression.cs) 连接运算  
    - [x] [EmptyExpression](https://github.com/Ninputer/VBF/blob/master/src/Compilers/Compilers.Scanners/EmptyExpression.cs) 空表达式`ε`  
    - [x] [KleeneStarExpression](https://github.com/Ninputer/VBF/blob/master/src/Compilers/Compilers.Scanners/KleeneStarExpression.cs) 克林闭包  
    - [x] [SymbolExpression](https://github.com/Ninputer/VBF/blob/master/src/Compilers/Compilers.Scanners/SymbolExpression.cs) 单一字符  


作者通过重载运算符可以简化部分操作，我自己写的关于`sql` `condition` 拼接的类，就直接参考本节实现的。  
这样哈，我用`C` 能不能也实现一个呢  