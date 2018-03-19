import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "^":
        return op1 ** op2
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1*1.0 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList=[]
    temp_tokenList=[]
    # infixexpr.encode("ascii")
    # tokenList = infixexpr.split()
    for x in infixexpr:
        tokenList.append(x.encode("ascii"))
    # tokenList = tokenList[1:-1]
    temp_tokenList.append(tokenList[0])
    # print tokenList
    for i in xrange(1,len(tokenList)):
        print tokenList[i]
        print temp_tokenList
        if tokenList[i] in "0123456789" and tokenList[i-1] in "0123456789":
            t=temp_tokenList.pop()
            temp=t+tokenList[i]
            temp_tokenList.append(temp)
        elif tokenList[i] in "0123456789" and tokenList[i-1] not in "0123456789":
            temp_tokenList.append(tokenList[i])
        else:
            temp_tokenList.append(tokenList[i])

    tokenList=temp_tokenList
    print tokenList

    for token in tokenList:
        if token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
# print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
# print(postfixEval(infixToPostfix("5 * 3 ^ ( 4 - 2 )")))
def process(input, entities=None):
    print str(input)
    s=input.split(' ')

    print s[0]
    print s[1]
    msg=postfixEval(infixToPostfix(s[0]))
    message=TextTemplate(str(msg)).get_message()
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output