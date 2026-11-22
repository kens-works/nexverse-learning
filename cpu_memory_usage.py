class AlertRule:
    def __init__(self, metric_name, threshold, severity):
        self.metric_name = metric_name
        self.threshold = threshold
        self.severity = severity

    def is_breached(self, current_value):
        self.current_value = current_value
        if self.current_value >= self.threshold:
          return True
        else:
          return False

    def evaluate(self, current_value):
        self.current_value = current_value
        if self.is_breached(current_value):
           return f"[{self.severity}] {self.metric_name} exceeded threshold {self.threshold} with {self.current_value}"
        else:
            return f"OK: {self.metric_name} within normal limits"

cpu_usage = AlertRule("cpu_usage", 85.0, "CRITICAL")
memory_usage = AlertRule("memory_usage", 70.0, "WARNING")

#Metric test values: CPU=91.2, Memory=65.0.
print(cpu_usage.evaluate(91.2))
print(memory_usage.evaluate(65.0))