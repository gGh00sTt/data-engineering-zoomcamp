from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
import pyarrow as pa
import pyarrow.parquet as pq
from os import path
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="/home/src/de-zoomcamp.json"

bucket_name = "mage-zoomcamp-csangam"
project_id = "de-zoomcamp-413116"

table_name = "green_taxi"

root_path = f"{bucket_name}/{table_name}"



@data_exporter
def export_data(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """

    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(table,root_path=root_path,partition_cols=['lpep_pickup_date'],filesystem=gcs)
