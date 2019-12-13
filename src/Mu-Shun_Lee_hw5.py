import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import argparse

def run_soup(year):
    r = requests.get('http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/'+ str(year))
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def run_soup2(year):
    r = requests.get('http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/'+ str(year) + '/start/51')
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def player_info(year,year2):
    dic_year = {}
    dic = {}
    for k in range(year, year2 + 1):
        soup = run_soup(k)
        main_table = soup.findAll('table', {'cellpadding' : "3"})[0]
        main_body = main_table.findAll('tr')
        for i in range(len(main_body)):
            if len(main_body[i].findAll('td')) != 16 or  main_body[i].findAll('td')[2].text == 'YRS':
                continue
            name = main_body[i].findAll('td')[1].text
            url = main_body[i].findAll('td')[1].find('a').attrs['href']
            games = float(main_body[i].findAll('td')[3].text)
            AB = float(main_body[i].findAll('td')[4].text)
            R = float(main_body[i].findAll('td')[5].text)
            BaseHit = float(main_body[i].findAll('td')[6].text)
            BaseHit2 = float(main_body[i].findAll('td')[7].text)
            BaseHit3 = float(main_body[i].findAll('td')[8].text)
            HR = float(main_body[i].findAll('td')[9].text)
            RBI = float(main_body[i].findAll('td')[10].text)
            BB = float(main_body[i].findAll('td')[11].text)
            SO = float(main_body[i].findAll('td')[12].text)
            SB = float(main_body[i].findAll('td')[13].text)
            CS = float(main_body[i].findAll('td')[14].text)
            BA = float(main_body[i].findAll('td')[15].text)
            dic[name] = [url, games, AB, R, BaseHit, BaseHit2, BaseHit3, HR, RBI, BB, SO, SB, CS, BA]
        soup = run_soup2(k)
        main_table = soup.findAll('table', {'cellpadding' : "3"})[0]
        main_body = main_table.findAll('tr')
        for i in range(len(main_body)):
            if len(main_body[i].findAll('td')) != 16 or  main_body[i].findAll('td')[2].text == 'YRS':
                continue
            name = main_body[i].findAll('td')[1].text
            url = main_body[i].findAll('td')[1].find('a').attrs['href']
            games = float(main_body[i].findAll('td')[3].text)
            AB = float(main_body[i].findAll('td')[4].text)
            R = float(main_body[i].findAll('td')[5].text)
            BaseHit = float(main_body[i].findAll('td')[6].text)
            BaseHit2 = float(main_body[i].findAll('td')[7].text)
            BaseHit3 = float(main_body[i].findAll('td')[8].text)
            HR = float(main_body[i].findAll('td')[9].text)
            RBI = float(main_body[i].findAll('td')[10].text)
            BB = float(main_body[i].findAll('td')[11].text)
            SO = float(main_body[i].findAll('td')[12].text)
            SB = float(main_body[i].findAll('td')[13].text)
            CS = float(main_body[i].findAll('td')[14].text)
            BA = float(main_body[i].findAll('td')[15].text)
            dic[name] = [url, games, AB, R, BaseHit, BaseHit2, BaseHit3, HR, RBI, BB, SO, SB, CS, BA]
        dic_year[k] = dic
        dic = {}
    return dic_year

