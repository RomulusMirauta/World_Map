import sqlite3
from world_map.tables import PATH_DB, connection, cursor


# Populam tabelul continents
# continents_query = '''
#     INSERT INTO continents (continent_name, continent_code)
#     VALUES (?, ?)
#     '''
#
# # list of tuples
# continents_to_add_list = [
#     ('Africa', 'AF'),
#     ('North America', 'NA'),
#     ('Oceania', 'OC'),
#     ('Antarctica', 'AN'),
#     ('Asia', 'AS'),
#     ('Europe', 'EU'),
#     ('South America', 'SA')
# ]
#
# cursor.executemany(continents_query, continents_to_add_list)
#
# connection.commit()
# connection.close()



# READ / GET ALL CONTINENTS
# cursor.execute('''SELECT * FROM continents''')
# continents = cursor.fetchall()
# print(continents)
# print(type(continents))



# DELETE ALL TABLE ENTRIES - while keeping intact the table structure
# cursor.execute('''SELECT * FROM continents''')
# continents = cursor.fetchall()
#
# for continent in continents:
#     table_name = continents[0]
#     deletion_query = '''
#     DELETE FROM continents
#     '''
#     cursor.execute(deletion_query)  # Deletes all rows from the table
# print(f"All data from the table has been deleted.")
#
# connection.commit()
# connection.close()



# DROP THE ENTIRE TABLE - useful for resetting id column's automatic numbering
# table_name = "continents"
# cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
# print(f"Table '{table_name}' has been deleted.")
# connection.commit()
# connection.close()
