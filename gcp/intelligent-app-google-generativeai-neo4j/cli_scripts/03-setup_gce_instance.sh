# Let's install python & pip first
apt install -y python
apt install -y pip
apt-get install -y python3-venv
python3 -m venv /app/venv/genai
source /app/venv/genai/bin/activate

# Now, let's create a Virtual Environment to isolate our Python environment and activate it
apt-get install -y python3-venv
python3 -m venv /app/venv/genai
source /app/venv/genai/bin/activate

#To install Streamlit and other dependencies:
cd ui
pip install -r requirements.txt


