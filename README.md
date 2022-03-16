               Telegram Locator
Python script that creates a precise map of people around you.

Features:
Collects data using people nearby telegram feature
Trilaterates the exact position of each person
Renders all the results on map.html
Example:
example.jpg

Usage:
Install dependencies:
python -m pip install -r ./requirements.txt
Run script:
python ./locate.py --number NUMBER --latitude LATITUDE --longitude LONGITUDE [--offset OFFSET] [--help]
Authenticate (if prompted):
Code: 
Password: 
Arguments:
Long	Short	Description
--help	-h	Show help message
--number NUMBER	-n NUMBER	Telephone number (aka Telegram login)
--latitude LATITUDE	-la LATITUDE	Latitude of your starting location
--longitude LONGITUDE	-lo LONGITUDE	Longitude of your starting location
--offset OFFSET	-o OFFSET	Trilateration scanning offset in degrees (default: 0.0007)
Third-party libraries:
Telethon - Pure Python 3 MTProto API Telegram client library.
gmplot - A matplotlib-like interface to render all the data you'd like on top of Google Maps.                                            
 youtube https://www.youtube.com/channel/UC2tQEkquHAakyIv1Z7b-lDQ                                                                          
 Telegram https://t.me/fuckyou506
