# recognize
API to recognize leishmaniasis images

# Create virtualenv
```
python3 -m venv .venv
```

# Activate virtualenv
```
source .venv/bin/activate
```

# Install packages python
```
pip install -r requeriments.txt
```

# Install Pillow
```
python3 -m pip install Pillow
```

# Create migrations
```
python manage.py makemigrations
```

# Create database
```
python manage.py migrate
```

# Create superuser
```
python manage.py createsuperuser
```

# Run the system
```
python manage.py runserver
```

# Access the system
```
http://127.0.0.1:8000/
```

# Access the system administrative area
```
http://127.0.0.1:8000/admin/
```

# Access to api documentation
```
http://127.0.0.1:8000/api/docs
```


# References
```
https://docs.djangoproject.com/en/5.1/
https://django-ninja.dev/
https://pillow.readthedocs.io/en/stable/reference/Image.html
https://docs.pydantic.dev/latest/
```
