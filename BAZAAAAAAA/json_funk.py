from pathlib import Path
import json

def create_file(filename,data):
    if not Path(filename).exists():
        file=open(filename,"w")
        file.write(data)
        file.close()
def create_json_file(filename):
    data={
            "all":[]
        }
    create_file(filename,json.dumps(data))
    
def add_to_json(filename,json_data):
    with open(filename,"r") as  file:
        qator=file.readline()
        full_dict=json.loads(qator)
    full_dict["all"].append(json_data)

    with open(filename,"w") as  file:
        file.write(json.dumps(full_dict))

    