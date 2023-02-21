from rich import inspect
import subprocess

results = subprocess.run(['cgps', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print(inspect(results))
