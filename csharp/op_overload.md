# 运算符重载  

## 一般用法  

```csharp
// 重载运算符| 为或运算
public static Condition operator | (Condition a,Condition b){
    return a.Or(b);  
}

Condition a = new Condition(),
    b = new Condition();
// 使用
Condtion result = a|b;
```

⚠：这种方法在`C#` 中好用，但却不一定能和`VB.NET` 共享，更好的方法是通过`CLR` 中的运算符属性进行重载。  

## 兼容写法  

```csharp
// 重载运算符|(op_BitwiseOr) 为或运算
[SpecialName]  // 要添加SpecialName 的属性
public static Condition operator op_BitwiseOr (Condition a,Condition b){
    return a.Or(b);  
}

Condition a = new Condition(),
    b = new Condition();
// 使用
Condtion result = a|b;
```

下面是一个运算符`SpecialName` 的清单，~~~因为访问[原网页](https://www.visualbasicplanet.info/framework-programming-2/operator-overload-methods.html) 似乎需要翻墙，本人也不太清楚应该去哪里找准确版本，~~~ 请参考《CLR via C#》 P191。与下表稍有出入，以书为准吧，所以这里将清单直接列举出来了  

### 名词  

`Unary` 一元运算符  

运算符|SpecialName|建议`CLS一致` 方法名|中文
---|---|---|---
+|op_UnaryPlus|Plus|正
-|op_UnaryNegation|Negate|负
`原文为空`|op_OnesComplement|OnesComplement|取补
++|op_Increment|Increment|自增
--|op_Decrement|Decrement|自减
(none)|op_True|IsTrue { get; }|真
(none)|op_False|IsFalse { get; }|假
+|op_Addition|Add|加
+=|op_AdditionAssignment|Add|加等于
-|op_Subtraction|Subtract|减
-=|op_SubtractionAssignment|Subtract|减等于
*|op_Multiply|Multiply|乘
*=|op_MultiplicationAssignment|Multiply|乘等于
/|op_Division|Divide|除以
/=|op_DivisionAssignment|Divide|除以等于
%|op_Modulus|Mod|取模
%=|op_ModulusAssignment|Mod|模等于
^|op_ExclusiveOr|Xor|按位异或
^=|op_ExclusiveOrAssignment|Xor|按位异或等于
&|op_BitwiseAnd|BitwiseAnd|按位与
&=|op_BitwiseAndAssignment|BitwiseAnd|按位与等于
\||op_BitwiseOr|BitwiseOr|按位或
\|=|op_BitwiseOrAssignment|BitwiseOr|按位或等于
&&|op_LogicalAnd|And|逻辑与
\|\||op_LogicalOr|Or|逻辑或
!|op_LogicalNot|Not|逻辑非
<<|op_LeftShift|LeftShift|左移
<<=|op_LeftShiftAssignment|LeftShift|左移等于
\>\>|op_RightShift|RightShift|右移
\>\>=|op_RightShiftAssignment|RightShift|右移等于
(none)|op_UnsignedRightShiftAssignment|RightShift|无符号右移等于
==|op_Equality|Equals|关系等于
!=|op_Inequality|Compare|关系不等于
<|op_LessThan|Compare|Compare|关系小于
\>|op_GreaterThan|Compare|关系大于
<=|op_LessThanOrEqual|Compare|关系小于等于
\>=|op_GreaterThanOrEqual|Compare|关系大于等于
=|op_Assign|很长，不贴了|请勿重载此运算符|

感觉就是知识的搬运工~~~