import pg
db = pg.DB(dbname='projects_db')

#problem1
# query = db.query('select * from project')
# print query



#problem2
# givemeName = raw_input("Enter a project name ")
#
# db.insert('project', name = givemeName)



#problem 3
takeID = raw_input("Please enter the ID of project you'd like to edit ")


updateInfo = raw_input("Please enter a new updated name to that project ")
db.update('project', id = takeID, name = updateInfo)
