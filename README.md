
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

You can ignore most of the warnings as they do not affect the proccess. BUT do keep in mind most of this code won't work when pandas 3.0 is released.

Now it would be amazing if I am able to run the prediction in a for loop and see what percentage of the games the machine has the teams winning, however, the current situation I am in is not ideal to run this type of experiment so unlucky. 
<img width="1440" alt="Screenshot 2025-06-16 at 21 12 14" src="https://github.com/user-attachments/assets/16d142d5-9947-4a85-9337-ae0210779a9c" />
So this means that the machine predicted the pacers to win game 5. I will comeback after game 5 to see if it was correct. You can ignore the actual as the game didn't happen yet and we are only interested in what the algorithm predicted.

So OKC did win game 5 so the prediction was wrong. The model isn't perfect as today Haliburton the pacer's star Point guard got a hamstring injury and the no amount of data can ever predict that. Some events are just unpredictable

Maybe next time we can try predicting when players will be injured.

I think I am done with this project for now maybe I will do it again next season and try to predict the entire season this time. Maybe I will try to remake this project but use pytorch instead of tensorflow
