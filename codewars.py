# Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

# Example:

# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
# Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right

class Calculator(object):
    def evaluate(self, string):
        if len(string) == 0:
            return 0
        
        values = string.split(" ")
        head = OperationHeap(values[0])

        # create a stack of our current head as each parenthesis starts a new stack
        heads = [head]
        
        # build our heap up with the values and operations
        for i in range(1, len(values)):
            heads[0].print()
            temp = OperationHeap(values[i])
            head = heads.pop()

            if values[i] == ")":
                if len(heads) == 0:
                    heads.append(head)
                continue
            
            head = head.add(temp)
            heads.append(head)

            if values[i] == "(":
                heads.append(temp)    

        # resolve the heap to get the value we need            
        return heads[0].resolve()

class OperationHeap:
    def __init__(self, val):
        self.val = val
        if val.isnumeric():
            self.opval = 4
        else:
            # create key value pairs for determining the order of our min value heap
            ops = {"(": 1, ")": 1, "*":3, "/":3, "+":2, "-":2}
            self.opval = ops[val]
        self.rChild = None
        self.lChild = None

    # useful debugging tool
    def print(self):
        print(self.val)
        if self.lChild != None:
            print("leftChild:")
            self.lChild.print()
        if self.rChild != None:
            print("rChild:")
            self.rChild.print()
        
    def isOp(self):
        return self.val is Number

    def add(self, node):
        if node.opval >= self.opval or node.opval == 1:
            if self.lChild == None and self.opval != 1:
                self.lChild = node
            elif self.rChild == None:
                self.rChild = node
            else:
                self.rChild = self.rChild.add(node)
                
            return self
        else:
            node.lChild = self
        return node
    
    def resolve(self):
        if self.opval == 4:
            return int(self.val)
        elif self.opval == 1:
            return self.rChild.resolve()
        elif self.val == "*":
            return self.lChild.resolve() * self.rChild.resolve()
        elif self.val == "/":
            return self.lChild.resolve() / self.rChild.resolve()
        elif self.val == "+":
            return self.lChild.resolve() + self.rChild.resolve()
        return self.lChild.resolve() - self.rChild.resolve()

# Tests for above problem
# @test.describe("Sample tests")
# def sample_tests():
#     test.assert_equals(Calculator().evaluate('1 + 1 + 1'), 3)
#     test.assert_equals(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
#     test.assert_equals(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
    
#     test.assert_equals(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
#     test.assert_equals(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
#     test.assert_equals(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
#     test.assert_equals(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)