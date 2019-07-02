#########################################
# 简单的加法器
#
# 源码地址：https://ruslanspivak.com/lsbasi-part1/
#
# 逐行读取表达式
#   将每个表达式分为左值，操作符，右值三部分
#   分别验证每个部分
#   完成加法操作
# 循环
#########################################

# EOF 代表文件尾(输入完成)

INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF"


class Token(object):
    def __init__(self, type, value):
        # 词素类型：整数，加号，结束
        self.type = type
        # 值：0-9，+，None
        self.value = value

    def __str__(self):
        # 重写转字符串方法
        return "Token({type},{value})".format(
            # repr() 返回对象的string 格式
            type=self.type, value=repr(self.value)
        )

    # 显示属性
    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # 输入的指令：3+5
        self.text = text
        # 指令的字符位置
        self.pos = 0
        # 当前词素实例
        self.current_token = None

    def error(self):
        raise Exception("错误：无法解析输入")

    def get_next_token(self):
        # 词法分析器：将语句分解为一个个词素

        text = self.text

        # 是否时指令结尾，如果是，则返回一个结束标致
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # 从当前位置获取一个字符
        current_char = text[self.pos]

        # 默认指令，数据都是单个字符
        # 数值
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        # 符号：+
        if current_char == "+":
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        # 抛异常
        self.error()

    def eat(self, token_type):
        # 判断当前词素类型是否符合指定类型
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        # 从输入获取第一个词素
        self.current_token = self.get_next_token()

        ###################
        # 迭代在eat() 方法内
        ###################

        # 验证左值
        left = self.current_token
        self.eat(INTEGER)
        # 验证操作符
        op = self.current_token
        self.eat(PLUS)
        # 验证右值
        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
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


# 运行主函数，常用的方法
if __name__ == "__main__":
    main()
