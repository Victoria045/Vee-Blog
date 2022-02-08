# Vee-Blog

# Author 
Built by: [Victoria Beryl](https://github.com/Victoria045)

## Description
This a blog post site where the owner is able to create, update and delete blog post and the user can comment, view on the posted blogs and get subscriptions upon subscribing. 

## Screenshot
<img src="./static/photos/img1.png">

# User Story 
## As a user:
* Able to comment.
* View the most recent posts.
* Post notifications by joining a subscription.
* See random quotes. 
## As a Writer:
* Create account in the application by signing in.
* Create blog from the site.
* Delete comments that are insulting and degrading.
* Update/Delete blogs created.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the application | On application load | Display of all blogs uploaded |
| Create account by SignUp | Enter email, username and password| Redirect to login|
| Login selected | Enter username and password you signed up with| Redirect to home page|
| Comment button selected | Comment | Input comment in a form and upload |
| Click the submit button | CLick | Redirected to page wih all the comments made on the post |
| Subscription | Email address |Message output on successfully subscribing |


#### Prerequisites 
* python3.6
* pip
* Flask

#### Cloning
* Open Terminal:

        $ git clone https://github.com/Victoria045/Vee-Blog.git
        $ cd Vee-Blog
        $ code . or atom . based on your text editor 

* Install all dependencies in requirements.txt

        $ pip install -r requirements.txt

### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:

        $ chmod +x manage.py
        $ ./manage.py

### Testing the Application       
* To run unittests for the class application and check if it functions well:

        $ python3 manager.py test


## Technologies Used
* markdown

* Flask_Bootstrap3 - for bootstrap version 3

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at victoriaberyl45@gmail.com

### License 
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)]
(https://github.com/Victoria045/Vee-Blog/blob/master/LICENSE)