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
@app.route('/')
def formfill():
    return render_template('testform.html')
# @app.route('/insert_recipe', methods=['POST','GET'])
# def insert_recipe():
#     recipe =  mongo.db.nesting
#     form = request.form.to_dict()
#     recipe.insert_one(form)
#     return redirect(url_for('test_aller'))

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe =  mongo.db.nesting
    arrayValues = []
    if request.method == "POST":
        form_one=request.form.to_dict()
        # for k, v in form_one.items():
        #     arrayValues.append(v)
        print(arrayValues)
        tname= request.form['task_name']
        tdescr= request.form['task_description']
        tradio= request.form['radio']
        # tmilk= request.form['milk1']
        # tcelery= request.form['celery1']
        # tmollucs= request.form['mollucs1']
        # tnuts= request.form['nuts1']
        # tsulf= request.form['sulfites1']
        form = {
            'task_name': tname,
            'task_description': tdescr,
            'radio': tradio,
            'allergens': arrayValues
                }
        recipe.insert_one(form)
        
        #print(form_one)
    return redirect(url_for('test_aller'))
    
@app.route('/test_aller')
def test_aller():
    return render_template('allergens.html')


# @app.route('/test_form')
# def test_form():
#     return render_template("testform.html", 
#     recipes=mongo.db.recipesColl.find())
    
# @app.route('/update_form', methods=["POST"])
# def update_recipe():
#     recipes=mongo.db.test_form
#     recipes.update_one({
#         'task_name':request.form.get['task_name'],
#         'category_name':request.form.get['category_name'],
#         'task_description': request.form.get['task_description'],
#         'due_date': request.form.get['due_date'],
#         'is_urgent':request.form.get['is_urgent'],
#         'boolean':request.form.get['boolean'],
#         'allergens': [request.form.get['milk'],request.form.get['celery'],request.form.get['nuts'],request.form.get['sulfites']]
#     }, upsert = True)
#     return render_template("testform.html")

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)