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
    
# fix

@app.route('/edit_recipe/<item_id>')
def edit_recipe(item_id):
    the_recipe =  mongo.db.nesting.find_one({"_id": ObjectId(item_id)})
    #all_categories =  mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.nesting
    arrayValues = []
    if request.method == "POST":
        form_one=request.form.to_dict()
        print(form_one)
        for k, v in form_one.items():
            if k not in ('author_name','author_dob','recipe_name','recipe_description','cuisine_name','serves','cooking_time', 'ingredients','method'):
            #if k != 'task_name' and k != 'task_description' and  k != 'radio':
                arrayValues.append(v)
        
        name = request.form.get('author_name')
        dob = request.form.get('author_dob')
        nrecipe = request.form.get('recipe_name')
        description = request.form.get('recipe_description')
        cuisine = request.form.get('cuisine_name')
        serves = int(request.form.get('serves'))
        ctime = int(request.form.get('cooking_time'))
        ingredients = request.form.get('ingredients')
        method = request.form.get('method')
        
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'author': name,
        'dob': dob,
        'recipe_name': nrecipe,
        'description': description,
        'cuisine': cuisine,
        'serves': serves,
        'time': ctime,
        'ingredients': ingredients,
        'method': method,
        'allergens': arrayValues
    })
    return redirect(url_for('test_aller'))
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)