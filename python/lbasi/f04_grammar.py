# 从语法到语言
# 语言再转化为代码
# 语言，规则 --> expr()
# 选择 --> if...else
# 可选，* --> while
# Token，词素 --> eat(T) 验证
#
# factor ([MUL|DIV]fator)*

INTEGER, MUL, DIV, EOF = "INTEGER", "MUL", "DIV", "EOF"


# 词素构造
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({type},{value})".format(
            type=self.type,
            value=self.value
        )

    def __repr__(self):
        return self.__str__()


# 词法分析
class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        # self.token 被取消了
        # self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("无效字符")

    # 字符指针后移
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        # while 循环()*
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == "*":
                self.advance()
                return Token(MUL, "*")

            if self.current_char == "/":
                self.advance()
                return Token(DIV, "/")
            self.error()
        return Token(EOF, None)


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("语法错误")

    # 验证操作符为什么不一起封装
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    # 验证因子
    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        result = self.factor()
        # 循环()*
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            # 选择[MUL|DIV]factor
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()
        return result


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()

# lexer 返回token
# grammer 利用token 求值
