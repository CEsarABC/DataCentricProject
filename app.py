import os
from flask import Flask, render_template, redirect, request, url_for,session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

''' flask application set and secret key for sessions, mongoDB
is setted acording to Data base'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb://recipes:Mongo3@ds021026.mlab.com:21026/recipes'

mongo = PyMongo(app)

''' route to the first page to greed the user '''

@app.route('/')
def intro():
    transferToJS()
    return render_template('intro.html')
    
''' route to the contact page '''
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
'''brings data from the database and shows all recipes in collection '''
    
@app.route('/Recipes')
def all_recipes():
    recipes =  mongo.db.nesting
    allrecipes = recipes.find()
    return render_template('all_recipes.html', allrecipes=allrecipes)
    
    
'''  takes the data sent from the recipes page and uses the id to 
isolate one document by its id '''

@app.route('/recipe/<item_id>')
def show_recipe(item_id):
    the_recipe =  mongo.db.nesting.find_one({"_id": ObjectId(item_id)})
    cuisine =  mongo.db.cuisine.find()
    return render_template('recipe_page.html', recipe=the_recipe, cuisine=cuisine)
    
    
''' brings the page where the form is, for the new recipes
the form is linked by action to a route which handles the data after validation'''

@app.route('/new_recipe')
def formfill():
    cuisine= mongo.db.cuisine.find()
    return render_template('new_recipe.html', cuisine=cuisine)


''' insert recipe brings the data from the form and converts it into a
dictionary, where every key stores its value in a variable to be used in
the new form, which uses the schema selected '''
''' the allergens part was complex. the need to create an array with 
selected values from form was evident as multiple selection was needed.
allergens is passed as an array of strings'''
''' couple of variables are converted in order to avoid errors later on,
strings converted to intergers and is capitalized '''
''' the variable dob is used only for validation and it helps later on to
retrieve recipes in edition mode'''


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
            #Taking all allergens from the form 
                arrayValues.append(v)
        #print(arrayValues)
        name = request.form.get('author_name').capitalize()
        dob = request.form.get('author_dob')
        nrecipe = request.form.get('recipe_name')
        description = request.form.get('recipe_description')
        cuisine = request.form.get('cuisine_name')
        serves = int(request.form.get('serves'))
        ctime = int(request.form.get('cooking_time'))
        ingredients = request.form.get('ingredients')
        method = request.form.get('method')
        
        
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
            "images_small": "/static/images/dish1.jpg",
            "images_large": "/static/images/dishL1.jpg",
            'allergens': arrayValues
                }
        recipe.insert_one(form)
       
        #print(form)
    return redirect(url_for('formfill'))
    

'''  tranferToJS brings the search page, more importantly the search route,
has a elaborated code which makes two arrays, one for authors names,
another one for total recipes.
these two arrays get passed to a js document created by python,
the arrays are passed and formated to javascript in order to be referenced
later on by the graphs used from charts.js'''
''' the file.js is opened and edited by python everytime we open this page,
the information gets updated because the method w+ re-writes the previous information,
keeping the document up to date'''
    
    
def transferToJS():
    listAuthor=[]
    recipe = mongo.db.nesting
    authors = recipe.find({},{'author':1, '_id':0})
    for item in authors:
        for k,v in item.items():
            if v not in listAuthor:
                listAuthor.append(v)
                
    num = []
    recipe = mongo.db.nesting
    for item in listAuthor:
        numbers = recipe.find({'author':item}).count()
        num.append(numbers)

    f = open( 'static/js/file.js', 'w+' )
    text = f.read()
    f.write('var myDict = ' + repr(num)+'\n')
    f.write('var myarray = ' + repr(listAuthor)+'\n')
    f.close()
    cuisine =  mongo.db.cuisine.find()
    
''' search uses transferToJS function to update file.js. renders the form
for search by autor, allegen filter and cuisine'''

@app.route('/search', methods=['POST','GET'])
def search():
    transferToJS()
    cuisine =  mongo.db.cuisine.find()
    return render_template('search_recipe.html', cuisine=cuisine)
    
'''this function takes the imput from a form and replace the 
values in the query with the vales in the new dictionary created 
from the form, the new cursor is sent back to the page '''

@app.route('/my_recipes', methods=['POST','GET'])
def my_recipes():
    nestingCollection =  mongo.db.nesting
    return render_template('my_recipes.html')

''' this route search and validates the user to edit and delete his/her recipes.
by quering the author name and a variable which is only stored in the data base recipes,
we authorize the author to view the recipes and edit or delete'''
''' flask sessions used  '''

@app.route('/authors', methods=['POST','GET'])
def check_author():
    nestingCollection =  mongo.db.nesting
    nesting=request.form.to_dict()
    items = nesting.items()
    author = nesting.get('author')
    dob = nesting.get('dob')
    # session['author'] = request.form['author']
    # session['dob']= request.form['dob']
    searchfile = nestingCollection.find({'author':author.capitalize(), 'dob':dob})
    return render_template('my_recipes.html', searchfile = searchfile, authorName=author.capitalize(),author=author,dob=dob)
    
    
''' we search by input where capitalize() method is applied to match the storing form
and avoid errors '''
    
@app.route('/search_recipe_author', methods=['POST','GET'])
def search_recipe_author():
    recipes = mongo.db.nesting
    cuisine =  mongo.db.cuisine.find()
    recipe=request.form.to_dict()## why to dictionary just bring the values?????
    author = (recipe.get('author')).capitalize()

    return render_template('search_recipe.html', searchAuthor = recipes.find({'author':author}), cuisine=cuisine)
    
    
''' not equal is used to filter allergens recipes.find({'allergen':{"$ne" : allergen}}), looks into an array '''
    
@app.route('/search_recipe_allergen', methods=['POST','GET'])
def search_recipe_allergen():
    recipes = mongo.db.nesting
    cuisine =  mongo.db.cuisine.find()
    recipe=request.form.to_dict()## why to dictionary just bring the values?????
    allergen = (recipe.get('allergen')).lower()
    
    return render_template('search_recipe.html', searchAuthor = recipes.find({'allergen':{"$ne" : allergen}}), cuisine=cuisine)
    
    
''' this query looks into a collection of documents where every document is a cuisine type  '''

@app.route('/search_recipe_cuisine', methods=['POST','GET'])
def search_recipe_cuisine():
    recipes = mongo.db.nesting
    cuisine =  mongo.db.cuisine.find()
    recipe=request.form.to_dict()## why to dictionary just bring the values?????
    cuisine1 = recipe.get('cuisine')
    print(cuisine1)

    return render_template('search_recipe.html', searchAuthor = recipes.find({'cuisine':cuisine1}), cuisine=cuisine)


'''     editing recipe template is called, the id reference is passed from the previous page and 
all the information is avaliable. the information is renderend into the correspondent fields '''


@app.route('/edit_recipe/<item_id>')
def edit_recipe(item_id):
    the_recipe =  mongo.db.nesting.find_one({"_id": ObjectId(item_id)})
    cuisine =  mongo.db.cuisine.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisine=cuisine)

''' similar to new recipe the form is converted to a dictionary and all its values are
then passed to a form which follows the schema'''

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
    return redirect(url_for('my_recipes_session'))
    
    
''' takes the id from the recipe page and deletes the item '''

@app.route('/delete_recipe/<item_id>')
def delete_recipe(item_id):
    mongo.db.nesting.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('my_recipes_session'))
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)