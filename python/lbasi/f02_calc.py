##########
# 加法器2
#
# 识别多位整数
# 忽略空白
# 实现减法
##########

# 为什么要这样写？？？

# token 类型
INTEGER, PLUS, MINUS, EOF = "INTEGER", "PLUS", "MINUS", "EOF"

###########
# Token
# +-- type
# +-- value
###########
class Token(object):
    def __init__(self, type, value):
        # token 类型
        self.type = type
        # token 值
        self.value = value

    def __str__(self):
        # 字符串实例
        return "Token({type},{value})".format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

##########
# Interpreter
# +-- text
# +-- pos
# +-- current_char
# +-- current_token  当前token
# + error()
# + advance()
# + skip_whitespace()
# + integer()
# + get_next_token()
# + eat()
# + expr()
###########
class Interpreter(object):
    def __init__(self, text):
        # 输入字符串
        self.text = text
        # 字符位置
        self.pos = 0
        # 当前的token
        self.current_token = None
        # 当前字符
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("错误：无法解析输入字符串")

    # 前进
    def advance(self):
        # 字符指针位置加一
        self.pos += 1
        if self.pos > len(self.text) - 1:
            # 判断是否已经到字符串尾
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    # 跳过空格
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            # 当前字符不为空 且 当前字符是空格
            self.advance()

    # 获取多位整型数值
    def integer(self):
        # 以字符串暂存数值
        result = ""
        # 是数值就一直读取
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    # 解析token
    def get_next_token(self):
        # 因为要解析多字符token 所以与上一个版本明显多了while 循环
        while self.current_char is not None:
            # 跳过空白
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # 数值类型
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    # 解析并执行
    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue

        # 每解析一行指令，需要新建一个翻译器对象
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()

