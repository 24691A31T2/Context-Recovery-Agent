from memory import find_project


def show_dashboard(project_name):

    project = find_project(project_name)

    if not project:
        print("\n❌ Project not found.")
        return

    completed = len(project["completed"])
    pending = len(project["pending"])
    total = completed + pending

    progress = 0

    if total != 0:
        progress = int((completed / total) * 100)

    print("\n" + "=" * 60)
    print("              PROJECT DASHBOARD")
    print("=" * 60)

    print(f"\nProject : {project['project']}")
    print(f"Description : {project['description']}")

    print("\nStatus : In Progress")

    print(f"\nProgress : {progress}%")

    print(f"\nCompleted Tasks ({completed})")

    if completed == 0:
        print("None")
    else:
        for task in project["completed"]:
            print(f"✓ {task}")

    print(f"\nPending Tasks ({pending})")

    if pending == 0:
        print("None")
    else:
        for task in project["pending"]:
            print(f"□ {task}")

    print("\n" + "=" * 60)