print("NEW MAIN.PY LOADED")
from agent import generate_project_plan, generate_summary

from memory import (
    save_project,
    find_project,
)

while True:

    print("\n" + "=" * 60)
    print("        CONTEXT RECOVERY AGENT")
    print("=" * 60)

    print("1. Create New Project")
    print("2. Search Project")
    print("3. Resume Project")
    print("4. Exit")

    choice = input("\nEnter your choice: ").strip()

    # ==========================================
    # CREATE PROJECT
    # ==========================================

    if choice == "1":

        project = input("\nProject Name : ").strip()
        description = input("Description  : ").strip()

        print("\nGenerating AI Project Plan...\n")

        plan = generate_project_plan(project, description)

        print(plan)

        project_data = {
            "project": project,
            "description": description,
            "completed": [],
            "pending": [
                task.strip()
                for task in plan.split("\n")
                if task.strip()
            ]
        }

        save_project(project_data)

        print("\n✅ Project created successfully!")

    # ==========================================
    # SEARCH PROJECT
    # ==========================================

    elif choice == "2":

        project = input("\nEnter Project Name : ").strip()

        result = find_project(project)

        if result:

            print("\nProject Found")
            print("-" * 50)

            print("Project :", result["project"])
            print("Description :", result["description"])

            print("\nCompleted Tasks")

            if result["completed"]:
                for task in result["completed"]:
                    print("✓", task)
            else:
                print("No completed tasks.")

            print("\nPending Tasks")

            if result["pending"]:
                for task in result["pending"]:
                    print("□", task)
            else:
                print("No pending tasks.")

        else:

            print("\n❌ Project not found.")

    # ==========================================
    # RESUME PROJECT
    # ==========================================

    elif choice == "3":

        project = input("\nEnter Project Name : ").strip()

        result = find_project(project)

        if result:

            print("\nGenerating AI Summary...\n")

            summary = generate_summary(
                result["project"],
                result["completed"],
                result["pending"]
            )

            print(summary)

        else:

            print("\n❌ Project not found.")

    # ==========================================
    # EXIT
    # ==========================================

    elif choice == "4":

        print("\n👋 Thank you for using Context Recovery Agent.")
        break
    else:
        print("\n❌ Invalid choice.")
