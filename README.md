# imdb_review_restapi
Python 3.6 with "requests" package <br>
This is a test program which takes couple of command line argument<br>
as name of movie and omdbkey and returns rotten tomatoes scoring.<br>
It uses the RESTful API of omdbapi to fetch the scoring, if<br>
doesn't find it uses the imdb ratings<br>

This program needs connectivity with internet to reach out www.omdbiapi.com<br>
  Author:  Madhur<br>
  Email :  talktomadhur@gmail.com<br>
  Year  :  Jan, 2019<br>
  
Sample output of restapi query<br>
{"Title":"Titanic","Year":"1997","Rated":"PG-13","Released":"19 Dec 1997","Runtime":"194 min","Genre":"Drama, Romance","Director":"James Cameron","Writer":"James Cameron","Actors":"Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates","Plot":"A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.","Language":"English, Swedish","Country":"USA","Awards":"Won 11 Oscars. Another 111 wins & 77 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.8/10"},{"Source":"Rotten Tomatoes","Value":"89%"},{"Source":"Metacritic","Value":"75/100"}],"Metascore":"75","imdbRating":"7.8","imdbVotes":"919,766","imdbID":"tt0120338","Type":"movie","DVD":"10 Sep 2012","BoxOffice":"N/A","Production":"Paramount Pictures","Website":"http://www.titanicmovie.com/","Response":"True"}<br><br>
omdb key can be generated from "http://omdbapi.com/"api

