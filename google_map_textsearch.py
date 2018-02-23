# Author: Hadrian Pranjoto
# Please pardon my shitty coding style

import requests
import json
import pandas as pd
import os
import datetime
import time

os.chdir("C:\\Users\\HP00495\\Desktop\\Python Test")
cwd = os.getcwd()
print ('Directory: ' + cwd)

start_time = datetime.datetime.now()
start_time_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')

result_file = 'google_map_textsearch_result_' + start_time_str + '.csv'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# TMS - Intelligent Routing: AIzaSyDVm_eu9y7mqS5qDZLcn_qPitStZGuXk1g
# Hadrian Test: AIzaSyCB5p18tfp4Gc19nXLmYSx4SvuokooBFOA

key = "AIzaSyCB5p18tfp4Gc19nXLmYSx4SvuokooBFOA"

locations =[
# 'BABELAN, Bekasi, West Java',
# 'Bojongmangu, Bekasi, West Java',
# 'CABANGBUNGIN, Bekasi, West Java',
# 'CIBARUSAH, Bekasi, West Java',
# 'CIBITUNG, Bekasi, West Java',
# 'West Cikarang, Bekasi, West Java',
# 'Central Cikarang, Bekasi, West Java',
# 'South Cikarang, Bekasi, West Java',
# 'East Cikarang, Bekasi, West Java',
# 'North Cikarang, Bekasi, West Java',
# 'KARANGBAHAGIA, Bekasi, West Java',
# 'KEDUNGWARINGIN, Bekasi, West Java',
# 'MUARA GEMBONG, Bekasi, West Java',
# 'PEBAYURAN, Bekasi, West Java',
# 'SERANG BARU, Bekasi, West Java',
# 'SETU, Bekasi, West Java',
# 'SUKAKARYA, Bekasi, West Java',
# 'SUKATANI, Bekasi, West Java',
# 'SUKAWANGI, Bekasi, West Java',
# 'TAMBELANG, Bekasi, West Java',
# 'South Tambun, Bekasi, West Java',
# 'North Tambun, Bekasi, West Java',
# 'TARUMAJAYA, Bekasi, West Java',
# 'BABAKAN MADANG, Bogor, West Java',
# 'BOJONG GEDE, Bogor, West Java',
# 'CARINGIN, Bogor, West Java',
# 'CARIU, Bogor, West Java',
# 'CIAMPEA, Bogor, West Java',
# 'CIAWI, Bogor, West Java',
# 'CIBINONG, Bogor, West Java',
# 'CIBUNGBULANG, Bogor, West Java',
# 'CIGOMBONG, Bogor, West Java',
# 'CIGUDEG, Bogor, West Java',
# 'CIJERUK, Bogor, West Java',
# 'CILEUNGSI, Bogor, West Java',
# 'CIOMAS, Bogor, West Java',
# 'CISARUA, Bogor, West Java',
# 'CISEENG, Bogor, West Java',
# 'CITEUREUP, Bogor, West Java',
# 'DRAMAGA, Bogor, West Java',
# 'GUNUNG PUTRI, Bogor, West Java',
# 'GUNUNG SINDUR, Bogor, West Java',
# 'JASINGA, Bogor, West Java',
# 'JONGGOL, Bogor, West Java',
# 'KELAPA NUNGGAL, Bogor, West Java',
# 'KEMANG, Bogor, West Java',
# 'LEUWILIANG, Bogor, West Java',
# 'LEUWISADENG, Bogor, West Java',
# 'MEGAMENDUNG, Bogor, West Java',
# 'NANGGUNG, Bogor, West Java',
# 'PAMIJAHAN, Bogor, West Java',
# 'PARUNG PANJANG, Bogor, West Java',
# 'PARUNG, Bogor, West Java',
# 'RANCA BUNGUR, Bogor, West Java',
# 'RUMPIN, Bogor, West Java',
# 'SUKAJAYA, Bogor, West Java',
# 'SUKAMAKMUR, Bogor, West Java',
# 'SUKARAJA, Bogor, West Java',
# 'TAJUR HALANG, Bogor, West Java',
# 'TAMANSARI, Bogor, West Java',
# 'TANJUNGSARI, Bogor, West Java',
# 'TENJO, Bogor, West Java',
# 'TENJOLAYA, Bogor, West Java',
'CENGKARENG, West Jakarta City, Jakarta',
'GROGOL PETAMBURAN, West Jakarta City, Jakarta',
'KALI DERES, West Jakarta City, Jakarta',
'KEBON JERUK, West Jakarta City, Jakarta',
'KEMBANGAN, West Jakarta City, Jakarta',
'PALMERAH, West Jakarta City, Jakarta',
'TAMAN SARI, West Jakarta City, Jakarta',
'TAMBORA, West Jakarta City, Jakarta',
'CEMPAKA PUTIH, Central Jakarta City, Jakarta',
'GAMBIR, Central Jakarta City, Jakarta',
'JOHAR BARU, Central Jakarta City, Jakarta',
'KEMAYORAN, Central Jakarta City, Jakarta',
'MENTENG, Central Jakarta City, Jakarta',
'SAWAH BESAR, Central Jakarta City, Jakarta',
'SENEN, Central Jakarta City, Jakarta',
'TANAH ABANG, Central Jakarta City, Jakarta',
'CILANDAK, South Jakarta City, Jakarta',
'JAGAKARSA, South Jakarta City, Jakarta',
'KEBAYORAN BARU, South Jakarta City, Jakarta',
'KEBAYORAN LAMA, South Jakarta City, Jakarta',
'MAMPANG PRAPATAN, South Jakarta City, Jakarta',
'PANCORAN, South Jakarta City, Jakarta',
'PASAR MINGGU, South Jakarta City, Jakarta',
'PESANGGRAHAN, South Jakarta City, Jakarta',
'SETIA BUDI, South Jakarta City, Jakarta',
'TEBET, South Jakarta City, Jakarta',
'CAKUNG, East Jakarta City, Jakarta',
'CIPAYUNG, East Jakarta City, Jakarta',
'CIRACAS, East Jakarta City, Jakarta',
'DUREN SAWIT, East Jakarta City, Jakarta',
'JATINEGARA, East Jakarta City, Jakarta',
'KRAMAT JATI, East Jakarta City, Jakarta',
'MAKASAR, East Jakarta City, Jakarta',
'MATRAMAN, East Jakarta City, Jakarta',
'PASAR REBO, East Jakarta City, Jakarta',
'PULO GADUNG, East Jakarta City, Jakarta',
'CILINCING, North Jakarta City, Jakarta',
'KELAPA GADING, North Jakarta City, Jakarta',
'KOJA, North Jakarta City, Jakarta',
'PADEMANGAN, North Jakarta City, Jakarta',
'PENJARINGAN, North Jakarta City, Jakarta',
'TANJUNG PRIOK, North Jakarta City, Jakarta',
# 'BANTARGEBANG, Bekasi City, West Java',
# 'West Bekasi, Bekasi City, West Java',
# 'South Bekasi, Bekasi City, West Java',
# 'East Bekasi, Bekasi City, West Java',
# 'North Bekasi, Bekasi City, West Java',
# 'JATIASIH, Bekasi City, West Java',
# 'JATISAMPURNA, Bekasi City, West Java',
# 'MEDAN SATRIA, Bekasi City, West Java',
# 'MUSTIKAJAYA, Bekasi City, West Java',
# 'PONDOKGEDE, Bekasi City, West Java',
# 'PONDOKMELATI, Bekasi City, West Java',
# 'RAWALUMBU, Bekasi City, West Java',
# 'West Bogor, Bekasi City, West Java',
# 'South Bogor, Bekasi City, West Java',
# 'Central Bogor, Bekasi City, West Java',
# 'East Bogor, Bekasi City, West Java',
# 'North Bogor, Bekasi City, West Java',
# 'TANAH SEREAL, Bekasi City, West Java',
# 'BEJI, Bekasi City, West Java',
# 'CIMANGGIS, Bekasi City, West Java',
# 'LIMO, Bekasi City, West Java',
# 'PANCORAN MAS, Bekasi City, West Java',
# 'SAWANGAN, Bekasi City, West Java',
# 'SUKMA JAYA, Bekasi City, West Java',
# 'BATUCEPER, Tangerang City, Banten',
# 'BENDA, Tangerang City, Banten',
# 'CIBODAS, Tangerang City, Banten',
# 'CILEDUG, Tangerang City, Banten',
# 'CIPONDOH, Tangerang City, Banten',
# 'JATI UWUNG, Tangerang City, Banten',
# 'KARANG TENGAH, Tangerang City, Banten',
# 'KARAWACI, Tangerang City, Banten',
# 'LARANGAN, Tangerang City, Banten',
# 'NEGLASARI, Tangerang City, Banten',
# 'PERIUK, Tangerang City, Banten',
# 'PINANG, Tangerang City, Banten',
# 'TANGERANG, Tangerang City, Banten',
# 'BALARAJA, Tangerang, Banten',
# 'CIKUPA, Tangerang, Banten',
# 'CIPUTAT TIMUR, South Tangerang City, Banten',
# 'CIPUTAT, South Tangerang City, Banten',
# 'CISAUK, Tangerang, Banten',
# 'CISOKA, Tangerang, Banten',
# 'CURUG, Tangerang, Banten',
# 'GUNUNG KALER, Tangerang, Banten',
# 'JAMBE, Tangerang, Banten',
# 'JAYANTI, Tangerang, Banten',
# 'KELAPA DUA, Tangerang, Banten',
# 'KEMIRI, Tangerang, Banten',
# 'KOSAMBI, Tangerang, Banten',
# 'KRESEK, Tangerang, Banten',
# 'KRONJO, Tangerang, Banten',
# 'LEGOK, Tangerang, Banten',
# 'MAUK, Tangerang, Banten',
# 'MEKAR BARU, Tangerang, Banten',
# 'PAGEDANGAN, Tangerang, Banten',
# 'PAKUHAJI, Tangerang, Banten',
# 'PAMULANG, South Tangerang City, Banten',
# 'PANONGAN, Tangerang, Banten',
# 'PASARKEMIS, Tangerang, Banten',
# 'PONDOK AREN, South Tangerang City, Banten',
# 'RAJEG, Tangerang, Banten',
# 'East Sepatan, Tangerang, Banten',
# 'SEPATAN, Tangerang, Banten',
# 'North Serpong, South Tangerang City, Banten',
# 'SERPONG, South Tangerang City, Banten',
# 'SETU, South Tangerang City, Banten',
# 'SINDANG JAYA, Tangerang, Banten',
# 'SOLEAR, Tangerang, Banten',
# 'SUKADIRI, Tangerang, Banten',
# 'SUKAMULYA, Tangerang, Banten',
# 'TELUKNAGA, Tangerang, Banten',
# 'TIGARAKSA, Tangerang, Banten'
]

