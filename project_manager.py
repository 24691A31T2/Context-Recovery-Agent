from datetime import datetime

from memory import (
    save_project,
    find_project,
    update_completed_task,
    add_new_requirement,
    get_all_projects,
    delete_project,
    get_progress,
    get_statistics
)

from agent import (
    generate_project_plan,
    generate_summary
)


# ==========================================
# CREATE PROJECT
# ==========================================

def create_project(project_name, description):

    existing_project = find_project(project_name)

    if existing_project:
        return None

    plan = generate_project_plan(project_name, description)

    tasks = [
        task.strip()
        for task in plan.split("\n")
        if task.strip()
    ]

    current_time = datetime.now().strftime("%d %B %Y | %I:%M %p")

    project_data = {
        "project": project_name,
        "description": description,
        "created_date": current_time,
        "last_updated": current_time,
        "completed": [],
        "pending": tasks
    }

    save_project(project_data)

    return tasks


# ==========================================
# RESUME PROJECT
# ==========================================

def resume_project(project_name):

    project = find_project(project_name)

    if not project:
        return None

    return generate_summary(
        project["project"],
        project["completed"],
        project["pending"]
    )


# ==========================================
# SEARCH PROJECT
# ==========================================

def search_project(project_name):
    return find_project(project_name)


# ==========================================
# COMPLETE TASK
# ==========================================

def complete_task(project_name, task_name):
    return update_completed_task(project_name, task_name)


# ==========================================
# ADD REQUIREMENT
# ==========================================

def add_requirement(project_name, requirement):
    return add_new_requirement(project_name, requirement)


# ==========================================
# LIST PROJECTS
# ==========================================

def list_projects():
    return get_all_projects()


# ==========================================
# DELETE PROJECT
# ==========================================

def remove_project(project_name):
    delete_project(project_name)


# ==========================================
# DASHBOARD
# ==========================================

def get_dashboard(project_name):

    project = find_project(project_name)

    if not project:
        return None

    return {
        "project": project["project"],
        "description": project["description"],
        "created_date": project.get("created_date", "Not Available"),
        "last_updated": project.get("last_updated", "Not Available"),
        "completed": project["completed"],
        "pending": project["pending"],
        "progress": get_progress(project_name)
    }


# ==========================================
# HOME STATISTICS
# ==========================================

def home_statistics():
    return get_statistics()