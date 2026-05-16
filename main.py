import subprocess
import time
import sys
import os

def start_services():
    print("🚀 Launching Intelligent Microgrid Digital Twin Framework...")
    print("---------------------------------------------------------")

    try:
        # 1. Start FastAPI Backend (API Layer)
        print("📡 Starting API Layer (FastAPI)...")
        api_process = subprocess.Popen(
            ["uvicorn", "api_layer.main_api:app", "--host", "0.0.0.0", "--port", "8000"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        # Wait for API to warm up
        time.sleep(2)

        # 2. Start Simulation Engine (Core/IoT Layer)
        print("⚙️  Starting Simulation Engine...")
        sim_process = subprocess.Popen(
            ["python", "scripts/run_simulation.py"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        # 3. Start Streamlit Dashboard (Visualization Layer)
        print("📊 Launching Visualization Dashboard...")
        # Streamlit-a run panna subprocess use panrom
        subprocess.run(["streamlit", "run", "visualization_layer/app_main.py"])

    except KeyboardInterrupt:
        print("\n🛑 Shutting down all services...")
        api_process.terminate()
        sim_process.terminate()
        print("✅ Cleanup complete. Goodbye!")

if __name__ == "__main__":
    # Project root-a path-la add panrom to avoid import errors
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    start_services()