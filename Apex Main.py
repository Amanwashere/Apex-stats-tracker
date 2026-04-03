import requests
import os
from dotenv import load_dotenv

load_dotenv()

def apex_stats():

    username = input("Enter the username of the players stats you want to fetch: ")
    api_key = os.getenv("APEX_API_KEY")
    url = f"https://api.mozambiquehe.re/bridge?auth={api_key}&player={username}&platform=PC"
    headers = {"Authorization": api_key}
    try:
        #Turn stats into Json format
        apex_info = requests.get(url, headers=headers)
        apex_json = apex_info.json()
    except:
        print("Error: Player not found")
        return

    name = apex_json["global"]["name"]
    account_level = apex_json["global"]["level"]
    rank = apex_json["global"]["rank"]["rankName"]
    career_kills = apex_json["total"]["career_kills"]["value"]
    Kd = apex_json["total"]["kd"]["value"]

    print(f"""
    name: {name}
    level: {account_level}
    rank: {rank}
    career_kills: {career_kills}
    Kd: {Kd}
    """)

apex_stats()