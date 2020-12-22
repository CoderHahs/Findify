# Findify 🎵

🔗 [https://findify.herokuapp.com/](https://findify.herokuapp.com/) (Sometimes it takes 5 seconds for the page to load, this is because the server is starting up)

Findify helps you find new songs to listen to based on previously liked music. It uses <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> as a backend to do computations involving Locality Sensitive Hashing. Data was fetched using <a href="https://developer.spotify.com/community/showcase/spotify-audio-analysis/">Spotify's Song Analysis API</a>. The app was deployed using <a href="https://www.heroku.com/">Heroku</a>.

Here is a sample of what the Song Analysis API gives:

| acousticness          | artists   | danceability       | duration_ms | energy | explicit | id                     | instrumentalness | key | liveness | loudness            | mode | name          | popularity | release_date | speechiness | tempo   | valence            | year |
| --------------------- | --------- | ------------------ | ----------- | ------ | -------- | ---------------------- | ---------------- | --- | -------- | ------------------- | ---- | ------------- | ---------- | ------------ | ----------- | ------- | ------------------ | ---- |
| 0.0026100000000000003 | ['Drake'] | 0.8909999999999999 | 267067      | 0.625  | 0        | 0wwPcA6wtMf6HUMpIRdeP7 | 0.000176         | 2   | 0.0504   | -7.8610000000000015 | 1    | Hotline Bling | 77         | 2016-05-06   | 0.0558      | 134.967 | 0.5479999999999999 | 2016 |

---

## How Findify Finds Songs Based on Previously Liked Songs

For each instance of song presented, a user is given two choices, either to like the song or to dislike it.

1. If a user dislikes a song

- A randomly selected song that they've never seen before is presented to them.

2. If a user likes a song

- A score based on the current song is generated based on the data given through the Song Analysis data. This score is then hashed using MinHashing. This technique is used to quickly estimating how similar two sets are. It employs the [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) in its calculations:
  > ![Jaccard formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/16331e8b32e275dfb724e1995708aca74c705800)
- Once a score is calculated, we use query a dictionary of MinHashes to find the closest related score based on Locality Sensitive Hashing. The following figure gives a good representation of LSH:  
  ![LSH](https://i.ytimg.com/vi/dgH0NP8Qxa8/hqdefault.jpg)
- On most instances the query would return several similar songs, so a song that hasn't been heard before is randomly chosen from the returned list of similar songs.
