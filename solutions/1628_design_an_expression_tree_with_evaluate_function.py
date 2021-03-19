import abc 
from abc import ABC, abstractmethod 


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class NumNode(Node):
    def __init__(self, val: int):
        self.val = val
    
    def evaluate(self) -> int:
        return self.val


class OpNode(Node):
    def __init__(self, left: 'Node', right: 'Node'):
        self.left = left
        self.right = right
    
    def evaluate(self) -> int:
        pass

    
class AddOpNode(OpNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class SubtractOpNode(OpNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

    
class MultiplyOpNode(OpNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()  

    
class DivideOpNode(OpNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()      


class TreeBuilder(object):
    def _handle_op(self, op, left, right):
        if op == '+':
            return AddOpNode(left, right)
        elif op == '-':
            return SubtractOpNode(left, right)
        elif op == '*':
            return MultiplyOpNode(left, right)
        else:
            return DivideOpNode(left, right)
    
    def buildTree(self, postfix: List[str]) -> 'Node':
        st = []
        for i in postfix:
            if '0' <= i[-1] <= '9':
                st.append(NumNode(int(i)))
            else:
                right = st.pop()
                left = st.pop()
                st.append(self._handle_op(i, left, right))
        return st[-1]
