# lyrics-machine
Enter any lyrics into unknown_lyrics.txt and the model will predict the genre of music it belongs to.

After placing any text in the "unknown_lyrics.txt" file, the user must enter one command line argument - k:
python driver.py [k]

where [k] determines the size of the n-grams (how long each string is) when we make the comparisons between the known texts and the unknown text. For example, k=2 would compare each possible string of 2 in the unkown text to strings of size 3 in the known text. The known lyrics text are taken from the free musixmatch API.

The possible genres are 'Hip Hop/Rap', 'Rock', 'Pop', 'Heavy Metal', 'Country'. The model gives you the rank order of genres in terms of likelihood.
