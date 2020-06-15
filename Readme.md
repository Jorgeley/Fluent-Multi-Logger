## Fluent Multi Log
This is a multi log fluent classes project, the main idea is to have different logs files, formats etc.

The main Log class has all the main methods, the AnotherLog and AnotherOneLog extend it and have their own format and configuration.

It can be extended to implement more functionalities.

###Installation 
* Clone this repository and cd into it
* Install dependencies:
    * `pip3 install -r requirements.txt`
* Add the path project to Python path:
    * `pip3 install -e .`

\* ***you can also use pipenv if you want***.

###Run
Before running it, create log directories manually (if not already created):
* `mkdir ./logs`

* Also, give permission to whoever is running the app:
    * `chown youruser:yourgroup ./logs`
    * `chmod 775 ./logs`

to run the app just do (considering you're into main folder):

`python3 main.py`

####Author
>jorgeley@gmail.com