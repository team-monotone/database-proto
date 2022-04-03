
from abc import ABCMeta
from abc import abstractmethod

from binary_tree import BinaryTree
from binary_tree import BinaryTreeType

from typing import Iterable

from os import listdir
from os.path import splitext

class AbstractTable(metaclass=ABCMeta):
    '''
    example.py
    table = InheritTable(name="table", storage="storage")
    index_trees = table.retrieve_index_tree("column1", "column2")
    '''

    _name = None
    _storage = None
    _storage_instances = None
    _index_trees = None

    @abstractmethod
    def __init__(self, name:str, storage:str='data'):
        '''
        
        '''
        self._name = name
        self._storage = storage
        self._storage_instances = self._retrieve_from_storage()

    @abstractmethod
    def _retrieve_from_storage(self) -> Iterable[str]:
        '''
        
        '''
        pass

    @abstractmethod
    def _retrieve_index_tree(self, column:str) -> BinaryTreeType:
        '''
        
        '''
        pass

    @abstractmethod
    def retrieve_index_tree(self, *columns:Iterable[str]) -> Iterable[BinaryTreeType]:
        '''
        
        '''
        # for column in columns:
        #     index_tree = self._retrieve_index_tree(column)
        #     pass
        
        pass

class Table(AbstractTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def storage(self):
        return self._storage

    @property
    def storage_instances(self):
        return self._storage_instances

    @property
    def index_trees(self):
        return self._index_trees
    
    def _retrieve_from_storage(self) -> Iterable[str]:

        column_list = listdir(f'{self._storage}/table_{self._name}')
        column_list = [splitext(x)[0].split("_")[1] for x in column_list ]
        column_list.sort()


        return column_list
        
    def _retrieve_index_tree(self, column: str) -> BinaryTreeType:
        file_name = f'column_{column}.json'

        with open(f'data/table_{self.name}/{file_name}', "r") as fp:
            column_tree = BinaryTree.load(BinaryTree,fp)
        return column_tree
    
    def retrieve_index_tree(self, *columns: Iterable[str]) -> Iterable[BinaryTreeType]:
        index_trees = []
        for column in columns:
            index_trees.append(self._retrieve_index_tree(column))
        return index_trees


if __name__ == "__main__":
    a = Table("mytable","data")
    print("column list")
    column_list = a._retrieve_from_storage()
    for x in column_list:
        print(x)
    print("json tree data")
    tree_list = a.retrieve_index_tree(*a._retrieve_from_storage())
    for x in tree_list:
        print(BinaryTree.dumps(BinaryTree,x))
    print("search a = 2")
    target_column = "a"
    for column in column_list:
        if(column.split("-")[1] == target_column):
            target_column_name = column
    tree_a = a.retrieve_index_tree(*[target_column_name])[0]
    row = tree_a.find(2).value
    import json
    print(json.loads(row))
    print(type(json.loads(row)))