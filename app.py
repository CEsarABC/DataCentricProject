import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb://recipes:Mongo3@ds021026.mlab.com:21026/recipes'

mongo = PyMongo(app)


@app.route('/Welcome')
def intro():
    return render_template('intro.html')
    
'''         insert recipe application                '''

''' inserts one dictionary when the form in addtask.html is submited '''
@app.route('/new_recipe')
def formfill():
    cuisine= mongo.db.cuisine.find()
    return render_template('testform.html', cuisine=cuisine)


''' working now saving eveything to data base and arrayValues
    of allergens working perfectly, filtering other values from dictionary 
    saving to two collections at the same time '''


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe =  mongo.db.nesting
    authorCollection =  mongo.db.authors
    arrayValues = []
    if request.method == "POST":
        form_one=request.form.to_dict()
        print(form_one)
        for k, v in form_one.items():
            if k not in ('author_name','author_dob','recipe_name','recipe_description','cuisine_name','serves','cooking_time', 'ingredients','method'):
            #if k != 'task_name' and k != 'task_description' and  k != 'radio':
                arrayValues.append(v)
        #print(arrayValues)
        name = request.form.get('author_name')
        dob = request.form.get('author_dob')
        nrecipe = request.form.get('recipe_name')
        description = request.form.get('recipe_description')
        cuisine = request.form.get('cuisine_name')
        serves = int(request.form.get('serves'))
        ctime = int(request.form.get('cooking_time'))
        ingredients = request.form.get('ingredients')
        method = request.form.get('method')
        
        #print(description + name)
        
        form = {
            'author': name,
            'dob': dob,
            'recipe_name': nrecipe,
            'description': description,
            'cuisine': cuisine,
            'serves': serves,
            'time': ctime,
            'ingredients': ingredients,
            'method': method,
            'views': 0,
            "images": "/static/images/dishes0.jpg",
            'allergens': arrayValues
                }
        recipe.insert_one(form)
       
        #print(form)
    return redirect(url_for('test_aller'))
    
'''         search application                 '''


@app.route('/')
@app.route('/search', methods=['POST','GET'])
def search():
    cuisine =  mongo.db.cuisine.find()
    return render_template('search_recipe.html', cuisine=cuisine)
    
'''this function takes the imput from a form and replace the 
values in the query with the vales in the new dictionary created 
from the form, the new cursor is sent back to the page '''

@app.route('/my_recipes', methods=['POST','GET'])
def my_recipes():
    nestingCollection =  mongo.db.nesting
    return render_template('my_recipes.html')


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


'''     editing recipe    '''


@app.route('/edit_recipe/<item_id>')
def edit_recipe(item_id):
    the_recipe =  mongo.db.nesting.find_one({"_id": ObjectId(item_id)})
    cuisine =  mongo.db.cuisine.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisine=cuisine)


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
    

@app.route('/test_aller')
def test_aller():
    return render_template('allergens.html')



    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)