from flask import Flask

from random_app import random_app

import csv
import random
import json

app = Flask(__name__)

sites = random_app.Random_Website()
with open('files/sites_by_ranked.json', 'r') as fp:
    sites.set_sites_by_ranked(json.loads(fp.read()))

@app.route('/random/website')
def random_website():
    value = random.randint(1, 10000000)

    return sites.get_site_by_value(value)

if __name__ == '__main__':
    app.run()
