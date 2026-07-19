import os
from dotenv import load_dotenv
from google import genai

# ==========================================
# LOAD ENVIRONMENT
# ==========================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# ==========================================
# GENERATE PROJECT PLAN
# ==========================================

def generate_project_plan(project_name, description):

    prompt = f"""
You are an expert software project planner.

Project Name:
{project_name}

Project Description:
{description}

Generate a project plan.

Rules:
- Generate a maximum of 20 important tasks.
- Do not generate more than 20 tasks.
- Include only major development phases.
- Do not split one feature into many small subtasks.
- Return ONLY task names.
- One task per line.
- No numbering.
- No explanations.
- Tasks must be specific to the given project.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    tasks = [
        task.strip()
        for task in response.text.strip().split("\n")
        if task.strip()
    ]

    # Maximum 20 tasks
    tasks = tasks[:20]

    return "\n".join(tasks)


# ==========================================
# GENERATE SUMMARY
# ==========================================

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

1. A short project summary.
2. Current progress.
3. Next recommended task.

Keep the response professional and under 150 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()


# ==========================================
# SUGGEST NEXT TASK
# ==========================================

def suggest_next_task(project_name, pending_tasks):

    prompt = f"""
You are a project planning assistant.

Project Name:
{project_name}

Pending Tasks:
{pending_tasks}

Suggest ONLY the next highest-priority task.

Return exactly one sentence.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()


# ==========================================
# AI ASSISTANT
# ==========================================

def ask_ai(project_name, completed_tasks, pending_tasks, question):

    prompt = f"""
You are an intelligent AI Project Assistant.

Project Name:
{project_name}

Completed Tasks:
{completed_tasks}

Pending Tasks:
{pending_tasks}

User Question:
{question}

Instructions:
- Answer only based on the project details.
- Keep the answer short.
- Be practical.
- Do not add unnecessary explanations.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()