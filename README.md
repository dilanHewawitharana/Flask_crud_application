# Flask REST API Application

This project implements a basic REST API application using the Python Flask framework.

## Project Structure

The repository contains the following files and directories:

- **create_db.py**: Creates a database (`recipes_database.db`) and inserts initial data (SQLite). After cloning the repository, run `python create_db.py` to create the database instance.
- **application.py**: Defines five REST API endpoints:
    - `POST /recipes`: Creates a recipe.
    - `GET /recipes`: Returns a list of all recipes.
    - `GET /recipes/<id>`: Returns the selected recipe by ID.
    - `PATCH /recipes/<id>`: Updates the selected recipe.
    - `DELETE /recipes/<id>`: Deletes the selected recipe.
- **requirements.txt**: Lists all necessary dependencies for the application.

## Running the Application

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Create the database by running `python create_db.py`.
4. Run the application using `python application.py`.

## Deployment Notes

- This application was initially a CRUD (Create, Read, Update, Delete) application. However, to pass test cases, the web application components were removed. Consequently, some unused HTML files may reside in the `templates` directory.
- This application is deployed to Amazon Web Services (AWS) using App Runner.
- **Deployed URL:** https://wkypax7uxy.ap-southeast-2.awsapprunner.com/

## GitHub Repository

This project is hosted on GitHub: https://github.com/dilanHewawitharana/Flask_rest_api_application.

You can track development via GitHub commit history.
