from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def tamim(request):
    return HttpResponse("Hello I am Tamim, Start Django learning Some Days")


def userinfo(request):
    cv = F"""
🌟 Basic Developer Portfolio Information\n

👤 Personal Info
--------------------
Name: Md Moniruzzaman Tamim
Title: Full Stack Developer (Python | Django | JavaScript)
Location: Khulna, Bangladesh
Email: tamim@example.com
Phone: +8801XXXXXXXXX
LinkedIn: linkedin.com/in/tamimdev
GitHub: github.com/tamimdev
Portfolio Website: www.tamimdev.com

💻 About Me
--------------------
I am a passionate and dedicated software developer with experience in building modern, responsive, and scalable web applications using Python, Django, and JavaScript.
I love problem-solving, exploring new technologies, and continuously improving my coding skills to build efficient and user-friendly applications.

🧰 Skills
--------------------
💡 Programming Languages:
- Python 🐍
- JavaScript
- HTML, CSS, Bootstrap
- SQL (MySQL / MariaDB)
- Bash / Shell scripting

⚙️ Frameworks & Tools:
- Django, Django REST Framework
- React (basic)
- Git & GitHub
- VS Code / PyCharm
- Linux (AlmaLinux, RHEL, Ubuntu)
- Docker (basic)

🗄️ Databases:
- MariaDB
- PostgreSQL
- SQLite

☁️ Others:
- API Integration
- RESTful Web Services
- JSON / AJAX
- Virtual Environments
- Debugging and Deployment

🚀 Projects
--------------------
🧮 Expense Tracker App (Python)
Built a personal expense tracking system using Python.
Features: Add/view expenses, monthly summary, category-wise totals.
Used: Lists, dictionaries, file handling, f-strings.

📬 Django Mail Server System
Configured a mail server using Postfix, Dovecot, and MariaDB.
Integrated with Django for mail management.
Used: AlmaLinux, RHEL 8, MariaDB, Python, Django.

📓 Blog Application (Django)
Developed a blog site where users can post, edit, and delete articles.
Used: Django MVT, SQLite, HTML, CSS, Bootstrap.

💾 iSCSI Server Setup
Configured an iSCSI server-client setup on AlmaLinux.
Used for centralized storage access via /dev/VG1/lvm1.

🎓 Education
--------------------
Bachelor of Science (B.Sc.) in Computer Science and Engineering
City University, Dhaka
(Expected Graduation: YYYY)

🏆 Achievements
--------------------
- Completed 100 Days of Python Programming Challenge 🐍
- Working on 100 Days of Data Structures & Algorithms with Python
- Built multiple real-world Django projects from scratch.

🧭 Career Objective
--------------------
To obtain a challenging position as a Python/Django Developer where I can utilize my programming skills, contribute to impactful projects, and continue growing as a full-stack developer.

❤️ Interests
--------------------
- Web Development
- Open Source Projects
- Linux Server Management
- AI & Automation
- Learning New Technologies
"""
    html_text = cv.replace('\n', '<br>')
    return HttpResponse(html_text)
