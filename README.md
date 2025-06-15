# nba-champion-predictor
Hello so the goal of this project is to train a machine learning algorithm using tensor flow to predict this seasons NBA champion.
The current time of me writting this is before the first game of the Conference finals have begun.
I will be using data from https://www.basketball-reference.com/ of the past 12 seasons to train the machine.

First for the scraping of the data I will use the library BeautifulSoup4. In basketball reference if we go look at the boxscores you will realize the standings are saved in different months. And then from the scraped html I scrape the individual games and save the html of the box score.

For parsing the data we save the basic and advanced stats differently. We also made a copy of the original csv so there is two data points for the same game(One based on the home team and one based on the opponent). Then use the pandas function pd.concat then convert it to a csv file. 

For the accuracy we use tensor flow to predict it. First we start with removing data that is unneccasary like Minuites played for example. You can see how the accuracy increases as we use the average 10 games and add more data. 

For the prediction you add in the opp_next, Home_next emptied area and track the number 2 in the file.

I would have loved to finish scrapeing this during the weekends leading up to the final but it took me over 12 hours to be done scrapeing and create the csv file and I have personal plans that limitates my wifi usage so I will be just spending June 3rd week re fixing the code and starting the next project(AI stock prediction).

At the end of your parsing process you may encounter a problem where you get an error after the code games_df = pd.concat(games,ignore_index=True) is executed. This problem occurs because although you should have 150 columns there are multiple columns where you have diffrent amount of columns. In order to check this use this code [g.shape[1] for g in games if g.shape[1]!=150] to check and if it returns false delete the columns

The data I will be using to predict the finals is updated enough so it includes game 4 of the NBA finals after the finals is over I will be adding the rest of the box scores.
