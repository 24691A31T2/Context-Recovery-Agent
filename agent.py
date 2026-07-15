import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_project_plan(project_name, description):

    prompt = f"""
You are an expert software project planner.

Project Name:
{project_name}

Project Description:
{description}

Generate ONLY a list of project tasks.

Rules:
- Use the given project name.
- Do NOT change the project name.
- Do NOT generate another project.
- Return only task names.
- One task per line.
- No numbering.
- No explanation.
- No markdown.

Example:

Requirement Analysis
Project Planning
Database Design
Frontend Development
Backend Development
Testing
Deployment
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()


def generate_summary(project_name, completed_tasks, pending_tasks):

    prompt = f"""
You are an AI Context Recovery Assistant.

Project Name:
{project_name}

Completed Tasks:
{completed_tasks}

Pending Tasks:
{pending_tasks}

Generate:

1. A short summary.
2. Current progress.
3. Next recommended task.

Keep the answer short and clear.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()


def suggest_next_task(project_name, pending_tasks):

    prompt = f"""
Project:
{project_name}

Pending Tasks:
{pending_tasks}

Suggest ONLY the next highest priority task.

Keep the answer in one sentence.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()