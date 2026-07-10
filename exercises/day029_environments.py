# Day 29: Environment Configuration Notes
import platform

print("System Platform:", platform.system(), platform.release())
print("Python Version:", platform.python_version())

requirements = [
    "pytest>=7.0.0",
    "requests>=2.28.0",
    "black>=22.0.0",
    "flake8>=5.0.0"
]

print("Recommended dev dependencies:")
for req in requirements:
    print(f"  - {req}")
