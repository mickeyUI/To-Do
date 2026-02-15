from task import Tasks
import json

with open("tasks.json", "r") as f:
    data = json.load(f)
def load_task():
    return data


def save_task(A):
    new_data = {"task_name": A, "complete": False}
    data.append(new_data)
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=2)
def complete(task):
    for i in data:
        if i["task_name"].lower() == task.lower():
            i['complete'] = True
def delete_task(task):
    for i in data:
        if i["task_name"].lower() == task.lower():
            data.remove(i)
    
