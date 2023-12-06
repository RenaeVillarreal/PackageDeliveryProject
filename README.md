# PackageDeliveryProject
# Data Structures and Algorithms II – C950

## WGUPS Routing Program 

<p align="center">
<img src="https://imgur.com/T05kGqx.png" height="120%" width="120%" alt="Program CLI"/>
</p>

### Description

This is my project for WGU C950 Data Structures and Algorithms II class. The goal is to solve a package delivery routing problem, which is essentially the traveling salesman problem with a dedicated starting node and a few restrictions/requirements. For my solution, I implemented the nearest neighbor algorithm which operates with a time-complexity of O(n).

## Usage

To get the code run this from the command line:

```commandline
git clone https://github.com/RenaeVillarreal/PackageDeliveryProject.git
```
(Optional)Set up a Virtual Environment For Windows:
```commandline
.\venv\Scripts\activate
```
(Optional)Set up a Virtual Environment For Unix or MacOS:
```commandline
.\venv\Scripts\activate
```

Once that is done, move to the main directory where `main.py` is located run:

```commandline
python main.py
```

depending on your python version^^^ or use (python3 main.py)

# From there you should see the Command Line Interface like this:
### Option 1

```commandline
Welcome to WGUs Package Delivery Simulator Main Menu
1. Show Which Packages are on each Truck, Delivery Logs, and Delivery Times/ With Total Mileage For Each Truck/Final Total Mileage
2. Enter A Time in (HH:MM MilitaryTime) Format and List All Package Info
3. Enter A Time in (HH:MM MilitaryTime) Format with Package ID to View ONE Packages Info
0. Exit
Enter your choice here --> : 1
Truck 1 Delivery Log:
Package 14 (Delivered) Address: 4300 S 1300 E City: Millcreek, State: UT ZIP Code: 84117 Deadline: 10:30 AM, Weight: 88 Notes: Must be delivered with 15, 19 Delivery Time: 08:00
Package 34 (Delivered) Address: 4580 S 2300 E City: Holladay, State: UT ZIP Code: 84117 Deadline: 10:30 AM, Weight: 2 Notes:  Delivery Time: 08:06
Package 15 (Delivered) Address: 4580 S 2300 E City: Holladay, State: UT ZIP Code: 84117 Deadline: 9:00 AM, Weight: 4 Notes:  Delivery Time: 08:13
Package 16 (Delivered) Address: 4580 S 2300 E City: Holladay, State: UT ZIP Code: 84117 Deadline: 10:30 AM, Weight: 88 Notes: Must be delivered with 13, 19 Delivery Time: 08:13
Package 20 (Delivered) Address: 3595 Main St City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: 10:30 AM, Weight: 37 Notes: Must be delivered with 13, 15 Delivery Time: 08:13
Package 19 (Delivered) Address: 177 W Price Ave City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: EOD, Weight: 37 Notes:  Delivery Time: 08:29
Package 40 (Delivered) Address: 380 W 2880 S City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: 10:30 AM, Weight: 45 Notes:  Delivery Time: 08:31
Package 1 (Delivered) Address: 195 W Oakland Ave City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: 10:30 AM, Weight: 21 Notes:  Delivery Time: 08:37
Package 29 (Delivered) Address: 1330 2100 S City: Salt Lake City, State: UT ZIP Code: 84106 Deadline: 10:30 AM, Weight: 2 Notes:  Delivery Time: 08:40
Package 37 (Delivered) Address: 410 S State St City: Salt Lake City, State: UT ZIP Code: 84111 Deadline: 10:30 AM, Weight: 2 Notes:  Delivery Time: 08:50
Package 30 (Delivered) Address: 300 State St City: Salt Lake City, State: UT ZIP Code: 84103 Deadline: 10:30 AM, Weight: 1 Notes:  Delivery Time: 09:04
Package 13 (Delivered) Address: 2010 W 500 S City: Salt Lake City, State: UT ZIP Code: 84104 Deadline: 10:30 AM, Weight: 2 Notes:  Delivery Time: 09:07
Package 31 (Delivered) Address: 3365 S 900 W City: Salt Lake City, State: UT ZIP Code: 84119 Deadline: 10:30 AM, Weight: 1 Notes:  Delivery Time: 09:21
Total Mileage for Truck 1: 34.0
Truck 2 Delivery Log:
Package 25 (Delivered) Address: 5383 South 900 East #104 City: Salt Lake City, State: UT ZIP Code: 84117 Deadline: 10:30 AM, Weight: 7 Notes: Delayed on flight---will not arrive to depot until 9:05 am Delivery Time: 09:10
Package 33 (Delivered) Address: 2530 S 500 E City: Salt Lake City, State: UT ZIP Code: 84106 Deadline: EOD, Weight: 1 Notes:  Delivery Time: 09:18
Package 28 (Delivered) Address: 2835 Main St City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: EOD, Weight: 7 Notes: Delayed on flight---will not arrive to depot until 9:05 am Delivery Time: 09:34
Package 32 (Delivered) Address: 3365 S 900 W City: Salt Lake City, State: UT ZIP Code: 84119 Deadline: EOD, Weight: 1 Notes: Delayed on flight---will not arrive to depot until 9:05 am Delivery Time: 09:37
Package 6 (Delivered) Address: 3060 Lester St City: West Valley City, State: UT ZIP Code: 84119 Deadline: 10:30 AM, Weight: 88 Notes: Delayed on flight---will not arrive to depot until 9:05 am Delivery Time: 09:47
Package 36 (Delivered) Address: 2300 Parkway Blvd City: West Valley City, State: UT ZIP Code: 84119 Deadline: EOD, Weight: 88 Notes: Can only be on truck 2 Delivery Time: 09:52
Package 27 (Delivered) Address: 1060 Dalton Ave S City: Salt Lake City, State: UT ZIP Code: 84104 Deadline: EOD, Weight: 5 Notes:  Delivery Time: 09:57
Package 35 (Delivered) Address: 1060 Dalton Ave S City: Salt Lake City, State: UT ZIP Code: 84104 Deadline: EOD, Weight: 88 Notes:  Delivery Time: 10:07
Package 39 (Delivered) Address: 2010 W 500 S City: Salt Lake City, State: UT ZIP Code: 84104 Deadline: EOD, Weight: 9 Notes:  Delivery Time: 10:07
Package 38 (Delivered) Address: 410 S State St City: Salt Lake City, State: UT ZIP Code: 84111 Deadline: EOD, Weight: 9 Notes: Can only be on truck 2 Delivery Time: 10:12
Package 3 (Delivered) Address: 233 Canyon Rd City: Salt Lake City, State: UT ZIP Code: 84103 Deadline: EOD, Weight: 2 Notes: Can only be on truck 2 Delivery Time: 10:23
Package 18 (Delivered) Address: 1488 4800 S City: Salt Lake City, State: UT ZIP Code: 84123 Deadline: EOD, Weight: 6 Notes: Can only be on truck 2 Delivery Time: 10:26
Total Mileage for Truck 2: 45.0
Truck 3 Delivery Log:
Package 21 (Delivered) Address: 3595 Main St City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: EOD, Weight: 3 Notes:  Delivery Time: 10:30
Package 4 (Delivered) Address: 380 W 2880 S City: Salt Lake City, State: UT ZIP Code: 84115 Deadline: EOD, Weight: 4 Notes:  Delivery Time: 10:36
Package 2 (Delivered) Address: 2530 S 500 E City: Salt Lake City, State: UT ZIP Code: 84106 Deadline: EOD, Weight: 44 Notes:  Delivery Time: 10:42
Package 7 (Delivered) Address: 1330 2100 S City: Salt Lake City, State: UT ZIP Code: 84106 Deadline: EOD, Weight: 8 Notes:  Delivery Time: 10:48
Package 10 (Delivered) Address: 600 E 900 South City: Salt Lake City, State: UT ZIP Code: 84105 Deadline: EOD, Weight: 1 Notes:  Delivery Time: 10:53
Package 9 (Delivered) Address: 410 S State St City: Salt Lake City, State: UT ZIP Code: 84111 Deadline: EOD, Weight: 2 Notes: Wrong address listed Delivery Time: 11:02
Package 5 (Delivered) Address: 410 S State St City: Salt Lake City, State: UT ZIP Code: 84111 Deadline: EOD, Weight: 5 Notes:  Delivery Time: 11:08
Package 8 (Delivered) Address: 300 State St City: Salt Lake City, State: UT ZIP Code: 84103 Deadline: EOD, Weight: 9 Notes:  Delivery Time: 11:08
Package 12 (Delivered) Address: 3575 W Valley Central Station bus Loop City: West Valley City, State: UT ZIP Code: 84119 Deadline: EOD, Weight: 1 Notes:  Delivery Time: 11:12
Package 17 (Delivered) Address: 3148 S 1100 W City: Salt Lake City, State: UT ZIP Code: 84119 Deadline: EOD, Weight: 2 Notes:  Delivery Time: 11:36
Package 24 (Delivered) Address: 5025 State St City: Murray, State: UT ZIP Code: 84107 Deadline: EOD, Weight: 7 Notes:  Delivery Time: 11:57
Package 26 (Delivered) Address: 5383 South 900 East #104 City: Salt Lake City, State: UT ZIP Code: 84117 Deadline: EOD, Weight: 25 Notes:  Delivery Time: 12:12
Package 22 (Delivered) Address: 6351 South 900 East City: Murray, State: UT ZIP Code: 84121 Deadline: EOD, Weight: 2 Notes:  Delivery Time: 12:18
Package 11 (Delivered) Address: 2600 Taylorsville Blvd City: Salt Lake City, State: UT ZIP Code: 84118 Deadline: EOD, Weight: 1 Notes:  Delivery Time: 12:22
Package 23 (Delivered) Address: 5100 South 2700 West City: Salt Lake City, State: UT ZIP Code: 84118 Deadline: EOD, Weight: 5 Notes:  Delivery Time: 12:45
Total Mileage for Truck 3: 47.4
Final Total Mileage For All Trucks: 126.4

Welcome to WGUs Package Delivery Simulator Main Menu
1. Show Which Packages are on each Truck, Delivery Logs, and Delivery Times/ With Total Mileage For Each Truck/Final Total Mileage
2. Enter A Time in (HH:MM MilitaryTime) Format and List All Package Info
3. Enter A Time in (HH:MM MilitaryTime) Format with Package ID to View ONE Packages Info
0. Exit
Enter your choice here --> :
```
### Option 2
```commandline
Welcome to WGUs Package Delivery Simulator Main Menu
1. Show Which Packages are on each Truck, Delivery Logs, and Delivery Times/ With Total Mileage For Each Truck/Final Total Mileage
2. Enter A Time in (HH:MM MilitaryTime) Format and List All Package Info
3. Enter A Time in (HH:MM MilitaryTime) Format with Package ID to View ONE Packages Info
0. Exit
Enter your choice here --> : 2
Enter a specific time (HH:MM)Military Time: 09:50
Total Mileage of route: 126.4
Package Status at 09:50
Package Status Table:
Package: 1    Status: Delivered  Address: 195 W Oakland Ave                      City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: 10:30 AM - (Delivered At: 08:37)  Weight: 21   Notes:  Truck: 1
Package: 2    Status: At Hub     Address: 2530 S 500 E                           City: Salt Lake City   State: UT  ZipCode: 84106 Deadline: EOD                               Weight: 44   Notes:  Truck: 3
Package: 3    Status: En Route   Address: 233 Canyon Rd                          City: Salt Lake City   State: UT  ZipCode: 84103 Deadline: EOD                               Weight: 2    Notes: Can only be on truck 2 Truck: 2
Package: 4    Status: At Hub     Address: 380 W 2880 S                           City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: EOD                               Weight: 4    Notes:  Truck: 3
Package: 5    Status: At Hub     Address: 410 S State St                         City: Salt Lake City   State: UT  ZipCode: 84111 Deadline: EOD                               Weight: 5    Notes:  Truck: 3
Package: 6    Status: Delivered  Address: 3060 Lester St                         City: West Valley City State: UT  ZipCode: 84119 Deadline: 10:30 AM - (Delivered At: 09:47)  Weight: 88   Notes: Delayed on flight---will not arrive to depot until 9:05 am Truck: 2
Package: 7    Status: At Hub     Address: 1330 2100 S                            City: Salt Lake City   State: UT  ZipCode: 84106 Deadline: EOD                               Weight: 8    Notes:  Truck: 3
Package: 8    Status: At Hub     Address: 300 State St                           City: Salt Lake City   State: UT  ZipCode: 84103 Deadline: EOD                               Weight: 9    Notes:  Truck: 3
Package: 9    Status: At Hub     Address: 300 State St                           City: Salt Lake City   State: UT  ZipCode: 84103 Deadline: EOD                               Weight: 2    Notes: Wrong address listed Truck: 3
Package: 10   Status: At Hub     Address: 600 E 900 South                        City: Salt Lake City   State: UT  ZipCode: 84105 Deadline: EOD                               Weight: 1    Notes:  Truck: 3
Package: 11   Status: At Hub     Address: 2600 Taylorsville Blvd                 City: Salt Lake City   State: UT  ZipCode: 84118 Deadline: EOD                               Weight: 1    Notes:  Truck: 3
Package: 12   Status: At Hub     Address: 3575 W Valley Central Station bus Loop City: West Valley City State: UT  ZipCode: 84119 Deadline: EOD                               Weight: 1    Notes:  Truck: 3
Package: 13   Status: Delivered  Address: 2010 W 500 S                           City: Salt Lake City   State: UT  ZipCode: 84104 Deadline: 10:30 AM - (Delivered At: 09:07)  Weight: 2    Notes:  Truck: 1
Package: 14   Status: Delivered  Address: 4300 S 1300 E                          City: Millcreek        State: UT  ZipCode: 84117 Deadline: 10:30 AM - (Delivered At: 08:00)  Weight: 88   Notes: Must be delivered with 15, 19 Truck: 1
Package: 15   Status: Delivered  Address: 4580 S 2300 E                          City: Holladay         State: UT  ZipCode: 84117 Deadline: 9:00 AM - (Delivered At: 08:13)   Weight: 4    Notes:  Truck: 1
Package: 16   Status: Delivered  Address: 4580 S 2300 E                          City: Holladay         State: UT  ZipCode: 84117 Deadline: 10:30 AM - (Delivered At: 08:13)  Weight: 88   Notes: Must be delivered with 13, 19 Truck: 1
Package: 17   Status: At Hub     Address: 3148 S 1100 W                          City: Salt Lake City   State: UT  ZipCode: 84119 Deadline: EOD                               Weight: 2    Notes:  Truck: 3
Package: 18   Status: En Route   Address: 1488 4800 S                            City: Salt Lake City   State: UT  ZipCode: 84123 Deadline: EOD                               Weight: 6    Notes: Can only be on truck 2 Truck: 2
Package: 19   Status: Delivered  Address: 177 W Price Ave                        City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: EOD - (Delivered At: 08:29)       Weight: 37   Notes:  Truck: 1
Package: 20   Status: Delivered  Address: 3595 Main St                           City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: 10:30 AM - (Delivered At: 08:13)  Weight: 37   Notes: Must be delivered with 13, 15 Truck: 1
Package: 21   Status: At Hub     Address: 3595 Main St                           City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: EOD                               Weight: 3    Notes:  Truck: 3
Package: 22   Status: At Hub     Address: 6351 South 900 East                    City: Murray           State: UT  ZipCode: 84121 Deadline: EOD                               Weight: 2    Notes:  Truck: 3
Package: 23   Status: At Hub     Address: 5100 South 2700 West                   City: Salt Lake City   State: UT  ZipCode: 84118 Deadline: EOD                               Weight: 5    Notes:  Truck: 3
Package: 24   Status: At Hub     Address: 5025 State St                          City: Murray           State: UT  ZipCode: 84107 Deadline: EOD                               Weight: 7    Notes:  Truck: 3
Package: 25   Status: Delivered  Address: 5383 South 900 East #104               City: Salt Lake City   State: UT  ZipCode: 84117 Deadline: 10:30 AM - (Delivered At: 09:10)  Weight: 7    Notes: Delayed on flight---will not arrive to depot until 9:05 am Truck: 2
Package: 26   Status: At Hub     Address: 5383 South 900 East #104               City: Salt Lake City   State: UT  ZipCode: 84117 Deadline: EOD                               Weight: 25   Notes:  Truck: 3
Package: 27   Status: En Route   Address: 1060 Dalton Ave S                      City: Salt Lake City   State: UT  ZipCode: 84104 Deadline: EOD                               Weight: 5    Notes:  Truck: 2
Package: 28   Status: Delivered  Address: 2835 Main St                           City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: EOD - (Delivered At: 09:34)       Weight: 7    Notes: Delayed on flight---will not arrive to depot until 9:05 am Truck: 2
Package: 29   Status: Delivered  Address: 1330 2100 S                            City: Salt Lake City   State: UT  ZipCode: 84106 Deadline: 10:30 AM - (Delivered At: 08:40)  Weight: 2    Notes:  Truck: 1
Package: 30   Status: Delivered  Address: 300 State St                           City: Salt Lake City   State: UT  ZipCode: 84103 Deadline: 10:30 AM - (Delivered At: 09:04)  Weight: 1    Notes:  Truck: 1
Package: 31   Status: Delivered  Address: 3365 S 900 W                           City: Salt Lake City   State: UT  ZipCode: 84119 Deadline: 10:30 AM - (Delivered At: 09:21)  Weight: 1    Notes:  Truck: 1
Package: 32   Status: Delivered  Address: 3365 S 900 W                           City: Salt Lake City   State: UT  ZipCode: 84119 Deadline: EOD - (Delivered At: 09:37)       Weight: 1    Notes: Delayed on flight---will not arrive to depot until 9:05 am Truck: 2
Package: 33   Status: Delivered  Address: 2530 S 500 E                           City: Salt Lake City   State: UT  ZipCode: 84106 Deadline: EOD - (Delivered At: 09:18)       Weight: 1    Notes:  Truck: 2
Package: 34   Status: Delivered  Address: 4580 S 2300 E                          City: Holladay         State: UT  ZipCode: 84117 Deadline: 10:30 AM - (Delivered At: 08:06)  Weight: 2    Notes:  Truck: 1
Package: 35   Status: En Route   Address: 1060 Dalton Ave S                      City: Salt Lake City   State: UT  ZipCode: 84104 Deadline: EOD                               Weight: 88   Notes:  Truck: 2
Package: 36   Status: En Route   Address: 2300 Parkway Blvd                      City: West Valley City State: UT  ZipCode: 84119 Deadline: EOD                               Weight: 88   Notes: Can only be on truck 2 Truck: 2
Package: 37   Status: Delivered  Address: 410 S State St                         City: Salt Lake City   State: UT  ZipCode: 84111 Deadline: 10:30 AM - (Delivered At: 08:50)  Weight: 2    Notes:  Truck: 1
Package: 38   Status: En Route   Address: 410 S State St                         City: Salt Lake City   State: UT  ZipCode: 84111 Deadline: EOD                               Weight: 9    Notes: Can only be on truck 2 Truck: 2
Package: 39   Status: En Route   Address: 2010 W 500 S                           City: Salt Lake City   State: UT  ZipCode: 84104 Deadline: EOD                               Weight: 9    Notes:  Truck: 2
Package: 40   Status: Delivered  Address: 380 W 2880 S                           City: Salt Lake City   State: UT  ZipCode: 84115 Deadline: 10:30 AM - (Delivered At: 08:31)  Weight: 45   Notes:  Truck: 1

Welcome to WGUs Package Delivery Simulator Main Menu
1. Show Which Packages are on each Truck, Delivery Logs, and Delivery Times/ With Total Mileage For Each Truck/Final Total Mileage
2. Enter A Time in (HH:MM MilitaryTime) Format and List All Package Info
3. Enter A Time in (HH:MM MilitaryTime) Format with Package ID to View ONE Packages Info
0. Exit
Enter your choice here --> :
```
### Option 3
```commandline
Welcome to WGUs Package Delivery Simulator Main Menu
1. Show Which Packages are on each Truck, Delivery Logs, and Delivery Times/ With Total Mileage For Each Truck/Final Total Mileage
2. Enter A Time in (HH:MM MilitaryTime) Format and List All Package Info
3. Enter A Time in (HH:MM MilitaryTime) Format with Package ID to View ONE Packages Info
0. Exit
Enter your choice here --> : 3
Enter a specific time (HH:MM) Military Time: 11:09
Enter the Package ID you want to view: 9
Package Status at 11:09
Package 9 Status: Delivered Address: 410 S State St City: Salt Lake City State: UT ZIP Code: 84111 Deadline: EOD - (Delivered At: 11:02) Weight: 2 Notes: Wrong address listed Truck: 3
```

