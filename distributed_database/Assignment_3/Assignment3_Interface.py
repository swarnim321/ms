#
# Assignment3 Interface
#

import psycopg2
import os
import sys
import threading

# Donot close the connection inside this file i.e. do not perform openconnection.close()
def ParallelSort (InputTable, SortingColumnName, OutputTable, openconnection):
    #Implement ParallelSort Here.
     #Remove this once you are done with implementation
     cur = openconnection.cursor()
     cur.execute("SELECT MAX( " + SortingColumnName + ") , MIN( " + SortingColumnName + ") FROM "+InputTable +";")
     max_val, min_val = cur.fetchone()
     increament = (max_val - min_val)/5
     thread=[0] * 5
     lower_bound = min_val
     upper_bound = lower_bound + increament
     for i in range(5):
        thread[i]=threading.Thread(target= sort_func_thread, args=(InputTable, "temp", SortingColumnName, lower_bound, upper_bound, i, openconnection))
        thread[i].start()
        lower_bound = upper_bound
        upper_bound = lower_bound + increament
     cur.execute("DROP TABLE IF EXISTS " + OutputTable + ";")
     cur.execute("CREATE TABLE " + OutputTable + " ( LIKE " + InputTable + " INCLUDING ALL );")
     for i in range(5):
        thread[i].join()
        table_name= "temp"+str(i)
        cur.execute("INSERT INTO " + OutputTable +" SELECT * FROM " + table_name + ";")
     cur.close()
     openconnection.commit()


     

def ParallelJoin (InputTable1, InputTable2, Table1JoinColumn, Table2JoinColumn, OutputTable, openconnection):
    #Implement ParallelJoin Here.
    # Remove this once you are done with implementation
    cur = openconnection.cursor()
    cur.execute("SELECT MAX(" + InputTable1+"."+Table1JoinColumn + ") , MIN(" + Table1JoinColumn + ") FROM " + InputTable1 +" ;")
    max_val1, min_val1= cur.fetchone()
    
    cur.execute("SELECT MAX(" + Table2JoinColumn + ") , MIN(" + Table2JoinColumn + ") FROM " + InputTable2 + " ;")
    max_val2, min_val2 = cur.fetchone()
    
    max_val = max(max_val1, min_val2)
    min_val = min(max_val1, min_val2)
    increament = (max_val - min_val)/ 5
    
    cur.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + InputTable1 + "';")
    meta_schema_1 = cur.fetchall()
    cur.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + InputTable2 + "';")
    meta_schema_2 = cur.fetchall()
    
    thread=[0]*5
    lower_bound = min_val
    upper_bound = lower_bound + increament    
    for i in range(5):
        thread[i]=threading.Thread(target=joinTable, args=(InputTable1, InputTable2, meta_schema_1, meta_schema_2, "temp_table1", "temp_table2", Table1JoinColumn, Table2JoinColumn, "output_temp", lower_bound, upper_bound , i, openconnection))
        thread[i].start()
        lower_bound = upper_bound
        upper_bound = lower_bound + increament
    cur.execute("DROP TABLE IF EXISTS " + OutputTable + ";")
    cur.execute("CREATE TABLE " + OutputTable + " ( LIKE " + InputTable1 + " INCLUDING ALL);")
    for j in range (len(meta_schema_2)):
        if j != len(meta_schema_2)-1:
            cur.execute ("ALTER TABLE " + OutputTable + " " + "ADD COLUMN " + meta_schema_2[j][0] + " " + meta_schema_2[j][1] + ";")
        else:
            cur.execute ("ALTER TABLE " + OutputTable + " " + "ADD COLUMN " + meta_schema_2[j][0] + " " + meta_schema_2[j][1] + ";")
    
    for i in range(5):
        thread[i].join()
        table_name =  "output_temp" +str(i)
        cur.execute("INSERT INTO " + OutputTable +" SELECT * FROM " + table_name + ";")
    cur.close()
    openconnection.commit()


def sort_func_thread(InputTable, temp_table, sortingColumnName,  lower_Bound, upper_Bound, i, openconnection):
    cur = openconnection.cursor()
    table_name= temp_table + str(i)
    cur.execute("DROP TABLE IF EXISTS " + table_name + ";")
    cur.execute("CREATE TABLE " + table_name + " ( LIKE " + InputTable + " INCLUDING ALL );")
    if i==0:
        cur.execute("INSERT INTO " + table_name +" SELECT * FROM " + InputTable + " WHERE " + sortingColumnName + " >= "+ str(lower_Bound) + " AND " + sortingColumnName + " <= " + str(upper_Bound) + " ORDER BY " + sortingColumnName + " ASC;")
    else:
        cur.execute("INSERT INTO " + table_name +" SELECT * FROM " + InputTable + " WHERE " + sortingColumnName + " > "+ str(lower_Bound) + " AND " + sortingColumnName + " <= " + str(upper_Bound) + " ORDER BY " + sortingColumnName + " ASC;")


   
