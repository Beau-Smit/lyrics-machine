import re
import sys
import pandas as pd
from markov import Markov

analysis_genres = ['Hip Hop/Rap', 'Rock', 'Pop', 'Heavy Metal', 'Country']

def process(unknown_txt, k):
    data = {}
    for genre in analysis_genres:
        fname = re.sub(' |/', '_', genre) + '.txt'
        with open(f'lyrics/{fname}') as f:
            model = Markov(f.read(), k)
        data[genre] = model.log_probability(unknown_txt)
    

    # which genre is most likely?
    probability_frame = pd.DataFrame.from_dict(data, orient='index').sort_values(0, ascending=False)
    
    print(f"Most likely genres:")
    for i, genre in enumerate(probability_frame.iterrows()):
        print(f"{i + 1}. {genre[0]}")


if __name__ == "__main__":

    _, k = sys.argv

    with open("unknown_lyrics.txt", "r") as f:
        lyrics = f.read()

    print(f'\nUnknown lyrics: \n{lyrics}\n')
    process(lyrics, int(k))
