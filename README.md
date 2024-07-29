# Flask_Rest_API_application

This is a Basic Rest API application using python Flask module.

create_db.py

This file purpose is to create data base and insert the initial data into data base.
I used sqlLite as the data base.
After clone this repo into local machine, you need to run 
python create_db.py
to run this file. It will create a new databse instance called recipes_database.db

application.py

This file consist of 5 rest api. Content is as follows.

POST /recipes -> Create a recipe.
GET /recipes -> Return the list of all of the recipes.
GET /recipes/(id) -> Return the selected recipe.
PATCH /recipes/(id) -> Update the selected recipe
DELETE /recipes/(id) -> Delete the selected recipe.

To run appication -> python application.py

Additional Notes

the requirements.txt file includes all necessary dependencies
I started this application as a crup application. but in order pass test cases I have to remove web application part. So there are some unwanted html.files in templates directory.

This application is deployed into amazon using App Runner service.
Deployed url is https://wkypax7uxy.ap-southeast-2.awsapprunner.com/

All the files are uploaded into github. Github repo url https://github.com/dilanHewawitharana/Flask_rest_api_application

You can check all the activities related to development using github commit history.