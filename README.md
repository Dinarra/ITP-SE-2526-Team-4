# 🎬 ITP-SE-2526-Team-4: Smart Content Recommendation System
Final Project for Introduction to Programming 2 (Python)

## 🌟 Project Overview
Our project is an interactive recommendation engine inspired by platforms like Netflix. It analyzes user preferences and suggests new content based on "social similarity" and shared tastes between users.

### How it works:
The system identifies profiles with overlapping interests by applying **Set Theory**. If two users share liked items, the engine recommends highly targeted content that one user has enjoyed but the target user hasn't discovered yet, with an option to persistently update the user's history directly on the disk.

---

## 🛠 Technical Implementation & Syllabus Compliance
This project strictly follows all advanced requirements from the course evaluation criteria:

* **Advanced OOP (4 Classes):** Implemented a robust hierarchy (`Content` -> `Movie` and `Viewer` -> `User`) demonstrating proper use of **Encapsulation** (private attributes with `@property` getters), **Inheritance** (`super().__init__()`), and **Polymorphism** (method overriding via `get_details()` and `get_role_profile()`).
* **Algorithmic Efficiency & Data Structures:** Utilized Python **Sets** for high-performance similarity tracking. By replacing nested loops with set intersections and differences, the recommendation logic achieves $O(1)$ lookup complexity, optimizing runtime from $O(n^2)$ to $O(n)$. **Dictionaries** are used for instant database record fetching by ID.
* **Data Persistence (File I/O):** Full integration of structured **JSON** handling. The system not only reads from `users.json` and `items.json` but dynamically writes and updates user matrices back to disk.
* **Advanced Python Features:** Leveraged memory-efficient **Generators** (`yield`) for streaming recommendation pipelines and **Lambda / Filter** functions for dynamic catalog processing.
* **Robust Error Handling:** Implemented granular `try-except` blocks to handle input exceptions, type conversions, and potential runtime anomalies without breaking execution.
* **Automated Unit Testing:** Includes a dedicated validation suite (`test_project.py`) utilizing strict `assert` statements to test edge cases and verify core algorithm integrity.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/Dinarra/ITP-SE-2526-Team-4.git](https://github.com/Dinarra/ITP-SE-2526-Team-4.git)
   Open the project folder in PyCharm.

Ensure Python interpreter is configured properly (Python 3.10+ recommended).

To execute automated tests: Run the testing suite:

Bash
python test_project.py
To run the main application: Execute the interactive simulation engine:

Bash
python main.py
👥 The Team (Group SE-2526)
Dinara (Lead / Architect) — Designed the core object-oriented class hierarchy, managed repository workflows, and enforced structural encapsulation standards.

Marzhan (Data Specialist) — Structured the JSON matrices and developed persistent file I/O operations for reading and writing data safely.

Balzhan (Logic Developer) — Engineered the set-theoretic matching algorithms, streaming generators, and lambda catalog filters.

Aigerim (QA & Integration) — Integrated individual modules into the final interactive application control flow, handled exception flows, and designed the automated assertion testing suite.