from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
        self.absolute_deadline = 0


# -----------------------------
# Simulation Function
# -----------------------------
def simulate(tasks_input, algorithm, total_time):
    tasks = [Task(t['name'], t['execution'], t['period']) for t in tasks_input]

    timeline = []
    missed = []

    for time in range(total_time):

        # Task arrival
        for t in tasks:
            if time == t.next_arrival:
                if t.remaining > 0:
                    missed.append(f"{t.name} missed deadline at t={time}")

                t.remaining = t.execution
                t.absolute_deadline = time + t.deadline
                t.next_arrival += t.period

        # Ready queue
        ready = [t for t in tasks if t.remaining > 0]

        # Scheduling
        if ready:
            if algorithm == "RM":
                ready.sort(key=lambda x: x.period)
            else:
                ready.sort(key=lambda x: x.absolute_deadline)

            current = ready[0]
            current.remaining -= 1
            timeline.append(f"{current.name}")
        else:
            timeline.append("Idle")

        # Deadline check
        for t in tasks:
            if time + 1 == t.absolute_deadline and t.remaining > 0:
                missed.append(f"{t.name} missed deadline at t={time+1}")
                t.remaining = 0

    return timeline, missed


# -----------------------------
# API
# -----------------------------
@app.route('/simulate', methods=['POST'])
def run_simulation():
    data = request.json
    tasks = data['tasks']
    total_time = data['time']

    rms, rms_missed = simulate(tasks, "RM", total_time)
    edf, edf_missed = simulate(tasks, "EDF", total_time)

    return jsonify({
        "RMS": {"timeline": rms, "missed": rms_missed},
        "EDF": {"timeline": edf, "missed": edf_missed}
    })


# -----------------------------
# Serve HTML
# -----------------------------
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
