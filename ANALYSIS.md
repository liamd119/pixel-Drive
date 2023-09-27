Analysis
========

------------------------------------------------------------------------------------------------------------------------

Problem Identification
----------------------
Most of the best modern-day games require powerful PC systems and, for online games, stable, fast, and reliable internet connections. This can be seen especially with car racing games, which, due to both the complex physics modelling and the high-definition graphics, are often both GPU and CPU intensive.
 
### What is a car racing game?
Car racing games are a genre of video game where the player takes part in a racing competition driving a car, usually with the aim of finishing a course or laps of a track first, and vary in terms of realism, from arcade-style and kart racing which are less realistic in their depiction of car behaviours and instead focus on the racing experience, and simulation games which are developed to provide the most realistic player experience.*

For example, "the most played racing game on Steam in 2023", [BeamNG.drive](https://www.wikipedia.org/wiki/BeamNG.drive 'BeamNG.drive on Wikipedia'),  with 9611 average concurrent players on Steam[^1], lists [requirements on Steam](https://store.steampowered.com/app/284160/BeamNGdrive/#:~:text=System%20Requirements&text=OS%3A%20Windows%207%20Service%20Pack,Nvidia%20GeForce%20GTX%20550%20Ti):

> ***BeamNG.drive* System Requirements**
> - Minimum:
    >  - Processor: AMD FX 6300 3.5GHz or Intel Core i3-6300 3.8GHz
>  - Memory: 16 GB
>  - Graphics: Radeon HD 7750 or Nvidia GeForce GTX 550 Ti
> - Recommended:
    >  - Processor: AMD Ryzen 7 1700 3.0GHz or Intel Core i7-6700 3.4GHz
>  - Memory: 32 GB
>  - Graphics: AMD R9 290 or Nvidia GeForce GTX 970

To buy the recommended Intel CPU costs [£195 on Amazon](https://amzn.eu/d/gpdW82u 'Intel Core i7-6700 3.4GHz on Amazon'), and to buy a currently readily available equivalent to the recommended Nvidia GPU on Nvidia's store costs either [£139 for a GeForce GTX 1650](https://store.nvidia.com/en-gb/geforce/store/?page=1&limit=9&locale=en-gb&category=DESKTOP,GPU&gpu=GTX%201650 'Nvidia GeForce GTX 1650 on Nvidia\'s store') or [£221 for a GeForce GTX 1650 Super](https://store.nvidia.com/en-gb/geforce/store/?page=1&limit=9&locale=en-gb&category=DESKTOP,GPU&gpu=GTX%201650 'Nvidia GeForce GTX 1650 Super on Nvidia\'s store'). The GeForce GTX 1650 benchmarks slightly below the GeForce GTX 970, and the GeForce GTX 1650 Super benchmarks slightly above the GTX 970[^2].

Also, there's the cost of the games themselves. BeamNG.drive is fairly cheap for a racing game at [£20 on Steam](https://store.steampowered.com/app/284160/BeamNGdrive/ 'BeamNG.drive on Steam'), as it's still in early access. However, to purchase the ten games on OverTake's list[^1] of the most played games would currently cost £305.45.

**Especially with the increasing cost of living in the UK[^3], it isn't feasible for individuals to spend large sums of money on gaming.**

[^1]: OverTake, written 31 March 2023, OverTake website, article, [The Most Played Racing Games on Steam in 2023](https://www.overtake.gg/top-lists-galleries/top-lists/the-most-played-racing-games-on-steam-in-2023/ 'The Most Played Racing Games on Steam in 2023')  
[^2]: PassMark®  Software, as of 4 September 2023, PassMark Videocard Benchmark website, benchmark comparison, [GeForce GTX 970 vs GeForce GTX 1650 vs GeForce GTX 1650 SUPER](https://www.videocardbenchmark.net/compare/2954vs4078vs4167/GeForce-GTX-970-vs-GeForce-GTX-1650-vs-GeForce-GTX-1650-SUPER)  
[^3]: Office for National Statistics (ONS), released 14 July 2023, ONS website, article, [Impact of increased cost of living on adults across Great Britain: February to May 2023](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/articles/impactofincreasedcostoflivingonadultsacrossgreatbritain/februarytomay2023)


### My solution
My solution is a 2D racing game written in Python that aims to capture the engagement and enjoyment of the best racing games while also benefiting from being lightweight in both file size and hardware demands, and as Python is an interpreted language, portability between a variety of processor architectures and operating systems.


### Why the problem is suited to a computational approach
This problem is amenable to a computational solution, as it's a problem caused by a lack of suitable existing software. It requires taking user input to control the car, modelling the behaviour of the car(s) to provide an authentic feel, and communicating that to the user. The only alternative solution would be an electro-mechanical one, for example, Scalextric®, which would bring many downsides, including the physical space required, the cost of the track and cars, and the limited input. Because of this, a computer-based solution is clearly the most suitable.

Throughout the development of the solution, I'll make use of several computational methods and problem-solving techniques in order to approach the problem in a logical way and ensure development is time-efficient.

- #### Decomposition
  Creating a game of any kind can be broken down into multiple smaller steps, for example, input handling, graphics processing, data storage, and AI. For a car racing game in particular, the steps are:
    1. Generate a model of the environment, including the player's and any opponents' cars, the track and weather conditions.
    2. Accept user input and model it as real-world input into a car (e.g. map key presses to steering wheel input).
    3. Calculate and model the effect of the input on the car and wider environment (e.g. turning the front wheels, collision modelling).
    4. Graphically represent the environment.

  These are the steps for the actual gameplay, this would be wrapped in UI layers.

- #### Abstraction
  In developing my solution , I will use multiple forms of abstraction. In order to use representational abstraction, I'll be using the object-oriented coding paradigm, such that each element of my game, whether a model of a real-world object (e.g. a wheel of a car) or an entirely virtual one (e.g. a menu screen), where each is represented as an object containing and representing only necessary details. Furthermore, I'll use data and process abstraction to reduce complexity when accessing and using object attributes and methods. This has many benefits, for example increasing readability by de-cluttering scripts, improving efficiency by preventing duplicate code and increasing maintainability as code only has to be changed in one place to change its functionality while leaving the rest of the code unchanged.

- #### Thinking ahead
  Before implementing each element of my game, I'll define the inputs and outputs it should have, and specify any preconditions. If an element is likely to have code similar to another that's already implemented, I'll consider creating a reusable component from the similar code.

- #### Thinking concurrently
    Throughout my solution, I'll determine which parts can run concurrently, and consider the benefits and drawbacks for each. For example, checking for player input can be done concurrently with other tasks as most of the processing can be done without considering input, while reading data from a file might be a poor example of when to use concurrent processing as code is likely to depend on the read values so there will be little to no performance benefit.


### Stakeholders
The target demographic for my game will be anyone who would like to play racing games, especially those who have computers not suitable for demanding titles, such as laptops or outdated PCs. However, people with systems capable of running more demanding racing games may still enjoy the simplicity of mine, and so my stakeholders will account for that. My game will incorporate some elements lending themselves to competitive play; however, it will also be very suitable for casual gameplay, so I have chosen stakeholders to represent both styles of play.

| Stakeholder   | Type of player | Has a computer system designed for gaming/resource intensive applications |
|:--------------|:--------------:|:-------------------------------------------------------------------------:|
| Aela Kelly    |     Casual     |                                    No                                     |
| Alice Cleaver |     Casual     |                                    No                                     |
| Nathan Smith? |  Competitive   |                                    No                                     |
| Louise Mellor |  Competitive   |                                    Yes                                    |
| JJ Boutell?   |  Competitive   |                                    Yes                                    |


#### Aela Kelly:
Suitable stakeholder as
#### Alice Cleaver:
Suitable stakeholder as
#### Nathan Smith?:
Suitable stakeholder as
#### Louise Mellor:
Suitable stakeholder as

------------------------------------------------------------------------------------------------------------------------

Interview
---------
### Questionare
In order to effectively gather information from my stakeholders, I will create a questionare that will be shared with all of my stakeholders. The questions will establish what they would like from my game and when they would be likely to play it.

#### The questions:
1. Do you currently play any racing games, car-racing or otherwise?  
    If yes,
    - Which titles do you play and/or enjoy the most?
    - What elements of these did you find the most appealing? What are the features of these titles that made them stand out to you (this could be unrelated to actual gameplay, for example friend recommendation or a low price)?
2. Have you ever found that a game you wanted to play either wouldn't run on your computer, or ran with too poor performance to be enjoyable? This could be any genre of video game, but especially racing games.  
    If yes,
    - What titles did you experience this with?
    - Was this on your current gaming setup?
    - If you know, what was the main reason behind this (for example, not having enough storage space)?
3. Where on the spectrum between [arcade-style and simulator racing games](#what-is-a-car-racing-game 'Link to "What is a car-racing game?" subheading') would you like this game to be, or would you prefer it to be customisable, or contain elements of both?
4. What disciplines of car racing would you like to see in a game? For example, time-trial, rally, drag, touge or tōge, circuit, autocross, drift, or any others?
5. Is there anything else you would like to mention

[//]: # (STUFF)

[//]: # (-----)

[//]: # (This problem is amenable to a computational approach as it requires a computer with hardware and an operating system capable of running a python interpreter, a suitable input device for controlling the game, and a monitor to display game output. This requires a computer as the alternative, electro-mechanical arcade racing games, are very expensive and less engaging.)
This problem is amenable to a computational approach as it requires a computer with hardware and an operating system capable of running a Python interpreter, an input device for controlling the game, and a monitor to display game output.

<!--Footnotes-->
