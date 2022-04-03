import sqlparse

sql = 'select * from foo; select * from bar;'
# print(sqlparse.split(sql))

sql = 'select * from foo where id in (select id from bar);'
# print(sqlparse.format(sql, reindent=True, keyword_case='upper'))

sql = 'select * from "someschema"."mytable" where id = 1'
parsed = sqlparse.parse(sql)

# print(parsed)

stmt = parsed[0]  # grab the Statement object
# print(stmt)
# for t in stmt.tokens:
#     print(t)