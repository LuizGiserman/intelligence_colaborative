import os
from auxiliar.model import GlobalMASModel as Model
import matplotlib.pyplot as plt

numberIterations = 15

model = Model()
for i in range(1,numberIterations+1):
  os.system('cls')
  percentage = float(100*i/numberIterations)
  print('Optimizing...\n')
  print('(' + '='*(int(0.2*percentage)-1) + '>' + '-'*(20-int(0.2*percentage)) + ') | {result:.2f}%\n'.format(result=percentage))
  model.step()

graphTabou = [i[0]["cost"] for i in model.evaluator.listTabou]
graphRecuit = [i[0]["cost"] for i in model.evaluator.listRecuit]
graphGenetic = [i[0]["cost"] for i in model.evaluator.listGenetic]

plt.plot(list(range(len(graphTabou))),graphTabou)
plt.plot(list(range(len(graphRecuit))),graphRecuit)
plt.plot(list(range(len(graphGenetic))),graphGenetic)
plt.legend(['Tabou', 'Recuit', 'Genetic'])
plt.title('Cost Function x Steps')
plt.xlabel('Steps')
plt.ylabel('Cost [Km]')
plt.grid(True)
plt.show()