from memory import (
    find_project,
    update_completed_task
)


def update_project():

    project_name = input("\nEnter Project Name : ").strip()

    project = find_project(project_name)

    if not project:
        print("\n❌ Project not found.")
        return

    if len(project["pending"]) == 0:
        print("\n🎉 Project already completed!")
        return

    print("\nPending Tasks\n")

    for index, task in enumerate(project["pending"], start=1):
        print(f"{index}. {task}")

    try:
        choice = int(input("\nSelect completed task number : "))

        if choice < 1 or choice > len(project["pending"]):
            print("\n❌ Invalid choice.")
            return

        task = project["pending"][choice - 1]

        update_completed_task(project_name, task)

        print(f"\n✅ '{task}' marked as completed.")

    except ValueError:
        print("\n❌ Please enter a valid number.")