# **Installation**

[[toc]]

## **Getting Ready**

- clone the repo

```bash
git clone https://github.com/Himasnhu-at/uci_integration.git
```

- things to be installed:

```bash
python3
python3-venv
npm # for docs
```

## **Dev Setup**

::: tip Activate virtual environment

this is optional but recommended to keep dependencies separate and remove any conflicts

```bash
python3 -m venv venv
source venv/bin/activate
```

:::

- install requirements

```bash
pip install -r requirements.txt
```

- setup dev-docs

```bash
cd dev-docs
npm install
```

## **Running the Project**

- migrate dB

```bash
python manage.py migrate
```

- run the app

```bash
python manage.py runserver
```

- run the docs

```bash
cd dev-docs
npm run dev
```

## **Project Structure**

- authentication/: This directory contains the files for your 'authentication' Django app. It includes the models (models.py), views (views.py), and other files that Django uses to build the app.

- data/: This directory contain data files used by your project.

- db.sqlite3: This is your SQLite database file.

- dev-docs/: This directory contains the documentation for your project.

- manage.py: This is a command-line utility that lets you interact with your Django project in various ways such as running the development server, running tests, creating database tables, etc.

- templates/: This directory contains Django templates. These templates define the structure of the HTML that Django will send to the client.

- uci_integration/: This directory contains the settings for your Django project (settings.py), as well as the root URL configuration (urls.py), and other files.

- venv/: This directory contains the virtual environment for your project. A virtual environment is a self-contained environment that you can use to keep the dependencies required by different projects separate.
