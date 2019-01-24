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

@app.route('/')
@app.route('/testauthor', methods=['POST','GET'])
def test_author():
    nestingCollection =  mongo.db.nesting
    return render_template('my_recipes.html')
    
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