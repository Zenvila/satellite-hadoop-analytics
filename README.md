# 🛰️ Satellite Hadoop Analytics

> Real satellite telemetry data analysis using Apache Hadoop MapReduce — fetched live from satellites orbiting Earth via the SatNOGS DB API.

---

## 🌍 What is this project?

This project fetches **real telemetry data from satellites currently orbiting Earth** and processes it using **Apache Hadoop MapReduce**. The data includes sensor readings like temperature, pressure, battery levels, ocean surface measurements, humidity, ozone levels, and more — all transmitted by actual satellites in space and received by ground stations worldwide.

The goal is to demonstrate how **big data tools like Hadoop** can be used to analyze large volumes of real-world sensor data efficiently.

---

## 📡 Where does the data come from?

The data is fetched from [SatNOGS DB](https://db.satnogs.org) — an open-source, community-driven satellite ground station network. Amateur and professional ground stations around the world receive satellite signals and upload the decoded telemetry to this public database.

The following satellites are used in this project:

| Satellite | Country | Type of Data |
|-----------|---------|--------------|
| CO-65 | Japan | Power levels, temperatures, battery |
| ISS | USA + Russia | Internal pressure, oxygen, battery, solar array |
| METEOR-M2-3 | Russia | Ice cover, sea surface temp, cloud distribution |
| METEOR-M2-4 | Russia | Ice cover, sea surface temp, cloud distribution |
| NOAA-15 | USA | Atmospheric temp, moisture, vegetation index |
| SARAL | France + India | Ocean topography, wave height, wind speed |
| METOP-B | EU | Humidity, temperature, ozone level |
| CSS-TIANHE | China | Internal pressure, oxygen, battery, solar array |

---

## ❓ Why Hadoop?

Satellite networks generate **massive amounts of telemetry data continuously** — potentially millions of readings per day across hundreds of satellites. Processing this on a single machine is slow and impractical at scale.

**Apache Hadoop** solves this by:
- **Splitting data into blocks** and distributing them across multiple nodes
- **Running mappers in parallel** to process data simultaneously
- **Aggregating results via reducers** efficiently across the cluster
- **Scaling horizontally** — just add more machines as data grows

This project explores how Hadoop performance changes with different **block sizes** and **number of mapper/reducer threads**, giving hands-on insight into how big data processing works in the real world.

---

## 🔬 What does this project analyze?

Using the MapReduce framework, this project answers questions like:

- How many total satellite sensor readings are in the dataset?
- How many unique sensors does the ISS have?
- What is the average Sea Surface Temperature across all readings?
- How are temperatures distributed across all satellites (histogram)?
- Is there a correlation between Ozone levels and Sea Surface Temperature?
- How does performance change with more mappers, reducers, or different block sizes?

---

## ⚙️ Tech Stack

- **Python 3** — Mapper and Reducer scripts
- **Apache Hadoop 3.3.6** — Distributed data processing
- **Hadoop Streaming** — Runs Python scripts as MapReduce jobs
- **HDFS** — Distributed file system for storing the dataset
- **SatNOGS DB API** — Source of real satellite telemetry data

---

## 🗂️ Project Structure

```
satellite-hadoop-analytics/
│
├── satellite_data_builder.py      # Fetches satellite data from SatNOGS API
├── satellite_measurements.csv     # Downloaded dataset
│
├── mapreduce/
│   ├── mapper.py / reducer.py         # Total measurement count
│   ├── mapper_t2q1.py / reducer_t2q1  # Unique ISS sensors
│   ├── mapper_t2q2.py / reducer_t2q2  # Unique METEOR sensors
│   ├── mapper_t2q3.py / reducer_t2q3  # Average Sea Surface Temp
│   ├── mapper_t2q4.py / reducer_t2q4  # Northern hemisphere filter
│   ├── mapper_t2q5.py / reducer_t2q5  # Southern hemisphere filter
│   ├── mapper_t2q6.py / reducer_t2q6  # Temperature histogram
│   └── mapper_t2q7.py / reducer_t2q7  # Ozone vs SST correlation
│
├── run_all_variations.sh          # Block size + thread variation tests
└── run_q9.sh                      # Mapper vs reducer variation tests
```

---

## 🚀 How to Run

### 1. Clone & setup
```bash
git clone https://github.com/Zenvila/satellite-hadoop-analytics.git
cd satellite-hadoop-analytics
python3 -m venv .venv && source .venv/bin/activate
pip install requests pandas skyfield Pillow
```

### 2. Add your SatNOGS API token
Get a free token at https://db.satnogs.org → Settings → API Token

```python
# In satellite_data_builder.py
API_TOKEN = "your_token_here"
```

### 3. Fetch data
```bash
python3 satellite_data_builder.py
```

### 4. Start Hadoop & upload data
```bash
start-dfs.sh && start-yarn.sh
hdfs dfs -mkdir -p /user/$USER/satellite/input
hdfs dfs -put satellite_measurements.csv /user/$USER/satellite/input/
```

### 5. Run a MapReduce job
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/$USER/satellite/input/satellite_measurements.csv \
  -output /user/$USER/satellite/output \
  -mapper "python3 mapreduce/mapper.py" \
  -reducer "python3 mapreduce/reducer.py"
```

---

## 👤 Author

**Zenvila** — [github.com/Zenvila](https://github.com/Zenvila)
