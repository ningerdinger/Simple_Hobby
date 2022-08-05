from pyspark.sql import SparkSession
# initializing spark session
# more on how to initialize the spark session:
# https://spark.apache.org/docs/latest/sql-getting-started.html
spark = SparkSession \
            .builder \
            .appName("Spark Basics and Spark SQL") \
            .getOrCreate()


# df = spark.read.json("data.json")
# df.show()
data_dict = {'t1': '1', 't2': '2', 't3': '3'}
spark.createDataFrame(data_dict.items()).show()