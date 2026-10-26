tasks = []

def add_task(task_name):
     print(f"Đã thêm công việc: {task_name}")
add_task("Học bài Git và GitHub")
def list_tasks():
    print("\nDANH SÁCH CÔNG VIỆC:")

    if not tasks:
        print("Chưa có công việc nào.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    list_tasks()
