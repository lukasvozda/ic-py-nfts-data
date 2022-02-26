from ic.agent import *
from ic.identity import *
from ic.client import *
from ic.candid import Types, encode, decode

# Inicialisation
client = Client(url = "https://ic0.app")
iden = Identity()
agent= Agent(iden, client)

# Endpoint that we want to pull data from
function_to_call = 'transactions'

# List of NFTs canisters we want to pull data from
# You can find it on Entrepot clicking on NFTs 
canisters = [
    {
        'name': 'Motokos',
        'id': 'oeee4-qaaaa-aaaak-qaaeq-cai'
    },
    {
        'name': 'DSA',
        'id': '3mttv-dqaaa-aaaah-qcn6q-cai'
    },
    {
        'name': 'OG medals',
        'id': 'rw623-hyaaa-aaaah-qctcq-cai'
    },
    {
        'name': 'BTC Flowers',
        'id': 'pk6rk-6aaaa-aaaae-qaazq-cai'
    },
    {
        'name': 'Poked bots',
        'id': 'bzsui-sqaaa-aaaah-qce2a-cai'
    },
    {
        'name': 'Cronics',
        'id': 'e3izy-jiaaa-aaaah-qacbq-cai'
    },
    {
        'name': 'ICPunks',
        'id': 'bxdf4-baaaa-aaaah-qaruq-cai'
    },                               

]

# File to write results to
f  = open('result.txt','w')
# Header row
f.write(f"collection,index,token,icp,time_updated,timestamp,seller,buyer")

for c in canisters:
    params = []

    params = encode(params)

    response = agent.query_raw(c["id"], function_to_call, params)

    print("Getting collection:", c["name"])

    trans = response[0]["value"]
    for i,t in enumerate(trans):
        price = str(t['_3364572809']/100000000)
        timestamp = t['_1291635725']
        token = t['_338395897']
        seller = t['_1782082687']
        buyer = t['_3136747827']
        f.write(f"\n{c['name']},{i},{token},{price},,{timestamp},{seller},{buyer}")

f.close()