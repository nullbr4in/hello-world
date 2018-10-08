
# coding: utf-8

# In[172]:


import csv
import os

#Assume that your cwd is set to './User/INF510/hw3'
os.chdir("/Users/Eunhye/INF510/hw3")
print(os.getcwd())

#Get a list of csv files
csv_files = os.listdir()

#Define csv reading function
def read(fname):
    with open(fname, 'r') as f:
        reader = csv.DictReader(f, delimiter = ",")
        csv_list = list(reader)
    return csv_list


# In[173]:


#Checking csv files to read
print(csv_files)

#td = total data
#Put all data lines into a list -> td
td = list()
for f in csv_files:
    eachYear = read(f)
    for dt in eachYear:
        #Convert str vars into int or float in order to use them as operands
        temp_dict = dict()
        temp_dict["action_plays"] = int(dt["action_plays"])
        #Skip if espn_game_id is missing
        if dt["espn_game_id"] == "":
            continue
        else:
            temp_dict["espn_game_id"] = int(float(dt["espn_game_id"]))
        temp_dict["espn_player_id"] = int(dt["espn_player_id"])
        temp_dict["first_name"] = dt["first_name"]
        temp_dict["home_away"] = dt["home_away"]
        temp_dict["last_name"] = dt["last_name"]
        temp_dict["opponent"] = dt["opponent"]
        temp_dict["opposition_score"] = int(dt["opposition_score"])
        temp_dict["pass_EPA"] = float(dt["pass_EPA"])
        temp_dict["penalty_EPA"] = float(dt["penalty_EPA"])
        temp_dict["qb_score"] = int(dt["qb_score"])
        temp_dict["raw_QBR"] = float(dt["raw_QBR"])
        temp_dict["run_EPA"] = float(dt["run_EPA"])
        temp_dict["sack_EPA"] = float(dt["sack_EPA"])
        temp_dict["team_name"] = dt["team_name"]
        temp_dict["total_EPA"] = float(dt["total_EPA"])
        temp_dict["total_QBR"] = float(dt["total_QBR"])
        #Convert the week value into 0 if it is not str
        if dt["week"] == "bowl":
            temp_dict["week"] = 0
        else:
            temp_dict["week"] = int(dt["week"])
        temp_dict["won_lost"] = dt["won_lost"]
        temp_dict["year"] = dt["year"]
        #Append all lines to td
        td.append(temp_dict)

#Checking if all data were read okay
print(len(td))
print(td[1])
print(td[10]['espn_game_id'])
len(td)


# In[174]:


#Define Game class
class Game:
    def __init__(self, gameID, homeAway, oppTeam, team, 
                 wonLost,year, total_QBR, action_plays):
        self.gameID = gameID
        self.homeAway = homeAway
        self.oppTeam = oppTeam
        self.team = team
        self.wonLost = wonLost
        self.year = year
        self.total_QBR = total_QBR
        self.action_plays = action_plays

        


# In[175]:


#Define Player class
class Player:
    def __init__(self,pid,fname,lname,team):
        #Define attributes
        self.pid = pid
        self.fname = fname
        self.lname = lname
        self.team = team
        self.gameList = []
        self.hst_QBR_lost = 0
        self.lst_QBR_won = 100
        self.hst_ap = 0
        self.ng = 0
        self.sum_QBR = 0
        self.avg_QBR = 0
        self.hst_QBR = 0
        self.lst_QBR = 0
        self.hst_QBR_lost_game = None
        self.lst_QBR_won_game = None
        self.hst_ap_game = None
        
    #Define a method that gets the highes value among the games a player played
    def get_highest_total_QBR_from_lost_games(self):
        for game in self.gameList:
            if game.wonLost == "L":
                if self.hst_QBR_lost < game.total_QBR:
                    self.hst_QBR_lost = game.total_QBR
                    self.hst_QBR_lost_game = game
                    
    #Define a method that gets the lowest value among the games a player played
    def get_lowest_total_QBR_from_won_games(self):
        for game in self.gameList:
            if game.wonLost == "W":
                if self.lst_QBR_won > game.total_QBR:
                    self.lst_QBR_won = game.total_QBR
                    self.lst_QBR_won_game = game
                    
    #Define a method that gets the highest value of action plays among the games a player played
    def get_highest_action_plays(self):
        for game in self.gameList:
            if self.hst_ap < game.action_plays:
                self.hst_ap = game.action_plays
                self.hst_ap_game = game
            
    #Define a method to get average QBR among the games
    def get_avg_QBR(self):
        for game in self.gameList:
            self.ng += 1
            self.sum_QBR += game.total_QBR
        self.avg_QBR = self.sum_QBR/self.ng
        
    #Define a method to get the highest QBR among the games a player played
    def get_hst_QBR(self):
        for game in self.gameList:
            if self.hst_QBR < game.total_QBR:
                self.hst_QBR = game.total_QBR
    
    #Define a method to get the lowest QBR among the games played by a player
    def get_lst_QBR(self):
        for game in self.gameList:
            if self.lst_QBR < game.total_QBR:
                self.lst_QBR = game.total_QBR
                
    #Define a method to append games played by a player to the list, gameList
    def appendGameList(self, game):
        self.gameList.append(game)
        
    #Method to print 
    def print_info(self,game):
        print("Player ID:%d" % self.pid)
        print("First name:%s" % self.fname)
        print("Last name:%s" % self.lname)
        print("Team name:%s" % self.team)
        print("Game ID:%d" % game.gameID)
        print("Game home/away:%s" % game.homeAway)
        print("Opponent:%s" % game.oppTeam)
        print("Won or lost:%s" % game.wonLost)
        print("Year:%s" % game.year)

    def print_player_info(self):
        print("Player ID:%d" % self.pid)
        print("First name:%s" % self.fname)
        print("Last name:%s" % self.lname)
        print("Team name:%s" % self.team)
        print("The number of games:%s" % self.ng)
        
    def print_game_info(self, game):
        print("Game ID:%d" % game.gameID)
        print("Game home/away:%s" % game.homeAway)
        print("Opponent:%s" % game.oppTeam)
        print("Won or lost:%s" % game.wonLost)
        print("Year:%s" % game.year)

        


