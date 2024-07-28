from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes_database.db'
db = SQLAlchemy(application)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    making_time = db.Column(db.String(100), nullable=False)
    serves = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
 
    def __repr__(self):
        return '<Recipe %r' % self.id

@application.route('/')
def home():
    return jsonify({"message": "Access base url"}), 404

@application.route('/recipes', methods=['POST', 'GET'])
def recipes():
    if request.method == 'POST':
        data = request.get_json()

        required_fields = ['title', 'making_time', 'serves', 'ingredients', 'cost']
        
        if not data or not all(field in data for field in required_fields):
            res = {
                "message": "Recipe creation failed!",
                "required": "title, making_time, serves, ingredients, cost"
            }
            return jsonify(res), 200
        
        # create new recipe and save to db
        try:
            new_recipe = Recipe(
                title=data['title'],
                making_time=data['making_time'],
                serves=data['serves'],
                ingredients=data['ingredients'],
                cost=data['cost'],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
            db.session.add(new_recipe)
            db.session.commit()

            res = {
                "message": "Recipe successfully created!",
                "recipe": [{
                    "id": new_recipe.id,
                    "title": new_recipe.title,
                    "making_time": new_recipe.making_time,
                    "serves": new_recipe.serves,
                    "ingredients": new_recipe.ingredients,
                    "cost": new_recipe.cost,
                    "created_at": new_recipe.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": new_recipe.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                }]
            }

            return jsonify(res), 200
        except Exception as e:
            res = {"message": "Recipe creation failed!", "error": str(e)}
            return jsonify(res), 404
    else:
        recipes = Recipe.query.order_by(Recipe.created_at).all()
        recipes_list = [{
            "id": recipe.id,
            "title": recipe.title,
            "making_time": recipe.making_time,
            "serves": recipe.serves,
            "ingredients": recipe.ingredients,
            "cost": recipe.cost
        } for recipe in recipes]

        res = {"recipes": recipes_list}
        return jsonify(res), 200
    
@application.route('/recipes/<int:id>')
def get_recipe_by_id(id):
    try:
        recipe = Recipe.query.get(id)
        if recipe is None:
            res = {"message": "Recipe not found"}
            return jsonify(res), 404
        
        # Prepare the response data
        recipe_data = [{
            "id": recipe.id,
            "title": recipe.title,
            "making_time": recipe.making_time,
            "serves": recipe.serves,
            "ingredients": recipe.ingredients,
            "cost": recipe.cost
        }]

        res = {
            "message": "Recipe details by id",
            "recipe": recipe_data
        }
        return jsonify(res), 200
    except Exception as e:
        res = {"message": "An error occurred while retrieving the recipe", "error": str(e)}
        return jsonify(res), 500

@application.route('/recipes/<int:id>', methods=['PATCH'])
def update_recipe(id):
    try:
        recipe = Recipe.query.get(id)
        if not recipe:
            res = {"message": "Recipe not found"}
            return jsonify(res), 404

        data = request.get_json()

        # Update each recipe attributes if need
        if 'title' in data:
            recipe.title = data['title']
        if 'making_time' in data:
            recipe.making_time = data['making_time']
        if 'serves' in data:
            recipe.serves = data['serves']
        if 'ingredients' in data:
            recipe.ingredients = data['ingredients']
        if 'cost' in data:
            recipe.cost = data['cost']
        
        # Update the 'updated_at' field
        recipe.updated_at = datetime.now(timezone.utc)

        db.session.commit()

        updated_recipe = [{
            "id": recipe.id,
            "title": recipe.title,
            "making_time": recipe.making_time,
            "serves": recipe.serves,
            "ingredients": recipe.ingredients,
            "cost": recipe.cost,
            "created_at": recipe.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": recipe.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }]

        res = {
            "message": "Recipe successfully updated!",
            "recipe": updated_recipe
        }
        return jsonify(res), 200

    except Exception as e:
        res = {"message": "An error occurred while updating the recipe", "error": str(e)}
        return jsonify(res), 500

@application.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    try:
        recipe = Recipe.query.get(id)
        if not recipe:
            res = {"message": "No recipe found"}
            return jsonify(res), 200

        # Delete recipe from the database
        db.session.delete(recipe)
        db.session.commit()

        res = {"message": "Recipe successfully removed!"}
        return jsonify(res), 200

    except Exception as e:
        res = {"message": "An error occurred while deleting the recipe", "error": str(e)}
        return jsonify(res), 500
    
@application.route('/home', methods=['POST', 'GET'])
def recipes_index():
    if request.method == 'POST':
        data = request.get_json()

        required_fields = ['title', 'making_time', 'serves', 'ingredients', 'cost']
        
        if not data or not all(field in data for field in required_fields):
            res = {
                "message": "Recipe creation failed!",
                "required": "title, making_time, serves, ingredients, cost"
            }
            return jsonify(res), 200
            render_template('index.html', recipes = recipes)
        
        # create new recipe and save to db
        try:
            new_recipe = Recipe(
                title=data['title'],
                making_time=data['making_time'],
                serves=data['serves'],
                ingredients=data['ingredients'],
                cost=data['cost'],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
            db.session.add(new_recipe)
            db.session.commit()

            res = {
                "message": "Recipe successfully created!",
                "recipe": [{
                    "id": new_recipe.id,
                    "title": new_recipe.title,
                    "making_time": new_recipe.making_time,
                    "serves": new_recipe.serves,
                    "ingredients": new_recipe.ingredients,
                    "cost": new_recipe.cost,
                    "created_at": new_recipe.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": new_recipe.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                }]
            }

            return jsonify(res), 200
        except Exception as e:
            res = {"message": "Recipe creation failed!", "error": str(e)}
            return jsonify(res), 404
    else:
        recipes = Recipe.query.order_by(Recipe.created_at).all()
        recipes_list = [{
            "id": recipe.id,
            "title": recipe.title,
            "making_time": recipe.making_time,
            "serves": recipe.serves,
            "ingredients": recipe.ingredients,
            "cost": recipe.cost
        } for recipe in recipes]

        res = {"recipes": recipes_list}
        return jsonify(res), 200
    
# @application.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         title = request.form['title']
#         making_time = request.form['making_time']
#         serves = request.form['serves']
#         ingredients = request.form['ingredients']
#         cost = request.form['cost']

#         new_recipe = Recipe(title=title, making_time=making_time, serves=serves, ingredients=ingredients, cost=cost)

#         try:
#             db.session.add(new_recipe)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an error when save data...'

#     else:
#         recipes = Recipe.query.order_by(Recipe.created_at).all()
#         return render_template('index.html', recipes = recipes)
    
@application.route('/delete/<int:id>')
def delete(id):
    recipe_to_delete = Recipe.query.get_or_404(id)

    try:
        db.session.delete(recipe_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that recipe'
    
@application.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    recipe_to_update = Recipe.query.get_or_404(id)

    if request.method == 'POST':
        recipe_to_update.title = request.form['title']
        recipe_to_update.making_time = request.form['making_time']
        recipe_to_update.serves = request.form['serves']
        recipe_to_update.ingredients = request.form['ingredients']
        recipe_to_update.cost = request.form['cost']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem updating your recipe'
    else:
        return render_template('update.html', recipe=recipe_to_update)


if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8080)