# Agro Nepal E-commerce Project

## Deployment Instructions for PythonAnywhere

### 1. Sign up for PythonAnywhere
- Go to [PythonAnywhere](https://www.pythonanywhere.com/)
- Create a free account

### 2. Upload Your Project
- In PythonAnywhere dashboard, go to Files tab
- Upload your project files using the upload button
- Or use Git to clone your repository

### 3. Set Up Virtual Environment
```bash
# Create a new virtual environment
mkvirtualenv --python=/usr/bin/python3.10 myenv

# Activate the virtual environment
workon myenv

# Install requirements
pip install -r requirements.txt
```

### 4. Configure Web App
1. Go to Web tab in PythonAnywhere dashboard
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Set up your virtual environment path

### 5. Configure WSGI File
- Go to Web tab
- Click on the WSGI configuration file link
- Replace the content with:

```python
import os
import sys

# Add your project directory to Python path
path = '/home/YOUR_USERNAME/UserAuth'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'UserAuth.settings'

# Activate virtual environment
activate_this = '/home/YOUR_USERNAME/.virtualenvs/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Configure Static Files
1. Go to Web tab
2. Under "Static files" section, add:
   - URL: /static/
   - Directory: /home/YOUR_USERNAME/UserAuth/static/

### 7. Configure Media Files
1. Go to Web tab
2. Under "Static files" section, add:
   - URL: /media/
   - Directory: /home/YOUR_USERNAME/UserAuth/media/

### 8. Update Settings
Make sure your settings.py has:
```python
DEBUG = False
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']

# Static files configuration
STATIC_ROOT = '/home/YOUR_USERNAME/UserAuth/static'
MEDIA_ROOT = '/home/YOUR_USERNAME/UserAuth/media'
```

### 9. Collect Static Files
```bash
python manage.py collectstatic
```

### 10. Database Setup
1. Go to Databases tab
2. Create a new database
3. Update settings.py with database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_USERNAME$default',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_DATABASE_PASSWORD',
        'HOST': 'YOUR_USERNAME.mysql.pythonanywhere-services.com',
    }
}
```

### 11. Run Migrations
```bash
python manage.py migrate
```

### 12. Create Superuser
```bash
python manage.py createsuperuser
```

### 13. Reload Web App
- Go to Web tab
- Click "Reload" button

Your site should now be live at: https://YOUR_USERNAME.pythonanywhere.com

## Important Notes
1. Replace YOUR_USERNAME with your PythonAnywhere username
2. Make sure to keep your secret key and database credentials secure
3. Update ALLOWED_HOSTS with your actual domain
4. Remember to collect static files after any changes
5. Always reload the web app after making changes 