# scoresaber2mqtt
Publish User's Scoresaber information to MQTT
data can be used in HomeAssistant, OpenHAB or any other tool that can read MQTT topics

----

## Install
* Install Python + paho-mqtt libary: ```apt install python3-paho-mqtt``` or ```pip install paho-mqtt```
* Put the python file ```scoresaber2mqtt.py``` in ```/usr/local/bin```
* Put the config file ```/etc/scoresaber.ini``` in ```/etc```
* Edit the config as needed

## Test Run & Crontab configuration
I usually run the script manually first and check with an MQTT Tool if the metrics are updated correctly.\
This tool does the job for me: https://github.com/thomasnordquist/MQTT-Explorer

After that you need to call the script regulary to keep the metrics up to date.\
I recommend using an unpriviledged user and crontab entry for that:
```
# Get Scoresaber ranking every 5 minutes
*/5 * * * * /usr/local/bin/scoresaber2mqtt.py
```

## Configuration in HomeAssistant
coming soon
