# Day 100 Milestone Project: CSV Data Summary Engine
import statistics

dataset = [
    {"user": "u1", "response_time_ms": 120, "status": 200},
    {"user": "u2", "response_time_ms": 340, "status": 200},
    {"user": "u3", "response_time_ms": 1150, "status": 500},
    {"user": "u4", "response_time_ms": 180, "status": 200},
    {"user": "u5", "response_time_ms": 210, "status": 200},
]

times = [row["response_time_ms"] for row in dataset]
errors = sum(1 for row in dataset if row["status"] >= 400)

report = {
    "requests": len(dataset),
    "error_rate": f"{(errors / len(dataset)) * 100:.1f}%",
    "avg_latency_ms": round(statistics.mean(times), 2),
    "p90_estimate": statistics.quantiles(times, n=10)[8] if len(times) >= 10 else max(times)
}
print("Server Performance Metrics:", report)
