import json 

#filename='mapping_global_data_set\data\eq_data_1_day_m1.json'
filename='mapping_global_data_set\data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)
    
class extracted_data():
    all_eq_dict=all_eq_data['features']
    all_eq_title=all_eq_data['metadata']['title']
    mags,lons,lats,hover_titles=[],[],[],[]
    for eq_dict in all_eq_dict:
        
        mags.append(eq_dict['properties']['mag'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_titles.append(eq_dict['properties']['title'])
      

   # print(mags[:10],lons[:5],lats[:5])

 
    