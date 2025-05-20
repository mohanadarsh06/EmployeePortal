import os
import subprocess

# First, run the Flask app directly
print("Starting Flask application on port 5001...")
flask_process = subprocess.Popen(["python", "run.py"])

# Wait for the Flask app to complete (which it won't unless terminated)
flask_process.wait()