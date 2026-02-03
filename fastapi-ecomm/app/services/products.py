import json
from pathlib import Path
from typing import Dict,List

data_file = Path(__file__).parent.parent / "data" / "products.json"

def load_prod() -> List[Dict]:
    if not data_file.exists():
        return[]
    with open(data_file,'r') as file :
        return json.load(file)

def get_all_prod() -> List[Dict]:
    return load_prod()
    