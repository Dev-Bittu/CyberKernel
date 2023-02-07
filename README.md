# Introduction

### CyberKernel
It is a project of blog management system.

---

# Installation

### Prerequirements
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
```
####### If your system is based on aarch64.
```bash
LDFLAGS="-L/system/lib64/"; CFLAGS="-I/data/data/com.termux/files/usr/include" #Required for pillow (pip)
```
####### Else
```bash
LDFLAGS="-L/system/lib/"; CFLAGS="-I/data/data/com.termux/files/usr/include" #Required for pillow (pip)                                               ```

##### Setup Project
```bash
git clone https://github.com/Dev-Bittu/CyberKernel.git
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# About
### About this project
Will write soon
