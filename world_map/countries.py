import sqlite3
from world_map.tables import PATH_DB, connection, cursor


# Populam tabelul countries
# countries_query = '''
#     INSERT INTO countries (country_code, country_name, continent_id, population)
#     VALUES (?, ?, ?, ?)
#     '''
#
# # list of tuples
# countries_to_add_list = [
#     ('RO', 'Romania', 6, 19132594),         # Europe
#     ('HU', 'Hungary', 6, 9769000),          # Europe
#     ('FR', 'France', 6, 65273511),          # Europe
#     ('DE', 'Germany', 6, 83166711),         # Europe
#     ('JP', 'Japan', 5, 125800000),          # Asia
#     ('CN', 'China', 5, 1444216107),         # Asia
#     ('US', 'United States', 2, 331893745),  # North America
#     ('BR', 'Brazil', 7, 213993437),         # South America
#     ('NG', 'Nigeria', 1, 211400708),        # Africa
#     ('AU', 'Australia', 3, 25788217),       # Oceania
#     ('AQ', 'Antarctica', 4, 0)              # Antarctica (has 0 permanent residents)
# ]
#
# cursor.executemany(countries_query, countries_to_add_list)
#
# connection.commit()
# connection.close()



# READ / GET ALL COUNTRIES
# cursor.execute('''SELECT * FROM countries ORDER BY country_name ASC''')
# countries = cursor.fetchall()
# print(countries)
# print(type(countries))



# DELETE ALL TABLE ENTRIES - while keeping intact the table structure
# cursor.execute('''SELECT * FROM countries''')
# countries = cursor.fetchall()
#
# for country in countries:
#     table_name = country[0]
#     deletion_query = '''
#     DELETE FROM countries
#     '''
#     cursor.execute(deletion_query)  # Deletes all rows from the table
# print(f"All data from the table has been deleted.")
#
# connection.commit()
# connection.close()



# DROP THE ENTIRE TABLE - useful for resetting id column's automatic numbering
# table_name = "countries"
# cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
# print(f"Table '{table_name}' has been deleted.")
# connection.commit()
# connection.close()





# 5. Scrie un query SQL care sa citeasca toate tarile din tabelul countries, ordonate dupa nume.
# cursor.execute('''SELECT country_name FROM countries ORDER BY country_name ASC''')
# country_names = cursor.fetchall()
# # print(country_names) # list of tuples
# # print(type(country_names))
# # print(*country_names) # unpacked list, just tuples
#
# for country in country_names:
#     print(*country) # unpacked strings (containing country names)



# 6. Scrie un query SQL care sa numere cate tari sunt in tabelul countries.
# cursor.execute('''SELECT COUNT(*) AS count_countries FROM countries''')
# count_all_countries = cursor.fetchone()
#
# print(count_all_countries) # tuple
# print(type(count_all_countries)) # ver
# print(*count_all_countries) # unpacked tuple
#
# print(count_all_countries[0]) # print first element in tuple
# print(f"Table 'countries' contains {count_all_countries[0]} countries") # Final



# 7. Scrie un query SQL care sa citeasca doar acele tari care au o populatie mai mare de 20 milioane locuitori.
# cursor.execute('''SELECT country_name FROM countries WHERE population > 20000000''')
# countries_with_population_constraints = cursor.fetchall() # fetchone() would only give 'France' as an output (first country that exceeds 20kk inhabitants that was found)
#
# for country in countries_with_population_constraints:
#     print(*country)



# 8. Scrie un query SQL care sa citeasca doar acele tari care incep cu o litera aleasa de tine.
cursor.execute('''SELECT country_name FROM countries WHERE country_name LIKE "A%"''')
countries_with_population_constraints = cursor.fetchall()

for country in countries_with_population_constraints:
    print(*country)
