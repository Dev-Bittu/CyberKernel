# Introduction

### CyberKernel
It is a project of blog management system.

---

# Features
  - Login system
  - Auther can add post
  - Diffrent types of users
  - Use can register, login & logout
  - Post categories

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
python3-pip install -r requirements.txt || pip install -r requirements.txt
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
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---
# Authers
### Bittu Kumar Goswami
### Contact With Me

# License
This project is licensed under the MIT License - see the LICENSE file for details

# TODO
  - Convert function views to classes
  - Add rest framework & channels (websocket)
  - Improve UI & UX

# About
### About this project
Will write soon
