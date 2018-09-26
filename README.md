<p align="center">
    <img src="assets/images/logo.png" alt="Tellescope Logo">
</p>

# Tellescope: A Messaging Interaction Model for Customer Service

> The future of customer service is here.

Tellescope is an IoT device that analyzes customers' facial expressions. If it detects that a shopper is frustrated or needs help, it uses Bluetooth beacons to send a helpful chatbot to their phone. Tellescope can be powered by a Raspberry Pi and a cheap camera and includes a self-cooling 3d-printed housing.

To learn more, [read the proposal](https://github.com/Tellescope/Tellescope/blob/master/proposal.md)

![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

### Here's what it looks like
![Tellescope render](https://raw.githubusercontent.com/davdhng/tellescope/master/assets/images/BBack.png)

### How it works
![Tellescope flowchart](https://raw.githubusercontent.com/davdhng/tellescope/master/assets/images/flowchart.png)

### How to build it in 7 steps
Tellescope is designed to be very easy to build. There is no need to solder anything or cut any wires. You just need to be able to order things online.
The total cost should be less than $100. 

1. Find the housing in case/PiChassis.stl and 3d print it. You can upload it to <https://www.shapeways.com/>and order it from there if you don't have a 3d printer.
2. You can order the Pi and Camera Board from anywhere you like. Just get whatever's cheapest.
3. The Pi fits into the housing sideways, like you would insert a book into a shelf. Make sure the ports are facing outward. The camera wraps around the pi onto the front of the side of the Pi, so that it lines up with the hole in the case.
4. Load `tellescope.py` into your Pi. There's one last adjustment to make before Tellescope is fully operational.
5. Create your chatbot.
    * You can use any service, as long as you're able to generate a link. 
    * We built our prototype using <https://dialogflow.com/>
6. Go into `tellescope.py` and update line 57 with the link to your chatbot **You must do this or Tellescope won't work for you**
7. Save everything and run `tellescope.py`. 


### Built with
* Python 3
* Raspberry Pi 3
* Raspberry Pi Camera Board v2
* OpenCV
* Dialogflow
* A 3D Printer

**Tellescope is alpha quality software. Please don't use this in production unless you make some major fixes yourself. We're not responsible for anything bad that happens because you built this.**

### License
This project is licensed under the MIT license.