def run_soup_pitcher(year):
    r = requests.get('http://www.espn.com/mlb/history/leaders/_/type/pitching/breakdown/season/year/'+ str(year))
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def run_soup_pitcher2(year):
    r = requests.get('http://www.espn.com/mlb/history/leaders/_/type/pitching/breakdown/season/year/'+ str(year) + '/start/51')
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def pitcher_info(year,year2):
    dic_year = {}
    dic = {}
    for k in range(year, year2 + 1):
        soup = run_soup_pitcher(k)
        main_table = soup.findAll('table', {'cellpadding' : "3"})[0]
        main_body = main_table.findAll('tr')
        for i in range(len(main_body)):
            if len(main_body[i].findAll('td')) != 16 or  main_body[i].findAll('td')[2].text == 'YRS':
                continue
            name = main_body[i].findAll('td')[1].text
            url = main_body[i].findAll('td')[1].find('a').attrs['href']
            games = int(main_body[i].findAll('td')[3].text)
            games_start = int(main_body[i].findAll('td')[4].text)
            complete_games = int(main_body[i].findAll('td')[5].text)
            shout_out = int(main_body[i].findAll('td')[6].text)
            inning_pitched = float(main_body[i].findAll('td')[7].text)
            hits = int(main_body[i].findAll('td')[8].text)
            earned_runs = int(main_body[i].findAll('td')[9].text)
            BB = int(main_body[i].findAll('td')[10].text)
            SO = int(main_body[i].findAll('td')[11].text)
            W = int(main_body[i].findAll('td')[12].text)
            L = int(main_body[i].findAll('td')[13].text)
            SV = int(main_body[i].findAll('td')[14].text)
            ERA = float(main_body[i].findAll('td')[15].text)
            dic[name] = [url, games, games_start, complete_games, shout_out, inning_pitched, hits, earned_runs\
                         , BB, SO, W, L, SV, ERA]
        soup = run_soup_pitcher2(k)
        main_table = soup.findAll('table', {'cellpadding' : "3"})[0]
        main_body = main_table.findAll('tr')
        for i in range(len(main_body)):
            if len(main_body[i].findAll('td')) != 16 or  main_body[i].findAll('td')[2].text == 'YRS':
                continue
            name = main_body[i].findAll('td')[1].text
            url = main_body[i].findAll('td')[1].find('a').attrs['href']
            games = int(main_body[i].findAll('td')[3].text)
            games_start = int(main_body[i].findAll('td')[4].text)
            complete_games = int(main_body[i].findAll('td')[5].text)
            shout_out = int(main_body[i].findAll('td')[6].text)
            inning_pitched = float(main_body[i].findAll('td')[7].text)
            hits = int(main_body[i].findAll('td')[8].text)
            earned_runs = int(main_body[i].findAll('td')[9].text)
            BB = int(main_body[i].findAll('td')[10].text)
            SO = int(main_body[i].findAll('td')[11].text)
            W = int(main_body[i].findAll('td')[12].text)
            L = int(main_body[i].findAll('td')[13].text)
            SV = int(main_body[i].findAll('td')[14].text)
            ERA = float(main_body[i].findAll('td')[15].text)
            dic[name] = [url, games, games_start, complete_games, shout_out, inning_pitched, hits, earned_runs\
                         , BB, SO, W, L, SV, ERA]
        dic_year[k] = dic
        dic = {}
    return dic_year

def run_soup_player_stats(url):
    url_temp = url
    url_temp = url_temp.replace('/_/', '/stats/_/')
    r = requests.get(url_temp)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def player_stats(name, url):
    dic_player = {}
    dic = {}
    soup = run_soup_player_stats(url)
    main_table = soup.findAll('table', {'cellpadding' : "3"})[0]
    main_body = main_table.findAll('tr')
    for k in range(len(main_body)):
        year_content = main_body[k].findAll('td')
        if len(year_content[0].text) != 4 or year_content[0].text == 'YEAR':
            continue
        else:
            year = int(year_content[0].text)
            team = year_content[1].text
            games_played = int(year_content[2].text)
            AB = int(year_content[3].text)
            R = int(year_content[4].text)
            BaseHit = int(year_content[5].text)
            BaseHit2 = int(year_content[6].text)
            BaseHit3 = int(year_content[7].text)
            HR = int(year_content[8].text)
            RBI = int(year_content[9].text)
            BB = int(year_content[10].text)
            SO = int(year_content[11].text)
            SB = int(year_content[12].text)
            CS = int(year_content[13].text)
            BA = float(year_content[14].text)
            OBP = float(year_content[15].text)
            SLG = float(year_content[16].text)
            OPS = float(year_content[17].text)
            WAR = float(year_content[18].text)
            dic[year] = [team, games_played, AB, R, BaseHit, BaseHit2, BaseHit3, HR, RBI, BB, SO, SB, CS, BA, OBP, SLG, OPS, WAR]
    dic_player[name] = dic
    return dic_player

def pitcher_stats(name, url):
    dic_player = {}
    dic = {}
    soup = run_soup_player_stats(url)
    main_table = soup.findAll('table', {'cellpadding' : "3"})
    main_body = main_table[0].findAll('tr')
    for k in range(len(main_body)):
        year_content = main_body[k].findAll('td')
        if len(year_content[0].text) != 4 or year_content[0].text == 'YEAR':
            continue
        else:
            year = int(year_content[0].text)
            team = year_content[1].text
            games_played = int(year_content[2].text)
            games_start = int(year_content[3].text)
            complete = int(year_content[4].text)
            Shutouts = int(year_content[5].text)
            if year_content[6].text == '--':
                Innings_Pitched = 0
            else:
                Innings_Pitched = float(year_content[6].text)
            Hits = int(year_content[7].text)
            Runs = int(year_content[8].text)
            Earned_Runs = int(year_content[9].text)
            HR = int(year_content[10].text)
            BB = int(year_content[11].text)
            SO = int(year_content[12].text)
            try:
                W = int(year_content[13].text)
            except:
                W = 0
            try:
                L = int(year_content[14].text)
            except:
                L = 0
            try:
                SV = int(year_content[15].text)
            except:
                SV = 0
            try:
                HLD = float(year_content[16].text)
            except:
                HLD = 0
            try:
                BLSV = int(year_content[17].text)
            except:
                BLSV = 0
            try:
                WAR = float(year_content[18].text)
            except:
                WAR = 0
            try:
                WHIP = float(year_content[19].text)
            except:
                if Innings_Pitched == 0:
                    WHIP = 'NA'
                else:
                    WHIP = (BB+Hits)/Innings_Pitched
            try:
                ERA = float(year_content[20].text)
            except:
                if Innings_Pitched == 0:
                    ERA = 'NA'
                else:
                    ERA = 9*(Earned_Runs)/Innings_Pitched
            dic[year] = [team, games_played, games_start, complete, Shutouts, Innings_Pitched, Hits, Runs, Earned_Runs\
                         , HR, BB, SO, W, L, SV, HLD, BLSV, WAR, WHIP, ERA]
    dic_player[name] = dic
    return dic_player

