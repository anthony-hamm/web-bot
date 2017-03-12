# HammCam Web-bot

Welcome to the HammCam Web-Bot, this would a really fun experience since this **Web-bot** is able to perform the following actions:

- Create an **User** whose password will be stores as a hash code
- Learn **Python Code** that will be sent as in a parsed JSON
- Return the **Weather** and a whole set of characteristics of a coutry or city
- Perform the four basic mathematical operations


## Map of the Routes in the applicacion
- / - **Main** - Default route of the application
- /**showSignUp** - Route that renders the **showSignUp** UI
- /**showUsers** - Router where the user can consult all the users registered users in the DataBase
- /**learnAction** - Route where the user sends the Python Code
- /**ShowActions** - Route where the user can consult all the actions learned that are into the DataBase
- /**showLogs** - Route where the user consult all who, when and the action performed
- /**deleteAllActions** - Route where the user can deletes all the actions learned that are in the DataBase
- /**learnMath** - Router where the user send the 4 basic mathematical operation
- /**showResults** - Route where the user can **Send** and see the **Results** from the 4 basic mathematical operations
- /**country_api** - Route where the user sends the country and or city, to verify the following information:
	- Temperature
	- Map Position
	- Weather
	- Wind Speed
	- Cloud Percentaje

## How to Create an user

User can access the page from the **Main** by clicking the **Sign up today** button under the **HammCam Web-bot** or by clicking the **Sign Up** option of the nav bar to be forwarded to:

### /**showSignUp**

In the new page the user must fill the fields:
* Name
* Email Address
* Password

An then click the **Sign Up** button

**NOTE:** At this point after clicking the button the user is not seeing any action being performed unless the developer console open

## How to Consult the users created at the Database

Via Postman or any other REST client the user can consult the users created at the DataBase using the route

### /**showUsers**

###Example:

[[https://github.com/anthony-hamm/web-bot/images/showusers.png|alt=showusers]]








