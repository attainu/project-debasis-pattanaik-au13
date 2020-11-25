## ParkingLot

---
Design a parking lot using Python with TDD approach

## Dependencies

---
You just need Python. The code is compatible with Python2 as well as Python3. Visit the link https://www.python.org/downloads/ to install Python.

## Description

---
This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.

ParkingLot.py script defines the following functions -

1. `create_parking_lot n` - Given n number of slots, create a parking lot
1. `park car_regno car_color` - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
1. `status` - Prints the slot number, registration number and color of the parked vehicles.
1. `leave x` - Removes vehicle from slot number x
1. There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with particular color etc.

ParkingLot.py can be run through shell or through file containing test cases. An example file `run_test_case.txt` has been provided in repo.

I have followed TDD approach while designing this. `test_parking_lot.py` uses `unittest` module of python. Here 6 test cases are written in order to test each functionality mentioned in ParkingLot.py

Vehicle.py is a separate class where we can define the type of vehicles that can be parked. As of now, it only contains class `Car`

## Setup

---
To create your own ParkingLot -

1. Clone the repository
2. Run `python ParkingLot.py` to run without input test case file. This opens a shell where you can write your commands like -

![img](https://i.imgur.com/12Sslyv.png[/img])

3. To run with a file execute `python ParkingLot.py -f run_test_case.txt`. You can modify the test cases.

![img](https://i.imgur.com/M4WV8ZZ.png[/img])

4. You can also run the test cases separately as `python test_parking_lot.py`. This runs the 6 test cases written in file. This is very useful when you want to create your own function and test it simultaneously.

![img](https://i.imgur.com/6Q3r2V7.png[/img])

---
