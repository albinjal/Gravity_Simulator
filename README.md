# Gravity Simulator
My attempt at simulating gravity via classical mechanics and specifically [Newton’s law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation) (Euler’s formula):

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/48f74b3b4d591ba1996c4d481f74ac3ab7e279d7)

## Example
 **Earth and Moon ~month**

   ![Earth and Moon](/moon2.gif)

This Gif shows a simulated trip for the moon (orange) around the earth (blue).
The red vector shows the direction of the applied force while the blue one shows the velocity of the object. 

**Config :** 
Frames: 686,
Steplength: 1s,
Seconds/Frame: 60 * 60 (1 Hour / Frame),

**Objects:**

| Data          | Earth         | Moon          |
| ------------- |:-------------:| ----------:   |
| X-Pos         | 0             | 0             |
| Y-Pos         | 0             | 369671000     |
| X-Vel         | 0             |    1082       |
| Y-Vel         | 0             |    0          |
| Mass          | 6 * 10 ** 24  |7.3 * 10 ** 22 |

 **Earth and Moon ~Year**
 
  ![Earth and Moon](/moon3.gif)
   
Frames: 365,
Steplength: 1s,
Seconds/Frame: 60 * 60 * 24 (1 Day / Frame),

## Run ##
1. Clone this repo
2. Make sure your python env has the required dependencies, otherwise install with pip install <Package>
    * imageio
    * matplotlib
3. Configure setting and indata in Simulation.py
4. Run Simulation.py with: Python3 Simulation.py
5. Simulation gif should be in the "Gifs" folder

This project was made to practice object-oriented programming in Python.