def run_soup_player_fielding_stats(url):
    url_temp = url
    url_temp = url_temp[:url_temp.rfind('/')]
    url_temp = url_temp.replace('/_/', '/stats/_/') + '/type/fielding'
    r = requests.get(url_temp)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup


def player_fielding_stats(name, url):
    dic_player = {}
    dic = {}
    soup = run_soup_player_fielding_stats(url)
    main_table = soup.findAll('table', {'cellpadding': "3"})[0]
    main_body = main_table.findAll('tr')
    for k in range(len(main_body)):
        year_content = main_body[k].findAll('td')
        if len(year_content[0].text) != 4 or year_content[0].text == 'YEAR':
            continue
        else:
            year = int(year_content[0].text)
            team = year_content[1].text
            position = year_content[2].text
            games_played = int(year_content[3].text)
            games_started = int(year_content[4].text)
            if year_content[5].text == '--':
                innings = 0
            else:
                innings = int(year_content[5].text)
            Total_Chances = int(year_content[6].text)
            Putouts = int(year_content[7].text)
            Assists = int(year_content[8].text)
            Errors = int(year_content[9].text)
            Doubles = int(year_content[10].text)
            Fielding_Percentage = float(year_content[11].text)
            Range_Factor = float(year_content[12].text)
            Zone_Rating = float(year_content[13].text)
            Passed_Balls = year_content[14].text
            Stolen_Bases = year_content[15].text
            Caught_Stealing = year_content[16].text
            Caught_Stealing_Percentage = year_content[17].text
            CERA = year_content[18].text
            DWAR = float(year_content[19].text)
            if year not in dic:
                dic[year] = []
                dic[year].append([position, team, games_played, games_started, innings, Total_Chances, Putouts, Assists, \
                                  Errors, Doubles, Fielding_Percentage, Range_Factor, Zone_Rating, Passed_Balls,
                                  Stolen_Bases \
                                     , Caught_Stealing, Caught_Stealing_Percentage, CERA, DWAR])
            else:
                dic[year].append([position, team, games_played, games_started, innings, Total_Chances, Putouts, Assists, \
                                  Errors, Doubles, Fielding_Percentage, Range_Factor, Zone_Rating, Passed_Balls,
                                  Stolen_Bases \
                                     , Caught_Stealing, Caught_Stealing_Percentage, CERA, DWAR])

    dic_player[name] = dic
    return dic_player

def get_personal_detail_from_API(name):
    k = str("http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part=" + "'"+ name + "'")
    response = requests.get(k)
    return response.json()['search_player_all']['queryResults']['row']

