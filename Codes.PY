 import MPYdata


db = MPYdata()

db.connect('data.db')   

db.create_table('data', 'name text, age integer')

db.insert('data', 'name, age')

db.getall('data')

db.rename_column('data', 'name', 'new_name')

db.rename_table('data', 'new_data')

db.delete_table('data')

db.delete_column('data', 'name')

db.delete('data', 'name')

db.update('data', 'name', 'new_name', 'name', 'new_name')

db.showallcolumns()

db.showalltables()

db.showalldata()

db.showalltypes()

db.showallvalues()

db.dbname()

db.select('data', 'name')

db.delete('data', 'name')

db.update('data', 'name', 'new_name', 'name', 'new_name')

db.rename_table('data', 'new_data')

db.close()

db.disconnect()

