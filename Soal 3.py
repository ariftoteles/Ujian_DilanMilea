import requests             

url = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
data = requests.get(url)
if data.status_code == 200:
    provinsi = data.json()
    # print(provinsi)
else:
    print('Request Error')

url = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
data = requests.get(url)
if data.status_code == 200:
    kota = data.json()
    # print(kota)
else:
    print('Request Error')
#dilan banten
#milea Jabar
keysProv = list(provinsi.keys())
valuesProv = list(provinsi.values())
ProvDilan = keysProv[valuesProv.index('BANTEN')]
ProvMilea = keysProv[valuesProv.index('JAWA BARAT')]
print(ProvDilan)
print(ProvMilea)

### Milea
### urban = 'CITARUM'
### sub_distric = 'BANDUNG WETAN'
### city = 'BANDUNG'
### provinsi_code = '32'
### postal_code = '40115'

## cari postal code Milea
Jabar = kota['32']
for i in Jabar:
    if i['urban'] == 'CITARUM' and i['sub_district'] == 'BANDUNG WETAN':
        postMilea = i['postal_code']
#         print(postMilea)

### Dilan
### urban = 'SAMPORA'
### sub_distric = 'CISAUK'
### city = 'TANGERANG'
### provinsi_code = '36'
### postal_code = '15345'
## cari postal code Dilan
Banten = kota['36']
for i in Banten:
    if i['urban'] == 'SAMPORA' and i['sub_district'] == 'CISAUK':
        postDilan = i['postal_code']
#         print(postDilan)

apiKey="Kap6KM9PtPC60IxH6nprOc8jYqPhU7qOYRMd7IX3aMNUDeTN04pUWcqeN5mGgt9u"
url= f"http://www.zipcodeapi.com/rest/{apiKey}/distance.json/{postDilan}/{postMilea}/km"

data = requests.get(url)
output = data.json()
jarak = output["distance"]

print(f"Kode Pos lokasi Dilan adalah {postDilan}")
print(f"Kode Pos lokasi Milea adalah {postMilea}")
print(f"Jarak Dilan & Milea adalah {jarak} km")
