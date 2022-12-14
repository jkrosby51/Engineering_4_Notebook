# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch_Pad](#launch_pad)
* [Crash_Avoidance](#crash_avoidance)
* [Landing_Area](#landing_area)
* [Morse_Code](#morse_code)
* [Beam_Design](#beam_design)

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

## Morse_Code

### Assignment Description

In this assignment, I took a user inputted string, and converted it to morse code. I then used both an LED and a piezzo buzzer to repeat the user's string in morse code.

### Evidence 

![evidence](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/MCP2.gif)

Evidence [from Josie](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/MCP2.gif)

### Wiring

![Wiring](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2wiring.PNG)

Wiring Diagram [from Josie](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2wiring.PNG)

### Code

Link to [code](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/raspberry-pi/morseCode.py)

### Reflection

This assignment went fairly smoothly, thought I did find some small issues by not double checking my code too closely. The piezo buzzer was very simple to wire and run, using `simpleio.tone(PIN, FREQ, LENGTH)` (you need to import simpleio first). Another small bit of code that saves a lot of time, is converting the user input into all lowercase before attempting to convert it using a dictionary. This makes sure that no matter what capitalization the user puts, it will always convert flawlessly.

&nbsp;

## Beam_Design

### Assignment Description

Design a 3D printed beam with one connection, to withstand as much weight as possible, based on vertical displacement and whether or not it breaks. The beam must use the given attachment block, be within 13g, 190mm long, and have no overhangs.

### Part Link 

[Onshape Document](https://cvilleschools.onshape.com/documents/fe9a149dbe992ae7287efdeb/w/abd769837872c651926f3788/e/81ef499ee19e4e9cf251027e?renderMode=0&uiState=637526cf34abbb53458f122f)

### Part Image

![Beam Design](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/images/beamDesignOnshape.png)

### Reflection

We did a lot of research on existing beam designs and their usage to find designs that we could incorporate in our design. What seemed to be the most efficient design feature was trusses. With that as our main design aspect, we went out to find the overall strongest design while keeping under 13g. We did this by having multiple beams connected and with different goals in mind, all with trusses in them to save weight. The most difficult part was keeping the design underweight without losing important features, and we had to find ways to remove material where it was least valuable. Before even simulating the strength of our beam, there was a lot of iteration and changes just based on the way it looked and places where we knew there would be weak points.

Once we were at a place where we weren't sure where to edit the design, we used SimScale to simulate a force at the end of the beam. This also allowed us to see where the weakest points of the design were and where it was most likely to break. We used this to help us in changing the design for the better, adding material where there were weaker points and removing material from where the beam was unlikely to break.

By going through the last process multiple times, we were able to continuously find the most and least valuable uses of material within our design, and changed the design according to the weak points. We found it was important to run the simulation frequently to ensure we knew what to change about the design before the final testing. This process made our beam design significantly more efficient and we ended up with a fairly efficient design. After the actual testing, we've discovered multiple new changes that would drastically help the design be more efficient
