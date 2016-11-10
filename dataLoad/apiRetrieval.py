import requests 

data = ''
with open("txtonly.txt", "r") as movieString:
    global data
    data = movieString.read().replace('\n', '')
    data = data.split("linebrk")

class Movie:
    def __init__(self, title, year, rated, runtime, imdbRating, tomatoMeter, tomatoConsensus, genre, director, actors, metascore, poster, movType, avg, website, plot):
        self.title = title
        self.year = year
        self.rated = rated
        self.runtime = runtime
        self.imdbRating = imdbRating
        self.tomatoMeter = tomatoMeter
        self.tomatoConsensus = tomatoConsensus
        self.genre = genre
        self.director = director
        self.actors = actors
        self.metascore = metascore
        self.poster = poster
        self.movType = movType
        self.avg = avg
        self.website = website
        self.plot = plot

movies = []

import tmdbsimple as tmdb
tmdb.API_KEY = "0a2c6dbffb29cf4e880ed6985f5a7233"
search = tmdb.Search()

from socket import error as SocketError
import errno
def getMovieInfo(movieName):
    movie = movieName.strip()
    url = "http://www.omdbapi.com/?t=" + movie + "&y=&plot=short&r=json&callback=?&tomatoes=true"
    url2 = "http://api.themoviedb.org/3/search/movie?query=" + movie + "&api_key=0a2c6dbffb29cf4e880ed6985f5a7233" 
    try:
        response = requests.get(url)
        almostReadyResponse = response.content[2:-2]
        readyResponse = eval(almostReadyResponse)
        return(readyResponse)
    except SocketError as e:
        if e.errno != errno.ECONNRESET:
            raise
        pass

import tmdbsimple as tmdb
tmdb.API_KEY = "0a2c6dbffb29cf4e880ed6985f5a7233"
search = tmdb.Search()
def getMoviePoster(movie):
    posterStart = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
    try: 
        response = search.movie(query=movie)
        if type(search.results) is list:
            if search.results[0].get('poster_path'):
                return posterStart + search.results[0].get('poster_path')
    except (SocketError, IndexError) as e: 
        pass

import re
def changeAttributeTypes(movie):
    try:   
        movie["Poster"] = getMoviePoster(movie)
    except ValueError:
        movie["Poster"] = 0
        pass
    try:
        movie["imdbRating"] = float(movie["imdbRating"])
    except ValueError:
        movie["imdbRating"] = 0 
        pass
    try:    
        movie["tomatoMeter"] = int(movie["tomatoMeter"])
    except ValueError:
        movie["tomatoMeter"] = 0
        pass    
    try:
        movie["tomatoUserMeter"] = int(movie["tomatoUserMeter"])
    except ValueError:
        movie["tomatoUserMeter"] = 0
        pass
    try:    
        movie["Year"] = int(movie["Year"])
    except ValueError:
        movie["Year"] = 0
        pass
    try:
        movie["Metascore"] = int(movie["Metascore"])
    except ValueError:
        movie["Metascore"] = 0
        pass
    try:
        divideBy = 0
        if movie["Metascore"] != 0:
            divideBy += 1
        if movie["tomatoMeter"] != 0:
            divideBy += 1
        if movie["imdbRating"] != 0:
            divideBy += 1
        
        movie["average"] = round(((movie["Metascore"] + movie["tomatoMeter"] + (movie["imdbRating"] * 10)) / divideBy), 1)
    except ZeroDivisionError:
        movie["average"] = 0
        pass
    try:
        runtime = movie["Runtime"]
        runtime = re.findall('\d+', runtime)
        if int(runtime[0]) > 60:
            movie["kind"] = "movie"
        else:
            movie["kind"] = "show"
    except IndexError:
        pass
    return movie 
previousMovie = "startValue"
import time
def getAllMovieInfo(aList):
    global movies
    global previousMovie
    x = 0
    for movie in aList:
        dictTemplate = {"model": "nfs.Movie", "pk": x, "fields": "none"}
        addThis =  getMovieInfo(movie)
        if addThis['Response'] is 'True':        
           dictTemplate["fields"] = changeAttributeTypes(addThis) 
           if dictTemplate["fields"] != previousMovie["fields"]:
               movies.append(dictTemplate)
               print(addThis["Title"])
               x += 1
        previousMovie = dictTemplate                
        time.sleep(.10)
        # API only accepts 40 calls per 10 seconds

getAllMovieInfo(data)

import json
with open("ready.json", "w") as ready:
   json.dump(movies, ready) 

# cannot add string + dict
