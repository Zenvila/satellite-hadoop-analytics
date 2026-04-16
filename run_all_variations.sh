#!/bin/bash

MAPPER="python3 /home/zenvila/satellite_project/mapreduce/mapper.py"
REDUCER="python3 /home/zenvila/satellite_project/mapreduce/reducer.py"
INPUT="/user/zenvila/satellite/input/satellite_measurements.csv"
JAR="/opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar"
RESULTS=~/satellite_project/results.txt

echo "Running all variations..." > $RESULTS

BLOCKS=(1048576 2097152 4194304 8388608 134217728)
BLOCK_NAMES=("1MB" "2MB" "4MB" "8MB" "Default")
TASKS=(2 4 8 16)

for i in "${!BLOCKS[@]}"; do
  for m in "${TASKS[@]}"; do
    OUTDIR="/user/zenvila/satellite/out_${m}m_${BLOCK_NAMES[$i]}"
    hdfs dfs -rm -r -f $OUTDIR > /dev/null 2>&1
    START=$(date +%s%3N)
    hadoop jar $JAR \
      -D dfs.blocksize=${BLOCKS[$i]} \
      -D mapreduce.job.maps=$m \
      -D mapreduce.job.reduces=$m \
      -input $INPUT -output $OUTDIR \
      -mapper "$MAPPER" -reducer "$REDUCER" > /dev/null 2>&1
    END=$(date +%s%3N)
    ELAPSED=$((END - START))
    echo "Mappers=$m Block=${BLOCK_NAMES[$i]} Time=${ELAPSED}ms" >> $RESULTS
    echo "Done: Mappers=$m Block=${BLOCK_NAMES[$i]} -> ${ELAPSED}ms"
  done
done

echo "All done! Results saved to $RESULTS"
