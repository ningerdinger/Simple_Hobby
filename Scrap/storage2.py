import cbsodata
import dropbox
from pyspark.sql import SparkSession
from pyspark.sql import Row
import json

dbx = dropbox.Dropbox('sl.BMwUDC47VdoK_GQCUpq6mwVlD18s5W6Enz-ImofkH5UyVAN6JGR6F2l7D-leoMLXw_JAdv0AGw-zbhail8QuoknAdQDoQW1ZkKwIn88527jtZDJlXr5iDyIXzWl0LCSaud3mul-riYGG')
# list_of_identifier = ['84669NED', '83583NED']
# list_of_identifier = [value['Identifier'] for value in tables]
# print(list_of_identifier)
# print(cbsodata.get_data('84669NED'))
# print(len(cbsodata.get_data('84669NED')))

# spark = SparkSession \
#             .builder \
#             .appName("Spark Basics and Spark SQL") \
#             .getOrCreate()

# spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
data_dict = cbsodata.get_data('84669NED')
# print(len(data_dict))
# df = spark.createDataFrame(Row(**x) for x in data_dict).show(truncate=False)
# df.show()
# df = spark.createDataFrame(data_dict.items()).show()
# df.show()
#80072NED
#dbx.files_upload("Potential headline: Game 5 a nail-biter as Warriors inch out Cavs", '/cavs vs warriors/game 5/story.txt')
with open('84669NED.json', 'w') as f:
    json.dump(data_dict, f, indent=1)