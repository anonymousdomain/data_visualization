from plotly.graph_objs import Scattergeo,Layout

from plotly import offline
from explore_data import extracted_data as d

#data=[Scattergeo(lon=d.lons,lat=d.lats)]
data=[{
    'type':'scattergeo',
    'lon':d.lons,
    'lat':d.lats,
    'text':d.hover_titles,
    'marker':{
        'size':[5*mag for mag in d.mags],
        'color':d.mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]
my_layout=Layout(title='Global Earthquaks')

fig={'data':data,'layout':my_layout}

offline.plot(fig,filename='img\global_earthquak.html')



