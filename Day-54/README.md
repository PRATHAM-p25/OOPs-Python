# Flask Project - Complete Build Guide

This is a **template project** with empty files. Follow this guide to build a complete Flask application from scratch.

## 📋 Project Overview

You will build a Flask web application with:
- **Flask routes** - Handle HTTP requests
- **Jinja2 templates** - Dynamic HTML pages
- **Static files** - CSS styling and JavaScript
- **Configuration** - Environment-based settings
- **Tests** - Pytest and UI test cases

## 📁 Project Structure

```
exskilence_project/
├── app.py                    # Main Flask application (CREATE THIS)
├── config.py                 # Configuration file (CREATE THIS)
├── requirements.txt          # Dependencies (UPDATE THIS)
├── README.md                 # This file
│
├── templates/                # HTML templates folder
│   ├── base.html            # Base template (CREATE THIS)
│   └── index.html           # Home page template (CREATE THIS)
│
└── static/                   # Static files folder
    ├── css/
    │   └── style.css        # Stylesheet (CREATE THIS)
    └── js/
        └── main.js         # JavaScript file (CREATE THIS)

testing_config/               # Testing configuration
├── py_tests/
│   └── task.py              # Pytest tests (CREATE THIS)
└── ui_tests/
    └── task.json            # UI test config (UPDATE THIS)
```

## 🚀 Step-by-Step Build Instructions

### Step 1: Set Up Dependencies

**File: `requirements.txt`**

Add the following dependencies:

```
Flask==3.0.0
python-dotenv==1.0.0
pytest==7.4.3
pytest-flask==1.3.0
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

---

### Step 2: Create Configuration File

**File: `config.py`**

Create a configuration class with step-by-step comments:

```python
"""
Configuration file for Flask application
This file manages application settings and environment variables

STEP-BY-STEP GUIDE:
==================
This file demonstrates how to manage configuration in Flask.
"""

# STEP 1: Import required modules
# os - For accessing environment variables
# load_dotenv - For loading .env file
import os
from dotenv import load_dotenv

# STEP 2: Load environment variables from .env file
# This allows you to store sensitive data in .env file
load_dotenv()

# STEP 3: Create configuration class
class Config:
    """
    Application configuration class
    
    This class stores all configuration settings for the Flask app.
    Settings can come from environment variables or default values.
    """
    # STEP 4: Define configuration variables
    # SECRET_KEY - Used for session management and security
    # Gets value from environment variable or uses default
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # You can add more configuration settings here
    # For example: database URLs, API keys, etc.
```

---

### Step 3: Create Main Flask Application

**File: `app.py`**

Create the main Flask app with routes and step-by-step comments:

```python
"""
Flask Application - Main File
This is the main Flask application file that handles all routes.

STEP-BY-STEP GUIDE:
==================
This file demonstrates the basic structure of a Flask application.
Follow the comments to understand each step of the setup process.
"""

# STEP 1: Import Flask and necessary modules
# Flask - The main web framework
# render_template - Function to render HTML templates
from flask import Flask, render_template

# STEP 2: Create Flask application instance
# __name__ tells Flask where to find templates and static files
# Flask will look for 'templates' and 'static' folders in the same directory
app = Flask(__name__)

# STEP 3: Define routes (URL endpoints)
# Routes map URLs to Python functions
# When a user visits a URL, Flask calls the corresponding function

# Route 1: Home page
# @app.route('/') - Decorator that tells Flask which URL triggers this function
# '/' means the root URL (http://localhost:5000/)
@app.route('/')
def home():
    """
    Home page route handler
    
    This function:
    1. Gets called when user visits http://localhost:5000/
    2. Renders the 'index.html' template
    3. Returns the HTML to the browser
    """
    # render_template() looks for 'index.html' in the 'templates' folder
    # It processes the template and returns HTML
    return render_template('index.html')

# Route 2: About page
# '/about' means the URL will be http://localhost:5000/about
@app.route('/about')
def about():
    """
    About page route handler
    
    This function:
    1. Gets called when user visits http://localhost:5000/about
    2. Renders the 'about.html' template
    3. Returns the HTML to the browser
    """
    return render_template('about.html')

