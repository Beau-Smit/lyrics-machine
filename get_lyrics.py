import requests
import re

apikey = '76ed9d69f0e44f2b0cc173c8b1eeb59c'
root_url = 'https://api.musixmatch.com/ws/1.1/'

###### Genres to analyze
analysis_genres = ['Hip Hop/Rap', 'Rock', 'Pop', 'Heavy Metal', 'Country']


def get_genre_track_ids(genre_id):
    '''
    '''
    genre_tracks = []
    # for pg in range(1, 11):
    #     response = requests.get(url = f'{root_url}/track.search?format=json&callback=callback&f_music_genre_id={genre_id}&f_lyrics_language=en&f_has_lyrics=1&quorum_factor=1&page_size=100&page={pg}&apikey={apikey}')
    #     data = response.json()
    #     for track_data in data['message']['body']['track_list']:
    #         genre_tracks.append(track_data['track']['track_id'])
        
    response = requests.get(url = f'{root_url}/track.search?format=json&callback=callback&f_music_genre_id={genre_id}&f_lyrics_language=en&f_has_lyrics=1&quorum_factor=1&page_size=100&apikey={apikey}')
    data = response.json()
    for track_data in data['message']['body']['track_list']:
        genre_tracks.append(track_data['track']['track_id'])
    return genre_tracks

def get_lyrics(track_id):
    '''
    '''
    response = requests.get(url = f'{root_url}track.lyrics.get?format=json&callback=callback&track_id={track_id}&apikey={apikey}')
    data = response.json()
    # split removes the warning at the end about commercial use
    try:
        lyrics = data['message']['body']['lyrics']['lyrics_body'].split('...')[0]
        lyrics = re.sub('\n|//', ' ', lyrics).lower()
        return lyrics
    except:
        return ''

def get_all_genres():
    '''
    '''
    all_genres = {}

    # this query returns all genres that exist in the database
    response = requests.get(url = f'{root_url}/music.genres.get?format=json&callback=callback&apikey={apikey}')
    data = response.json()

    # add all genres to the dictionary
    for genre_data in data['message']['body']['music_genre_list']:
        genre_id = genre_data['music_genre']['music_genre_id']
        genre_name = genre_data['music_genre']['music_genre_name']
        all_genres[genre_name] = genre_id
    
    return all_genres

def add_lyrics_to_genres(all_genres):
    '''
    '''
    # add the lyrics for each genre to a list
    genre_lyrics = {key:[] for key in analysis_genres}
    for genre in analysis_genres:
        # search for 100 tracks of this genre
        genre_track_ids = get_genre_track_ids(all_genres[genre])
        # add to dictionary
        for track_id in genre_track_ids:
            lyrics = get_lyrics(track_id)
            genre_lyrics[genre].append(lyrics)
    return genre_lyrics

def write_output(genre_lyrics):
    '''write the lyrics for each genre to a text file
    '''
    for genre, lyric_list in genre_lyrics.items():
        genre = re.sub('/| ', '_', genre)
        with open(f'lyrics/{genre}.txt', 'w') as f:
            genre_lyrics = ''.join(lyric_list)
            f.write(genre_lyrics)

def main():

    all_genres = get_all_genres()

    genre_lyrics = add_lyrics_to_genres(all_genres)

    write_output(genre_lyrics)


if __name__ == "__main__":
    main()
