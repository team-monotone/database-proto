
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
    _column_names = [] # whole column names of table

    @abstractmethod
    def __init__(self, name:str, storage:str='data'):
        '''
        
        '''
        self._index_trees = {} # init index_trees
        self._name = name # table_name
        self._storage = storage # folder_name
        self._storage_instances = self._get_column_list()
        self._column_key_mapper = {} # {1:'a', 2:'b', 'a':1, 'b':2}


    @abstractmethod
    def load_index_trees(self, table_id:int) -> list: # list or something appropriate data structure
        # do something
        return list()
        
    @abstractmethod
    def _get_column_list(self) -> Iterable[str]:
        '''
        
        '''
        pass

    @abstractmethod
    def _retrieve_index_tree(self, column:str) -> BinaryTreeType:
        '''
        
        '''
        pass

class Table(AbstractTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._column_names = self._get_column_list()
        for column in self._column_names:
            column_splitted = column.split("-")
            self._column_key_mapper[column_splitted[0]] = column_splitted[1]
            self._column_key_mapper[column_splitted[1]] = column_splitted[0]

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

    def load_index_tree(self, column : str) -> BinaryTreeType:
        return self._retrieve_index_tree(column)

    def load_index_trees(self, columns:list)  -> Iterable[BinaryTreeType]: # list or something appropriate data structure
        # do something
        # table_name = self.name
        for column in columns:
            self._index_trees[column] = self._retrieve_index_tree(column)
        # return index_trees
    
    def _get_column_list(self) -> Iterable[str]:

        column_list = listdir(f'{self._storage}/table_{self._name}')
        column_list = [splitext(x)[0].split("_")[1] for x in column_list ]
        column_list.sort()
        return column_list
        
    def _retrieve_index_tree(self, column: str) -> BinaryTreeType:
        file_name = f'column_{self._column_key_mapper[column]}-{column}.json'

        with open(f'data/table_{self.name}/{file_name}', "r") as fp:
            column_tree = BinaryTree.load(BinaryTree,fp)
        return column_tree
        

    @staticmethod
    def check_table_exists(storage_name:str, table_name:str) -> bool:
        idx = -1
        try:
            table_list = listdir(storage_name)
            idx = table_list.index(f'table_{table_name}')
        except:
            return False        
        return idx >= 0
        
    @staticmethod
    def check_table_column_exists(storage_name:str, table_name:str, table_column:str) -> bool:
        column_list = listdir(f'{storage_name}/table_{table_name}')
        column_list = [splitext(x)[0].split("_")[1] for x in column_list ]
        
        res = False
        for column in column_list:
            if column.split("-")[1] == table_column:
                res = True
        
        return res

if __name__ == "__main__":
    
    a = Table("mytable","data")
    column_list = a._column_names
    print("column list = ",column_list)

    print("json tree data")
    a.load_index_trees(['a', 'b'])
    print(a._index_trees)
    
    for tree in a._index_trees.values():
        print(BinaryTree.dumps(BinaryTree, tree))

    print("search a = 2")
    target_column = "a"
    tree_a = a.load_index_tree(target_column)
    print(BinaryTree.dumps(BinaryTree,tree_a))

    row = tree_a.find(2).value

    import json
    print(json.loads(row))
    print(type(json.loads(row)))

    print(Table.check_table_exists('data', 'mytabl'))
    print(Table.check_table_column_exists('data', 'mytable', 'd'))