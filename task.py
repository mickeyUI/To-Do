class Tasks:
    def __init__(self, task_name, complete = False):
        self.task_name = task_name
        self.complete = complete

    def to_dic(self):
        return [{
            "task_name": self.task_name,
            "complete": self.complete
        }]
    @staticmethod
    def to_list(data):
        count = 1
        for task in data:
            print(f"{count}. {task["task_name"]} |{com(task)}|")
            count += 1
            
def com(task): 
                if task['complete'] == True:
                    return "completed"
                else:
                    return "not completed"