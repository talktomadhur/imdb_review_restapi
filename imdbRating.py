# This is a test program which takes couple of command line argument
# as name of movie and omdbkey then feedback to user the rotten
# tomatoes scoring.
# It uses the RESTAPI of omdbapi to fetch the scoring, if
# doesn't find it uses the imdb ratings and classify them
# into rotten tomatoes scoring.
# This program needs connectivity with internet to reach
# out www.omdbiapi.com
# Author:  Madhur
# Email :  talktomadhur@gmail.com
# Year  :  Jan, 2019
# Sample output of restapi query
#{"Title":"Titanic","Year":"1997","Rated":"PG-13","Released":"19 Dec 1997","Runtime":"194 min","Genre":"Drama, Romance","Director":"James Cameron","Writer":"James Cameron","Actors":"Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates","Plot":"A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.","Language":"English, Swedish","Country":"USA","Awards":"Won 11 Oscars. Another 111 wins & 77 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.8/10"},{"Source":"Rotten Tomatoes","Value":"89%"},{"Source":"Metacritic","Value":"75/100"}],"Metascore":"75","imdbRating":"7.8","imdbVotes":"919,766","imdbID":"tt0120338","Type":"movie","DVD":"10 Sep 2012","BoxOffice":"N/A","Production":"Paramount Pictures","Website":"http://www.titanicmovie.com/","Response":"True"}
# omdb key can be generated from "http://omdbapi.com/"
import requests,sys
if len(sys.argv) <=2:
   print('''Usage:
            python imdbRating.py <apikey> <'movie name'>
            "" or '' is required for movie name having space in its name
            example: python imdbRating.py 31dd31a "Speed 2"
                     python imdbRating.py 31dd31a 'Speed 2' ''')
else:
   reqHandle = requests.get("http://www.omdbapi.com/?t=" + sys.argv[2] + "&apikey="+ sys.argv[1])
   if reqHandle.status_code is 200:
      print('Movie name - ' + reqHandle.json().get('Title'))
      if "Rotten Tomatoes" in str(reqHandle.json().get('Ratings')):
          print("Ratings by " + reqHandle.json().get('Ratings')[1].get('Source') + " " + reqHandle.json().get('Ratings')[1].get('Value'))
      else:
           print("Looks like Roten Tomoteos did not have rating here")
           print("Fetching ratings from IMDB directly..")
           print("Ratings by " + reqHandle.json().get('Ratings')[0].get('Source') + " " + reqHandle.json().get('Ratings')[0].get('Value'))
   else:
           print("Retry after sometime or check movie name/omdbkey, there was a bad response from server")
