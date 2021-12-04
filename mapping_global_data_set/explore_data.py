import json 

filename='mapping_global_data_set\data\eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data=json.load(f)
    
readable_file='mapping_global_data_set\data\readable_eq_data.json'
    
all_eq_dict=all_eq_data['features']

mags=[]

for eq_dict in all_eq_dict:
    
    mag=eq_dict['properties']['mag']
    mags.append(mag)
print(mags[:6])
