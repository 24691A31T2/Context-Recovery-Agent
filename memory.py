import json
import os
from datetime import datetime

FILE_PATH = "data/projects.json"


# ==========================================
# LOAD ALL PROJECTS
# ==========================================

def load_all_projects():

    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return []

            return data

    except:
        return []


# ==========================================
# SAVE ALL PROJECTS
# ==========================================

def save_all_projects(projects):

    with open(FILE_PATH, "w") as file:
        json.dump(projects, file, indent=4)


# ==========================================
# SAVE PROJECT
# ==========================================

def save_project(project):

    projects = load_all_projects()

    projects.append(project)

    save_all_projects(projects)


# ==========================================
# FIND PROJECT
# ==========================================

def find_project(project_name):

    projects = load_all_projects()

    for project in projects:

        if project["project"].lower() == project_name.lower():
            return project

    return None


# ==========================================
# UPDATE COMPLETED TASK
# ==========================================

def update_completed_task(project_name, task_name):

    projects = load_all_projects()

    for project in projects:

        if project["project"].lower() == project_name.lower():

            if task_name in project["pending"]:

                project["pending"].remove(task_name)

                project["completed"].append(task_name)

                # Update last modified time
                project["last_updated"] = datetime.now().strftime(
                    "%d %B %Y | %I:%M %p"
                )

                save_all_projects(projects)

                return True

    return False


# ==========================================
# ADD NEW REQUIREMENT
# ==========================================

def add_new_requirement(project_name, requirement):

    projects = load_all_projects()

    for project in projects:

        if project["project"].lower() == project_name.lower():

            project["pending"].append(requirement)

            # Update last modified time
            project["last_updated"] = datetime.now().strftime(
                "%d %B %Y | %I:%M %p"
            )

            save_all_projects(projects)

            return True

    return False


# ==========================================
# DELETE PROJECT
# ==========================================

def delete_project(project_name):

    projects = load_all_projects()

    projects = [
        project
        for project in projects
        if project["project"].lower() != project_name.lower()
    ]

    save_all_projects(projects)


# ==========================================
# GET ALL PROJECTS
# ==========================================

def get_all_projects():

    return load_all_projects()


# ==========================================
# PROJECT STATISTICS
# ==========================================

def get_statistics():

    projects = load_all_projects()

    total_projects = len(projects)

    completed_tasks = 0
    pending_tasks = 0

    for project in projects:

        completed_tasks += len(project["completed"])
        pending_tasks += len(project["pending"])

    return {
        "projects": total_projects,
        "completed": completed_tasks,
        "pending": pending_tasks,
    }


# ==========================================
# PROJECT PROGRESS
# ==========================================

def get_progress(project_name):

    project = find_project(project_name)

    if not project:
        return 0

    completed = len(project["completed"])
    pending = len(project["pending"])

    total = completed + pending

    if total == 0:
        return 0

    return round((completed / total) * 100)