import urllib2
from bs4 import BeautifulSoup


player_list = ["Lonzo Ball",
               "Vander Blue",
               "Andrew Bogut",
               "Corey Brewer",
               "Thomas Bryant",
               "Kentavious Caldwell - Pope",
               "Alex Caruso",
               "Jordan Clarkson",
               "Luol Deng",
               "Tyler Ennis",
               "Josh Hart",
               "Brandon Ingram",
               "Kyle Kuzma",
               "Brook Lopez",
               "Larry Nance Jr.",
               "Julius Randle",
               "Ivica Zubac"]

def getLakerSub(espn_url):
    url_page = espn_url
    # url_page ="http://www.bloomberg.com/quote/SPX:IND"
    page = urllib2.urlopen(url_page)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")
    name_list = []
    time_list = []
    logo_list = []
    # Take out the <div> of name and get its value
    name_boxes = soup.find_all("td", attrs={"class": "game-details"})

    for name_box in name_boxes:
        name = name_box.text.strip()  # strip() is used to remove starting and trailing
        # print name
        name_list.append(name)

    time_boxes = soup.find_all("td", attrs={"class": "time-stamp"})
    for time_box in time_boxes:
        time = time_box.text.strip()
        # print time
        time_list.append(time)

    logo_boxes = soup.find_all("td", attrs={"class": "logo"})
    for logo_box in logo_boxes:
        logo = logo_box.text.strip()
        # print logo
        logo_list.append(logo)

    comb_list = []

    for i in range(0, len(name_list) - 1):
        if "enter" in name_list[i]:
            # if name_list
            name = name_list[i].split()[:2]
            # if name[0] +" "+ name[1] in player_list:
            #     print(name_list[i].split()[:2])
            comb_list.append((time_list[i], name_list[i]))

    # for sub in comb_list:
    #     print(sub)
    return comb_list

#10/19 vs(home) LAC clippers L 92-108
vsClippersSub = getLakerSub("http://www.espn.com/nba/playbyplay?gameId=400974442")

for sub in vsClippersSub:
    print(sub)

#10/20 @(away) PHX suns W 132-130
vsSunsSub = getLakerSub("http://www.espn.com/nba/playbyplay?gameId=400974777")
for sub in vsSunsSub:
    print sub
#10/22 vs NO new orleans L 112-119
vsPelicansSub = getLakerSub("http://www.espn.com/nba/playbyplay?gameId=400974791")

for sub in vsPelicansSub:
    print sub

