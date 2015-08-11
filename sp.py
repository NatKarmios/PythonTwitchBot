"""
   === STRAWPOLL CREATOR AND RESULTS RETRIEVER ===

You shouldn't have to change anything here, unless you want to make tweaks yourself.

create() makes a poll, with the first parameter being the poll's title, and the second being a list of strings that are
the poll's options. Bear in mind that Strawpoll allows allows a maximum of 30 options. The function will return the
newly created Strawpoll's URL, or None if there is a problem in creation.

results() will give you all the current data about a Strawpoll - you can give the full URL or just the ID - as long as
there are no characters after the poll's ID. It returns a dictionary with all necessary data. 'title' is the poll's
title, 'options' is a list of the poll's options, and 'votes' is a list of the number of votes recieved by each option.

"""

import requests
import re
import json


def create(poll_title="Test Poll", poll_options=["Answer 1", "Answer 2", "Answer 3"]):
    base_url = 'http://strawpoll.me/api/v2/polls'
    data = {
        'title': poll_title,
        'options': poll_options,
        'multi': False,
        'permissive': True
    }

    response = requests.post(base_url, data=data)
    if response.status_code != 201:
        return None

    poll_id = response.json().get('id', None)
    if poll_id is None:
        return None
    return 'http://strawpoll.me/' + str(poll_id)


def results(url):
    r = requests.get("http://strawpoll.me/api/v2/polls/%s" % re.findall("(\d+)$", url)[0])
    if r.status_code != requests.codes.ok: return {"Error":"Request codes"}

    content = r.content.decode()
    data = json.loads(content)
    return data