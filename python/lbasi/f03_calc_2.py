INTEGER, PLUS, MINUS, EOF = "INTEGER", "PLUS", "MINUS", "EOF"


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


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    ###########
    # 词法分析 #
    ###########
    def error(self):
        raise Exception("无效语法")

    # 读取下一个字符
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    # 跳过空白符
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
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")
        return Token(EOF, None)

    # 验证token，验证完成后token 下移
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    # term 对数值型的token 提取值
    def term(self):
        token = self.current_token
        # eat 之后，curren_token 下移
        self.eat(INTEGER)
        return token.value

    # 真正的执行
    def expr(self):
        # 获取第一个token，数值
        self.current_token = self.get_next_token()
        # 获取数值
        result = self.term()
        # 第二个操作数必须为+/-
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                # eat 验证之后，current_token 下移
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
        return result


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()

# 会画语法图很重要
# 状态图也很重要
