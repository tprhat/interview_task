# Interview task solutions

To run the tasks in this repository, you should clone the repository first.
It includes all the source code and files needed to run the tasks.

Cloning the repository:
```
git clone https://github.com/tprhat/interview_task.git
```

In this readme, I will go over the concept of my solutions and how to run them.
The code is well documented, so you can find more details in the source code.

## Task 1
I solved the first task using the OpenLayers library and Vite. 
The solution creates a map using OpenStreetMap as a base layer and adds the polygon to the map.

To run the code:
```
cd task1
npm install
npm start
```
After using the `npm start` command, the development server will start, and the map will be available at http://localhost:5173.


## Tasks 2 & 3 setup
Both task 2 and task 3 use the same requirements.txt file. I created a virtual environment and installed the required packages using the following commands:
```
python -m venv venv
source venv/bin/activate.bat
pip install -r requirements.txt
```
To run the code:
```
cd task2 or task3
python app.py
```

## Task 2
I solved the second task by creating a Flask application with a single POST endpoint that takes data formatted as the example in the task description. 
The endpoint returns all the unauthorized sales.