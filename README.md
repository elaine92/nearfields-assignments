# Nearfields Instruments - Assignments
The repository contains 2 assignments

## Assignment - 01
assignment-01 contains the Test Plan and the Test specification for a Home security embedded system.

The additional referencing files are added in the reference folder within assignment-01.

Please note the Test Specification contains only 10 critical test scenarios. The scope had to be limited due to the time limitations.


## Assignment - 02
Assignment 2: Measuring the robot's work area coverage

### Project Structure
The project consists of 3 folders, single runner class, and the requirements.txt file

<img width="262" alt="image" src="https://user-images.githubusercontent.com/107974358/182582959-6a9edd28-b076-4eb9-a484-572f5ba093ac.png">

**1. data:** The folder contains all the input, output data, and the test results are exported back to the same

<img width="156" alt="image" src="https://user-images.githubusercontent.com/107974358/182584142-75cbbc93-18e5-430a-9b46-427efd5fe3a0.png">

**2. test:** The folder can be used to manage all the test classes, and currently it contains the test class for work area test

**3. util:** The folder can be used to manage all the util methods and classes, and currently it contains the util class for file operations

**4. main.py:** The file will be the runner class for this project

**5. requirements.txt:** Contains all the packages and their corresponding versions to install before executing the test

### Set up Project & Test Execution
<ul>
  <li>Step 1: Clone the project</li>
  <li>Step 2: Navigate to the project through terminal & activate the virtual env (MacOS --> source venv/bin/activate)</li>
  <li>Step 3: Install requirements.txt (Command --> pip3 install -r requirements.txt)</li>
  <li>Step 4: Execute the test (Command --> python3 main.py)</li>
</ul>

### Assumptions
<ul>
  <li>Eventhough robot has covered expected points from the input file, if these points are out of the rectangle area , those points are considered as invalid points. Based on the assignment robot is suppose to cover the points only within the rectangle area</li>
</ul>
