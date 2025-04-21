import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    args
        sentiments: A list of strings

    return
        Bar graph of sentiments(Negative, Positive, Neutral, Irrelevant)
    """
    x = sentiments.count('positive') 
    y = sentiments.count('negative')
    z = sentiments.count('neutral')
    a = sentiments.count('irrelevant')
    fig,ax = plt.subplots()
    ax.bar(['positive', 'negative', 'neutral', 'irrelevant'],[x, y, z, a])
    ax.set_title("occurence of sentiments in reviews")
    ax.set_xlabel('sentiments')
    ax.set_ylabel('frequency or occurence')

    fig.savefig('images')
   
