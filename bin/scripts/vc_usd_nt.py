#
# Copyright (c) 2017 Sugimoto Takaaki
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import urllib
import json
from collections import OrderedDict

# dictionary of api url
d = OrderedDict()
d['btc']='https://api.cryptonator.com/api/ticker/btc-usd'
d['ltc']='https://api.cryptonator.com/api/ticker/ltc-usd'
d['doge']='https://api.cryptonator.com/api/ticker/doge-usd'
d['xrp']='https://api.cryptonator.com/api/ticker/xrp-usd'
d['eth']='https://api.cryptonator.com/api/ticker/eth-usd'
d['mona']='https://api.cryptonator.com/api/ticker/mona-usd'

outputString = ""

for url in d.values():

    sock = urllib.urlopen(url)
    jsonString = sock.read()
    sock.close()

    jsonCurrency = json.loads(jsonString)
    price = jsonCurrency['ticker']['price']

    outputString = outputString + price + " "

print outputString
