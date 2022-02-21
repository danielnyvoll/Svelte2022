from debugpy import listen
from flask import Flask, send_from_directory
import operator
import seaborn as sns
import matplotlib.pyplot as plt
from fpl import FPL
import asyncio
import aiohttp
import random
import json

sns.set()

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)


@app.route("/rand")
def hello():
    return (asyncio.run(main()))

#@app.route("/stats")
#def hello():
#    return str(asyncio.run(main()))


def positions_calc(players, first_attr, second_attr=None):
    positions = ['GK', 'DEF', 'MID', 'FWD']
    first_dict = dict({(position, 0) for position in positions})
    second_dict = dict({(position, 0) for position in positions})
    for player in players:
        position = positions[player.element_type-1]
        if first_attr == 'now_cost':
            first_dict[position] += getattr(player, first_attr) / 10
        else:
            first_dict[position] += getattr(player, first_attr)
        if second_attr == 'now_cost':
            second_dict[position] += getattr(player, second_attr) / 10
        else:
            second_dict[position] += 1
    avg_dict = dict({(position, first_dict[position]/second_dict[position]) for position in positions})
    ordered_avg_dict = dict(sorted(avg_dict.items(), key=operator.itemgetter(1), reverse=True))
    return ordered_avg_dict    

def get_top_dict(players, n):
    top_performance = sorted(players, key=lambda x: x.total_points, reverse=True)
    ret_dict = dict()
    for player in top_performance[:n]:
        ret_dict[player.web_name] = player.total_points
    return ret_dict


def get_costs(players, n):
    top_performance = sorted(players, key=lambda x: x.total_points, reverse=True)
    ret_dict = dict()
    for player in top_performance[:n]:
        ret_dict[player.web_name] = player.now_cost / 10
    return ret_dict


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

        # average points per player in each position
        positions_avg_points = positions_calc(players, first_attr='total_points')
        # from this chart, the best formation is 3-4-3

        # average price per player in each position
        positions_avg_prices = positions_calc(players, first_attr='now_cost')
        # we will use this to get the bench players budget (1 GK, 2 DEF, 1 MID) = 20 Millions

        # average points per price in each position
        points_per_million = positions_calc(players, first_attr='total_points', second_attr='now_cost')
        # from this we can say that each million bring equal amount of points in each position (10 points per million)
        # so Budgets => FWD:(80/11)*3 = 22 million , DEF: (80/11)*3 = 22 million , MID = (80/11)*4 = 30 million , GK = 6 million

        # --------------------------------

        # get all players in each position
        GK_players = [player for player in players if player.element_type == 1]
        DEF_players = [player for player in players if player.element_type == 2]
        MID_players = [player for player in players if player.element_type == 3]
        FWD_players = [player for player in players if player.element_type == 4]

        # GK Budget = 6 Millions
        # top 5 GK with total_points
        # Choose 1 player
        top_GK = get_top_dict(GK_players, 5)
        GK_costs = get_costs(GK_players, 5)
        # from 2 charts the best GK is Martinez from Aston Villa cost = 5.5m
        # put remaining 0.5m in DEF Budget

        # DEF Budget = 22 + 0.5 = 22.5 Millions
        # top 5 DEF with total_points
        # Choose 3 players
        top_DEF = get_top_dict(DEF_players, 5)
        DEF_costs = get_costs(DEF_players, 5)
        # from 2 charts the best 3 DEF:

        # MID Budget = 30 + 4 = 34 Millions
        # top 5 MID with total_points
        # Choose 4 players
        top_MID = get_top_dict(MID_players, 10)
        MID_costs = get_costs(MID_players, 10)
        # from 2 charts the best 4 MID:


        # FWD Budget = 22 + 0.5 = 22.5 Millions
        # top 5 FWD with total_points
        # Choose 3 players
        top_FWD = get_top_dict(FWD_players, 10)
        FWD_costs = get_costs(FWD_players, 10)

        # Bench Budget = 20 + 0.5 = 20.5 Millions
        # 3 players with cost 5m and 1 player with 5.5m
        GK_costs = get_costs(GK_players, 10)
        DEF_costs = get_costs(DEF_players, 10)
        MID_costs = get_costs(MID_players, 10)

        headers = ["Name","ID","Minutes","Goals","Assists","Yellow Cards", "Red Cards"]
        listen = []
        scoringer = []
        for player in GK_players:
            lst = [player.web_name,player.id, player.minutes, player.goals_scored,player.assists,player.yellow_cards,player.red_cards]
            scoringer.append(lst)
        #scoringer = [dict(zip(headers,entry))for entry in scoringer]
        return json.dumps(scoringer)

if __name__ == "__main__":
    app.run(port=5000 ,debug=True)