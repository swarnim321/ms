
import psycopg2
import os
import sys
# Donot close the connection inside this file i.e. do not perform openconnection.close()
def RangeQuery(ratingMinValue, ratingMaxValue, openconnection, outputPath):
    cur = openconnection.cursor()
    prefix_Range = "RangeRatingsPart"
    cur.execute("Select * from RangeRatingsMetaData")
    count = 1
    range_data=cur.fetchall()
    for row in range_data:
        min_rating = row[1]
        max_rating = row[2]
        if not ((ratingMinValue > max_rating) or (ratingMaxValue < min_rating)):
            table_name=prefix_Range + str(row[0])
            cur.execute("select * from " + table_name + " where rating >= " + str(ratingMinValue) + " and rating <= " + str(ratingMaxValue) + ";" )
            results=cur.fetchall()
            if count==1:
                with open(outputPath, "w+") as file:
                    for result in results:
                        file.write(str(table_name) +"," + str(result[0]) +"," +str(result[1]) + "," + str(result[2]) +"\n")
                count += count
            elif count >1:
                with open(outputPath, "a+") as file:
                    print(result[0], result[1], result[2])
                    for result in results:
                        file.write(str(table_name) + "," + str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "\n")


    prefinx_rrobin = "RoundRobinRatingsPart"
    cur.execute ("select partitionnum from RoundRobinRatingsMetaData")
    numPartition = cur.fetchall()[0][0]
    for i in range(0, numPartition):
        table_name_robin = prefinx_rrobin + str(i)
        cur.execute("select * from " + table_name_robin + " where rating >=" + str(ratingMinValue) + " and rating <= " + str(ratingMaxValue) + ";" )
        results=cur.fetchall()
        with open(outputPath, "a+") as file:
            for result in results:
                file.write(str(table_name_robin) + "," + str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "\n")



def PointQuery(ratingValue, openconnection, outputPath):
    cur = openconnection.cursor()
    cur.execute("select * from RangeRatingsMetaData")
    range_data=cur.fetchall()
    prefix_Range = "RangeRatingsPart"
    for row in range_data:
        min_rating = row[1]
        max_rating = row[2]
        table_name = prefix_Range + str(row[0])
        if ((row[0] == 0 and min_rating <= ratingValue and max_rating >= ratingValue) or (row[0] != 0 and min_rating < ratingValue and max_rating >= ratingValue)):
            cur.execute("select * from " + table_name + " where rating = " + str(ratingValue) + ";")
            results= cur.fetchall()
            with open(outputPath , "w") as file:
                for result in results:
                    file.write(str(table_name) + "," + str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "\n")

    prefix_rrobin = "RoundRobinRatingsPart"
    cur.execute("select * from RoundRobinRatingsMetaData")
    numPartition = cur.fetchall()[0][0]
    for i in range(0,numPartition):
        table_name = prefix_rrobin + str(i)
        cur.execute("select * from " + table_name + " where rating = " + str(ratingValue) + ";")
        results = cur.fetchall()
        with open(outputPath , "a") as file:
            for result in results:
                file.write(str(table_name) + "," + str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "\n")