def get_personal_detail_from_API_with_ID(ID):
    k = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id=" + "'"+ str(ID) + "'"
    response = requests.get(k)
    return response.json()['player_info']['queryResults']['row']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-source", choices=["local", "remote", "test"], help="where data should be gotten from")
    args = parser.parse_args()
    
    location = args.source

    if location == "local":
        try:
            conn = sqlite3.connect('../data/MLB.db')
            cur = conn.cursor()
            print('Connect Local')
        except:
            print('No Local')
    elif location == "remote":
        print('Run Remote')
        players_dic = player_info(1980,2019)
        pitcher_dic = pitcher_info(1980,2019)

        # Get player's stats
        player_url_dic = {}
        for i in players_dic:
            for j in players_dic[i]:
                if j not in player_url_dic:
                    player_url_dic[j] = players_dic[i][j][0]
        player_stats_dic = {}
        for i in player_url_dic:
            player_stats_dic[i] = player_stats(i, player_url_dic[i])[i]

        # Get player's fielding stats
        player_field_stats_dic = {}
        for i in player_url_dic:
            player_field_stats_dic[i] = player_fielding_stats(i, player_url_dic[i])[i]

        # Get pitcher's stats
        pitcher_url_dic = {}
        for i in pitcher_dic:
            for j in pitcher_dic[i]:
                if j not in pitcher_url_dic:
                    pitcher_url_dic[j] = pitcher_dic[i][j][0]
        pitcher_stats_dic = {}
        for i in pitcher_url_dic:
            pitcher_stats_dic[i] = pitcher_stats(i, pitcher_url_dic[i])[i]

        # All baseball stars' personal detailed data from API (if attainable)
        personal_details_dictionary = {}
        for i in player_url_dic:
            try:
                personal_details_dictionary[i] = get_personal_detail_from_API(i)
            except:
                continue
        for i in pitcher_url_dic:
            try:
                personal_details_dictionary[i] = get_personal_detail_from_API(i)
            except:
                continue

        personal_details_dictionary_id = {}
        for i in personal_details_dictionary:
            try:
                ID = personal_details_dictionary[i]['player_id']
                personal_details_dictionary_id[ID] = get_personal_detail_from_API_with_ID(ID)
            except:
                continue

        #players_dic
        #pitcher_dic
        #player_stats_dic
        #pitcher_stats_dic
        #player_field_stats_dic
        #personal_details_dictionary
        #personal_details_dictionary_id

        conn = sqlite3.connect('MLB.db')
        cur = conn.cursor()

        cur.execute("CREATE TABLE MLB_year_player(Year INTEGER, Name TEXT, Url TEXT, Games_Played INTEGER, At_Bats INTEGER, \
                        Runs INTERGER, Hits INTEGER, Doubles INTEGER, Triples INTEGER, Home_Runs INTEGER, Runs_Batted_In INTEGER, \
                        Walks INTEGER, Strikeouts INTEGER, Stolen_Base INTEGER, Caught_Stealing INTEGER, Batting_Average FLOAT);")
        query = """insert into MLB_year_player (Year, Name, Url, Games_Played, At_Bats, Runs, Hits, Doubles, Triples, Home_Runs, \
                    Runs_Batted_In, Walks, Strikeouts, Stolen_Base, Caught_Stealing, Batting_Average) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in players_dic:
            for j in players_dic[i]:
                cur.execute(query, (i, j, players_dic[i][j][0], players_dic[i][j][1], players_dic[i][j][2], players_dic[i][j][3]\
                                   , players_dic[i][j][4], players_dic[i][j][5], players_dic[i][j][6], players_dic[i][j][7]\
                                   , players_dic[i][j][8], players_dic[i][j][9], players_dic[i][j][10], players_dic[i][j][11]\
                                   , players_dic[i][j][12], players_dic[i][j][13]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_year_pitcher(Year INTEGER, Name TEXT, Url TEXT, Games_Played INTEGER, Games_Start INTEGER, \
                        Complete_Games INTERGER, Shutouts INTEGER, Inning_Pitched FLOAT, Hits INTEGER, Earned_Runs INTEGER, Walks INTEGER, \
                        Strikeouts INTEGER, Wins INTEGER, Losses INTEGER, Saves INTEGER, Earned_Runs_Average FLOAT);")
        query = """insert into MLB_year_pitcher (Year, Name, Url, Games_Played, Games_Start, Complete_Games, Shutouts,\
                    Inning_Pitched, Hits, Earned_Runs, Walks, Strikeouts, Wins, Losses, Saves, Earned_Runs_Average) \
                    values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in pitcher_dic:
            for j in pitcher_dic[i]:
                cur.execute(query, (i, j, pitcher_dic[i][j][0], pitcher_dic[i][j][1], pitcher_dic[i][j][2], pitcher_dic[i][j][3]\
                                   , pitcher_dic[i][j][4], pitcher_dic[i][j][5], pitcher_dic[i][j][6], pitcher_dic[i][j][7]\
                                   , pitcher_dic[i][j][8], pitcher_dic[i][j][9], pitcher_dic[i][j][10], pitcher_dic[i][j][11]\
                                   , pitcher_dic[i][j][12], pitcher_dic[i][j][13]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_stat_player(Name TEXT, Year INTEGER, Team TEXT, Games_Played INTEGER, At_Bats INTEGER, \
                        Runs INTERGER, Hits INTEGER, Doubles INTEGER, Triples INTEGER, Home_Runs INTEGER, Runs_Batted_In INTEGER, Walks INTEGER, Strikeouts INTEGER, \
                        Stolen_Base INTEGER, Caught_Stealing INTEGER, Batting_Average FLOAT, On_Base_Percentage FLOAT, Slugging_Percentage FLOAT,\
                        OPS FLOAT, Wins_Above_Replacement FLOAT);")
        query = """insert into MLB_stat_player (Name, Year, Team, Games_Played, At_Bats, Runs, Hits, Doubles, Triples, Home_Runs, \
                    Runs_Batted_In, Walks, Strikeouts, Stolen_Base, Caught_Stealing, Batting_Average, On_Base_Percentage, Slugging_Percentage,\
                    OPS, Wins_Above_Replacement) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in player_stats_dic:
            for j in player_stats_dic[i]:
                cur.execute(query, (i, j, player_stats_dic[i][j][0], player_stats_dic[i][j][1], player_stats_dic[i][j][2], player_stats_dic[i][j][3]\
                                   , player_stats_dic[i][j][4], player_stats_dic[i][j][5], player_stats_dic[i][j][6], player_stats_dic[i][j][7]\
                                   , player_stats_dic[i][j][8], player_stats_dic[i][j][9], player_stats_dic[i][j][10], player_stats_dic[i][j][11]\
                                   , player_stats_dic[i][j][12], player_stats_dic[i][j][13], player_stats_dic[i][j][14], player_stats_dic[i][j][15]\
                                   , player_stats_dic[i][j][16], player_stats_dic[i][j][17]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_stat_pitcher(Name TEXT, Year INTEGER, Team TEXT, Games_Played INTEGER, Games_Start INTEGER, \
                        Complete_Games INTERGER, Shutouts INTEGER, Inning_Pitched FLOAT, Hits INTEGER, Runs INTEGER, Earned_Runs INTEGER, Home_Runs INTEGER, Walks INTEGER, \
                        Strikeouts INTEGER, Wins INTEGER, Losses INTEGER, Saves INTEGER, Holds INTEGER, Blown_Saves INTEGER, \
                        Wins_Above_Replacement FLOAT, Walks_Hits_per_Innings_Pitched FLOAT, Earned_Runs_Average FLOAT);")
        query = """insert into MLB_stat_pitcher (Name, Year, Team, Games_Played, Games_Start, Complete_Games, Shutouts,\
                    Inning_Pitched, Hits, Runs, Earned_Runs, Home_Runs, Walks, Strikeouts, Wins, Losses, Saves, Holds, Blown_Saves, \
                    Wins_Above_Replacement, Walks_Hits_per_Innings_Pitched, Earned_Runs_Average) \
                    values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in pitcher_stats_dic:
            for j in pitcher_stats_dic[i]:
                cur.execute(query, (i, j, pitcher_stats_dic[i][j][0], pitcher_stats_dic[i][j][1], pitcher_stats_dic[i][j][2], pitcher_stats_dic[i][j][3]\
                                   , pitcher_stats_dic[i][j][4], pitcher_stats_dic[i][j][5], pitcher_stats_dic[i][j][6], pitcher_stats_dic[i][j][7]\
                                   , pitcher_stats_dic[i][j][8], pitcher_stats_dic[i][j][9], pitcher_stats_dic[i][j][10], pitcher_stats_dic[i][j][11]\
                                   , pitcher_stats_dic[i][j][12], pitcher_stats_dic[i][j][13], pitcher_stats_dic[i][j][14], pitcher_stats_dic[i][j][15]\
                                   , pitcher_stats_dic[i][j][16], pitcher_stats_dic[i][j][17], pitcher_stats_dic[i][j][18], pitcher_stats_dic[i][j][19]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_field_stat_player(Name TEXT, Year INTEGER, Position TEXT, Team TEXT, Games_Played INTEGER, Games_Started INTEGER, \
                        Innings INTERGER, Total_Chances INTEGER, Putouts INTEGER, Assists INTEGER, Errors INTEGER, Doubles INTEGER, Fielding_Percentage INTEGER, Range_Factor INTEGER, \
                        Zone_Rating INTEGER, Passed_Balls TEXT, Stolen_Bases TEXT, Caught_Stealing TEXT, Caught_Stealing_Percentage TEXT, CERA TEXT, \
                        Defensive_Wins_Above_Replacement FLOAT);")
        query = """insert into MLB_field_stat_player (Name, Year, Position, Team, Games_Played, Games_Started, Innings, Total_Chances, Putouts, Assists, Errors, \
                    Doubles, Fielding_Percentage, Range_Factor, Zone_Rating, Passed_Balls, Stolen_Bases, Caught_Stealing, Caught_Stealing_Percentage, CERA, \
                    Defensive_Wins_Above_Replacement) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in player_field_stats_dic:
            for j in player_field_stats_dic[i]:
                for k in range(len(player_field_stats_dic[i][j])):
                    cur.execute(query, (i, j, player_field_stats_dic[i][j][k][0], player_field_stats_dic[i][j][k][1], player_field_stats_dic[i][j][k][2], player_field_stats_dic[i][j][k][3]\
                                       , player_field_stats_dic[i][j][k][4], player_field_stats_dic[i][j][k][5], player_field_stats_dic[i][j][k][6], player_field_stats_dic[i][j][k][7]\
                                       , player_field_stats_dic[i][j][k][8], player_field_stats_dic[i][j][k][9], player_field_stats_dic[i][j][k][10], player_field_stats_dic[i][j][k][11]\
                                       , player_field_stats_dic[i][j][k][12], player_field_stats_dic[i][j][k][13], player_field_stats_dic[i][j][k][14], player_field_stats_dic[i][j][k][15]\
                                       , player_field_stats_dic[i][j][k][16], player_field_stats_dic[i][j][k][17], player_field_stats_dic[i][j][k][18]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_personal_detail_id(ID TEXT, Name TEXT, birth_country TEXT, college TEXT, height_inches TEXT, age INTEGER, height_feet TEXT,\
                    high_school TEXT, birth_state TEXT, birth_city TEXT, start_date TEXT, jersey_number INTEGER, weight FLOAT);")
        query = """insert into MLB_personal_detail_id (ID, Name, birth_country, college, height_inches, age, height_feet, high_school, \
                    birth_state, birth_city, start_date, jersey_number, weight) values (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in personal_details_dictionary_id:
            cur.execute(query, (i, personal_details_dictionary_id[i]['name_display_first_last'],\
                               personal_details_dictionary_id[i]['birth_country'], personal_details_dictionary_id[i]['college'],\
                               personal_details_dictionary_id[i]['height_inches'], personal_details_dictionary_id[i]['age'],\
                               personal_details_dictionary_id[i]['height_feet'], personal_details_dictionary_id[i]['high_school'],\
                               personal_details_dictionary_id[i]['birth_state'], personal_details_dictionary_id[i]['birth_city'],\
                               personal_details_dictionary_id[i]['start_date'], personal_details_dictionary_id[i]['jersey_number'],\
                               personal_details_dictionary_id[i]['weight']))
        conn.commit()
        print('Complete!')
    else:
        print('Run Test')
        players_dic = player_info(2019,2019)
        pitcher_dic = pitcher_info(2019,2019)

        # Get player's stats
        player_url_dic = {}
        for i in players_dic:
            for j in players_dic[i]:
                if j not in player_url_dic:
                    player_url_dic[j] = players_dic[i][j][0]
        player_stats_dic = {}
        for i in player_url_dic:
            player_stats_dic[i] = player_stats(i, player_url_dic[i])[i]

        # Get player's fielding stats
        player_field_stats_dic = {}
        for i in player_url_dic:
            player_field_stats_dic[i] = player_fielding_stats(i, player_url_dic[i])[i]

        # Get pitcher's stats
        pitcher_url_dic = {}
        for i in pitcher_dic:
            for j in pitcher_dic[i]:
                if j not in pitcher_url_dic:
                    pitcher_url_dic[j] = pitcher_dic[i][j][0]
        pitcher_stats_dic = {}
        for i in pitcher_url_dic:
            pitcher_stats_dic[i] = pitcher_stats(i, pitcher_url_dic[i])[i]

        # All baseball stars' personal detailed data from API (if attainable)
        personal_details_dictionary = {}
        for i in player_url_dic:
            try:
                personal_details_dictionary[i] = get_personal_detail_from_API(i)
            except:
                continue
        for i in pitcher_url_dic:
            try:
                personal_details_dictionary[i] = get_personal_detail_from_API(i)
            except:
                continue

        personal_details_dictionary_id = {}
        for i in personal_details_dictionary:
            try:
                ID = personal_details_dictionary[i]['player_id']
                personal_details_dictionary_id[ID] = get_personal_detail_from_API_with_ID(ID)
            except:
                continue

        #players_dic
        #pitcher_dic
        #player_stats_dic
        #pitcher_stats_dic
        #player_field_stats_dic
        #personal_details_dictionary
        #personal_details_dictionary_id

        conn = sqlite3.connect('MLB.db')
        cur = conn.cursor()

        cur.execute("CREATE TABLE MLB_year_player(Year INTEGER, Name TEXT, Url TEXT, Games_Played INTEGER, At_Bats INTEGER, \
                        Runs INTERGER, Hits INTEGER, Doubles INTEGER, Triples INTEGER, Home_Runs INTEGER, Runs_Batted_In INTEGER, \
                        Walks INTEGER, Strikeouts INTEGER, Stolen_Base INTEGER, Caught_Stealing INTEGER, Batting_Average FLOAT);")
        query = """insert into MLB_year_player (Year, Name, Url, Games_Played, At_Bats, Runs, Hits, Doubles, Triples, Home_Runs, \
                    Runs_Batted_In, Walks, Strikeouts, Stolen_Base, Caught_Stealing, Batting_Average) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in players_dic:
            for j in players_dic[i]:
                cur.execute(query, (i, j, players_dic[i][j][0], players_dic[i][j][1], players_dic[i][j][2], players_dic[i][j][3]\
                                   , players_dic[i][j][4], players_dic[i][j][5], players_dic[i][j][6], players_dic[i][j][7]\
                                   , players_dic[i][j][8], players_dic[i][j][9], players_dic[i][j][10], players_dic[i][j][11]\
                                   , players_dic[i][j][12], players_dic[i][j][13]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_year_pitcher(Year INTEGER, Name TEXT, Url TEXT, Games_Played INTEGER, Games_Start INTEGER, \
                        Complete_Games INTERGER, Shutouts INTEGER, Inning_Pitched FLOAT, Hits INTEGER, Earned_Runs INTEGER, Walks INTEGER, \
                        Strikeouts INTEGER, Wins INTEGER, Losses INTEGER, Saves INTEGER, Earned_Runs_Average FLOAT);")
        query = """insert into MLB_year_pitcher (Year, Name, Url, Games_Played, Games_Start, Complete_Games, Shutouts,\
                    Inning_Pitched, Hits, Earned_Runs, Walks, Strikeouts, Wins, Losses, Saves, Earned_Runs_Average) \
                    values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in pitcher_dic:
            for j in pitcher_dic[i]:
                cur.execute(query, (i, j, pitcher_dic[i][j][0], pitcher_dic[i][j][1], pitcher_dic[i][j][2], pitcher_dic[i][j][3]\
                                   , pitcher_dic[i][j][4], pitcher_dic[i][j][5], pitcher_dic[i][j][6], pitcher_dic[i][j][7]\
                                   , pitcher_dic[i][j][8], pitcher_dic[i][j][9], pitcher_dic[i][j][10], pitcher_dic[i][j][11]\
                                   , pitcher_dic[i][j][12], pitcher_dic[i][j][13]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_stat_player(Name TEXT, Year INTEGER, Team TEXT, Games_Played INTEGER, At_Bats INTEGER, \
                        Runs INTERGER, Hits INTEGER, Doubles INTEGER, Triples INTEGER, Home_Runs INTEGER, Runs_Batted_In INTEGER, Walks INTEGER, Strikeouts INTEGER, \
                        Stolen_Base INTEGER, Caught_Stealing INTEGER, Batting_Average FLOAT, On_Base_Percentage FLOAT, Slugging_Percentage FLOAT,\
                        OPS FLOAT, Wins_Above_Replacement FLOAT);")
        query = """insert into MLB_stat_player (Name, Year, Team, Games_Played, At_Bats, Runs, Hits, Doubles, Triples, Home_Runs, \
                    Runs_Batted_In, Walks, Strikeouts, Stolen_Base, Caught_Stealing, Batting_Average, On_Base_Percentage, Slugging_Percentage,\
                    OPS, Wins_Above_Replacement) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in player_stats_dic:
            for j in player_stats_dic[i]:
                cur.execute(query, (i, j, player_stats_dic[i][j][0], player_stats_dic[i][j][1], player_stats_dic[i][j][2], player_stats_dic[i][j][3]\
                                   , player_stats_dic[i][j][4], player_stats_dic[i][j][5], player_stats_dic[i][j][6], player_stats_dic[i][j][7]\
                                   , player_stats_dic[i][j][8], player_stats_dic[i][j][9], player_stats_dic[i][j][10], player_stats_dic[i][j][11]\
                                   , player_stats_dic[i][j][12], player_stats_dic[i][j][13], player_stats_dic[i][j][14], player_stats_dic[i][j][15]\
                                   , player_stats_dic[i][j][16], player_stats_dic[i][j][17]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_stat_pitcher(Name TEXT, Year INTEGER, Team TEXT, Games_Played INTEGER, Games_Start INTEGER, \
                        Complete_Games INTERGER, Shutouts INTEGER, Inning_Pitched FLOAT, Hits INTEGER, Runs INTEGER, Earned_Runs INTEGER, Home_Runs INTEGER, Walks INTEGER, \
                        Strikeouts INTEGER, Wins INTEGER, Losses INTEGER, Saves INTEGER, Holds INTEGER, Blown_Saves INTEGER, \
                        Wins_Above_Replacement FLOAT, Walks_Hits_per_Innings_Pitched FLOAT, Earned_Runs_Average FLOAT);")
        query = """insert into MLB_stat_pitcher (Name, Year, Team, Games_Played, Games_Start, Complete_Games, Shutouts,\
                    Inning_Pitched, Hits, Runs, Earned_Runs, Home_Runs, Walks, Strikeouts, Wins, Losses, Saves, Holds, Blown_Saves, \
                    Wins_Above_Replacement, Walks_Hits_per_Innings_Pitched, Earned_Runs_Average) \
                    values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in pitcher_stats_dic:
            for j in pitcher_stats_dic[i]:
                cur.execute(query, (i, j, pitcher_stats_dic[i][j][0], pitcher_stats_dic[i][j][1], pitcher_stats_dic[i][j][2], pitcher_stats_dic[i][j][3]\
                                   , pitcher_stats_dic[i][j][4], pitcher_stats_dic[i][j][5], pitcher_stats_dic[i][j][6], pitcher_stats_dic[i][j][7]\
                                   , pitcher_stats_dic[i][j][8], pitcher_stats_dic[i][j][9], pitcher_stats_dic[i][j][10], pitcher_stats_dic[i][j][11]\
                                   , pitcher_stats_dic[i][j][12], pitcher_stats_dic[i][j][13], pitcher_stats_dic[i][j][14], pitcher_stats_dic[i][j][15]\
                                   , pitcher_stats_dic[i][j][16], pitcher_stats_dic[i][j][17], pitcher_stats_dic[i][j][18], pitcher_stats_dic[i][j][19]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_field_stat_player(Name TEXT, Year INTEGER, Position TEXT, Team TEXT, Games_Played INTEGER, Games_Started INTEGER, \
                        Innings INTERGER, Total_Chances INTEGER, Putouts INTEGER, Assists INTEGER, Errors INTEGER, Doubles INTEGER, Fielding_Percentage INTEGER, Range_Factor INTEGER, \
                        Zone_Rating INTEGER, Passed_Balls TEXT, Stolen_Bases TEXT, Caught_Stealing TEXT, Caught_Stealing_Percentage TEXT, CERA TEXT, \
                        Defensive_Wins_Above_Replacement FLOAT);")
        query = """insert into MLB_field_stat_player (Name, Year, Position, Team, Games_Played, Games_Started, Innings, Total_Chances, Putouts, Assists, Errors, \
                    Doubles, Fielding_Percentage, Range_Factor, Zone_Rating, Passed_Balls, Stolen_Bases, Caught_Stealing, Caught_Stealing_Percentage, CERA, \
                    Defensive_Wins_Above_Replacement) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in player_field_stats_dic:
            for j in player_field_stats_dic[i]:
                for k in range(len(player_field_stats_dic[i][j])):
                    cur.execute(query, (i, j, player_field_stats_dic[i][j][k][0], player_field_stats_dic[i][j][k][1], player_field_stats_dic[i][j][k][2], player_field_stats_dic[i][j][k][3]\
                                       , player_field_stats_dic[i][j][k][4], player_field_stats_dic[i][j][k][5], player_field_stats_dic[i][j][k][6], player_field_stats_dic[i][j][k][7]\
                                       , player_field_stats_dic[i][j][k][8], player_field_stats_dic[i][j][k][9], player_field_stats_dic[i][j][k][10], player_field_stats_dic[i][j][k][11]\
                                       , player_field_stats_dic[i][j][k][12], player_field_stats_dic[i][j][k][13], player_field_stats_dic[i][j][k][14], player_field_stats_dic[i][j][k][15]\
                                       , player_field_stats_dic[i][j][k][16], player_field_stats_dic[i][j][k][17], player_field_stats_dic[i][j][k][18]))
        conn.commit()

        cur.execute("CREATE TABLE MLB_personal_detail_id(ID TEXT, Name TEXT, birth_country TEXT, college TEXT, height_inches TEXT, age INTEGER, height_feet TEXT,\
                    high_school TEXT, birth_state TEXT, birth_city TEXT, start_date TEXT, jersey_number INTEGER, weight FLOAT);")
        query = """insert into MLB_personal_detail_id (ID, Name, birth_country, college, height_inches, age, height_feet, high_school, \
                    birth_state, birth_city, start_date, jersey_number, weight) values (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        for i in personal_details_dictionary_id:
            cur.execute(query, (i, personal_details_dictionary_id[i]['name_display_first_last'],\
                               personal_details_dictionary_id[i]['birth_country'], personal_details_dictionary_id[i]['college'],\
                               personal_details_dictionary_id[i]['height_inches'], personal_details_dictionary_id[i]['age'],\
                               personal_details_dictionary_id[i]['height_feet'], personal_details_dictionary_id[i]['high_school'],\
                               personal_details_dictionary_id[i]['birth_state'], personal_details_dictionary_id[i]['birth_city'],\
                               personal_details_dictionary_id[i]['start_date'], personal_details_dictionary_id[i]['jersey_number'],\
                               personal_details_dictionary_id[i]['weight']))
        conn.commit()
        print('Complete!')

if __name__ == "__main__":
    main()
