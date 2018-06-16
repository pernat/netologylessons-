#!/usr/bin/python
# -*- coding: utf-8 -*-
from Diplom.main import get_user_friends

TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
TARGET_USER_ID = '5030613'
USER_ID_PACK_SIZE = {500: 1, 1000: 3, 2000: 5, 3000: 7, 4000: 9, 5000: 11, 6000: 13, 7000: 15, 8000: 17, 9000: 19}
FRIEND_LIST_LEN = get_user_friends()
