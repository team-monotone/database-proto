"""
This code was written without considering the join statement yet.
http://www.gurubee.net/lecture/2392
http://wiki.gurubee.net/pages/viewpage.action?pageId=24870953
"""

"""
FK 연결하면 두 테이블 간 연결된 컬럼에서 같은 값을 가지는 데이터만으로 트리 만들어야 할 듯. -> 이거만 찾으면 훨씬 더 빠름
"""

from storage_manager_copy import Table

class SQLParser:    

    _sql_splited = None
    _sql_class = None
    _sql_type = None
    _is_sql = None

    def __init__(self, sql) -> None:
        """

        """
        # self.sql
        # if(self.validate_sql()):
        #    do something.
        
        self._sql_splited = self.split_sql(sql)      

        pass

    def split_sql(self, sql) -> list:
        sql_split = []
        sql_split = sql.replace(" ", ",").replace(";", ",").split(",")
        for i, s in enumerate(sql_split):
            if s == "":
                sql_split.pop(i)

        return sql_split

    def check_sql_type(self, sql:str) -> None:
        self.sql_class = None
        self.sql_type = None
        pass

    def validate_sql(self, sql:str)->bool:
        """
        return true if the sql is valid
        else return false
        how to check?
        """
        # self.check_sql_type(sql)
        # do something...

        # if 'select' not in sql:
        #     pass
        # if 'from' not in sql:
        #     pass

        def validate_select():
            #check existance of table and columns
            #use static method of storage_manager
            
            sql = self.__sql_splited
            valid_val = True
            table_name = None
            idx = -1
            
            is_from_exist = False
            is_where_exist = False

            from_idx = None
            where_idx = None
        
            for i, s in enumerate(sql):
                if s.lower() == "from":
                    is_from_exist = True
                    from_idx = i
                if s.lower() == "where":
                    is_where_exist = True
                    where_idx = i
                
            # parse column list
            if is_from_exist and len(sql) > (from_idx+1):
                table_name = sql[from_idx+1]
                valid_val = Table.check_table_exists('data',table_name)
                for i in range(1, from_idx):
                    valid_val = valid_val and Table.check_table_column_exists('data',table_name, sql[i])
                    if not valid_val:
                        break
            
            
            # if is_from_exist and is_where_exist:
            #     pass
            
            
            


            return valid_val
                    
        sql_types = {'select' : validate_select}

        res = sql_types[self._sql_splited[0].lower()]()
            
        return res

    def parse_select(self, sql:str)-> dict:
        """
        parse the select statement.
        find select in statement, then search other keywords such as from, where, etc.
        and create a information about the query.

        sample output:
        {sql_type: : DML, DDL,...,
            detail : 
            {
                sql_class : 'select'
                column_names : ['a', 'b'],
                table_names : ['sample_table'],
                where_conditions : None(TBD) / [] }
            }
        }
        """
        pass

    def parse_insert(self, statement:str)->dict:
        # TBD
        pass



class QueryTransformer:
    def __init__(self, parsed_query:dict) -> None:
        pass

    @staticmethod
    def access_table_by_index(table_name, index_name):
        t = Table(name=table_name)
        idx = list(index_name)
        it = Table.retrieve_index_tree(idx)
        return it
        

    @staticmethod
    def scan_index_by_condition(table_object, condition_value)->list:
        res = []
        res.append(table_object.find(condition_value))
        return res
    
    @staticmethod
    def scan_all(table_object, condition)->list:
        res = []
        for node in table_object:
            res.append(node)
        return res

class PlanGenerator:
    # it'll do a simple re-optimization of plan/executions by greedy algorithm e.g. load table(from) first, ...
    # Builder Pattern..?
    def __init__(self) -> None:
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
    def __init__(self, jobs:list) -> None:
        self.jobs = jobs

if __name__ == "__main__":
    sql = 'select a, b,c from my_table;'
    parser = SQLParser(sql)
    print(parser._sql_splited)
    # do test codes
    
