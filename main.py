from flask import request, jsonify
from config import app, db
from models import Task

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    json_tasks = list(map(lambda x: x.to_json(), tasks))
    return jsonify({"tasks": json_tasks})

@app.route("/tasks/<string:date>", methods=["GET"])
def get_tasks_by_date(date):
    tasks = Task.query.filter_by(date=date).all()
    json_tasks = list(map(lambda x: x.to_json(), tasks))
    if not json_tasks:
        return jsonify({"message": "No tasks found for this date"}), 404
    return jsonify({"tasks": json_tasks})

@app.route("/create_task", methods=["POST"])
def create_task():
    title = request.json.get("title")
    description = request.json.get("description")
    date = request.json.get("date")
    time = request.json.get("time")

    if not title or not date:
        return jsonify({"message": "Title and date are required"}), 400

    new_task = Task(title=title, description=description, date=date, time=time)
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Task created!"}), 201

@app.route("/update_task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    title = request.json.get("title")
    description = request.json.get("description")
    date = request.json.get("date")
    time = request.json.get("time")

    if not title or not date:
        return jsonify({"message": "Title and date are required"}), 400

    task.title = title
    task.description = description
    task.date = date
    task.time = time

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Task updated!"}), 200


@app.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted!"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
