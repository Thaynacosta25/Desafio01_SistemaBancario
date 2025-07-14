import json
from datetime import datetime, timedelta
import os 

DATA_FILE = 'data.json' 
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"lancamentos": [], "mes_atual": datatime.today().strftime('%Y-%m')}, f, indent = 4)

def load_data():
    with open(DATA_FILE, 'r') as f:
        json.load(f)