def joinTable(InputTable1, InputTable2, meta_schema1, meta_schema2, table1, table2, join_col_for_1, join_col_for_2, output_temp, lower_Bound, upper_Bound, i, openconnection):
   #Function to join two single partition based on join_col_for_1 and join_col_for_2 using a thread
    con = openconnection
    cur = con.cursor()
    temp_table_name_1 = table1 + str(i)
    temp_table_name_2 = table2 + str(i)
    temp_output_table_name = output_temp + str(i)
    cur.execute("DROP TABLE IF EXISTS " + temp_table_name_1 + ";")
    cur.execute("CREATE TABLE " + temp_table_name_1 + " ( LIKE " + InputTable1 + " INCLUDING ALL);")
	 
    cur.execute("DROP TABLE IF EXISTS " + temp_table_name_2 + ";")
    cur.execute("CREATE TABLE " + temp_table_name_2 + " ( LIKE " + InputTable2 + " INCLUDING ALL);")
	 
    cur.execute("DROP TABLE IF EXISTS " + temp_output_table_name + ";")
    cur.execute("CREATE TABLE " + temp_output_table_name + " ( LIKE " + InputTable1 + " INCLUDING ALL);")
	 
	
    for j in range(len(meta_schema2)):
        if j != len(meta_schema2)-1:
            cur.execute("ALTER TABLE " + temp_output_table_name + " " + "ADD COLUMN " + meta_schema2[j][0] + " " + meta_schema2[j][1] + ";")
        else:
            cur.execute("ALTER TABLE " + temp_output_table_name + " " + "ADD COLUMN " + meta_schema2[j][0] + " " + meta_schema2[j][1] + ";" )
    if i==0:
        cur.execute("INSERT INTO " + temp_table_name_1 +" SELECT * FROM " + InputTable1 + " WHERE " + join_col_for_1 + " >= "+ str(lower_Bound) + " AND " + join_col_for_1 + " <= " + str(upper_Bound) + ";")
        cur.execute("INSERT INTO " + temp_table_name_2 +" SELECT * FROM " + InputTable2 + " WHERE " + join_col_for_2 + " >= "+ str(lower_Bound) + " AND " + join_col_for_2 + " <= " + str(upper_Bound) + ";")
    else:
        cur.execute("INSERT INTO " + temp_table_name_1 +" SELECT * FROM " + InputTable1 + " WHERE " + join_col_for_1 + " > "+ str(lower_Bound) + " AND " + join_col_for_1 + " <= " + str(upper_Bound) + ";"	)
        cur.execute("INSERT INTO " + temp_table_name_2 +" SELECT * FROM " + InputTable2 + " WHERE " + join_col_for_2 + " > "+ str(lower_Bound) + " AND " + join_col_for_2 + " <= " + str(upper_Bound) + ";"	)
    cur.execute("INSERT INTO " + temp_output_table_name + " SELECT * FROM " + temp_table_name_1 + " INNER JOIN " + temp_table_name_2 + " ON " + temp_table_name_1 + "." + join_col_for_1 + " = " + temp_table_name_2 + "." + join_col_for_2 + ";")
	 
    
             


################### DO NOT CHANGE ANYTHING BELOW THIS #############################


# Donot change this function
def getOpenConnection(user='postgres', password='1234', dbname='ddsassignment3'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

# Donot change this function
def createDB(dbname='ddsassignment3'):
    """
    We create a DB by connecting to the default user and database of Postgres
    The function first checks if an existing database exists for a given name, else creates it.
    :return:None
    """
    # Connect to the default database
    con = getOpenConnection(dbname='postgres')
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    # Check if an existing database with the same name exists
    cur.execute('SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname=\'%s\'' % (dbname,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute('CREATE DATABASE %s' % (dbname,))  # Create the database
    else:
        print('A database named {0} already exists'.format(dbname))

    # Clean up
    cur.close()
    con.commit()
    con.close()

# Donot change this function
def deleteTables(ratingstablename, openconnection):
    try:
        cursor = openconnection.cursor()
        if ratingstablename.upper() == 'ALL':
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()
            for table_name in tables:
                cursor.execute('DROP TABLE %s CASCADE' % (table_name[0]))
        else:
            cursor.execute('DROP TABLE %s CASCADE' % (ratingstablename))
        openconnection.commit()
    except psycopg2.DatabaseError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
        sys.exit(1)
    except IOError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()


