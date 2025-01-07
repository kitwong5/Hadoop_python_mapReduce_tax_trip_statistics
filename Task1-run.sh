#!/bin/bash

# remove Input or Output folder
hadoop fs -rm -f -r /Input
hadoop fs -rm -f -r /Output/Task1
# create Input folder
hadoop fs -mkdir /Input
# copy source file to Input folder
hadoop fs -copyFromLocal ./Trips.txt /Input/Trips.txt


# use the first 2 fields as key
# use the first field to partitioner
# use the first 2 field for sorting
# use 3 reducer
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,1n \
-D mapred.text.key.comparator.options='-k1,1n -k2,2r' \
-D mapred.reduce.tasks=3 \
-file ./mapper_t1.py \
-mapper ./mapper_t1.py \
-file ./reducer_t1.py \
-reducer ./reducer_t1.py \
-input /Input/Trips.txt \
-output /Output/Task1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner





