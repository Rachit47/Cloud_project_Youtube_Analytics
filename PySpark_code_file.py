import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from awsglue.dynamicframe import DynamicFrame

# @params: [JOB_NAME]
arguments = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
gc = GlueContext(sc)
spark = gc.spark_session
glue_job = Job(gc)
glue_job.init(arguments['JOB_NAME'], arguments)

# @type: DataSource
# @args: [database = "youtube-data-analysis-useast-1-dev-env", table_name = "raw_statistics", transformation_ctx = "datasource0"]
# @return: datasource0
# @inputs: []
############################### Updated by Rachit ###############################
region_predicate = "region in ('ca','gb','us')"

datasource0 = gc.create_dynamic_frame.from_catalog(database = "youtube-data-analysis-useast-1-dev-env", table_name = "raw_statistics", transformation_ctx = "datasource0", push_down_predicate = region_predicate)

# @type: ApplyMapping
# @args: [mapping = [("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "long", "category_id", "long"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "long", "views", "long"), ("likes", "long", "likes", "long"), ("dislikes", "long", "dislikes", "long"), ("comment_count", "long", "comment_count", "long"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "boolean", "comments_disabled", "boolean"), ("ratings_disabled", "boolean", "ratings_disabled", "boolean"), ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"), ("description", "string", "description", "string"), ("region", "string", "region", "string")], transformation_ctx = "applymapping1"]
# @return: applymapping1
# @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "long", "category_id", "long"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "long", "views", "long"), ("likes", "long", "likes", "long"), ("dislikes", "long", "dislikes", "long"), ("comment_count", "long", "comment_count", "long"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "boolean", "comments_disabled", "boolean"), ("ratings_disabled", "boolean", "ratings_disabled", "boolean"), ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"), ("description", "string", "description", "string"), ("region", "string", "region", "string")], transformation_ctx = "applymapping1")

# @type: ResolveChoice
# @args: [choice = "make_struct", transformation_ctx = "resolvechoice2"]
# @return: resolvechoice2
# @inputs: [frame = applymapping1]
resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_struct", transformation_ctx = "resolvechoice2")

# @type: DropNullFields
# @args: [transformation_ctx = "dropnullfields3"]
# @return: dropnullfields3
# @inputs: [frame = resolvechoice2]
dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")

# @type: DataSink
# @args: [connection_type = "s3", connection_options = {"path": "s3://bigdata-on-youtube-cleansed-euwest1-14317621-dev/youtube/raw_statistics/"}, format = "parquet", transformation_ctx = "datasink4"]
# @return: datasink4
# @inputs: [frame = dropnullfields3]
############################### Updated by Rachit ###############################

datasink1 = dropnullfields3.toDF().coalesce(1)
df_final_output = DynamicFrame.fromDF(datasink1, gc, "df_final_output")
datasink4 = gc.write_dynamic_frame.from_options(frame = df_final_output, connection_type = "s3", connection_options = {"path": "s3://de-on-youtube-cleansed-useast1-dev/youtube/raw_statistics/", "partitionKeys": ["region"]}, format = "parquet", transformation_ctx = "datasink4")

############################### Updated by Rachit ###############################
glue_job.commit()
