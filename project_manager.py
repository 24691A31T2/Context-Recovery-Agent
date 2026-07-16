from memory import (
    save_project,
    find_project,
    update_completed_task,
    add_new_requirement,
    get_all_projects,
    delete_project
)

from agent import (
    generate_project_plan,
    generate_summary
)


def create_project(project_name, description):

    plan = generate_project_plan(project_name, description)

    project_data = {
        "project": project_name,
        "description": description,
        "completed": [],
        "pending": [
            task.strip()
            for task in plan.split("\n")
            if task.strip()
        ]
    }

    save_project(project_data)

    return plan


def resume_project(project_name):

    project = find_project(project_name)

    if not project:
        return None

    summary = generate_summary(
        project["project"],
        project["completed"],
        project["pending"]
    )

    return summary