from flask import Flask, request, jsonify

app = Flask(__name__)

# -----------------------------
# Task Class
# -----------------------------
class Task:
    def __init__(self, name, execution, period):
        self.name = name
        self.execution = execution
        self.period = period
        self.deadline = period

        self.remaining = 0
        self.next_arrival = 0
        self.absolute_deadline = period

# -----------------------------
# Scheduler Logic
# -----------------------------
def simulate(tasks_data, max_time, algorithm):
    tasks = [Task(t["name"], t["execution"], t["period"]) for t in tasks_data]
    timeline = []

    for time in range(max_time):

        # Release tasks
        for t in tasks:
            if time == t.next_arrival:
                t.remaining = t.execution
                t.absolute_deadline = time + t.deadline
                t.next_arrival += t.period

        # Pick task
        ready = [t for t in tasks if t.remaining > 0]

        if ready:
            if algorithm == "RMS":
                current = min(ready, key=lambda x: x.period)
            else:
                current = min(ready, key=lambda x: x.absolute_deadline)

            current.remaining -= 1
            timeline.append(current.name)
        else:
            timeline.append("Idle")

    return timeline

# -----------------------------
# API Endpoint
# -----------------------------
@app.route("/simulate", methods=["POST"])
def run_simulation():
    data = request.json

    tasks = data["tasks"]
    max_time = data["time"]

    rms = simulate(tasks, max_time, "RMS")
    edf = simulate(tasks, max_time, "EDF")

    return jsonify({
        "rms": rms,
        "edf": edf
    })

if __name__ == "__main__":
    app.run(debug=True)
