# Smart-Mirror
Raspberry powered mirror which can display the news, weather, and time.

## Installation and Updating
### Code
If you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed, clone the repository.

```
git clone git@github.com:HackerHouseYT/Smart-Mirror.git
```

**Alternatively, you can download a zip file containing the project (green button on the repository page)**

Navigate to the folder for the repository

```
cd Smart-Mirror
```

### Install your dependencies 
make sure you have [pip](https://pip.pypa.io/en/stable/installing/) installed before doing this

```
sudo pip install -r requirements.txt
```

```
sudo apt-get install python-imaging-tk
```
```
pip install bs4
```

### Add your weather-underground url
Go to https://www.wunderground.com  
search for your location  
copy the url and paste it into line 27 of smartmirror.py

```
weather_url = "https://www.wunderground.com/...." ############# put weather underground url here ###################
```
the url should look like this
```[
weather_url = "https://www.wunderground.com/weather/us/il/chicago"
```


## Running
To run the application run the following command in this folder

```
python smartmirror.py
```

## Demo and Build Instructions 
(click image for link to video)
[![Link to youtube how-to video](http://i.imgur.com/cMyaSHT.png)](https://youtu.be/fkVBAcvbrjU)