# STEP 4: Run the application
# This code only runs when you execute this file directly (not when imported)
# __name__ == '__main__' means the script is being run directly
if __name__ == '__main__':
    """
    Start the Flask development server
    
    Parameters:
    - debug=True: Enables debug mode (shows errors, auto-reloads on changes)
    - host='0.0.0.0': Makes server accessible from any network interface
    - port=5000: Runs on port 5000 (default Flask port)
    
    Access the app at: http://localhost:5000
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

### Step 4: Create Base Template

**File: `templates/base.html`**

Create the base template that other pages will extend:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- STEP 1: Basic HTML structure -->
    <!-- Meta tags for character encoding and responsive design -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- STEP 2: Page title with Jinja2 template block -->
    <!-- Defines a block that can be overridden in child templates -->
    <title>{% block title %}Flask Project{% endblock %}</title>
    
    <!-- STEP 3: Link to CSS file using Flask's url_for() -->
    <!-- url_for('static', filename='css/style.css') generates the correct path -->
    <!-- Flask automatically serves files from the 'static' folder -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    
    <!-- STEP 4: Extra CSS block for page-specific styles -->
    <!-- Child templates can add additional CSS here -->
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- STEP 5: Main container div -->
    <div class="container">
        
        <!-- STEP 6: Navigation bar -->
        <!-- url_for('home') - Generates URL for the 'home' route function -->
        <!-- url_for('about') - Generates URL for the 'about' route function -->
        <!-- This is better than hardcoding URLs because Flask handles routing -->
        <nav class="navbar">
            <a href="{{ url_for('home') }}">Home</a>
            <a href="{{ url_for('about') }}">About</a>
        </nav>
        
        <!-- STEP 7: Content block -->
        <!-- Main content area -->
        <!-- Child templates will replace this block with their content -->
        {% block content %}{% endblock %}
    </div>
    
    <!-- STEP 8: Link to JavaScript file -->
    <!-- Similar to CSS, Flask serves JS files from the 'static' folder -->
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    
    <!-- STEP 9: Extra JavaScript block for page-specific scripts -->
    <!-- Child templates can add additional JavaScript here -->
    {% block extra_js %}{% endblock %}
</body>
</html>

<!-- 
TEMPLATE INHERITANCE EXPLANATION:
==================================
This is the BASE TEMPLATE. Other templates (index.html, about.html) will:
1. Extend this template using {% extends "base.html" %}
2. Override blocks like block content with their own content
3. Inherit the structure, navigation, and styling from this template

Benefits:
- DRY (Don't Repeat Yourself) - Write common HTML once
- Easy maintenance - Change navigation in one place
- Consistent layout across all pages

IMPORTANT: Do NOT include Jinja2 syntax ({% or %}) inside HTML comments!
Use plain text descriptions instead.
-->
```

---

### Step 5: Create Home Page Template

**File: `templates/index.html`**

Create the home page that extends the base template:

```html
<!-- STEP 1: Extend the base template -->
<!-- {% extends "base.html" %} tells Jinja2 to use base.html as the parent template -->
<!-- This means index.html will inherit all HTML structure from base.html -->
{% extends "base.html" %}

<!-- STEP 2: Override the title block -->
<!-- This replaces block title in base.html -->
<!-- The page title will be "Home - Flask Project" -->
{% block title %}Home - Flask Project{% endblock %}

<!-- STEP 3: Override the content block -->
<!-- This replaces block content in base.html -->
<!-- Everything inside this block will appear in the main content area -->
{% block content %}
<div class="content">
    <!-- STEP 4: Add page-specific content -->
    <!-- This is regular HTML that will be inserted into the base template -->
    <h1>Welcome to Flask Project</h1>
    <p>This is a simple Flask application to learn project setup.</p>
    <p>You've successfully set up a Flask project!</p>
    
    <!-- STEP 5: Add styled content sections -->
    <div class="info-box">
        <h2>Project Structure</h2>
        <ul>
            <li><strong>app.py</strong> - Main Flask application file</li>
            <li><strong>config.py</strong> - Configuration settings</li>
            <li><strong>templates/</strong> - HTML templates</li>
            <li><strong>static/</strong> - CSS, JavaScript, images</li>
        </ul>
    </div>
</div>
{% endblock %}

<!-- 
HOW THIS WORKS:
===============
1. User visits http://localhost:5000/
2. Flask calls the home() function in app.py
3. home() returns render_template('index.html')
4. Flask finds index.html in the templates folder
5. Jinja2 processes the template:
   - Sees extends "base.html"
   - Loads base.html
   - Replaces block title with "Home - Flask Project"
   - Replaces block content with the content above
6. Flask returns the final HTML to the browser
-->
```

**File: `templates/about.html`** (Create this too)

```html
{% extends "base.html" %}

{% block title %}About - Flask Project{% endblock %}

{% block content %}
<div class="content">
    <h1>About This Project</h1>
    <p>This project demonstrates Flask basics.</p>
    <p>Learn how to set up routes, templates, and static files.</p>
</div>
{% endblock %}
```

---

### Step 6: Create CSS Stylesheet

**File: `static/css/style.css`**

Create styles with step-by-step comments:

```css
/* Flask Project - CSS Stylesheet */

/* STEP 1: CSS Reset */
/* Removes default browser styling for consistent appearance */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* STEP 2: Body styling */
/* Sets default font and background for entire page */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* STEP 3: Container */
/* Centers content and sets maximum width */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* STEP 4: Navigation bar */
/* Styles the navigation menu */
.navbar {
    background-color: #333;
    padding: 15px;
    margin-bottom: 20px;
}

.navbar a {
    color: white;
    text-decoration: none;
    margin-right: 20px;
    padding: 10px 15px;
}

.navbar a:hover {
    background-color: #555;
}

/* STEP 5: Content area */
/* Styles the main content section */
.content {
    background-color: white;
    padding: 30px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

/* STEP 6: Info box */
/* Styles information boxes */
.info-box {
    background-color: #e8f4f8;
    padding: 20px;
    margin-top: 20px;
    border-radius: 5px;
}

.info-box h2 {
    margin-bottom: 10px;
}

.info-box ul {
    margin-left: 20px;
}

/* 
CSS IN FLASK:
=============
Flask automatically serves files from the 'static' folder.
When you use url_for('static', filename='css/style.css'), Flask:
1. Looks in the 'static' folder
2. Finds 'css/style.css'
3. Generates the correct URL: /static/css/style.css
4. Browser requests the file and Flask serves it

This is why we link CSS in templates using:
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
*/
```

---

### Step 7: Create JavaScript File

**File: `static/js/main.js`**

Create JavaScript with step-by-step comments:

```javascript
// Flask Project - JavaScript File

// STEP 1: Wait for DOM to load
// DOMContentLoaded fires when HTML is fully loaded
// This ensures all elements exist before we try to access them
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page loaded successfully!');
    
    // STEP 2: Add your JavaScript code here
    // Example: Add click handlers, form validation, etc.
    
    // Example: Add click handler to navigation links
    const navLinks = document.querySelectorAll('.navbar a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            console.log('Navigating to:', this.href);
        });
    });
});

/* 
JAVASCRIPT IN FLASK:
====================
JavaScript runs in the browser (client-side), not on the server.
Flask serves JavaScript files from the 'static' folder just like CSS.

When you use url_for('static', filename='js/main.js'), Flask:
1. Looks in the 'static' folder
2. Finds 'js/main.js'
3. Generates the correct URL: /static/js/main.js
4. Browser downloads and executes the JavaScript

This is why we link JS in templates using:
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
*/
```

---

### Step 8: Create Pytest Test Cases

**File: `testing_config/py_tests/task.py`**

Create test cases with step-by-step comments:

```python
"""
Flask Project - Pytest Test Cases

