# ZoneMinder-Scripts
ZoneMinder Scripts


Zoneminder Darknet yolov2 tiny Hack
Post by operat0r » Fri Jan 19, 2018 9:24 am

UPDATE 8:55 PM 4/18/2018: I gave up on trying to figure out syslog/logrotate and just running tail -F --retry on the normal /var/log/zm/* path...my script would stop working every time the log file rotated. I could never figure out why my logs stopped going to my external mount and I still have not sorted out way to log the system service I setup for the script

UPDATE 01/19/2018: 38% BOAT! Got it working using syslog and just pulling the event ID it bails on the first match person|cat|dog|car

Video:
https://www.flickr.com/photos/freeload101/38899662735

Crazy TODO'S :

* use alarm frames for input only and not entire event? zmtrigger.pl ? API ?
* have it send alerted event ID, alerted frame image (predictions.png) , object(s) detected to email etc
* sort out darknet and make it faster /better
* face detection
* automated face training ?!
* automated car training ?!
* licence plate logging
* match cars/faces
* count trained objects over time create logs/graphs ( IE alert when mail person potentially changes )

Output from the service script:
![enter image description here](https://github.com/freeload101/ZoneMinder-Scripts/blob/master/ZM1.png?raw=true)
Gmail tag for alerts deliverd:
![enter image description here](https://github.com/freeload101/ZoneMinder-Scripts/blob/master/ZM2.png?raw=true)
