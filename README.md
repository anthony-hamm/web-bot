# HammCam Web-bot

Welcome to the HammCam Web-Bot, this would a really fun experience since this **Web-bot** is able to perform the following actions:

- Create an **User** whose password will be stores as a hash code
- Learn **Python Code** that will be sent as in a parsed JSON
- Return the **Weather** and a whole set of characteristics of a coutry or city
- Perform the four basic mathematical operations


## Map of the Routes in the applicacion
- /**Main** - Default route of the application
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

Via Postman or any other REST client with a GET method the user can consult the users created at the DataBase using the route

### /**showUsers**

###Example:

![ShowUsers](https://cloud.githubusercontent.com/assets/8117872/23837385/ec388c58-074c-11e7-8c0c-5a001294d1ce.png)

In Order to see in a better way the results you can use a JSON formater or check the records in the DataBase


![ShowUsersJSON](https://cloud.githubusercontent.com/assets/8117872/23837831/f6087c28-0753-11e7-8b5f-8b2fdc8ee4c4.png)

![ShowUsersDB](https://cloud.githubusercontent.com/assets/8117872/23837837/030482e6-0754-11e7-9b27-502585cb84f1.png)

**NOTE:** In the previous images in the field password you can notice the password using hash


## How to Learn an action via JSON

Via Postman or any other REST client with a POST method teach the Web-Bot Python Code using an specific format in a JSON file

### /**learnAction**

### Code
```
{
  "code": "def HelloWorld():\n  print(\"hello world print\")\n  return \"final de hello world\"\n\n",
  "name": "Hello World",
  "description": "This function shoul display a Hello World message",
  "callback": "HelloWorld()"
}
```
### REST Client Example

![ActionLearRestClient](https://cloud.githubusercontent.com/assets/8117872/23837912/660f818c-0755-11e7-8c0f-7a417e1b265f.png)

## How to Consult the Actions learned at the Database

Via Postman or any other REST client with a GET method the user can consult the users created at the DataBase using the route

### /**ShowActions**

###Example:
![ShowActionsRESTClient](https://cloud.githubusercontent.com/assets/8117872/23838021/9f8e0ac2-0756-11e7-9e97-1336778f4c2c.png)

In Order to see in a better way the results you can use a JSON formater or check the records in the DataBase

![ShowActionsDB](https://cloud.githubusercontent.com/assets/8117872/23837994/5110fb70-0756-11e7-8a0d-028145e0ce5f.png)

![ShowActionsDB](https://cloud.githubusercontent.com/assets/8117872/23837917/72f37886-0755-11e7-87e4-9e575dcda2fb.png)

## How to Consult Logs in the Data

Via Postman or any other REST client with a GET method the user can consult the logs created at the DataBase using the route

### /**showLogs**

###Example:
![showlogs](https://cloud.githubusercontent.com/assets/8117872/23838545/9ae223f4-075c-11e7-9394-71e413269283.png)

In Order to see in a better way the results you can use a JSON formater or check the records in the DataBase

![showlogsJSON](https://cloud.githubusercontent.com/assets/8117872/23838559/b185c61a-075c-11e7-85ec-d33e31b70f43.png)

![showlogsDB](https://cloud.githubusercontent.com/assets/8117872/23838583/c2cbb5ce-075c-11e7-9f70-aecf48917ded.png)

**NOTE**: Be carefull we are saving the IP's so we can find you

###How to Delete all the actions Learned
Via Postman or any other REST client with a DELETE method the user can consult delete all the actions previously learned

###/**deleteAllActions**

#### Example
![Deletememory](https://cloud.githubusercontent.com/assets/8117872/23838108/86b4ccce-0757-11e7-9b45-d73e4a1b0704.png)

**NOTE**: You got to be really carefull with this because this will delete all the actions in the database that were previousylerned

##How to load the four Basic Math Methods
Via Postman or any other REST client with a GET method teach the Web-Bot the four basic math methods that will generated and learned in background

###/**learnMath**

###Example
![learnMath](https://cloud.githubusercontent.com/assets/8117872/23838416/13ac0b08-075b-11e7-9b0e-0ed40f8052ec.png)

##How to execute and consult the results of the four Basic Math Methods

Via Postman or any other REST client with a POST all the user got to do is to send two different numbers and all the calculation will be done by the Web-bot and then it will return the results

### Code
```
{
	"param1":25,
	"param2":10
}
```

###Examples
![showMath](https://cloud.githubusercontent.com/assets/8117872/23838435/43541a4e-075b-11e7-9e83-907ca78f1a25.png)

##How to consult the country/state information using the Web-Bot with a third party API

This Web-bot is also connected to a thir party API called [openweathermap](https://openweathermap.org/), all you got to do is to register and then go to the [API documentation](https://openweathermap.org/current) to create and connect with your own bot.

Our implementation requires the name to be send as a paramter in a JSON and then the web-bot goes to the openweathermap API and retrieve the information of the country or state sent.

###Code sent in REST Client
```
{
	"country":"Costa Rica"
}
```
###Code returned by the openweather API
```
{
  "base": "stations",
  "clouds": {
    "all": 64
  },
  "cod": 200,
  "coord": {
    "lat": -23.42,
    "lon": -54.65
  },
  "dt": 1489367951,
  "id": 3465303,
  "main": {
    "grnd_level": 988.36,
    "humidity": 92,
    "pressure": 988.36,
    "sea_level": 1025.86,
    "temp": 295.554,
    "temp_max": 295.554,
    "temp_min": 295.554
  },
  "name": "Costa Rica",
  "rain": {
    "3h": 4.715
  },
  "sys": {
    "country": "BR",
    "message": 0.1592,
    "sunrise": 1489397975,
    "sunset": 1489442155
  },
  "weather": [
    {
      "description": "moderate rain",
      "icon": "10n",
      "id": 501,
      "main": "Rain"
    }
  ],
  "wind": {
    "deg": 168.003,
    "speed": 5.57
  }
}
```

###Examples
![weather](https://cloud.githubusercontent.com/assets/8117872/23838457/86be5e2a-075b-11e7-9739-b3a7110d65b0.png)

##Developers:
* [Anthony Hamm](https://github.com/anthony-hamm)
* [Camilo Martinez](https://github.com/marticam)








