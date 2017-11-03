import urllib2
from bs4 import BeautifulSoup

url_page = "http://www.espn.com/nba/playbyplay?gameId=400974442"
# url_page ="http://www.bloomberg.com/quote/SPX:IND"
page = urllib2.urlopen(url_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")
name_list = []
time_list = []
# Take out the <div> of name and get its value
name_boxes = soup.find_all("td", attrs={"class": "game-details"})

for name_box in name_boxes:
    name = name_box.text.strip()  # strip() is used to remove starting and trailing
    print name
name_list.append(name)
time_boxes = soup.find_all("td", attrs={"class": "time-stamp"})
for time_box in time_boxes:
    time = time_box.text.strip()
    print time
    time

player_list = [Lonzo Ball, Vander Blue, Andrew Bogut, Corey Brewer, Thomas Bryant, Kentavious Caldwell - Pope, Alex
               Caruso,
               Jordan Clarkson,
               Luol Deng,
               Tyler Ennis,
               Josh Hart,
               Brandon Ingram,
               Kyle Kuzma,
               Brook Lopez,
               Larry Nance Jr.,
               Julius Randle,
               Ivica Zubac]
