import psycopg2


RROBIN_TABLE_PREFIX = 'rrobin_part'
RANGE_TABLE_PREFIX = 'range_part'

def getOpenConnection(user='postgres', password='1234', dbname='postgres'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")


def loadRatings(ratingstablename, ratingsfilepath, openconnection):
    output = []
    cur = openconnection.cursor()
    cur.execute("DROP TABLE IF EXISTS RATINGS;")
    handle = open(ratingsfilepath, 'r')

    cur.execute(
        "CREATE TABLE {0} (userid int, temp1 varchar, movieid int, temp2 varchar, rating float, temp3 varchar, temp4 varchar)".format(
            ratingstablename))

    # Handling empty values by replacing it with null. Using null='' option. This option replaces empty strings with NULL.
    cur.copy_from(handle, ratingstablename, sep=":", null='')

    drop_column = 'ALTER TABLE {} DROP temp1, DROP temp2, DROP temp3, DROP temp4'.format(ratingstablename)
    cur.execute(drop_column)
    cur.close()
    openconnection.commit()


def rangePartition(ratingstablename, numberofpartitions, openconnection):
    cur = openconnection.cursor()
    partition = 5 / numberofpartitions
    add = partition
    prev = 0
    part = 0
    cur.execute("DROP TABLE IF EXISTS meta_range")
    cur.execute("CREATE TABLE meta_range (num_part INTEGER);")
    cur.execute("INSERT INTO META_RANGE  (num_part) values (%d) ;" % numberofpartitions)
    while partition <= 5:
        if part == 0:
            cur.execute("DROP TABLE IF EXISTS range_part" + str(part))
            cur.execute("CREATE TABLE range_part" + str(
                part) + " AS (SELECT * FROM " + ratingstablename + " WHERE RATING >= " + str(
                prev) + " AND RATING<= " + str(partition) + " );")
            prev = partition
            partition += add
            part += 1
        elif partition <= 5 and part != 0:
            cur.execute("DROP TABLE IF EXISTS range_part" + str(part))
            cur.execute("CREATE TABLE range_part" + str(
                part) + " AS (SELECT * FROM " + ratingstablename + " WHERE RATING > " + str(
                prev) + " AND RATING <= " + str(partition) + " );")
            prev = partition
            partition += add
            part += 1
    cur.close()
    openconnection.commit()


def roundRobinPartition(ratingstablename, numberofpartitions, openconnection):
    cur = openconnection.cursor()
    cur.execute("select * from " + ratingstablename + ";")
    rows = cur.fetchall()
    count = 0

    for i in range(0, numberofpartitions):
        cur.execute("DROP TABLE IF EXISTS rrobin_part" + str(i))
        cur.execute("CREATE TABLE rrobin_part" + str(i) + " AS (SELECT * FROM " + ratingstablename + " LIMIT 0);")

    cur.execute("DROP TABLE IF EXISTS meta_rrobin")
    cur.execute("CREATE TABLE meta_rrobin (num_part INTEGER , curr_table INTEGER);")
    cur.execute("INSERT INTO META_RROBIN  (num_part , curr_table) values (%s , %s) ;" % (numberofpartitions, i))

    for row in rows:
        table_name = RROBIN_TABLE_PREFIX + str(count)
        if row[0] is None and row[1] is None:
            row_0 = 'NULL'
            row_1 = 'NULL'
            cur.execute( "INSERT INTO {0} (UserID, MovieID, Rating) VALUES ({1}, {2}, {3})".format(table_name, row_0, row_1, row[2]))
        elif row[0] is None and row[1] is not None:
            row_0='NULL'
            cur.execute(" INSERT INTO {0} (UserID, MovieID, Rating) VALUES ({1}, {2}, {3})".format(table_name, row_0, row[1], row[2]))
        elif row[1] is None and row[0] is not None:
            row_1='NULL'
            cur.execute(" INSERT INTO {0} (UserID, MovieID, Rating) VALUES ({1}, {2}, {3})".format(table_name, row[0], row_1, row[2]))
        else:
            cur.execute(
                " INSERT INTO {0} (UserID, MovieID, Rating) VALUES ({1}, {2}, {3})".format(table_name, row[0], row[1],row[2]))
        count = (count + 1) % numberofpartitions
    cur.close()
    openconnection.commit()

def roundRobinInsert(ratingstablename, userid, itemid, rating, openconnection):
    cur = openconnection.cursor()
    cur.execute("select * from meta_rrobin;")
    row = cur.fetchall()
    count = row[0][0]
    curr_table = row[0][1]
    cur.execute("INSERT INTO %s (USERID, MOVIEID, RATING) VALUES (%s, %s, %s) ;" % (ratingstablename, userid, itemid, rating))
    suffix = (curr_table + 1) % count
    table_name = RROBIN_TABLE_PREFIX + str(suffix)
    cur.execute("INSERT INTO %s (USERID, MOVIEID, RATING) VALUES (%s, %s, %s) ;" % (table_name, userid, itemid, rating))
    cur.execute("UPDATE META_RROBIN SET CURR_TABLE = %s ;" % suffix)
    cur.close()
    openconnection.commit()


def rangeInsert(ratingstablename, userid, itemid, rating, openconnection):
    cur = openconnection.cursor()
    cur.execute("select * from meta_range;")
    count = cur.fetchone()[0]
    temp = 5 / count
    table_num_temp = rating / temp
    cur.execute("INSERT INTO %s (USERID, MOVIEID, RATING) VALUES (%d, %d, %f) ;" % (ratingstablename, userid, itemid, rating))
    if table_num_temp == 0:
        table_num = 0
    else:
        table_num = int(table_num_temp) - 1
    cur.execute("INSERT INTO range_part" + str(table_num) + " (USERID, MOVIEID, RATING) VALUES (%d, %d, %f) ;" % (
    userid, itemid, rating))
    cur.close()
    openconnection.commit()


def createDB(dbname='dds_assignment1'):
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
    con.close()


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
    except IOError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
    finally:
        if cursor:
            cursor.close()