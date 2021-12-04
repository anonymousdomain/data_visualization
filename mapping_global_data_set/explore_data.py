import json 

filename='mapping_global_data_set\data\eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data=json.load(f)
    
readable_file='mapping_global_data_set\data\readable_eq_data.json'
    
all_eq_dict=all_eq_data['features']

mags,lons,lats=[],[],[]

for eq_dict in all_eq_dict:
    
    mag=eq_dict['properties']['mag']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10],lons[:5],lats[:5])

 
    