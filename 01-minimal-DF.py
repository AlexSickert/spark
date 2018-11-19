# -*- coding: utf-8 -*-
"""



"""



from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test01').getOrCreate()

df = spark.read.csv("/home/alex/SPARK/test-data-01.csv", header = True)

df.show()