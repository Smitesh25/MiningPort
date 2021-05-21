USER MANUAL

MINING_PORT- A WEB APPLICATION USED TO DETECT DRIFT AND CLASSIFY DATASET

	
Installation Process
Make sure that python is installed on the system and the path is specified. In order to verify this, open the terminal and type the command python --version. The version of the python will be displayed if it is installed and the path is set. Otherwise install python. 
Open a terminal window in the project directory, and type the command: pip install -r requirements.txt ( This will install all the required python libraries specified in the requirements.txt file ).  If there is some error in installing python libraries then you can use the Anaconda navigator desktop software. Install and open the anaconda software and then open VS Code Editor through that (this will give VS Code access to all the essential python libraries).
Now open the project folder in an editor. Eg: VS Code
Install Node.js and NPM and check through a terminal if it's installed properly. You can use this guide: Link.
In the editor (VS Code) open the project folder then open a terminal and type the command npm i to to install the required node modules.
Next, type the command node app.js to start the project.
The project will be served on localhost port 3000 (Open http://localhost:3000/ in any browser).


How to use the software
 Register yourself to access the detect drift and classify dataset use cases. You can also log in using already registered users ids like Username : demo, Password : demo. 
(The email id you enter during registration will receive the final results of the project on execution).
In either of the use cases, upload the dataset which is already contained in the project folder named Datasets.
For detecting drift: i.Click on detect drift button
                              ii. Now upload the dataset from the Datasets folder.
                              iii. Enter the window length (Eg. 100,500,1000)
                              iv. Click on detect drift button
For classification: i. Click on classify dataset button
                                         ii. Now upload the dataset from the Datasets folder
                                        iii. Click on the classify dataset button.
To use other functionalities(About and FAQ), simply click on the About/FAQ button in the navbar. 



