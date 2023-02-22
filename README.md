[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Introduction

### CyberKernel
It is a project of blog management system.

---

# Features
  - Login system
  - Auther can add post
  - Diffrent types of users
  - Account system (register, login, logout)
  - Categories system
  - Implemented ckeditor
  - Introduced post route for auther to post blogs
  - Custom user model
  - User friendly
  - Rsponsive UI, made with bootstrap 5
  - Custom errors pages
  - Log users activities by middlewares and by python logging module

---

# Getting Started

### Prerequisites
1. Python
2. Python packages
   - django
   - ckeditor (django-ckeditor)
   - tzdata
   - pillow
3. Git

### Setup
##### Install Requirements
```bash
apt install python3 -y
apt install git -y
apt install python3-pip -y || apt install python-pip -y
```
##### Setup Project
```bash
git clone https://github.com/Dev-Bittu/CyberKernel.git
python3 setup.py install || python setup.py install
python3 manage.py makemigrations || python manage.py makemigrations
python3 manage.py migrate || python manage.py migrate
python3 manage.py runserver|| python manage.py runserver
```

### Setup in termux
##### Install requirements
```bash
apt install python3 git libjpeg-turbo -y
pip install wheel
apt install python-cryptography python-pillow -y
```

##### Setup Project
```bash
git clone https://github.com/Dev-Bittu/CyberKernel.git
python setup.py install
sh rmcache.sh
```

---

# Authers
Anuj & Bittu

### Contact With Us
  - [GitHub](https://github.com/Dev-Bittu "Dev-Bittu")

---

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE "Lincense file") file for details

---

# TODO
  - Convert function views to classes
  - Add rest framework & channels (websocket)
  - Improve UI & UX
  - Introduce about page
  - Improve search functionality
  - Introduce Comment & Reply system
  - Add donation system
  - Introduce middleware (Under maintaince)
  - Add notification system

---

# About
### About this project
Will write soon
