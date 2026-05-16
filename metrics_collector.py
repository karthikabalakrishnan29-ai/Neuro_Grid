from prometheus_client import start_http_server, Gauge, Counter
import time
import random

# Define Metrics
POWER_GENERATION = Gauge('microgrid_power_gen_kw', 'Current Total Power Generation')
BATTERY_LEVEL = Gauge('microgrid_battery_soc', 'Battery State of Charge Percentage')
ANOMALY_COUNT = Counter('microgrid_anomalies_total', 'Total number of detected anomalies')

class MetricsCollector:
    def __init__(self, port=9090):
        self.port = port

    def start_server(self):
        # Prometheus intha port-la thaan data-va 'scrape' pannum
        start_http_server(self.port)
        print(f"Metrics server started on port {self.port}")

    def update_metrics(self, solar, wind, battery_soc, is_anomaly):
        POWER_GENERATION.set(solar + wind)
        BATTERY_LEVEL.set(battery_soc)
        if is_anomaly:
            ANOMALY_COUNT.inc()

# Usage Example:
# collector = MetricsCollector()
# collector.start_server()
try:
    from prometheus_client import start_http_server, Gauge, Counter
    import time
    from utils.logger import logger
except ImportError:
    print("Error: prometheus_client not found. Run 'pip install prometheus-client'")

class MetricsCollector:
    def __init__(self, port=9090):
        self.port = port
        # Dashboard-ku thevaiyaana specific metrics
        self.power_gauge = Gauge('microgrid_output_kw', 'Live Power Output')
        self.anomaly_counter = Counter('microgrid_faults_total', 'Total Faults Detected')

    def start_monitoring(self):
        try:
            start_http_server(self.port)
            logger.info(f"Prometheus metrics server live at port {self.port}")
        except Exception as e:
            logger.error(f"Failed to start metrics server: {e}")

    def log_data(self, power_val, is_fault):
        self.power_gauge.set(power_val)
        if is_fault:
            self.anomaly_counter.inc()