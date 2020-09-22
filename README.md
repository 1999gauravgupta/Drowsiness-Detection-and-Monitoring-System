# Driver Drowsiness Detection and Monitoring System

## Context
Driving when you are sleepy & exhausted? Well, you're as much of a safety hazard as a drunk driver. “Drowsy driving” occurs when a person who is operating a motor vehicle is too tired to remain alert. The effect of drowsiness is similar to alcohol; it will make your driver inputs(steering, acceleration, and braking) poorer, destroy your reaction time and blur your thought processes.

Now it is high time we take control and help in reducing these kinds of accidents that pose a severe risk of life.

## Solution

In order to mitigate the drowsy-driving accidents ,we are using a set of multiple technologies such as:
`OpenCV + Tkinter + NodeJS + MongoDB`
This interface system will consist of a camera which will turn on whenever the driver starts running the main engine and  then it will check two major aspects of drowsiness:
- Yawning- checked through facial landmark detection.
- Eye closing- analyzed through eye-aspect ratio.

## Process
Whenever the driver yawns or closes his eyes for more than threshold time then the alarm goes on to signal the driver as well as the respective activity count is increased by one. On the closing of software the totals of each activity count will be stored in database against that user object.

## Team
We are a group of 5 people working together to solve this problem in an economically feasible manner.
- Vineet Jha: Team Leader and Manager
- Gaurav Gupta: Computer Vision Engineer
- Rishabh Sharma: Frontend Engineer
- Deepak Malik: Backend Engineer

## Versions
The work on this project is still ongoing and till far these versions have been released:
- v1.0 : Implemented eyes close and yawn detection feature individually.
- v2.0: Sequenced their execution to work together in one program.
- v3.0: Made them work concurrently with the use of threading and also a website for monitoring system displaying all the collected analytics using infographics.

## Future
Currently we are trying to make the code more general and implementing SOS and location features with improvement in codebase neatness too.

## How to run?
1. Navigate to `/public/js` folder and run python script using `python main.py`.
2. Wait for script to start and then test it using closing eyes or yawning. Use keystroke `q` to close window and see this run analytics. 
3. On closing it the database will be updated with newest values so we are ready to move to monitoring system.
4. Navigate to project home directory and run `npm install` and then start server using `nodemon`.
5. Visit localhost:5000 on your browser and click on "Lets's get started" and then tap on admin login.
6. You will have access to monitoring system now and can use it to access data.

###### Note:
- On non Windows System you need to edit main.py and change active thread count in alarm code from 2 to 1 and use `python3 main.py` instead(in some cases this may not work depending on how many threads are present at start of program).
- The Login ID and password of monitoring system are:`bitrebels` and `bit123`.

## Conclusion
This model, if implemented correctly on a large scale, can prevent losses in road accidents due to drowsy driving and save thousands of lives. The system can be installed in different vehicles whether those are buses , trucks, cars or even in the railways. This model includes the direct influence of monitoring the drivers' way of correctly running the vehicle which will ultimately result in reduction of roadside accidents due to drowsy driving and maintaining the records of drivers past records which will ultimately lead to streamlined traffic flow.
