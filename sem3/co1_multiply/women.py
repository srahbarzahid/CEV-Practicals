import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import legend

groups = ['Group 1','Group 2','Group 3','Group 4','Group 5']
men_scores = [22,30,35,35,36]
women_scores = [25,32,30,35,29]
x=np.arange(len(groups))
width=0.35
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, men_scores,width,label='Men')
bars2=ax.bar(x + width/2,women_scores,width,label='Women')
ax.set_xlabel('Group')
ax.set_ylabel('Score')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()
plt.savefig('women.png')

