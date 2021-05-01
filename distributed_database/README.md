#######Assignment 1#############

The required task is to simulate data partitioning approaches on-top of an open source relational database management system (i.e., PostgreSQL). Each student must generate a set of Python functions that load the input data into a relational table, partition the table using different horizontal fragmentation approaches, and insert new tuples into the right fragment. A detailed explanation about round-robin partitioning and range partitioning can be found here: https://www.ibm.com/support/knowledgecenter/en/SSZJPZ_11.7.0/com.ibm.swg.im.iis.ds.parjob.dev.doc/topics/partitioning.html (Links to an external site.)

Input Data. The input data is a Movie Rating data set collected from the MovieLens web site (http://movielens.org). The raw data is available in the file ratings.dat.

The rating.dat file contains 10 million ratings and 100,000 tag applications applied to 10,000 movies by 72,000 users. Each line of this file represents one rating of one movie by one user, and has the following format:

UserID::MovieID::Rating::Timestamp


######Assignment 2##########
RangeQuery() –
o Implement a Python function RangeQuery that takes as input: (1)
RatingMinValue (2) RatingMaxValue (3) openconnection (4) outputPath
o Please note that the RangeQuery would not use ratings table but it would use the
range and round robin partitions of the ratings table.
o RangeQuery() then returns all tuples for which the rating value is larger than or
equal to RatingMinValue and less than or equal to RatingMaxValue.
o The returned tuples should be stored in outputPath. Each line represents a tuple
that has the following format such that PartitionName represents the full name
of the partition i.e. RangeRatingsPart1 or RoundRobinRatingsPart4 etc. in
which this tuple resides.
Example:
PartitionName, UserID, MovieID, Rating
RangeRatingsPart0,1,377,0.5
RoundRobinRatingsPart1,1,377,0.5
o Note: Please use ‘,’ (COMMA, no space character) as delimiter between
PartitionName, UserID, MovieID and Rating.
PointQuery() –
o Implement a Python function PointQuery that takes as input: (1) RatingValue.
(2) openconnection (3) outputPath
o Please note that the PointQuery would not use ratings table but it would use the
range and round robin partitions of the ratings table.
o PointQuery() then returns all tuples for which the rating value is equal to
RatingValue.
o The returned tuples should be stored in outputPath. Each line represents a tuple
that has the following format such that PartitionName represents the full name
of the partition i.e. RangeRatingsPart1 or RoundRobinRatingsPart4 etc. in
which this tuple resides.
Example
PartitionName, UserID, MovieID, Rating
RangeRatingsPart3,23,459,3.5
RoundRobinRatingsPart4,31,221,0
o Note: Please use ‘,’ (COMMA, no space character) as delimiter between
PartitionName, UserID, MovieID and Rating.

#######Assginment 3#########
The required task is to build a generic parallel sort and parallel join algorithm.
1. Implement a Python function ParallelSort() that takes as input: (1) InputTable stored in a PostgreSQL database, (2) SortingColumnName the name of the column used to order
the tuples by. ParallelSort() then sorts all tuples (using five parallelized threads) and stores the sorted tuples for in a table named OutputTable (the output table name is passed to the function). The OutputTable contains all the tuple present in InputTable sorted in ascending order.


#######Assignment 4#########
The required task is to write a map-reduce program that will perform equijoin.•ThecodeshouldbeinJava (useJava1.8.x)usingHadoopFramework(useHadoop2.7.x).•The code would take two inputs, one would be the HDFS location of the file on which  the equijoin should be performed and other would be the HDFS location of the file, where the output should bestored.Format of the Input File: -Table1Name, Table1JoinColumn, Table1Other Column1, Table1OtherColumn2, ........ Table2Name, Table2JoinColumn, Table2Other Column1, Table2OtherColumn2, .........Format of the Output File: -If Table1JoinColumn value is equal to Table2JoinColumn value, simply append both line side by    side    for    Output.    If    Table1JoinColumn    value does    not    match    any    value    of Table2JoinColumn, simply remove them for the output file. You should not include two joins contains same row (No duplicate joins in output file).

#######Assignment 5#########
The required task is two write two functions, which will perform some textual and spatial searching on MongoDB. Details are explained below.
mplement the function provided in Assignment5_Interface.py to perform the operations as listed below:a.FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection)This function searches the ‘collection’ given to find all the business present in  the  city  provided  in  ‘cityToSearch’  and  save  it  to  ‘saveLocation1’.  For each  business  you  found,  you  should  store  name  Full  address,  city,  state  of business in the following format.Each line of the saved file will contain, Name$FullAddress$City$State. ($ is the separator and must be present)b.FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection)This function searches the ‘collection’ given to find name of all the business present in the ‘maxDistance’ from the given ‘myLocation’that covers allthe given categories(please use the distance algorithm given below) and save them to ‘saveLocation2’.Each line of the output file will contain the name of the business only.--categoriesToSearch: a list of categories need to be covered--‘myLocation’ will be given with format [“40.3”, “51.6”].--maxDistance: the search distance--saveLocation2: output location
