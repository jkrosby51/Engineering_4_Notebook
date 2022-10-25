# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch_Pad](#launch_pad)
* [Crash_Avoidance](#crash_avoidance)
* [Landing_Area](#landing_area)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp; 

## Launch_Pad

### Assignment Description

Simulate the countdown and basic launch sequence of a rocket, using a Raspberry pico and Circuit Python.

### Evidence 

![Evidence](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/Launchpad%20pt4.gif)

Evidence gif [from Josie](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/Launchpad%20pt4.gif)


### Wiring

![Wiring Diagram](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/images/launchPad-Wiring.png)

### Code
[Link to code](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/raspberry-pi/launchPad.py)

### Reflection

The main issue I had to solve was in allowing the user to abort the countdown at any time by pressing the button. Originally I was using `time.sleep(seconds)` to control the speed of the program (led blinks every half a second, and countdown counts seconds), however, `time.sleep()` puts the entire program to rest for the specified time, meaning the button cant be pressed during the delay. Since this left for only a small window each second where the button would work, I had to find another way to do it. The final result is shown in the code, but it essentially takes the time each second, and every frame within that second, it checks current time - initial time to see how much time has passed since the initial time was taken. This allowed me to control the time without forcing any delays in the code. Another small problem was that `time.time()`, which is used to check the current time, doesnt work correctly with circuit python, and had to be replaced with `time.monotonic()`.

&nbsp;

## Crash_Avoidance

### Assignment Description

Simulate the data of a moving in-air vehicle. Keep track of and display the x, y, and z, acceleration values of the vehicle and give a warning if it is on it's side or upsidedown. The module also has to be powered off of a mobile power source.

### Evidence 

![gif showing crash avoidance module](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/images/ezgif.com-gif-maker.gif)

### Wiring

![wiring](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/CAP3wiring.PNG)

Wiring diagram [from Josie](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/CAP3wiring.PNG)

### Code
[Link to code](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/raspberry-pi/crashAvoidance.py)

### Reflection

One part of this assignment that caused some trouble, was managing two devices both using I2C. Since error messages found were not very descriptive, I ended up having trouble finding what exactly was wrong. I was able to solve all of the problems by completely redoing my wiring. I didn't find the issue when simply looking at my wiring, but when I did a full restart it ended up working. Sometimes the best thing to do is just completely restart on the wiring and/or code, and do it better the second time.

&nbsp;

## Landing_Area

### Assignment Description

In this assignment, I take three vertices from the user, find the area of the given triangle, and display the given triangle on an OLED screen.

### Evidence 

![Evidence gif](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2.gif)

Evidence gif [from Josie](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2.gif)

### Wiring

![Wiring Diagram](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2wiring.PNG)

Wiring diagram [from Josie](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2wiring.PNG)

### Code

Link to [code](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/raspberry-pi/landingArea.py)

### Reflection

I didn't have many issues during this assignment, but I did have to create a bit of a process for creating the try loop. When coding, it was important for me to exclude the try except statement until after I was sure that my code works fine, otherwise it would create an infinite loop, as well as exclude important error messages that I needed for debugging.

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!