place_types = [
"bakery",
"bar",
"cafe",
"convenience_store",
"department_store",
"night_club",
"restaurant",
"shopping mall",
"spa",
"store",
"supermarket"
]

cols = [
'location_search_term', 
'name', 
'place_id', 
'street_address', 
'lat', 
'long', 
'types'
]

result_count = 0
page_count = 0

print('==START==')

for location in locations:

    for place_type in place_types:

        next_page_token = ''

        print('\nLocation: ' + location)
        print('\nPlace Type: ' + place_type)

        #Traversing through the result pages
        while True:

            page_count += 1
            print('\nPage #' + str(page_count))

            time.sleep(3)    
            querystring = {
                "query": place_type + " in " + location,
                "key":key,
                "pagetoken":next_page_token,
                "type":place_type
            }
            res = requests.request("GET", url, params=querystring)
            json_res = json.loads(res.text)

            status = json_res['status']
            print('Request Status: ' + status)

            if ('error_message') in json_res:
                print('Error: ' + json_res['error_message'])

            #Error handling
            if (status == 'OVER_QUERY_LIMIT'):
                break
            elif (status == 'REQUEST_DENIED'):
                break
            elif (status == 'ZERO_RESULTS'):
                break
            elif (status == 'INVALID_REQUEST'):
                time.sleep(3)
                continue
            elif (status == 'UNKNOWN_ERROR'): 
                break

            df = pd.DataFrame(columns=cols)

            for result in json_res['results']:

                time.sleep(3)

                location_search_term = location
                name = result['name']
                place_id = result['place_id']
                address = result['formatted_address']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                types = result['types']
                df = df.append(
                    pd.Series([location_search_term, name, place_id, address, lat, lng, types],
                              index=cols),
                    ignore_index=True
                    )
                result_count += 1

            if (page_count==1):
                df.to_csv(result_file, index=False)
                print('Start writing .csv')
            else:
                df.to_csv(result_file, index=False, mode='a', header=None)
                print('Append to .csv')
            
            print(str(result_count) + ' results retrieved')

            #exit clause
            if ('next_page_token' not in json_res):
                print('\nnext_page_token not found')
                break
            else:
                next_page_token = json_res['next_page_token']
                print('\nnext_page_token: ' + next_page_token)

end_time = datetime.datetime.now()
time_elapsed = end_time - start_time
print('\nTime elapsed: ' + str(time_elapsed))

print('Result saved as ' + result_file)
print('==END==')
