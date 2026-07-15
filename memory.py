import json
import os

FILE_PATH = "data/context.json"


def load_all_projects():
    """
    Load all projects from context.json
    """
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        try:
            data = json.load(file)

            # If old format exists (single dictionary), convert to empty list
            if isinstance(data, dict):
                return []

            return data

        except:
            return []


def save_project(project):
    """
    Save a new project
    """
    projects = load_all_projects()

    projects.append(project)

    with open(FILE_PATH, "w") as file:
        json.dump(projects, file, indent=4)


def find_project(project_name):
    """
    Search project by name
    """
    projects = load_all_projects()

    for project in projects:
        if project["project"].lower() == project_name.lower():
            return project

    return None


def update_completed_task(project_name, task_name):
    """
    Move a task from Pending to Completed
    """
    projects = load_all_projects()

    for project in projects:

        if project["project"].lower() == project_name.lower():

            for task in project["pending"]:

                if task.strip().lower() == task_name.strip().lower():

                    project["pending"].remove(task)
                    project["completed"].append(task)

                    with open(FILE_PATH, "w") as file:
                        json.dump(projects, file, indent=4)

                    return True

    return False


def add_new_requirement(project_name, requirement):
    """
    Add a new pending task
    """
    projects = load_all_projects()

    for project in projects:

        if project["project"].lower() == project_name.lower():

            project["pending"].append(requirement)

            with open(FILE_PATH, "w") as file:
                json.dump(projects, file, indent=4)

            return True

    return False


def get_all_projects():
    """
    Return all projects
    """
    return load_all_projects()


def delete_project(project_name):
    """
    Delete a project
    """
    projects = load_all_projects()

    updated_projects = [
        project
        for project in projects
        if project["project"].lower() != project_name.lower()
    ]

    with open(FILE_PATH, "w") as file:
        json.dump(updated_projects, file, indent=4)