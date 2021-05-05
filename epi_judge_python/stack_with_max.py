from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.internal_list = []
        self.max_stack = []
        self.max_stack_counts = []
        self.max_int = None

    def empty(self):
        return len(self.internal_list) == 0

    def max(self):
        return self.max_int

    def pop(self):
        temp = self.internal_list.pop()
        if len(self.internal_list) == 0:
            self.__init__()
            return temp

        # if we are popping the max_int we have to update our max_int
        if temp == self.max_int:
            # first decrease the counter for that max_int as we may have duplicates
            self.max_stack_counts[-1] -= 1
            # if we have no duplicates get the next largest number on the stack
            if self.max_stack_counts[-1] == 0:
                self.max_stack_counts.pop()
                self.max_int = self.max_stack.pop()

        return temp

    def push(self, x):
        if self.max_int == None or x > self.max_int:
            # add old max_int to stack
            self.max_stack.append(self.max_int)

            # update new max_int
            self.max_int = x
            
            # update our counts for this max int
            self.max_stack_counts.append(1)
        elif x == self.max_int:
            self.max_stack_counts[-1] += 1

        self.internal_list.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
