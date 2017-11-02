# Smart Mirror with Google AIY
This project originally has been forked by HackerHouseYT.
Their oiginal readme with base instructions to get the project installed can be found below.
In advance to that the project has been refined and extended:

1)
The configuration has been sorted out of the main file into a seperate config.py.

2)
There are two martmirror.py files now:

2a)
smartmirror.py - The basic Smart Mirror which shows weather, time and news.

2b)
smartmirror_aiy.py - The Smart Mirror with integrated Google AIY. This version will only work when
you have installed the Google AIY Raspian image and set up speaker and microphone.
Once started, the Smart Mirror will show the same as the base version, untill you start conversation
with the "OK, Google" keywords. Then there will be a conversation feedback shown in the middle of
the screen as well as the Google Assistant replying to your requests.


##### HacherHouseYT Readme #####

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

### Add your api token
Make sure vim is installed on your system: `sudo apt-get install vim`
Use `vim` to edit you file

```
vim smartmirror.py
```

replace `weather_api_token` with the token you got from forecast.io

## Running
To run the application run the following command in this folder

```
python smartmirror.py
```

## Demo and Build Instructions 
(click image for link to video)
[![Link to youtube how-to video](http://i.imgur.com/cMyaSHT.png)](https://youtu.be/fkVBAcvbrjU)
