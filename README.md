# 🎬 ITP-SE-2526-Team-4: Smart Content Recommendation System
**Final Project for Introduction to Programming 2 (Python)**

## 🌟 Project Overview
Our project is a simplified recommendation engine inspired by platforms like Netflix and Amazon. It analyzes user preferences and suggests new content (movies or books) based on "social similarity" between users.

### How it works:
The system identifies users with similar tastes by applying **Set Theory**. If two users share several liked items, the engine recommends items that one user has enjoyed but the other hasn't discovered yet.

---

## 👥 The Team (Group SE-2526)
* **Dinara (Lead / Architect)** — Designed the class hierarchy and managed the Git repository workflow.
* **Marzhan (Data Specialist)** — Handled JSON data persistence and file I/O operations.
* **Balzhan (Logic Developer)** — Developed the similarity algorithms and recommendation generation logic.
* **Aigerim (QA & Integration)** — Managed final system assembly, error handling, and unit testing.

---

## 🛠 Technical Implementation
This project follows all mandatory requirements from the course syllabus:
* **OOP (3+ Classes):** Implemented `User`, `Item`, and `Engine` classes using encapsulation.
* **Smart Data Structures:** Used `set` operations (intersections and differences) for high-performance similarity matching.
* **Data Persistence:** All user preferences are stored and retrieved from `.json` files.
* **Advanced Features:** Implemented `generators` (using `yield`) for memory-efficient recommendation streaming.
* **Error Handling:** Robust `try-except` blocks to manage missing data or file errors.

---

## 🚀 How to Run
1. Clone the repository: `git clone https://github.com/Dinarra/ITP-SE-2526-Team-4.git`
2. Open the project in PyCharm.
3. Ensure `users.json` and `items.json` are in the root directory.
4. Run the main script: `python main.py`