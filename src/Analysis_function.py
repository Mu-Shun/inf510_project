import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
conn = sqlite3.connect('data/MLB.db')
cur = conn.cursor()

def All_Star_team(year): 
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_player.Name, MLB_stat_player.Wins_Above_Replacement FROM MLB_stat_player WHERE MLB_stat_player.Year = " + str(year) + " ORDER BY Wins_Above_Replacement DESC")
    results_WAR = cur.fetchall()
    cur.execute("SELECT MLB_field_stat_player.Name , MLB_field_stat_player.Defensive_Wins_Above_Replacement, MLB_field_stat_player.Position\
                FROM MLB_field_stat_player WHERE MLB_field_stat_player.Year = " + str(year) + " and MLB_field_stat_player.Games_Played > 81 ORDER BY Defensive_Wins_Above_Replacement DESC")
    results_DWAR = cur.fetchall()
    dic_DWAR = {}
    for i in range(len(results_DWAR)):
        dic_DWAR[results_DWAR[i][0]] = [results_DWAR[i][1], results_DWAR[i][2]]
    dic_Annual_All_Star_team = {}
    position_list = ['C', '1B' , '2B', '3B', 'SS', 'CF', 'RF', 'LF']
    for i in range(len(results_WAR)):
        if results_WAR[i][0] in dic_DWAR:
            total = results_WAR[i][1] + dic_DWAR[results_WAR[i][0]][0]
            if dic_DWAR[results_WAR[i][0]][1] not in dic_Annual_All_Star_team:
                dic_Annual_All_Star_team[dic_DWAR[results_WAR[i][0]][1]] = [results_WAR[i][0], total]
            elif total > dic_Annual_All_Star_team[dic_DWAR[results_WAR[i][0]][1]][1]:
                dic_Annual_All_Star_team[dic_DWAR[results_WAR[i][0]][1]] = [results_WAR[i][0], total]
    return dic_Annual_All_Star_team

def All_Star_team_Pitcher(year): 
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_pitcher.Name, MLB_stat_pitcher.Wins_Above_Replacement\
                FROM MLB_stat_pitcher WHERE MLB_stat_pitcher.Year = " + str(year) + " ORDER BY Wins_Above_Replacement DESC")
    results_WAR = cur.fetchall()
    return results_WAR

def All_Star_Specific_Team(year, team): 
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_player.Name, MLB_stat_player.Wins_Above_Replacement\
                FROM MLB_stat_player WHERE MLB_stat_player.Year = " + str(year) + " and MLB_stat_player.Team = " + "'" + str(team) + "'" + \
                "ORDER BY Wins_Above_Replacement DESC")
    results_WAR = cur.fetchall()
    cur.execute("SELECT MLB_field_stat_player.Name , MLB_field_stat_player.Defensive_Wins_Above_Replacement, MLB_field_stat_player.Position\
                FROM MLB_field_stat_player WHERE MLB_field_stat_player.Year = " + str(year) + " and MLB_field_stat_player.Games_Played > 81 \
                and MLB_field_stat_player.Team = " + "'" + str(team) + "'" + " ORDER BY Defensive_Wins_Above_Replacement DESC")
    results_DWAR = cur.fetchall()
    dic_DWAR = {}
    for i in range(len(results_DWAR)):
        dic_DWAR[results_DWAR[i][0]] = [results_DWAR[i][1], results_DWAR[i][2]]
    dic_Annual_All_Star_team = {}
    position_list = ['C', '1B' , '2B', '3B', 'SS', 'CF', 'RF', 'LF']
    for i in range(len(results_WAR)):
        if results_WAR[i][0] in dic_DWAR:
            total = results_WAR[i][1] + dic_DWAR[results_WAR[i][0]][0]
            if dic_DWAR[results_WAR[i][0]][1] not in dic_Annual_All_Star_team:
                dic_Annual_All_Star_team[dic_DWAR[results_WAR[i][0]][1]] = [results_WAR[i][0], total]
            elif total > dic_Annual_All_Star_team[dic_DWAR[results_WAR[i][0]][1]][1]:
                dic_Annual_All_Star_team[dic_DWAR[results_WAR[i][0]][1]] = [results_WAR[i][0], total]
    return dic_Annual_All_Star_team

def All_Star_Specific_Team_Pitcher(year, team): 
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_pitcher.Name, MLB_stat_pitcher.Wins_Above_Replacement\
                FROM MLB_stat_pitcher WHERE MLB_stat_pitcher.Year = " + str(year) + " \
                and MLB_stat_pitcher.Team = " + "'" + str(team) + "'" + "ORDER BY Wins_Above_Replacement DESC")
    results_WAR = cur.fetchall()
    return results_WAR
    
