# 优先级

INTEGER, PLUS, MINUS, MUL, DIV, EOF = (
    "INTEGER", "PLUS", "MINUS", "MUL", "DIV", "EOF"
)


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


##############################
# 词法分析器
# 作用：读取字符流，切分成token
# 包括操作符(+-*/)、数值([0-9-+)
# 和空token(None)
##############################
class Lexer(object):
    # 初始化
    # 传入字符流
    # 私有变量：当前字符、字符指针
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    # 异常处理
    def error(self):
        raise Exception("无效的字符")

    # 按字符读取流
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    # 空字符处理
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    # 截取常量数据，其实这里可以不用封装
    # 一部分封装，一部分不封装，反而不太好理解了
    # 其实应该可以用哈希表的
    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    # 获取下一个token
    # 根据当前字符做类型判断，因为数字和操作符的区别还是很明显的
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
            if self.current_char == "*":
                self.advance()
                return Token(MUL, "*")
            if self.current_char == "/":
                self.advance()
                return Token(DIV, "/")
            self.error()
        return Token(EOF, None)


##############################
# 翻译器
# 作用：根据一定的语言规则，将词法分析器
# 产生的token 按照语言规则，进行运算
##############################
class Interpreter(object):
    # 构造函数
    # 传入语法分析器
    # 私有变量：当前的token
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    # 异常处理
    def error(self):
        raise Exception("无效语法")

    # token验证
    # 其实这个验证除了将当前的token 后移，好像没啥用
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    ####################################
    # 每一个rule 都是一个方法
    # 选择用if
    # 多项用while
    # 整型就是顺序
    ####################################

    # factor：返回当前数据的值
    # 这样说的话，还有一条规则的优先级最高：单值表达式(就是数值本身，自己取的名字哈哈哈)
    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    # term：不知道该怎么翻译，短语？
    # 计算乘除法的
    def term(self):
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()
        return result

    # expr：计算加减法
    # 加减法调用乘除法为输入值(左右值更形象一些)
    def expr(self):
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
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
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        # 按优先级由低到高依次调用
        # 求加减法
        #   调用乘除法
        #       调用数值
        print(result)


if __name__ == '__main__':
    main()
