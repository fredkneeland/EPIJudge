class Calculator(object):
    print("---------")
    def evaluate(self, string):
        if len(string) == 0:
            return 0
        
        
        values = string.split(" ")
        head = OperationHeap(values[0])
        heads = [head]
        
        # build our 
        for i in range(1, len(values)):
            print("--------------")
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
                print("push")
                heads.append(temp)                
        print("---------")
        heads[0].print()
        print("---------")
        return heads[0].resolve()
            
ops = {"(": 1, ")": 1, "*":3, "/":3, "+":2, "-":2, "0":4, "1":4, "2":4, "3":4, "4":4, "5":4, "6":4, "7":4, "8":4, "9":4}

class OperationHeap:
    def __init__(self, val):
        self.val = val
        self.opval = ops[val]
        self.rChild = None
        self.lChild = None

    def print(self):
        print(self.val)

        if self.lChild != None:
            print("leftChild:")
            self.lChild.print()
        # print(self.val)
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
#         print("resolve: ", self.val)
        if self.opval == 4:
            print(self.val)
            return int(self.val)
        elif self.opval == 1:
            print("return "+str(self.rChild.resolve()))
            return self.rChild.resolve()
        elif self.val == "*":
            print(str(self.lChild.resolve())+"*"+str(self.rChild.resolve()))
            return self.lChild.resolve() * self.rChild.resolve()
        elif self.val == "/":
            print(str(self.lChild.resolve())+"/"+str(self.rChild.resolve()))
            return self.lChild.resolve() / self.rChild.resolve()
        elif self.val == "+":
            print(str(self.lChild.resolve())+"+"+str(self.rChild.resolve()))
            return self.lChild.resolve() + self.rChild.resolve()
        print(str(self.lChild.resolve())+"-"+str(self.rChild.resolve()))
        return self.lChild.resolve() - self.rChild.resolve()