from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    args
        filepath: An unopened json file

    return
        string: A list of sentiments
    """
    # open the json object
    with open (filepath, 'r') as file:
        senti = json.load(file)
        
    # extract the reviews from the json file
    reviews = senti['results']


    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews).strip('\n')

        # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
