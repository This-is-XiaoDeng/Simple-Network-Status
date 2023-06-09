DEFAULT_CONFIG = {
    "siteTitle": "网络状态",
    "title": None,
    "intro": "更新时间：%UPDATE_TIME%",
    "links": [
        {
            "name": "主页",
            "url": "/"
        },
        {
            "name": "GitHub",
            "url": "https://github.com/This-is-XiaoDeng/Simple-Network-Status"
        }
    ],
    "refresh_interval": [900, 3600, 1800],
    "index_url": "/",
    "slow_ttlb": 10,
    "site_list": [],
    "lang": {
        "status": {
            "working": "正常",
            "error": "出错",
            "slow": "缓慢"
        },
        "refresh": "<a href=\"/refresh\">（点此刷新）</a>"
    }
}
