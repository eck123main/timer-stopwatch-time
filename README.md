# **Timer / stopwatch / time tkinter application**
I made this mainly to experiment with tkinter so i could play around with a gui and customize things. It was quite fun integrating the logic for the needed applications into a gui so i could visualize it and i definitely learning alot

# **Features**
1. Displays current time 
2. Timer (one timer at a time allowed). This comes with the ability to reset the timer early. When the timer goes off, it will play a sound, however i think this only works on early python versions as for example the playsound import wasnt working for python 3.14
3. Stopwatch that can begin once clicked and show time when stop button clicked.
4. Interactive GUI

# **How to run**
1. Download the file
2. Ensure you are using a python version below 3.14 as playsound is not yet compatible, else it wont work.
3. Run the tkinter file

# **Logic.py**
I moved the inner functionality for the tkinter applications within a seperate file for readability purposes.

# **Tkinter**
I used tkinter alongside logic, datetime and playsound. Tkinter made up the GUI which is why i felt it was worth noting.
## Here we use Tkinter to do the following: 
1. Creating the main application window that is opened when the tkinker file is ran.
2. Handling the user interaction through buttons and input
3. Displaying all the dynamic values i wanted on the screen - e.g current time and timer countdown
4. Managing the multiple pages required on the screen

Creating this was intriguing and definitely took me a while to get the hang of. It was particularly interesting to learn how the different "frames" (basically a page in tkinter) work and how i could use them for each part i eventually wanted.
Then it was just a matter of adding my widges to each page and customizing it to my liking with titles and such.
