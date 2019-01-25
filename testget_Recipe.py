import os
from flask import Flask, render_template, redirect, request, url_for,session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb://recipes:Mongo3@ds021026.mlab.com:21026/recipes'

mongo = PyMongo(app)



''' testing author with form, we send author name and dob, the system creates
a new search with those two values and gets the document'''

'''first page has the form which has as action the function which 
interects with the form '''

#@app.route('/')
def myrecipes():
    return render_template('my_recipes.html')

#@app.route('/')
@app.route('/my_recipes', methods=['POST','GET'])
def my_recipes():
    nestingCollection =  mongo.db.nesting
    return render_template('my_recipes.html')
    
@app.route('/')
@app.route('/search', methods=['POST','GET'])
def search():
    cuisine =  mongo.db.cuisine.find()
    return render_template('search_recipe.html', cuisine=cuisine)
    
'''this function takes the imput from a form and replace the 
values in the query with the vales in the new dictionary created 
from the form, the new cursor is sent back to the page '''
    

@app.route('/authors', methods=['POST','GET'])
def check_author():
    recipe =  mongo.db.nesting
    nestingCollection =  mongo.db.nesting
    nesting=request.form.to_dict()## why to dictionary just bring the values?????
    items = nesting.items()
    author = nesting.get('author')
    dob = nesting.get('dob')
    print(nesting.get('author'))
    return render_template('my_recipes.html', searchfile = nestingCollection.find({'author':author, 'dob':dob}), authorName=author.capitalize())
    
@app.route('/search_recipe_author', methods=['POST','GET'])
def search_recipe_author():
    recipes = mongo.db.nesting
    cuisine =  mongo.db.cuisine.find()
    recipe=request.form.to_dict()## why to dictionary just bring the values?????
    author = recipe.get('author')

    return render_template('search_recipe.html', searchAuthor = recipes.find({'author':author}), cuisine=cuisine)
    
@app.route('/search_recipe_allergen', methods=['POST','GET'])
def search_recipe_allergen():
    recipes = mongo.db.nesting
    cuisine =  mongo.db.cuisine.find()
    recipe=request.form.to_dict()## why to dictionary just bring the values?????
    allergen = recipe.get('allergen')

    return render_template('search_recipe.html', searchAuthor = recipes.find({'allergens':allergen}), cuisine=cuisine)
    
@app.route('/search_recipe_cuisine', methods=['POST','GET'])
def search_recipe_cuisine():
    recipes = mongo.db.nesting
    cuisine =  mongo.db.cuisine.find()
    recipe=request.form.to_dict()## why to dictionary just bring the values?????
    cuisine1 = recipe.get('cuisine')
    print(cuisine1)

    return render_template('search_recipe.html', searchAuthor = recipes.find({'cuisine':cuisine1}), cuisine=cuisine)


@app.route('/test_aller')
def test_aller():
    return render_template('allergens.html')
    
@app.route('/edit_recipe/<item_id>')
def edit_recipe(item_id):
    the_recipe =  mongo.db.nesting.find_one({"_id": ObjectId(item_id)})
    #all_categories =  mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)