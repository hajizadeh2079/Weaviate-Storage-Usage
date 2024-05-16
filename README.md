# Weaviate Storage Usage Calculator

The aim of this project is to address the challenge of calculating storage usage in Weaviate. Since Weaviate lacks built-in metrics for storage usage, we've developed a manual solution.

In this project, we utilize custom metrics in Node Exporter to periodically monitor Weaviate's underlying storage. These metrics are then scraped using Prometheus for visualization and analysis.

## Project Overview

### Files

- **`testsamples.py`, `insert.py`, `requirements.txt`**: These files simulate the insertion of one million objects across two different classes. `Person` includes properties like name, age, and address, while `Organization` includes only a name property.
- **`docker-compose.yml`, `prometheus.yml`**: Docker Compose is used to manage Weaviate, Node Exporter, and Prometheus for easy setup of the testing environment.
- **`storage.bash`**: This script creates a custom metric for Weaviate's storage usage.

### Simulation Process

1. **Setting Up the Environment**: Start Weaviate, Node Exporter, and Prometheus using the command:
   ```bash
   docker-compose up
   ```
   Ensure you create `weaviate-data` and `node-exporter-data` directories alongside the repository files for storage volumes.

2. **Retrieving Storage Metrics**: Run the `storage.bash` script to obtain custom metrics for Weaviate's storage usage:
   ```bash
   bash storage.bash
   ```
   Note: Run with root privileges (`sudo`). You can also integrate this script into `crontab` for automated monitoring.

3. **Inserting Data**: Execute `insert.py` to insert one million objects into the `Person` and `Organization` classes:
   ```bash
   python insert.py
   ```
   Ensure you've installed the dependencies specified in `requirements.txt`.

## Results

The resulting storage usage of each class and the total storage usage of Weaviate are visualized in the provided `result.png`. Please note that fluctuations are inherent due to Weaviate's mechanisms like creating and deleting temporary files during data operations.

---

By implementing this solution, we gain insights into Weaviate's storage usage, enabling better resource management and optimization.
