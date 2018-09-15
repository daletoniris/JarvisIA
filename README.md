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
Once you have everything ready you just have to run: python3 speakyou.py
Happy hacking!!




JarvisIA es una idea de Daniel Dieser @initiasur, @NiperiaLab, investigador de robótica independiente y I.A. JarvisIA es el primer asistente de voz en español y fue creado para fomentar el uso y desarrollo de tecnologías de Inteligencia Artificial entre los latinos. Los colaboradores de este desarrollo son un equipo muy loco y genial que fueron estudiantes de programación y hacking de Daniel Dieser en la ciudad de Puerto Madryn, Argentina. Ellos son: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu y Matías Giménez

https://www.youtube.com/watch?v=0dOnX5DsTNM&t=30s

Para comenzar debes clonar el repositorio, puede ejecutar este código en S.O ubuntu en una PC o en una raspberry pi. Una vez clonado, ejecuta el archivo: speakyou.py de la siguiente manera: python3 speakyou.py Seguramente tendrás errores ya que tendrás que instalar todas las dependencias, para instalarlas ejecuta lo siguiente: sudo pip3 install "y el nombre de la biblioteca". Esto es si estás en python3 pero si estás en python 2.7 hacelo de la siguiente manera: sudo pip install "y el nombre de la biblioteca". Debe instalar python pip antes.

Una vez que instales todo, debes crear una aplicación en https://wit.ai/. Entra en ingenio y crea tu aplicación con las entidades que quieras, puedes mirar el archivo: "jarvispoc.py" para que crees las entidades tal como se crean allí, si eres nuevo en esto te conviene hacerlo de esa manera camino.

JarvisIA puede trabajar con wit.ai o puede tener su propio traductor de voz a texto, wit.ai es una muy buena alternativa si está comenzando y te permitirá comprender el lenguaje natural para desarrolladores, de esa manera vas a poder traducir tu voz a texto que es grabada en el archivo test1.wav

Luego irás a la configuración de tu aplicación, en la configuración y allí va a copiar su token de acceso al servidor, ese token de acceso lo pegarás en el archivo: "utils.py".

Ahora debe instalar Google Speech para la voz de tu asistente. Ingresa a la carpeta de voz de google y siga los pasos para instalar el archivo Readme.

Ahora dependerá de cómo quiera usar tu asistente, puede ejecutar todo en  solo una Raspberry pi, o puedes usar un servidor y Raspberry Pi como módulos que controlan los componentes electrónicos de tu hogar. Mira el archivo jarvispoc.py para comprender cómo hacer estas pequeñas modificaciones. JarvisIA es totalmente modular, puedes usar lo que quieras y modificarlo según tus necesidades. Para comenzar solo: decí palabras como: "Hola, Jarvis" o "Quiero escuchar travis" o "Quiero saber sobre Albert Einstein" o "¿Cuál es la fecha actual" o "o cuál es la hora actual" o "¿Cuál es el clima en Puerto Madryn?" (modifica tu ciudad en el archivo clima1.py). Esperamos que lo disfrutes mucho y que puedas aprender jugando con él, no hemos lanzado todo el código, pero una gran parte de el, para fomentar el desarrollo de asistentes de voz en América Latina y porque sabemos que la forma de aprender es leer otro código y probarlo, así que no tengas miedo y diviértete! Una vez que tengas todo listo, solo tienes que ejecutar: python3 speakyou.py ¡Feliz hackeo!
