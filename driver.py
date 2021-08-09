'''
Beau Smit

This series of programs can compare 2 speakers to predict which was more likely
to utter the unknown text. This program could be expanded to compare more than 
2 potential speakers at a time. The text files used are from presidential 
debates.

The numbers returned may be compared to eachother, but do not necessarily have 
any meaning outside that particular comparison.
'''

import os
import re
import sys
import pandas as pd
import numpy as np
from markov import Markov


# which speakers would you like to compare? choices: [BUSH, KERRY, OBAMA, MCCAIN]
GENRE_A = 'Country'
GENRE_B = 'Hip_Hop_Rap'

analysis_genres = ['Hip Hop/Rap', 'Rock', 'Pop', 'Heavy Metal', 'Country']

# what is the unknown text file? please enter a speaker's name - a number
# UNKNOWN_TXT_FILE = 


def process(unknown_txt, k):
    data = {}
    for genre in analysis_genres:
        fname = re.sub(' |/', '_', genre) + '.txt'
        with open(f'lyrics/{fname}') as f:
            model = Markov(f.read(), k)
        data[genre] = model.log_probability(unknown_txt)
    

    # which genre is most likely?
    probability_frame = pd.DataFrame.from_dict(data, orient='index').sort_values(0, ascending=False)
    probability_frame.columns = ['relative_scores']
    most_likely = probability_frame.iloc[0].name
    
    print(probability_frame)
    print(f'Most likely genre: {most_likely}')


if __name__ == "__main__":
    # the user must enter one command line argument - k
    # k determines the size of the n-grams (how long each string is) when we make the comparisons
    # between the known texts and the unknown text. k=2 would compare each possible string of 2 in the
    # unkown text to strings of size 3 in the known text.
    _, k = sys.argv

    with open("unknown_lyrics.txt", "r") as f:
        lyrics = f.read()

    print(f'Unknown lyrics: \n{lyrics}\n')
    process(lyrics, int(k))

    # true genre =
