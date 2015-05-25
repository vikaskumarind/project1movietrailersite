import webbrowser

#Class to store the details of a movie like story,poster and trailer link

class Movie():
    
    """ Class for movies """

    #Method to initialize the class with the passed paramters 
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
         self.title = movie_title
         self.storyline = movie_storyline
         self.poster_image_url = poster_image
         self.trailer_youtube_url = trailer_youtube


    #Method to open the trailer in a window
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


         
