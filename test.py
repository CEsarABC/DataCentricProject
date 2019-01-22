import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb://recipes:Mongo3@ds021026.mlab.com:21026/recipes'

mongo = PyMongo(app)


# def get_record():
#     allergens=mongo.db.allergensColl
#     print("")
    
#     try:
#         document = allergens.find_one()
#     except:
#         print("Error accessing the database")
    
#     if not document:
#         print("")
#         print("Error! No results found.")
    
#     return document
    
# def find_record():
#     doc = get_record()
#     if doc:
#         print("")
#         for k, v in doc.items():
#             if k != "_id":
#                 return(v)
                
# find_record()

# superlist = find_record()

# for item in superlist:
#     print(item)



''' Brings all the tasks to the main page '''

# @app.route('/get_recipe')
# def get_tasks():
#     return render_template("test.html", 
#     recipes=mongo.db.recipesColl.find())
    
   
# @app.route('/get_allergen')
# def get_allergens():
#     return render_template("allergens.html", superlist=superlist,
#     allergens=mongo.db.allergensColl.find(),allergensList=mongo.db.allergensColl.find({'allergens':'milk'},{'allergens':1, '_id':0}))

''' inserts one dictionary when the form in addtask.html is submited '''
#@app.route('/')
def formfill():
    return render_template('testform.html')



''' testing author with form, we send author name and dob, the system creates
a new search with those two values and gets the document'''
#@app.route('/')
def myrecipes():
    return render_template('myrecipes.html')
    
@app.route('/testauthor')
def test_author():
    return render_template('testsAuthor.html')
    
@app.route('/')
@app.route('/authors', methods=['POST','GET'])
def check_author():
    recipe =  mongo.db.nesting
    authorCollection =  mongo.db.authors
    keysDict = []
    if request.method == "POST":
        authorform=request.form.to_dict()
        print(authorform)
        # items = authorform.items()
        # print(items)
        ggg = authorform.get('author')
        kkk = authorform.get('dob')
        searchfile = authorCollection.find_one({'author':ggg, 'dob':kkk})
        print(searchfile)
        print(authorform.get('author'))
        return redirect(url_for('test_author'))
        
    return render_template('myrecipes.html', searchfile=searchfile)


''' working now saving eveything to data base and arrayValues
    of allergens working perfectly, filtering other values from dictionary '''


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
        name = request.form['author_name']
        dob = request.form['author_dob']
        nrecipe = request.form['recipe_name']
        description = request.form['recipe_description']
        cuisine = request.form['cuisine_name']
        serves = int(request.form['serves'])
        ctime = int(request.form['cooking_time'])
        ingredients = request.form['ingredients']
        method = request.form['method']
        
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
            'allergens': arrayValues
                }
        recipe.insert_one(form)
        
        authorForm = {
            'author': name,
            'dob': dob,
            'recipe_name': [{'name': nrecipe}]
        }
        authorCollection.insert_one(authorForm)
        
        #print(form_one)
    return redirect(url_for('test_aller'))
    
@app.route('/test_aller')
def test_aller():
    return render_template('allergens.html')



    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)