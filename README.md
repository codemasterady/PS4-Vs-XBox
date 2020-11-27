# PS4 Vs XBox Research

Welcome my fellow bots to this one and for all historic moment where I crack the big question of what console is better, PlayStation or X-Box. Like in the video, don't take my opinions as facts, tho data can be very convincing your happiness is what matters the most to me. So even if you preferred X-Box but PlayStation won during this research don't stop using the X-Box. Anyway, I am getting off track. This project uses data from the website [kaggle](https://www.kaggle.com/gregorut/videogamesales) that contains information about games and all their details. I have used many comparisons when making this research but before I get on to that, let's talk about the dataset.

## About the dataset
This dataset contains **11** fields. More information is provided on the table below.

| Field      | Description | Data Type |
| ----------- | ----------- |----------- |
| Rank      | The ranking of the game       | int
| Name   | The name of the game        | String
| Platform   | The console that the game was sold on        | String
| Year   | The time the game was sold at        | int
| Genre   | The Genre of the game (i.e Sports, Action)        | String
| Publisher   | The company that published the games        | String
| NA_Sales   | The sales in North America (millions)      | float
| EU_Sales   | The sales in Europe (millions)       | float
| JP_Sales   | The sales in Japan (millions)       | float
| Other_Sales   | The sales in other parts of the world apart from the mentioned top mentioned 3       | float
| World_Sales   | The sales total in the world (millions)       | float



---

## Procedure of the experiment
Here is how this research is going to function. All the consoles or, as known in this dataset, **Platforms** will be compared with each important category essentially making up a **Round**. Although this dataset contains multiple consoles, we will only be comparing the ones with Playstation with the ones of X-Box. Feel free to modify code to include your console of choice. Each round competed will earn a point which will be awarded to the winning console. There is a maximum of **5 points** with **6 rounds** including an extra bonus round. These rounds are listed below.


1.   Round(a):- Publisher Vs Console (Which publisher Prefers what console)?
2.   Round(b):- What console had the most games?
3.   Round(c):- Genre Vs Console (What genre was most popular in each console i.e the best genre (per console))?
4. Round(d):- Console Usage Over the years (Console vs Year).
5. Round(e):- Most Popular consoles in NA, EU, JP & Others.
6. Round(f)(bonus):- Ranking of game vs Overall Console Usage

***Lets take a look at these rounds in more detail!!!***
