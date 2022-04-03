"""
This code was written without considering the join statement yet.
http://www.gurubee.net/lecture/2392
"""

"""
FK 연결하면 두 테이블 간 연결된 컬럼에서 같은 값을 가지는 데이터만으로 트리 만들어야 할 듯. -> 이거만 찾으면 훨씬 더 빠름
"""

import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where, Comparison, Parenthesis
from sqlparse.tokens import Keyword, DML, Text

import binary_tree


class SQLParser:
    def __init__(self, sql) -> None:
        self.tokens = []
        sql = sqlparse.format(sql, keyword_case = 'upper')
        statements = sqlparse.split(sql)
        for stat in statements:
            token = sqlparse.parse(stat)
            self.tokens.append(token)

        for sql in self.tokens:
            for statement in sql:
                if statement.get_type() == 'SELECT':
                    self.parse_select(statement)
                else:
                    raise NotImplementedError()

    def parse_select(self, statement):
        it = self.statement_generator(statement)


        for item in statement:
            if item.ttype is DML and item.value.upper() == 'SELECT':
                while(item.ttype is Text.Whitespace)
                print('select')
                continue
            elif item.ttype is Text.Whitespace:
                print('ws')
                continue
            elif item.ttype is Identifier:
                print(item)

    def statement_generator(self, statement):
        for stat in statement:
            yield stat


    

class SQLPlanner:
    # it'll work a simple relocation of plan/executions by greedy algorithm e.g. load table(from) first, ...
    # Builder Pattern..?
    def __init__(self) -> None:
        pass

    def access_table(self):
        pass

    def access_table_by_index(self):
        pass

    def access_table_by_condition(self):
        pass

class SQLExecutor:
    def __init__(self, tokens) -> None:
        pass

    def _select(self, statement):
        # load table

        # filtering using origin_colname

        # replace colname to alias
        pass

        
class QueryOptimizer:
    """Optimize whole process of a execution of the query
    """
    pass

class PrecedenceGraph:
    pass

class Job:
    # it will be a one of the operations in parsed sql
    # its container will be implemented as a linked list in order to easy to sort
    def __init__(self, func, tree, *args, **kargs) -> None:
        self.func = func
        self.tree = tree
        self.args = args
        self.kargs = kargs

    def run(self):
        self.func(self.tree, *self.args, **self.kargs)

class JobModule:
    def __init__(self, *args) -> None:
        self.jobs = args

if __name__ == "__main__":
    sql = 'select a,b,c from my_table;'
    parser = SQLParser(sql)
    
