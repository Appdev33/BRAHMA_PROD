
# Online Python - IDE, Editor, Compiler, Interpreter
# import pandas as pd


import json

def flatten_json(obj, parent_key='', sep='_'):
    items = {}
    for k, v in obj.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, (dict, list)):
                    items.update(flatten_json(item, f"{new_key}_{i}", sep=sep))
                else:
                    items[f"{new_key}_{i}"] = item
        else:
            items[new_key] = v
    return items

	



input_data = {
    "database": {
        "connections": [
            {
                "name": "primary",
                "host": "db1.example_com",
                "port": 5432,
                "ssl": True,
                "credentials": {
                    "username": "admin",
                    "encrypted": True,
                    "roles": ["read", "write", "admin"]
                }
            },
            {
                "name": "secondary",
                "host": "db2.example_com",
                "port": 5433,
                "ssl": False,
                "credentials": {
                    "username": "readonly",
                    "encrypted": False,
                    "roles": ["read"]
                }
            }
        ],
        "settings": {
            "pool_size": 10,
            "timeout": 30.5,
            "retry": True,
            "options": {
                "autocommit": False,
                "isolation_level": "READ_COMMITTED",
                "features": ["transactions", "prepared_statements"]
            }
        }
    },
    "logging": {
        "level": "INFO",
        "handlers": ["console", "file"],
        "formatters": {
            "simple": "%(message)s",
            "detailed": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "version": "2.1.0",
    "production": False
}

flat_output = flatten_json(input_data)
for k, v in flat_output.items():
    print(f'"{k}": {json.dumps(v)},')



# df = pd.json_normalize(input)
# print(df)
