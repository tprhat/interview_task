# Interview task solutions

To run the tasks in this repository, you should clone the repository first.
It includes all the source code and files needed to run the tasks.

Cloning the repository:
```
git clone https://github.com/tprhat/interview_task.git
```

Now your base directory should include the `interview_task` directory.

Let's go to the `interview_task` directory:
```
cd interview_task
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
Both task 2 and task 3 use the same requirements.txt file. 
I created a virtual environment and installed the required packages using the following commands:
```
python -m venv <your-env-name>
<your-env-name>\Scripts\activate.bat
pip install -r requirements.txt
```
<i>The code above works for Windows.</i>

To run the code:
```
cd task2 or task3
python app.py
```

Both tasks endpoints are available at the base URL: http://localhost:5000.
I used Postman to test the endpoints, but you can use any tool you prefer.

## Task 2
I solved the second task by creating a Flask application with a single POST endpoint that takes data formatted as the example in the task description. 
The endpoint returns all the unauthorized sales. 

Data example:
```json
{
        "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
        "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}
```

The unauthorized sales include all the sales that not in the productListings or when sellerID is not in the authorizedSellers dictionary.
In case of no unauthorized sales, the endpoint returns a string "No unauthorized sales".

## Task 3
The third task is similar to the second task. 
This endpoint returns the number of maximum non-overlapping interviews a person can attend.

Input data example:
```json
{
  "start_times": [10, 20, 22, 23, 25, 50, 60],
  "end_times":   [15, 25, 25, 26, 27, 55, 65]
}
```

My solution uses a greedy algorithm. 
First it sorts the zipped arrays by the end times. 
Then it iterates through the sorted array and checks if the start time is greater or equal than the previous end time. 
If it is, the counter is incremented.
The complexity of the algorithm is O(nlogn) because of the sorting.