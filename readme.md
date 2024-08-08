******This is about PySpark project ******

**Here are some common areas where you might using PySpark.**
1. Data Processing: Loading, transforming, and saving data using PySpark.
2. DataFrames: Operations and manipulations on DataFrames.
3. RDDs: Working with Resilient Distributed Datasets.
4. Machine Learning: Using PySpark MLlib for machine learning tasks.
5. Performance Tuning: Optimizing PySpark jobs for better performance.
6. Cluster Management: Configuring and managing Spark clusters.

PySpark is the Python API for Apache Spark, which is a distributed computing framework used for big data processing. PySpark allows you to write Spark applications using Python, and it integrates well with Python libraries and tools.

**Install python3.9**

**Key Concepts in PySpark**
1. Apache Spark: A fast and general-purpose cluster computing system for big data processing. It provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

2. PySpark: The Python API for Spark, allowing you to harness the power of Spark using Python.

3. Resilient Distributed Datasets (RDDs): The fundamental data structure of Spark, which is an immutable distributed collection of objects that can be processed in parallel.

4. DataFrames: Similar to pandas DataFrames, but distributed across a cluster. They provide a higher-level API for handling structured data.

5. Spark SQL: A module for working with structured data using SQL queries.

6. Spark MLlib: A library for scalable machine learning (ML) in Spark.

**Install Apache Spark:**
Download Spark from the official website.
Extract the downloaded file to a directory on your computer(spark-3.4.3-bin-hadoop3).

**Install PySpark:**
You can install PySpark using pip: `pip install pyspark==3.4.3`
Set Environment Variables (optional but recommended): Add Spark and Hadoop binaries to your system's PATH variable.

**Install Java**: Download and install jdk-11.0.22_windows-x64_bin.exe

**Set Environment Variables:** 
Right-click on 'This PC' or 'Computer' on the desktop or in File Explorer.
Click on 'Properties'.
Click on 'Advanced system settings'.
Click on the 'Environment Variables' button.
Under 'System variables', click 'New' and add JAVA_HOME as the variable name and the path to your JDK installation as the variable value (e.g., C:\Program Files\Java\jdk-11.0.1).
Find the Path variable in the 'System variables' section, select it, and click 'Edit'. Add %JAVA_HOME%\bin to the end of the variable value.
**Verify Java Installation**
To verify that Java is correctly installed and the environment variables are set, open a terminal or command prompt and run:
`java -version`

**Download winutils.exe and set Environment Variable**
Download the winutils.exe binary corresponding to your Hadoop version(3.2.1).
env $HADOOP_HOME with the value of the directory containing winutils.exe and find the Path variable in the "System variables" section, select it, and click "Edit". Add %HADOOP_HOME%\bin to the list.

`echo %HADOOP_HOME%`

Here are set env var:
setx JAVA_HOME C:\Program Files\Java\jdk-11
setx PATH "%PATH%;%JAVA_HOME%\bin"

setx SPARK_HOME D:\temp\python\pySpark\source\spark-3.4.3-bin-hadoop3
setx PATH "%PATH%;%SPARK_HOME%\bin"

setx HADOOP_HOME D:\temp\python\pySpark\source\winutils-master\winutils-master\hadoop-3.2.1
setx PATH "%PATH%;%HADOOP_HOME%\bin"

setx PYSPARK_DRIVER_PYTHON D:\temp\python\pySpark\myenv3.9\Scripts\python.exe
setx PYSPARK_PYTHON D:\temp\python\pySpark\myenv3.9\Scripts\python.exe