def get_All_Period_Star_Specific_Team(team):
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    dic_All_Period_Star_Specific_Team = {}
    best_pitcer = []
    for i in range(1980, 2020):
        dic_temp = All_Star_Specific_Team(i, team)
        for j in dic_temp:
            if j not in dic_All_Period_Star_Specific_Team:
                dic_All_Period_Star_Specific_Team[j] = dic_temp[j] + [i]
            elif dic_temp[j][1] > dic_All_Period_Star_Specific_Team[j][1]:
                dic_All_Period_Star_Specific_Team[j] = [dic_temp[j][0], dic_temp[j][1], i]
        if not best_pitcer:
            try:
                best_pitcer = list(All_Star_Specific_Team_Pitcher(i, team)[0]) + [i]
            except:
                continue
        elif list(All_Star_Specific_Team_Pitcher(i, team)[0])[1] > best_pitcer[1]:
            best_pitcer = list(All_Star_Specific_Team_Pitcher(i, team)[0]) + [i]
    dic_All_Period_Star_Specific_Team['P'] = best_pitcer
    return dic_All_Period_Star_Specific_Team

def historical_all_star():
    dic_All_Period_Star_team = {}
    Best_Pitcher = tuple()
    for i in range(1980, 2020):
        dic_temp = All_Star_team(i)
        for j in dic_temp:
            if j not in dic_All_Period_Star_team:
                dic_All_Period_Star_team[j] = dic_temp[j] + [i]
            elif dic_temp[j][1] > dic_All_Period_Star_team[j][1]:
                dic_All_Period_Star_team[j] = [dic_temp[j][0], dic_temp[j][1], i]
        if not Best_Pitcher:
            Best_Pitcher = list(All_Star_team_Pitcher(i)[0]) + [i]
        elif All_Star_team_Pitcher(i)[0][1] > Best_Pitcher[1]:
            Best_Pitcher = list(All_Star_team_Pitcher(i)[0]) + [i]
    dic_All_Period_Star_team['P'] = Best_Pitcher
    return dic_All_Period_Star_team

def country_count():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_personal_detail_id.birth_country, count(MLB_personal_detail_id.birth_country)\
            FROM MLB_personal_detail_id  group by MLB_personal_detail_id.birth_country ORDER BY count(MLB_personal_detail_id.birth_country) DESC")
    country = cur.fetchall()
    return country

def state_count():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_personal_detail_id.birth_state, count(MLB_personal_detail_id.birth_state)\
            FROM MLB_personal_detail_id  group by MLB_personal_detail_id.birth_state ORDER BY count(MLB_personal_detail_id.birth_state) DESC")
    state = cur.fetchall()
    return state

def city_count():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_personal_detail_id.birth_city, count(MLB_personal_detail_id.birth_city)\
            FROM MLB_personal_detail_id  group by MLB_personal_detail_id.birth_city ORDER BY count(MLB_personal_detail_id.birth_city) DESC")
    city = cur.fetchall()
    return city

def expect_year_of_player():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_player.Name, count(MLB_stat_player.Name)\
            FROM MLB_stat_player group by MLB_stat_player.Name \
            ORDER BY count(MLB_stat_player.Name) DESC")
    Name = cur.fetchall()
    total_year = 0
    for i in Name:
        total_year = total_year + i[1]
    print("Expect year that a good player can be employed in MLB : ", total_year/len(Name))
    return Name

def expect_year_of_pitcher():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_pitcher.Name, count(MLB_stat_pitcher.Name)\
            FROM MLB_stat_pitcher group by MLB_stat_pitcher.Name \
            ORDER BY count(MLB_stat_pitcher.Name) DESC")
    Pitcher = cur.fetchall()
    total_year = 0
    for i in Pitcher:
        total_year = total_year + i[1]
    print("Expect year that a good pitcher can be employed in MLB : ", total_year/len(Pitcher))
    return Pitcher

def expect_year_of_good_player():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_year_player.Name, count(MLB_year_player.Name)\
            FROM MLB_year_player group by MLB_year_player.Name \
            ORDER BY count(MLB_year_player.Name) DESC")
    Name_year = cur.fetchall()
    total_year = 0
    for i in Name_year:
        total_year = total_year + i[1]
    print("The Expect year that a good player can be ranked in the top 100 of AVG/ERA : ", total_year/len(Name_year))
    return Name_year

def expect_year_of_good_pitcher():
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_year_pitcher.Name, count(MLB_year_pitcher.Name)\
            FROM MLB_year_pitcher group by MLB_year_pitcher.Name \
            ORDER BY count(MLB_year_pitcher.Name) DESC")
    Name_year = cur.fetchall()
    total_year = 0
    for i in Name_year:
        total_year = total_year + i[1]
    print("The Expect year that a good pitcher can be ranked in the top 100 of AVG/ERA : ", total_year/len(Name_year))
    return Name_year

def total_WAR(year):
    conn = sqlite3.connect('data/MLB.db')
    cur = conn.cursor()
    cur.execute("SELECT MLB_stat_player.Team , sum(MLB_stat_player.Wins_Above_Replacement)\
            FROM MLB_stat_player WHERE MLB_stat_player.Year = " + str(year) + " group by MLB_stat_player.Team ORDER BY sum(MLB_stat_player.Wins_Above_Replacement) DESC")
    results_team = cur.fetchall()
    return results_team
