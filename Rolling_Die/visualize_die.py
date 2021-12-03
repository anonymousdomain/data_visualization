from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


die = Die()
results = []
for sides in range(100):
    result = die.roll()
    results.append(result)

frquencies = []

for value in range(1, die.num_sides+1):
    frquency = results.count(value)
    frquencies.append(frquency)

x_values = list(range(1, die.num_sides+1))

data = [Bar(x=x_values, y=frquencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'frquencies of Result'}

my_layout = Layout(title='Results of Rolling one D6 1000 time',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='img\d6.html')
