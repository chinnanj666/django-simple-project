# Django Hello World Project

This is a simple Django project to demonstrate the basic setup and rendering of a "Hello World" page with some custom styles.

## Features
- A basic Django app that renders a "Hello World" message.
- Simple inline CSS to style the page.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django

You can install Django using pip:

```bash
pip install django

# Project Structure
cpp
Copy

helloworld-django/
├── hello/
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── hello/
│   │       └── index.html
│   ├── static/
│   │   └── hello/
│   │       └── styles.css
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── settings.py
