# Data Centric Development Milestone Project

The project is focused in the use of data bases as the use of python and flask to put all together.

My cooking book concept, is a space where users can check, create or edit their own recipes, with a simple, yet balanced
desing, the user experience is clean and the navigation through pages creates a space where you can come and go as you please,
never limitating the user.

This project delivers by using the mongo data base, which is flexible and intuitive. 


## Application guidelines
  - [x] MongoDB to hold a data base based on cooking recipes
  - [x] User is presented to a web page inviting to see create or edit recipes
  - [x] User can create, edit and delete recipes created by him
  - [x] User has a simple verification method to access his/her own recipes
  - [x] The page flow is intuitive and lets the user navigate to any place at any moment
  - [x] The web development has sections which allow for the distrubution of information
  - [x] A graph shows users the amount of authors and recipes in the site
  - [x] 

## Project guidelines
  - [x] Logic written in python. other technologies used
  - [x] Semantic HTML
  - [x] The website must be data-driven (MongoDB)
  - [x] Use Flask, a micro-framework, to run your application
  - [x] Instructions to deploy (see deployment)
  - [x] Share details of how you created your database schema in your README.
  - [x] Make sure the site is responsive
  - [x] User stories, wireframes
  - [x] CSS and Bootstrap frameworks used
  - [x] README.md file made
  - [x] GitHub version control used during development
  - [x] Final version of the code deployed in Heroku



## Technologies used

- HTML
- CSS
- Bootstrap 4.0
- Python 3.6
- JavaScript
- Charts.js
- Flask
- Cloud9
- mLab MongoDB
- Adobe Illustrator
- Abobe Photoshop


## Basic project tree

  - cooking-recipes
      - static
        - css
        - images
        - js
      - templates
      - Wireframes


  - app.py **(main application)**
  

## UX
- This development presents th content to the users and let them chose what path they want to take.
- The information in simple and clean manner
- the introduction invites the users to interact and find wht they are looking for.
- 


## Features
- User can navegate in any section of the site 
- User can see all recipes in the data base
- User can search by author name, cuisine or search by filtering an allergen
- User is able to add recipes, important fields are required in the form
- User validation for editing or deleting recipes
- User is able to retrieve all his/her recipes for edition or deletion
- User can see how many recipes all users have

### Left to Implement
Bringing this project to life took some time and some ideas where left on the side just because of time
- [ ] A better and more complete search section
- [ ] giving the user option to upload their own pictures
- [ ] adding more grahps to display more information on the database
- [ ] more visually appealing design 
- [ ] pagination for extensive results

## Testing





## Deployment
- Project fully deployed to Heroku  https://practical-project.herokuapp.com/
  - The project was deployed following the guidelines from the code academy materials
  - Working in virtual environment
  - New project was created in Heroku
  - requirements.txt was created
  - Procfile was created
  - Heroku remote was set in order to push application
  - Configuration variables were changed as indicated to have 'IP' = (0.0.0.0) and 'PORT' = (5000)


- To run this code locally I have some lines of code, one to use in cloud9 and one to use in any other IDE like Atom which I used when not connected to the internet

- The last Python version enabled for cloud9 was installed **Python-3.6.2** in order to create the virtual environment based on it. Code taken from https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

- My project in cloud9 had the pip module updated to the last version and the module **virtualenv** installed to manage my environment
- After the environment was created based on python3.6 flask was installed

- Requirements.txt
    - Click==7.0
    - Flask==1.0.2
    - itsdangerous==1.1.0
    - Jinja2==2.10
    - MarkupSafe==1.1.0
    - Werkzeug==0.14.1

**Running locally - in the terminal**
- To run this application outside the virtual environment `$ python3 app.py`
- To activate the virtual environment `$ source env/bin/activate`
- To run this application inside the virtual environment `$ python app.py`

## Credits

- Some samples where taken from http://flask.pocoo.org/docs/0.12/testing/ for testing flask sessions
- This module was complemented through a couple of courses from **Udemy**
  - Automated software testing with python
  - Python and Flask bootcamp
- Victor Miclovich **(Mentor)**

## Media
- Fonts taken from google fonts
- No other external media used

## Acknowledgments
Thank you to the code institute for the support. This last project has been challenging and took me some time to develop. I have learned a lot and I hope to keep learning to become the professional I want to be.
Thank you to the slack channels for the support and the code academy tutors which always had answers to help me move forward.

Merry Christmas and happy New Year friends.

https://unsplash.com/search/photos/food

https://getbootstrap.com/

https://dc-js.github.io/dc.js/

https://docs.mongodb.com/manual/reference/method/js-cursor/

<a href="https://www.freepik.com/free-photos-vectors/food">Food vector created by bimbimkha - www.freepik.com</a>