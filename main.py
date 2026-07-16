print("NEW MAIN.PY LOADED")

from update import update_project
from dashboard import show_dashboard

from project_manager import (
    create_project,
    resume_project
)

from memory import (
    find_project,
)

while True:

    print("\n" + "=" * 60)
    print("        CONTEXT RECOVERY AGENT")
    print("=" * 60)

    print("1. Create New Project")
    print("2. Search Project")
    print("3. Resume Project")
    print("4. Dashboard")
    print("5. Update Progress")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()

    # ==========================================
    # CREATE PROJECT
    # ==========================================

    if choice == "1":

        project = input("\nProject Name : ").strip()
        description = input("Description : ").strip()

        print("\nGenerating AI Project Plan...\n")

        plan = create_project(project, description)

        print(plan)

        print("\n✅ Project created successfully!")

    # ==========================================
    # SEARCH PROJECT
    # ==========================================

    elif choice == "2":

        project = input("\nEnter Project Name : ").strip()

        result = find_project(project)

        if result:

            print("\nProject Found")
            print("-" * 60)

            print(f"Project     : {result['project']}")
            print(f"Description : {result['description']}")

            print("\nCompleted Tasks")

            if result["completed"]:
                for task in result["completed"]:
                    print(f"✓ {task}")
            else:
                print("No completed tasks.")

            print("\nPending Tasks")

            if result["pending"]:
                for task in result["pending"]:
                    print(f"□ {task}")
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

            summary = resume_project(project)

            print(summary)

        else:

            print("\n❌ Project not found.")

    # ==========================================
    # DASHBOARD
    # ==========================================

    elif choice == "4":

        project = input("\nEnter Project Name : ").strip()

        show_dashboard(project)

    # ==========================================
    # UPDATE PROGRESS
    # ==========================================

    elif choice == "5":

        update_project()

    # ==========================================
    # EXIT
    # ==========================================

    elif choice == "6":

        print("\n👋 Thank you for using Context Recovery Agent.")
        break

    else:

        print("\n❌ Invalid choice.")