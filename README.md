**USER MANUAL**

**MINING_PORT- A WEB APPLICATION USED TO DETECT DRIFT AND CLASSIFY DATASET**

	
_**Installation Process**_
1. Download the Code folder from [here](https://drive.google.com/drive/folders/17T6AFhPrAt_8PGyWBrneISJrU2L9o1bl?usp=sharing) or clone this github repository.
1. Make sure that python is installed on the system and the path is specified. In order to verify this, open the terminal and type the command python --version. The version of the python will be displayed if it is installed and the path is set. Otherwise install python. 
1. Open a terminal window in the project directory, and type the command: pip install -r requirements.txt ( This will install all the required python libraries specified in the requirements.txt file ).  If there is some error in installing python libraries then you can use the Anaconda navigator desktop software. Install and open the anaconda software and then open VS Code Editor through that (this will give VS Code access to all the essential python libraries).
1. Now open the project folder in an editor. Eg: VS Code
1. Install Node.js and NPM and check through a terminal if it's installed properly. You can use this guide: Link.
1. In the editor (VS Code) open the project folder then open a terminal and type the command npm i to to install the required node modules.
1. Next, type the command node app.js to start the project.
1. The project will be served on localhost port 3000 (Open http://localhost:3000/ in any browser).


_**How to use the software**_
1. Register yourself to access the detect drift and classify dataset use cases. You can also log in using already registered users ids like Username : demo, Password : demo. 
(The email id you enter during registration will receive the final results of the project on execution).
1. In either of the use cases, upload the dataset which is already contained in the project folder named Datasets.
1. For detecting drift: 
	1. Click on detect drift button
	1. Now upload the dataset from the Datasets folder.
	1. Enter the window length (Eg. 100,500,1000)
	1. Click on detect drift button
1. For classification: 
	1. Click on classify dataset button
	1. Now upload the dataset from the Datasets folder
	1. Click on the classify dataset button.
1. To use other functionalities(About and FAQ), simply click on the About/FAQ button in the navbar. 



