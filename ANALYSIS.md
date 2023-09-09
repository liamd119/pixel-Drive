Analysis
========
Problem Identification
----------------------
<!--research the problem  -->
Most of the best modern day games require powerful PC systems and for online games, stable, fast and reliable internet connections.
This can be seen especially with car racing games, which due to both the complex physics modelling and the high-definition graphics, are often both GPU and CPU intensive. <br/>

- *Car racing games are a genre of video-game where the player takes part in a racing competition driving a car, usually with the aim of finishing a course or laps of a track first, and vary in terms of realism from arcade-style and kart racing to simulations of real driving*

For example, "the most played racing game on Steam in 2023", [BeamNG.drive](https://www.beamng.com/ 'The BeamNG.drive website, www.beamng.com'),  with 9611 average concurrent players on Steam[^1], lists [requirements on Steam](https://store.steampowered.com/app/284160/BeamNGdrive/#:~:text=System%20Requirements&text=OS%3A%20Windows%207%20Service%20Pack,Nvidia%20GeForce%20GTX%20550%20Ti):

> ***BeamNG.drive* System Requirements**
> - Minimum:
    >   - Processor: AMD FX 6300 3.5Ghz / Intel Core i3-6300 3.8Ghz
>  - Memory: 16 GB RAM
>  - Graphics: Radeon HD 7750 / Nvidia GeForce GTX 550 Ti
> - Recommended:
    >  - Processor: AMD Ryzen 7 1700 3.0Ghz / Intel Core i7-6700 3.4Ghz
>  - Memory: 32 GB RAM
>  - Graphics: AMD R9 290 / Nvidia GeForce GTX 970

To buy the recommended Intel CPU costs [£195 on Amazon](https://amzn.eu/d/gpdW82u 'Intel Core i7-6700 3.4GHz on Amazon'), and to buy a currently readily available equivalent to the recommended Nvidia GPU on Nvidia's store costs either [£139 for a GeForce GTX 1650](https://store.nvidia.com/en-gb/geforce/store/?page=1&limit=9&locale=en-gb&category=DESKTOP,GPU&gpu=GTX%201650 'Nvidia GeForce GTX 1650 on Nvidia\'s store'), or [£221 for a GeForce GTX 1650 Super](https://store.nvidia.com/en-gb/geforce/store/?page=1&limit=9&locale=en-gb&category=DESKTOP,GPU&gpu=GTX%201650 'Nvidia GeForce GTX 1650 Super on Nvidia\'s store'). The GeForce GTX 1650 benchmarks slightly below the GeForce GTX 970, and the GeForce GTX 1650 Super benchmarks slightly above the GTX 970[^2].

Also, there's the cost of games themselves. BeamNG.drive is fairly cheap for a racing game at [£20 on Steam](https://store.steampowered.com/app/284160/BeamNGdrive/ 'BeamNG.drive on Steam'), as it's still in early access. However, to purchase the ten games in OverTake's list of the most played games would currently cost £305.45.


<h3>

Especially with the increasing cost of living in the UK[^4], it isn't feasible for individuals to spend large sums of money on gaming.

</h3>

Therefore, there is a need for a lightweight racing game that can be played on a wide range of PCs and operating systems.


My solution
-----------
My solution is a 2D racing game written in Python that aims to capture the engagement and enjoyment of the best racing games while also benefiting from being lightweight, in both file size and hardware demands, and as Python is an interpreted language, portability between a variety of processor architectures and operating systems.

Stakeholders
------------
The target demographic for my game will be anyone who would like to play racing games, especially those who have computers not suitable for demanding titles, such as laptops or outdated PCs. As the game is designed for a wide range of players, the stakeholders will be varied, including casual and competitive gamers, and those with a specific

STUFF
-----

[//]: # (This problem is amenable to a computational approach as it requires a computer with hardware and an operating system capable of running a python interpreter, a suitable input device for controlling the game, and a monitor to display game output. This requires a computer as the alternative, electro-mechanical arcade racing games, are very expensive and less engaging.)
This problem is amenable to a computational approach as it requires a computer with hardware and an operating system capable of running a Python interpreter, an input device for controlling the game, and a monitor to display game output.

<!--Footnotes-->
[^1]: OverTake, written 31 March 2023, OverTake website, article, [The Most Played Racing Games on Steam in 2023](https://www.overtake.gg/top-lists-galleries/top-lists/the-most-played-racing-games-on-steam-in-2023/ 'The Most Played Racing Games on Steam in 2023')  
[^2]: PassMark®  Software, as of 4 September 2023, PassMark Videocard Benchmark website, benchmark comparison, [GeForce GTX 970 vs GeForce GTX 1650 vs GeForce GTX 1650 SUPER](https://www.videocardbenchmark.net/compare/2954vs4078vs4167/GeForce-GTX-970-vs-GeForce-GTX-1650-vs-GeForce-GTX-1650-SUPER)  
[^3]: Office for National Statistics (ONS), released 14 July 2023, ONS website, article, [Impact of increased cost of living on adults across Great Britain: February to May 2023](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/articles/impactofincreasedcostoflivingonadultsacrossgreatbritain/februarytomay2023)
