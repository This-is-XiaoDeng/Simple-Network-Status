# Simple-Network-Status

简单的网络状态

## 搭建

### Linux

#### 自动脚本

1. 安装 Python3
2. 运行`run.sh`，将自动创建虚拟环境、安装依赖并启动服务器

> 若要指定 uWSGI Worker 数量和监听端口，请设置`WORKER_COUNT`和`SERVER_PORT`环境变量

#### 手动开启

> 仅限有能力的用户

1. 安装 Python3
2. 安装`requests`、`flask`和任意 WSGI 服务器（您也可以直接使用 flask 内置的服务器）
3. 启动服务器（`flask run` 或其他）

### Windows

1. 安装 Python3
2. `pip install -r requirements.txt`
3. `uwsgi --master -p 4 --http 0.0.0.0:<端口> -w app:app`

> 请将 `<端口>` 修改为实际端口


## 配置

您可以在软件工作目录下创建`config.json`文件，软件将在开启后自动更新配置

```json
{
    "siteTitle": "网络状态",
    "title": null,
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
    "site_list": [],
    "lang": {
        "status": {
            "working": "正常",
            "error": "出错"
        }
    }
}
```

- `siteTitle`：网站标题
- `title`：网站标题（导航栏和主标题，为`null`则指向`siteTitle`）
- `intro`：副标题（可用`%UPDATE_TIME%`替换为数据更新时间）
- `links`：导航栏链接
    - `name`：链接名称
    - `url`：地址
- `refresh_interval`：更新间隔（待完善，单位秒）
    - `0`：正常更新间隔
    - `1`：访问较少时的更新间隔（如果网站炸的比较快或者摸不准可以把这个和前项设置成一样的）
    - `2`：“访问较少”阈值（如果无人访问时间超过次配置项的时间则判定为“访问较少”）
- `index_url`：站点根目录
- `site_list`：节点列表
    - `name`：节点名称
    - `url`：节点地址（用于判断状态）
    - `display_url`：显示url（用于隐藏真实地址）
- `lang`：部分语言文本
    - `status`：状态提示文本
        - `working`：状态·工作中
        - `error`：状态·错误

