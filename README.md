# Real-time-Scheduler
Real-Time Scheduling Algorithm Simulator

A simulator for visualizing and analyzing real-time CPU scheduling algorithms such as Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF). The project demonstrates how tasks are scheduled under strict timing constraints, including preemption and deadline handling.

Overview

Real-time systems require tasks to be completed within specified deadlines. This simulator models periodic tasks and executes them over a timeline, helping users understand scheduling behavior and system performance under different algorithms.

Features
Supports RMS (fixed priority scheduling)
Supports EDF (dynamic priority scheduling)
Simulates periodic task execution
Handles task preemption
Detects missed deadlines
Visualizes execution using a Gantt chart timeline
Displays CPU utilization and performance metrics
Enables comparison between RMS and EDF
Concepts Covered
Real-Time Scheduling
CPU Scheduling Algorithms
Task Preemption
Deadline Constraints
System Feasibility
Tech Stack
Language: (Add your language, e.g., JavaScript / Python)
Frontend: HTML, CSS
Visualization: Canvas / Chart library (if used)
Tools: VS Code, GitHub
How It Works
Input task parameters:
Execution Time (C)
Period (T)
Deadline (D)
Select scheduling algorithm (RMS or EDF)
The simulator:
Releases tasks periodically
Assigns priority based on the selected algorithm
Executes tasks with possible preemption
Outputs:
Execution timeline
Missed deadlines
Performance metrics
