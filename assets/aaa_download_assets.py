import requests
import re

BASE_URL = 'https://storage.googleapis.com/atlas-assets/Android/'

bundles = []
with open('../gamefiles/manifest.txt') as f:
    for line in f.readlines():
        res = re.search(r'string bundleName = "(.*)"$', line)
        if res:
            bundles.append(res.group(1))

for bundle_name in bundles:
    print(bundle_name)
    resp = requests.get(BASE_URL + bundle_name)
    with open(bundle_name + '.asset', 'wb') as f:
        f.write(resp.content)
