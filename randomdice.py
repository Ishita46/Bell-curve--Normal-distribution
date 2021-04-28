import random
import plotly.express as px
import plotly.figure_factory as ff
count = []
dice_result = []
for i in range(0,100):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  dice_result.append(dice1+ dice2)
  count.append(i)

print(count, dice_result)

#ff - figure factory, create_distplot - distribution plot([from where data is coming],["label"])
fig = ff.create_distplot([dice_result],["result"])
fig.show()

#scipy file is to be installed first for using bell curves things in visual studio code.
