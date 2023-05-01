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
        try:
            req = requests.get(site["url"])
        except:
            site_data[length].update({
                "status": config["lang"]["status"]["error"],
                "status_type": "danger"
            })
            length += 1
            continue

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

        # 补全 Key
        if "display_url" not in site_data[length].keys():
            site_data[length]["diaplay_url"] = None

        length += 1
        
get_site_status()

@app.route(config["index_url"])
def home():
    global latest_visit
    latest_visit = time.time()
    links = config["links"]
    for i in range(len(links)):
        links[i]["is_active"] = links[i]["url"] == config["index_url"]
    return flask.render_template(
        "index.html",
        title=config["title"] or config["siteTitle"],
        links=links,
        intro=config["intro"].replace(
            "%UPDATE_TIME%",
            time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime(data_update_at))
            ) + "" if time.time() - latest_visit <= config["refresh_interval"][2]\
                else config["lang"]["too_old"],
        data=site_data)

@app.route("/refresh")
def refresh():
    if time.time() - latest_visit >= config["refresh_interval"][2]:
        get_site_status()
        return "已刷新"
    else:
        return "刷新失败：数据未过期"

def get_status_task():
    while True:
        time.sleep(config["refresh_interval"][0]\
            if time.time() - latest_visit <= config["refresh_interval"][2]\
            else config["refresh_interval"][1])
        get_site_status()
    # 算法目前比较答辩，坐等好人pr（x）

threading.Thread(target=get_status_task).start()

