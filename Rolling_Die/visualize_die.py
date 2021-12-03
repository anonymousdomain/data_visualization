from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


die1 = Die()
die2 = Die()
results = []
for sides in range(1000):
    result = die1.roll()+die2.roll()
    results.append(result)

frquencies = []

max_res = die1.num_sides+die2.num_sides
for value in range(2, max_res+1):
    frquency = results.count(value)
    frquencies.append(frquency)

x_values = list(range(2, max_res+1))

data = [Bar(x=x_values, y=frquencies)]
x_axis_config = {'title': 'Result','dtick':1}
y_axis_config = {'title': 'frquencies of Result'}

my_layout = Layout(title='Results of Rolling two D6 1000 time',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='img\\roll_2_dies.html')
