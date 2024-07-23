from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    making_time = db.Column(db.String(100), nullable=False)
    serves = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
 
    def __repr__(self):
        return '<Recipe %r' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        making_time = request.form['making_time']
        serves = request.form['serves']
        ingredients = request.form['ingredients']
        cost = request.form['cost']

        new_recipe = Recipe(title=title, making_time=making_time, serves=serves, ingredients=ingredients, cost=cost)

        try:
            db.session.add(new_recipe)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error when save data...'

    else:
        recipes = Recipe.query.order_by(Recipe.created_at).all()
        return render_template('index.html', recipes = recipes)
    
@app.route('/delete/<int:id>')
def delete(id):
    recipe_to_delete = Recipe.query.get_or_404(id)

    try:
        db.session.delete(recipe_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that recipe'
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
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
    app.run(debug=True)