from auxiliar.model import GlobalMASModel as Model
import matplotlib.pyplot as plt

numberIterations = 15

model = Model()
for i in range(numberIterations):
  print('Iteration : ' + str(i) + ' ({result:.2f}%)'.format(result=100*i/numberIterations))
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