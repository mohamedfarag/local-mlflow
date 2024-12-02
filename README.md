# Mlflow on local machine

Here We will see how to implement PySpark for Machine Learning and MLflow for model tracking, registry and expose in production as you can see below:

<div align="center">
  <img src="imgs/mlflowjpg.jpg" alt="image" width="500"/>
</div>

Make sure to have Spark and Java installed and configured properly.

To run this locally on your machine, please run this steps. After you clone this repository, conduct the following actions on the cloned repository.


```sh
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
pyspark --packages io.delta:delta-core_2.12:0.7.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

Then, in a separate terminal, to run the MLflow UI, execute:

```sh
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

And you can visualize the experiments, see them artifacts, parameters, metrics, tags and so on. Check the versioning of models, the yaml files, stages and other objects in the mlruns dir, because that's how MLflow makes easier deployment and production.

<div align="center">
  <img src="imgs/mlflowui.png" alt="image" width="1000"/>
</div>
