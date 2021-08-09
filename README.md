# lyrics-machine
This k-th order markov chain model will predict which genre of music the given text belongs to.

After placing any text in the "unknown_lyrics.txt" file, the user must enter one command line argument - k:
python driver.py [k]

where [k] determines the size of the n-grams (how long each string is) when we make the comparisons between the known texts and the unknown text. For example, k=2 would compare each possible string of 2 in the unkown text to strings of size 3 in the known text. The known lyrics text are taken from the free musixmatch API.

The possible genres are 'Hip Hop/Rap', 'Rock', 'Pop', 'Heavy Metal', 'Country'. The model gives you the rank order of genres in terms of likelihood.
