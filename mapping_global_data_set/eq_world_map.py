from plotly.graph_objs import Scattergeo,Layout

from plotly import offline
from explore_data import extracted_data as d

data=[Scattergeo(lon=d.lons,lat=d.lats)]

my_layout=Layout(title='Global Earthquaks')

fig={'data':data,'layout':my_layout}

offline.plot(fig,filename='img\global_earthquak.html')



