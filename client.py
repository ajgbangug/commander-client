#!/usr/bin/env python
import config
import pymongo
import json
import subprocess

if __name__ == "__main__":
    connection = pymongo.Connection(config.DBSERVER, config.PORT)
    db = connection[config.DATABASE]
    db.authenticate(config.DBUSER, config.DBPASS)

    hosts = db.hosts
    
    key = json.loads(subprocess.check_output(["facter", "--json", "macaddress"]))
    facts = json.loads(subprocess.check_output(["facter", "--json"]))
    hosts.update(key, facts, upsert = True)
