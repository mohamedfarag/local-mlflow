import os
import warnings
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkFiles
from pyspark.sql import SQLContext

warnings.filterwarnings('ignore')
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages  org.apache.spark:spark-avro_2.12:3.4.1,io.delta:delta-core_2.12:2.4.0 pyspark-shell'
# RUN spark-shell --packages org.apache.spark:spark-avro_2.12:3.4.1
# RUN spark-shell --packages io.delta:delta-core_2.12:2.4.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"

spark = SparkSession.builder.appName("Spark_ML") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")\
        .getOrCreate()

df = spark.read.format('csv')\
    .option("header", "true")\
    .option("sep", ";")\
    .option("inferSchema", "true")\
    .option("mergeSchema", "true")\
    .load('saber11.csv')

df = df.dropna()

for column in df.columns:
    col_ = column.replace(' ','').replace('  ','')
    df = df.withColumnRenamed(column, col_)

spark.sql("CREATE DATABASE IF NOT EXISTS default")
spark.sql("DROP TABLE IF EXISTS default.saber11")
df.write.format("delta").mode("overwrite").option("path", "delta/saber11").save()
spark.sql("CREATE TABLE default.saber11 USING DELTA LOCATION 'delta/saber11'")