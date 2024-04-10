# Django Overview

Django is a high-level web framework for building web applications using Python. It follows the model-view-template (MVT) architectural pattern, which is similar to the model-view-controller (MVC) pattern but with a slightly different structure.

Here are some key features and components of Django:

1. **Object-Relational Mapping (ORM)**: Django provides an ORM system that allows developers to interact with the database using Python code instead of SQL queries directly. This simplifies database operations and makes the code more portable across different database backends.

2. **Admin Interface**: Django comes with a built-in admin interface that can be easily customized and used to manage the application's data models. Developers can create, read, update, and delete (CRUD) records in the database through the admin interface without writing additional code.

3. **URL Routing**: Django uses a URL routing mechanism that maps URLs to views. Developers can define URL patterns in the project's URL configuration file, which directs incoming requests to the appropriate view functions.

4. **Template Engine**: Django's template engine allows developers to create HTML templates that are rendered dynamically with data from the application. Templates can include variables, loops, conditionals, and other control structures to generate dynamic content.

5. **Security**: Django includes built-in security features such as protection against common web vulnerabilities like SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), and click jacking. It also provides user authentication and authorization mechanisms.

6. **Middleware**: Django middleware is a framework of hooks that allows developers to modify request/response objects globally in the application. Middleware can perform tasks such as authentication, logging, error handling, and more.

7. **Internationalization (i18n) and Localization (l10n)**: Django supports internationalization and localization, allowing developers to create multilingual websites easily. It provides tools for translating text strings, formatting dates, times, and numbers based on different locales.

8. **Modularity**: Django applications are organized into reusable components called apps. Each app can contain models, views, templates, static files, and other resources related to a specific functionality or feature of the application.

Overall, Django is popular among developers for its scalability, security, built-in features, and rapid development capabilities, making it a preferred choice for building complex web applications and websites.

## virtual environment

A virtual environment allows you to have a virtual installation of Python and packages on your computer.

why would you ever want or need this?

Packages change and get updated often!
There are changes that break backwards compatibility

***virtual environment creation with conda***

```bash
conda create --name myEnv django
```

Here we created an environment called “myEnv” with the latest version of Django.
You can then activate the environment

```bash
conda activate myEnv
```

See the virtual environment name is prefixed with project path

```bash
(myEnv)<project path>\
```

Now, anything installed with pip or conda when this environment is activated, will only be installed for this environment.

You can then deactivate the environment

```bash
conda deactivate
```

***virtual environment creation with python***

Step 1: install virtual environment

```bash
pip install virtualenv
```

Step 2: Create a virtual environment

```bash
python -m virtualenv venv
```

Step 3: activate virtualenv

```bash
<PATH>\venv\Scripts>activate
(venv) <PATH>\venv\Scripts>
```

Step 4: deactivate virtualenv

```bash
(venv) <PATH>\venv\Scripts>deactivate
```

Step 5: install django

```bash
(venv) <PATH>\venv\Scripts>pip install django
```

Step 6: migrate

```bash
python manage.py migrate
```