STEP-BY-STEP TEST SETUP:
========================
This file contains test cases for the Flask application.
Tests verify that routes work correctly and templates render properly.
"""

import pytest
import sys
import os

# STEP 1: Set up Python path
# We need to add the exskilence_project folder to Python path
# This allows us to import the Flask app
# Path: Go up 3 levels from task.py to reach project root, then join exskilence_project
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
exskilence_path = os.path.join(project_root, 'exskilence_project')
sys.path.insert(0, exskilence_path)
os.chdir(exskilence_path)

# STEP 2: Import Flask application
# Now we can import the app from exskilence_project
from app import app

# STEP 3: Configure app for testing
# TESTING mode disables error catching during request handling
# This allows test framework to catch errors
app.config['TESTING'] = True

@pytest.fixture
def client():
    """
    Create test client fixture
    
    This fixture:
    1. Creates a test client for the Flask app
    2. Allows us to make HTTP requests to test routes
    3. Returns the client for use in test functions
    """
    with app.test_client() as c:
        yield c

def test_home_route_exists(client):
    """
    Test Case 1: Verify home route is accessible
    
    This test:
    1. Makes a GET request to the home route (/)
    2. Checks that response status is 200 (success)
    3. Verifies that expected content is present
    """
    response = client.get('/')
    assert response.status_code == 200, "Home route should return status 200"
    assert b'Welcome' in response.data, "Home page should contain 'Welcome'"

def test_about_route_exists(client):
    """
    Test Case 2: Verify about route is accessible
    """
    response = client.get('/about')
    assert response.status_code == 200, "About route should return status 200"
    assert b'About' in response.data, "About page should contain 'About'"

def test_navigation_links_present(client):
    """
    Test Case 3: Verify navigation links are present in templates
    """
    response = client.get('/')
    assert b'Home' in response.data, "Navigation should contain 'Home' link"
    assert b'About' in response.data, "Navigation should contain 'About' link"

def test_templates_render_correctly(client):
    """
    Test Case 4: Verify templates render without raw Jinja2 syntax
    """
    response = client.get('/')
    # Check that Jinja2 syntax is processed (not shown as raw text)
    assert b'{%' not in response.data, "Templates should not show raw Jinja2 syntax"
    assert b'%}' not in response.data, "Templates should not show raw Jinja2 syntax"

def test_static_files_referenced(client):
    """
    Test Case 5: Verify static files (CSS/JS) are referenced in templates
    """
    response = client.get('/')
    # Check that CSS and JS files are linked
    assert b'style.css' in response.data, "Template should reference style.css"
    assert b'main.js' in response.data, "Template should reference main.js"
```

**Run tests:**
```bash
cd testing_config/py_tests
pytest task.py -v
```

---

### Step 9: Configure UI Tests

**File: `testing_config/ui_tests/task.json`**

Update the JSON configuration:

```json
{
  "id": "ui_tests",
  "validation": {
    "static": {
      "requiredElements": [
        {
          "selector": "nav.navbar",
          "description": "Navigation bar should exist"
        },
        {
          "selector": ".container",
          "description": "Container div should exist"
        },
        {
          "selector": ".content",
          "description": "Content div should exist"
        }
      ],
      "requiredSelectors": [
        ".navbar",
        ".container",
        ".content",
        ".info-box"
      ]
    },
    "pytest": {
      "testFile": "testing_config/py_tests/task.py",
      "timeout": 30,
      "runTests": {
        "test_home_route_exists": "Test home route accessibility",
        "test_about_route_exists": "Test about route accessibility",
        "test_navigation_links_present": "Test navigation structure",
        "test_templates_render_correctly": "Test template rendering",
        "test_static_files_referenced": "Test static file references"
      }
    },
    "dynamic": {
      "flaskApp": "exskilence_project/app.py",
      "baseUrl": "http://localhost:5000",
      "screenshot": true,
      "testCases": [
        {
          "name": "Home page loads correctly",
          "url": "/",
          "assertions": [
            {
              "type": "contains",
              "selector": "body",
              "value": "Welcome"
            }
          ]
        },
        {
          "name": "About page loads correctly",
          "url": "/about",
          "assertions": [
            {
              "type": "contains",
              "selector": "body",
              "value": "About"
            }
          ]
        }
      ]
    }
  }
}
```

---

## ✅ Verification Checklist

After building all files, verify:

- [ ] `requirements.txt` has Flask and python-dotenv
- [ ] `config.py` has Config class with SECRET_KEY
- [ ] `app.py` has Flask app with at least 2 routes
- [ ] `templates/base.html` has navigation and blocks
- [ ] `templates/index.html` extends base.html
- [ ] `templates/about.html` extends base.html
- [ ] `static/css/style.css` styles the page
- [ ] `static/js/main.js` has JavaScript code
- [ ] `testing_config/py_tests/task.py` has 5+ test cases
- [ ] `testing_config/ui_tests/task.json` is configured

---

## 🚀 Running the Project

1. **Install dependencies:**
   ```bash
   cd exskilence_project
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access in browser:**
   - Home: http://localhost:5000/
   - About: http://localhost:5000/about

4. **Run tests:**
   ```bash
   cd testing_config/py_tests
   pytest task.py -v
   ```

---

## 📚 Key Concepts to Learn

### Flask Routes
- Routes map URLs to Python functions
- Use `@app.route()` decorator
- Return HTML using `render_template()`

### Template Inheritance
- Base template defines common structure
- Child templates extend base template
- Use `{% block %}` for replaceable sections

### Static Files
- CSS and JavaScript go in `static/` folder
- Use `url_for('static', filename='...')` to link files
- Flask automatically serves static files

### Testing
- Use pytest for unit tests
- Test routes, templates, and functionality
- Configure UI tests in JSON

---

## 🐛 Common Issues

**Port already in use:**
- Change port in `app.py`: `app.run(port=5001)`

**Module not found:**
- Make sure you're in `exskilence_project` folder
- Run `pip install -r requirements.txt`

**Templates not found:**
- Check templates are in `templates/` folder
- Verify template names match exactly

**Static files not loading:**
- Check files are in `static/` folder
- Verify `url_for()` syntax is correct

---

## 🎓 Next Steps

After completing this project:

1. Add more routes and pages
2. Add forms and form handling
3. Integrate a database (SQLAlchemy)
4. Add user authentication
5. Deploy to production

---

**Good luck building your Flask project! 🚀**

Follow each step carefully, and refer to the code examples above. All files should have step-by-step comments explaining what each part does.

