# Dataproject-SQLalchemy

## Aim
- Create SQL script for create and delete the role and database in postgres. 
- Create schema according to csv files.
- Push all the csv data in created database with the help of SQLalchemy.
- Fatch the required data from database with the help of SQLalchemy.
- Present the data in HTML page, use the HighCharts JavaScript Lib for plotting.

## Project Requirements
- Python version should be more then 3.7+
- List of all the dependencies in `requirements.txt`
- Basic internet browser
- Postgresql

## How To Get Data
1. To download the data [click here](https://www.kaggle.com/manasgarg/ipl/version/5). Here you will get two data files.
2. Third data file is present in assets folder in project itself.
3. Copy and paste all two downloaded csv files in **assets**.

## How To Run
1. Download the zip file and extract it in your system or clone this project in your system.
2. To install **requirements.txt** run this `pip install -r requirements.txt`.
3. Run **create.sql** file in postgre. Use `\i create.sql;`.
4. Run python `main.py` file.
5. Open `index.html` file in your browser to see the output.
6. You can also use python server to see the result. Run this command in project directory `python3 -m http.server 8000`.
7. For clear up, role and database. Run this `\i drop.sql;` in postgres. 

#### Graph 1: Foreign umpire analysis
- Obtain a source for country of origin of umpires. Plot a chart between number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph.

#### Graph 2: Top batsman for Royal Challengers Bangalore
- Considered only games played by Royal Challengers Bangalore. Plot between total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.

#### Graph 3: Total runs scored by team
- Plot a chart between total runs scored by each teams over the history of IPL.

#### Graph 4: Stacked chart of matches played by team by season
- Plot a stacked bar chart of :
- Number of games played
- By team
- By season
