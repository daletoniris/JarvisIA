# JarvisIA
JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos. The collaborators of this development are a very crazy and cool team that were students of programming and hacking of Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu and Matias Gimenez

https://www.youtube.com/watch?v=0dOnX5DsTNM&t=30s

To start cloning the repository, you can run this code in ubuntu in a PC or in a raspberry pi.
Once cloned, execute the file: speakyou.py in the following way: python3 speakyou.py
There surely you will have errors since you will have to install all the dependencies, to install them execute the following: sudo pip3 install "and the name of the library". This is if you are in python3 but: sudo pip install "and the name of the library". You must install python pip before.

Once you install everything you must create an app in https://wit.ai/.
Enter wit and create your app with the entities that you want, you can look at the file: "jarvispoc.py" so that you create the entities as they are created there, if you are new in this it suits you to do it that way.

JarvisIA can work with wit.ai or you can have your own speech to text, wit.ai is a very good alternative if you are starting and will allow you to understand the Natural Language for Developers, that way you can translate your voice that is recorded to the file test1.wav

Then you will go to the configuration of your app, in setting and there you will copy your
Server Access Token, that access token you will paste in the file: "utils.py".


Now you have to install Google Speech for your assistant's voice. Enter
to the google speech folder and follow the steps of installing the readme file.

Now it will depend on how you want to use your assistant, you can run everything in one raspberry pi, or you can use a server and raspberry pi as modules that control the electronics of your home. Look at the jarvispoc.py file to understand how to make these small modifications.
JarvisIA is totally modular, you can use what you want and modify it to your needs.
To start alone: ​​say words like: "Hello Jarvis" or "I want to hear travis" or "I want to know about Albert Einstein" or "what is the current date" or "or what is the current time" or "what is the weather in puerto madryn "(modify your city in the clima1.py file).
We hope you enjoy it a lot and you can learn by playing with it, we have not released all the code but a great part to encourage the development of voice assistants in Latin America and because we know that the way to learn is reading another code and testing so do not be afraid and have fun! 
Happy hacking!!
