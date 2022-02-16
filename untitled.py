
'''
[module structure hierarchy]

unidentified class which will be discussed in future

    +- binary tree 01
        +- node instance 01
        +- node instance 02
        > node instances goes on ...

    +- binary tree 02
        +- node instance 01
        +- node instance 02
        > node instances goes on ...
    
    > binary tree instances goes on ...

'''

from typing import TypeVar
from typing import IO

# variables for strong-type.

from strong_type import Itself
from strong_type import is_satisfied_strongly

strong_node_init = (
    (1, 'key', [int]), 
    (3, 'node_on_left', [None, Itself]), 
    (4, 'node_on_right', [None, Itself]),
    )

strong_btree_init = (
    (1, 'key', [int]),
    )

# variables for type-hint.

NodeType = TypeVar('NodeType')
BinaryTreeType = TypeVar('BinaryTreeType')

# module description.

class ArgumentException(Exception):
    '''argument exception class'''

    def __init__(self, message:str):
        super().__init__(message)

class Node(object):
    '''node class'''

    # key for identify node instance
    _key = None

    # value which is contained node instance
    _value = None

    # left node instance on this instance (reference) 
    _node_on_left = None

    # right node instance on this instance (reference)
    _node_on_right = None
    
    @is_satisfied_strongly(strong_node_init)
    def __init__(
            self, 
            key:int, 
            value:object=None,
            node_on_left:NodeType=None,
            node_on_right:NodeType=None
            ):

        # key should be given by 
        # relative-upper management class instance,
        # not by itself.
        # e.g. this node key is generated by its tree.

        self._key = key
        self._value = value
        self._node_on_left = node_on_left
        self._node_on_right = node_on_right

    def __str__(self):
        return f'{self.__class__.__name__}<{self.key},{self.value}>'
    
    def __repr__(self):
        return f'{self.__class__.__name__}<{self.key},{self.value}>'

    @property
    def key(self) -> str:
        return self._key

    @property
    def value(self) -> object:
        return self._value

    @property
    def node_on_left(self) -> NodeType:
        return self._node_on_left

    @property
    def node_on_right(self) -> NodeType:
        return self._node_on_left

class BinaryTree(object):
    '''node class'''
    
    # key for identify binary tree instance
    _key = None

    # root node instance
    _root = None

    @is_satisfied_strongly(strong_btree_init)
    def __init__(self, key:int):
        # key should be given by 
        # a relative-upper management class instance,
        # not by itself.

        self._key = key

    @property
    def key(self) -> str:
        return self._key

    @property
    def nodes(self) -> NodeType:
        # yield or enumerate nodes that are contained itself.
        
        yield None

    def _insert_as_value(self, value:object) -> bool:
        # do not describe anything directly.
        # your code goes here, not a public method.

        pass
    
    def _insert_as_node(self, node:NodeType) -> bool:
        # do not describe anything directly.
        # your code goes here, not a public method.

        pass

    def _remove(self, key:int) -> bool:
        # do not describe anything directly.
        # your code goes here, not a public method.
        
        pass

    def _find(self, key:int) -> NodeType:
        # do not describe anything directly.
        # your code goes here, not a public method.
        
        pass

    def insert(self, value:object, node:NodeType) -> bool:
        # your code goes here in a public method.

        if value is not None and node is not None:
            raise ArgumentException('value and node not to be given at the same time.')

        pass

    def remove(self, key:int) -> bool:
        # your code goes here in a public method.

        pass

    def find(self, key:int) -> NodeType:
        # your code goes here in a public method.
        
        pass

    @staticmethod
    def dumps(cls, object_:BinaryTreeType) -> str:
        # this method should be treated as static method.

        pass

    @staticmethod
    def loads(cls, str_:str) -> BinaryTreeType:
        # this method should be treated as static method.

        pass

    @staticmethod
    def dump(cls, object_:BinaryTreeType, fp:IO[str]) -> str:
        # this method should be treated as static method
        # and also described with static method "dumps"

        pass

    @staticmethod
    def load(cls, fp:IO[str]) -> BinaryTreeType:
        # this method should be treated as static method
        # and also described with static method "loads"

        pass