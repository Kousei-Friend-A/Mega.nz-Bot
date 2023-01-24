# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = 17945796
    API_HASH = "4a05481a5da2d66f801acffc4ca5ee4b"
    BOT_TOKEN = "5700920410:AAEk8j5NZb6wiIVuu3-NS6AL243bl57EpvU"
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5152809878").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["True", "true"]
    LOGS_CHANNEL = int(os.environ.get("-1001874063925")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")
