from abc import *

from binary_tree import BinaryTree, BinaryTreeType

# 테이블 로드 객체 
#    잡다한 기능은 따로 구현 하고 베이스 기능만 구현(우리의 목표는 select * from table)

class AbstractTable(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *args, **kargs) -> None:
        """
        어떻게 해당 테이블에 index tree, column name 등의 metadata를 저장할 것인가?
        """
        # parameter handling

        # it contains Binary tree instances (index b-trees). key: (primary or user-defined) key of table, value: BinaryTree instance id
        # how to handle / load tree which created by join-based operation? 
        self._index_trees = {} 
        self._column_names = [] # whole column names of table
        self._column_types = []
        self._table_name = ""
        self._table_id = ""

    "================LOAD / DUMP======================"

    @abstractmethod
    def load_index_tree(self, tree_id:int) -> BinaryTreeType:
        # do something
        return BinaryTreeType

    @abstractmethod
    def load_index_trees(self, table_id:int) -> list: # list or something appropriate data structure
        # do something
        return list()

    @abstractmethod
    def dump_index_tree(self, tree:BinaryTreeType) -> BinaryTreeType:
        # do something
        return BinaryTreeType

    @abstractmethod
    def dump_index_trees(self, trees:list) -> list: # list or something appropriate data structure
        # do something
        return list()

    # "dump is same as above"

    "================SINGLE TREE======================"
    @abstractmethod
    def add_data_by_tree_id(self, tree_id, data) -> None:
        # load tree by tree_id

        # add new node in tree

        # dump updated tree
        pass
    
    @abstractmethod
    def delete_data_by_tree_id(self, tree_id, data) -> None:
        # load tree by tree_id

        # remove node in tree

        # dump updated tree
        pass

    @abstractmethod
    def modify_data_by_tree_id(self, tree_id, data) -> None:
        # load tree by tree_id

        # modify node in tree

        # dump updated tree
        pass
    

    "================WHOLE TREE======================"
    @abstractmethod
    def add_data_on_whole_tree(self, data) -> None:
        for _, tree_id in self._index_trees:
            # load tree by tree_id

            # add new node in tree

            # dump updated tree
            pass

    @abstractmethod
    def delete_data_on_whole_tree(self, data) -> None:
        for _, tree_id in self._index_trees:
            # load tree by tree_id

            # remove node in tree

            # dump updated tree

            pass

    @abstractmethod
    def modify_data_on_whole_tree(self, data) -> None:
        for _, tree_id in self._index_trees:
            # load tree by tree_id

            # remove node in tree

            # dump updated tree

            pass


    "================INTEGRITY CHECK======================"
    @abstractmethod
    def check_integrity() -> bool:
        # 모든 트리가 같은 데이터를 가지고 있는지 확인

        # 수정로직은 TBD(변경사항 저장해두었다가 나중에 한번에 적용 등)
        pass

    "================OPTIMIZATION======================"
    @abstractmethod
    def balancing() -> None:
        # 모든 트리에 대해 밸런싱해서 깊이를 낮춤
        pass
