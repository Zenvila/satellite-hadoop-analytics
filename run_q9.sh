#!/bin/bash
MAPPER="python3 /home/zenvila/satellite_project/mapreduce/mapper.py"
REDUCER="python3 /home/zenvila/satellite_project/mapreduce/reducer.py"
INPUT="/user/zenvila/satellite/input/satellite_measurements.csv"
JAR="/opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar"

for m in 2 4 8 16; do
  for r in 2 4 8 16; do
    OUTDIR="/user/zenvila/satellite/out_q9_${m}m_${r}r"
    hdfs dfs -rm -r -f $OUTDIR > /dev/null 2>&1
    START=$(date +%s%3N)
    hadoop jar $JAR \
      -D mapreduce.job.maps=$m \
      -D mapreduce.job.reduces=$r \
      -input $INPUT -output $OUTDIR \
      -mapper "$MAPPER" -reducer "$REDUCER" > /dev/null 2>&1
    END=$(date +%s%3N)
    echo "Map=$m Reduce=$r Time=$((END-START))ms"
  done
done
