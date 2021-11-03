'''use ArrayStack to implement arithmetic expression evaluation'''
class ArrayStack:

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Exception()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Exception()
        return self.array.pop(-1)

    def __repr__(self):
        return str(self.array)


def compute(left, right, operator):
    if (operator == "+"):
        return left + right
    elif (operator == "-"):
        return left - right
    elif (operator == "/"):
        return left / right
    elif (operator == "*"):
        return left * right


def evaluate(string):
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    table = {"+": 2, "-": 2, "*": 3, "/": 3, "(": 1, ")": 1}
    tokens = string.split()
    for token in tokens:
        if token not in table.keys():  # operand
            operand_stack.push(int(token))

        elif token == '(':
            operator_stack.push(token)

        elif token == ')':
            operator = operator_stack.pop()
            while operator != '(':
                operand1 = operand_stack.pop()
                operand2 = operand_stack.pop()
                operand_stack.push(compute(operand2, operand1, operator))
                operator = operator_stack.pop()

        else:  # operator
            while (not operator_stack.is_empty()) and \
                    (table[operator_stack.top()] >= table[token]):
                operand1 = operand_stack.pop()
                operand2 = operand_stack.pop()
                operator = operator_stack.pop()
                operand_stack.push(compute(operand2, operand1, operator))
            operator_stack.push(token)

    while (not operator_stack.is_empty()):
        operand1 = operand_stack.pop()
        operand2 = operand_stack.pop()
        operator = operator_stack.pop()
        operand_stack.push(compute(operand2, operand1, operator))

    return operand_stack.pop()


if __name__ == '__main__':
    print(evaluate("9 + 8 * ( 7 - 6 ) / ( 2 / 8 )"))  # 41
    print(evaluate("9 + 8 * 7 / ( 6 + 5 ) - ( 4 + 3 ) * 2"))  # 0.0909090909
    print(evaluate("9 + 8 * 7 / ( ( 6 + 5 ) - ( 4 + 3 ) * 2 )"))  # -9.66666666667