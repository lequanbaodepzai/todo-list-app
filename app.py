

tasks = []

def add_task(task_name):
    tasks.append({
        "name": task_name,
        "completed": False
    })
    print(f"Đã thêm công việc: '{task_name}'")

# Hàm xóa công việc
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)

        print(f"Đã xóa công việc: '{deleted_task['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")
def list_tasks():
    print("\nDANH SÁCH CÔNG VIỆC:")

    if not tasks:
        print("Chưa có công việc nào.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['name']}")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Đã hoàn thành: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    list_tasks()

    complete_task(0)

    list_tasks()
