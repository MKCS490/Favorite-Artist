# Project 1

To use this repository, you must follow these steps: 
0. Sign up for a twitter developer account [https://developer.spotify.com/documentation/web-api/quick-start
1. Make a new app
2. Access your token keys/secret/API keys which you will use in your code 
3. Create spotify.env file you are doing this so you dont put your secret keys in your python file for the whole world to see. paste the following in your .env file and fill in with secret keys. CLIENT_ID='' " CLIENT_SECRET='' "
4. In your python file you will import os and will set the env variables to os.environ["CLIENT_ID"] and the same for secret
5. import flask in your python file. Flask will help us build the web application. to initialize flask @app.route('/') def index(): put code here
6. in the return statement pass the html file, and all the variables you will be using in the html file. example return flask.render_template( "index.html", current_Artist= currentArtist)
7. import random. I used random to pick a random artist to display on the page. I then set the random artist to the variable currentArtist.
8. At the end of the program we want to run the web app. We do so with the following command app.run( port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'), debug=True )
9. Now we open to the HTML file in the template folder, index.html
10. In the header we link the style.css
11. In the body we display the variables which we passed the render template we have to use a certain syntax for that for example: h1 {{ current_Artist }} h1
12. Link the css file in the html header
13. I went to google fonts and imported a font from there called 'Fredoka One"
14. I downloaded a background from the internet by using the wget command in my static folder.
15. I edited my h1, h2,h3,h4 tags and adding certain padding values to make them appear where I wanted them to appear.


# Installation 
1. Install flask sudo pipe3 install flask
2. Install python dotenv or sudo pipe3 install python-dotenv
3. Install python requests

## Technical Issues

1. I was having trouble getting the variables to be displayed in HTML. After doing some debugging, I found out it was because I was passing the wrong variables.
2. I was having trouble display texts in certain places in CSS. I solved that by looking at different values for paddings, sizes and widths.
3. I had an issue where I would get a broken song preview and image URL from the response. The issue was that the value returned was a string with "" so I used .strip python function and that fixed my issue.
