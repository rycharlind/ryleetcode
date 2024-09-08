from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("CSV Read Filter Example") \
    .getOrCreate()

# Read the CSV file into a DataFrame
df = spark.read.csv("./data/sample_data.csv", header=True, inferSchema=True)

# Filter the DataFrame where a specific column value meets a condition
filtered_df = df.filter(df["age"] > 40)

df.explain(extended=False)

# Show the result
filtered_df.show()

# Stop the Spark session
spark.stop()