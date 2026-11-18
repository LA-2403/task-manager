from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "user_name": "Harsh",
        "user_id": "u_001",
        "email": "harsh@example.com",
        "title": "Submit Python assignment",
        "category": "Academics",
        "due_date": datetime.now().strftime("%Y-%m-%d"),
        "timeline": "Morning",
        "completed": False,
    }
]


@app.route("/")
def index():
    today = datetime.now().strftime("%Y-%m-%d")
    category_filter = request.args.get("category", "All")

    if category_filter != "All":
        display_tasks = [t for t in tasks if t["category"] == category_filter]
    else:
        display_tasks = tasks

    sorted_tasks = sorted(
        display_tasks, key=lambda x: (x["completed"], x["due_date"])
    )

    return render_template(
        "index.html",
        tasks=sorted_tasks,
        today=today,
        current_filter=category_filter,
    )


@app.route("/add", methods=["POST"])
def add_task():
    user_name = request.form.get("user_name")
    user_id = request.form.get("user_id")
    email = request.form.get("email")
    title = request.form.get("title")
    category = request.form.get("category", "Other")
    due_date = request.form.get("due_date")
    timeline = request.form.get("timeline") or "Anytime"

    if not due_date:
        due_date = datetime.now().strftime("%Y-%m-%d")

    if title and email:
        new_task = {
            "id": len(tasks) + 1,
            "user_name": user_name.strip(),
            "user_id": user_id.strip(),
            "email": email.strip(),
            "title": title.strip(),
            "category": category,
            "due_date": due_date,
            "timeline": timeline.strip(),
            "completed": False,
        }
        tasks.append(new_task)

    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)