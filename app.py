import flask
from config import DEFAULT_CONFIG
import json
import threading
import time
import requests

app = flask.Flask(__name__)
config = DEFAULT_CONFIG.copy()
try:
    config.update(json.load(open("config.json", encoding="utf-8")))
except:
    pass
site_data = config["site_list"]
latest_visit = time.time()
data_update_at = 0

def get_site_status():
    global data_update_at
    data_update_at = time.time()
    length = 0
    for site in site_data:
        req = requests.get(site["url"])
        # print(req)
        if req.status_code == 200:
            site_data[length].update({
                "status": config["lang"]["status"]["working"],
                "status_type": "success"
            })
        else:
            site_data[length].update({
                "status": config["lang"]["status"]["error"],
                "status_type": "danger"
            })
        length += 1
    # print(site_data)
get_site_status()

@app.route(config["index_url"])
def _():
    global latest_visit
    latest_visit = time.time()
    links = config["links"]
    for i in range(len(links)):
        # print(links[i]["url"], config["index_url"])
        links[i]["is_active"] = links[i]["url"] == config["index_url"]
    return flask.render_template(
        "index.html",
        title=config["title"] or config["siteTitle"],
        links=links,
        intro=config["intro"].replace(
            "%UPDATE_TIME%",
            time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime(data_update_at))),
        data=site_data
    )

def get_status_task():
    while True:
        time.sleep(config["refresh_interval"][0]\
            if time.time() - latest_visit <= config["refresh_interval"][2]\
            else config["refresh_interval"][1])
        get_site_status()


threading.Thread(target=get_status_task).start()