# In[176]:


#Putting player id into a dictionary
dict_pl = dict()

#Creating player instances
for i in range(len(td)):
    pl = td[i]['espn_player_id']
    dict_pl[pl] = Player(td[i]['espn_player_id'], 
                         td[i]['first_name'],
                         td[i]['last_name'],
                         td[i]['team_name'])


# In[177]:


#Creating Game instances 
for i in range(len(td)):
    pl = td[i]['espn_player_id']    
    tmpGame = Game(td[i]['espn_game_id'], 
                   td[i]['home_away'],
                   td[i]['opponent'],
                   td[i]['team_name'],
                   td[i]['won_lost'],
                   td[i]['year'],
                   td[i]['total_QBR'],
                   td[i]['action_plays'])  
    #Add them to the gameList of each player by using player's id
    dict_pl[pl].appendGameList(tmpGame)


# ### Q1.Which player in which game had the highest total_QBR in a loss? What was the value?

# In[178]:


#Run the method to get the highest total QBR for each player
for pl in dict_pl:
    dict_pl[pl].get_highest_total_QBR_from_lost_games()

pid = None
total_highest_QBR_lost = None

#Compare total QBR of each players in order to find the highest total_QBR
for pl in dict_pl:
    if total_highest_QBR_lost == None or total_highest_QBR_lost < dict_pl[pl].hst_QBR_lost:
        total_highest_QBR_lost = dict_pl[pl].hst_QBR_lost
        pid = dict_pl[pl]

print('The highest total QBR in a lost game:',total_highest_QBR_lost)
print('--Player and game info--')
pid.print_info(pid.hst_QBR_lost_game)


#  ### Q2. Which player in which game had the lowest total_QBR in a win? What was the value?

# In[179]:


#Run the method to find the lowest total_QBR for each player
for pl in dict_pl:
    dict_pl[pl].get_lowest_total_QBR_from_won_games()

pid = None
total_lowest_QBR_won = None

#Compare the lowest total_QBR of each player to find the lowest value in a won game
for pl in dict_pl:
    if total_lowest_QBR_won == None or total_lowest_QBR_won > dict_pl[pl].lst_QBR_won:
        total_lowest_QBR_won = dict_pl[pl].lst_QBR_won
        pid = dict_pl[pl]

print('The lowest total QBR in a won game:',total_lowest_QBR_won)
print('--Player and game info--')
pid.print_info(pid.lst_QBR_won_game)


# ### Q3. Which player in which game had the highest number of action_plays?

# In[180]:


#Run a method to find the highest action plays for each player
for pl in dict_pl:
    dict_pl[pl].get_highest_action_plays()

pid = None
highest_actionPlays = None

#Compare action plays of all players to find the highest one
for pl in dict_pl:
    if highest_actionPlays == None or highest_actionPlays < dict_pl[pl].hst_ap:
        highest_actionPlays = dict_pl[pl].hst_ap
        pid = dict_pl[pl]

print('The highest number of action plays:', highest_actionPlays)
print('--Player and game info--')
pid.print_info(pid.hst_ap_game)


# ### Q4. The player with the highest average total_QBR?

# In[181]:


#Run a method to find the average QBR of each player
for pl in dict_pl:
    dict_pl[pl].get_avg_QBR()

pid = None
highest_avg_QBR = None

#Compare average QBR of all player to find the highest one
for pl in dict_pl:
    if highest_avg_QBR == None or highest_avg_QBR < dict_pl[pl].avg_QBR:
        highest_avg_QBR = dict_pl[pl].avg_QBR
        pid = dict_pl[pl]
        
print('The highest average QBR:', highest_avg_QBR)
print('--Player and game info--')
pid.print_player_info()


# ### Extra Credit. What are the highest and lowest total QBR values for players who only started 1 game?

# In[182]:


#Create a list to store players who played only one game
only_game = list()

for pl in dict_pl:
    if dict_pl[pl].ng == 1:
        only_game.append(dict_pl[pl])

#Create variables to store the highest and the lowest QBRs
hst_QBR_oneGame = None
lst_QBR_oneGame = None

#Find the highest QBR among the players who started only one game
for player in only_game:
    if hst_QBR_oneGame == None or hst_QBR_oneGame < player.gameList[0].total_QBR:
        hst_QBR_oneGame = player.gameList[0].total_QBR
        #Store player id to pid_h in order to access the Player object
        pid_h = player

#Find the lowest QBR among the players who started only one game
for player in only_game:
    if lst_QBR_oneGame == None or lst_QBR_oneGame > player.gameList[0].total_QBR:
        lst_QBR_oneGame = player.gameList[0].total_QBR
        pid_l = player

print('The highest value among the players who started 1 game:',hst_QBR_oneGame)
print('--Player & game info--')
pid_h.print_player_info()
pid_h.print_game_info(pid_h.gameList[0])

print('\nThe lowest value among the players who started 1 game:',lst_QBR_oneGame)
print('--Player & game info--')
print(lst_QBR_oneGame)
pid_l.print_player_info()
pid_l.print_game_info(pid_l.gameList[0])

