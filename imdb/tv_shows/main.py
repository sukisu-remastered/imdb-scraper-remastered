import requests
from bs4 import BeautifulSoup
import time

from tvshow import getTVShows
from tvshowrating import getTVRatings
from tvshowvotings import getVotesTV

#tvDictionary = {}
#intVotings = []
#all_titles = []
#floatRating = []
def tvDict(genre):
    all_titles = getTVShows(genre)
    intVotings = getVotesTV(genre)
    floatRatings = getTVRatings(genre)
    tvDictionary = dict(zip(all_titles,zip(floatRatings, intVotings)))
    print(tvDictionary)
    


tvDict('comedy')
