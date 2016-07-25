import pg
db = pg.DB(dbname='restaurant_db')


query = db.query('select * from user_table')
print query

# query = db.query('''
#     select
#         *
#     from
#         reviews
#     where
#         review = 'Another hipster coffee joint'
#     order by
#         review desc
#     limit
#         3
# ''')
# print query


#This is to get tuples ...
# query = db.query('''
# select * from user_table
#
# ''')
#
# tupled_result = query.getresult()
# print tupled_result


#This is to get dictionaries
# query = db.query('''
# select * from user_table
# ''')
# dictionaried_result = query.dictresult()
#
# print dictionaried_result


#This is to get named-tuples:
# query = db.query('''
# select * from user_table ''')
#
# named_result = query.namedresult()
# print named_result


#named result using for loop
# query = db.query('''
# select * from user_table ''')
#
# users = query.namedresult()
# for user in users:
#     print "User: %s, Email: %s, Karma: %s" % (user.name, user.email, user.karma)


#Insert data
# db.insert('user_table', id = 14, name='Hank Hill', email='hh@gmail.com')


#To UPDATE the dictionary needs to be updated too
# db.update('user_table', {'id': 7, 'name': 'Kahn replaced'})





#to DELETE
# db.delete('user_table', {'id': 8
# })
