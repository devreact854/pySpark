import os
from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

# Create an RDD and perform a simple operation
data = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
result = data.reduce(lambda x, y: x + y)

print("==============================================================Sum of elements:====================================================", result)

spark.stop()