## INTRODUCTION

```text
For this assessment, you will apply the algorithms and data structures you studied in this course to solve a real programming problem. You will also implement an algorithm to route
delivery trucks that will allow you to meet all delivery deadlines while traveling under 140 miles. You will also describe and justify the decisions you made while creating
this program.

The skills you showcase in your completed project may be useful in responding to technical interview questions for future employment. This project may also be added to your
portfolio to show to future employers.
```

## SCENARIO

```text
The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD) because packages are
not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day.
Each package has specific criteria and delivery requirements that are listed in the attached “WGUPS Package File.”

Your task is to determine an algorithm, write code, and present a solution where all 40 packages will be delivered on time while meeting each package’s requirements and keeping
the combined total distance traveled under 140 miles for two of the trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances
to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU
has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

 

The supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has
been delivered and at what time the delivery occurred.
```

#### Assumptions
•  Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•  The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•  There are no collisions.

•  Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•  Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.

•  The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.

•  There is up to one special note associated with a package.

•  The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

•  The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.

•  The day ends when all 40 packages have been delivered.


## REQUIREMENTS

```text
Your submission must be your original work. No more than a combined total of 30% of the submission and no more than a 10% match to any one individual source can be directly quoted or closely
paraphrased from sources, even if cited correctly. The similarity report that is provided when you submit your task can be used as a guide.



You must use the rubric to direct the creation of your submission because it provides detailed criteria that will be used to evaluate your work. Each requirement below may be evaluated by more
than one rubric aspect. The rubric aspect titles may contain hyperlinks to relevant portions of the course.



Tasks may not be submitted as cloud links, such as links to Google Docs, Google Slides, OneDrive, etc., unless specified in the task requirements. All other submissions must be file types that are
uploaded and submitted as attachments (e.g., .docx, .pdf, .ppt).



Note: Use only appropriate built-in data structures, except dictionaries. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the
internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.



A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the
    hash table:

  •   delivery address

  •   delivery deadline

  •   delivery city

  •   delivery zip code

  •   package weight

  •   delivery status (i.e., at the hub, en route, or delivered), including the delivery time


B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:

  •   delivery address

  •   delivery deadline

  •   delivery city

  •   delivery zip code

  •   package weight

  •   delivery status (i.e., at the hub, en route, or delivered), including the delivery time


C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and
    “WGUPS Package File.”

  1.  Create an identifying comment within the first line of a file named “main.py” that includes your student ID.

  2.  Include comments in your code to explain both the process and the flow of the program.


D.  Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should
    report the package as at the hub, en route, or delivered. Delivery status must include the time.)

  1.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.

  2.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.

  3.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.


E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.


F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:

  1.  Describe two or more strengths of the algorithm used in the solution.

  2.  Verify that the algorithm used in the solution meets all requirements in the scenario.

  3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.

    a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.


G.  Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.


H.  Verify that the data structure used in the solution meets all requirements in the scenario.

  1.  Identify two other data structures that could meet the same requirements in the scenario.

    a.  Describe how each data structure identified in H1 is different from the data structure used in the solution.


I.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.


J.  Demonstrate professional communication in the content and presentation of your submission.
