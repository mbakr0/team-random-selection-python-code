# -*- coding: utf-8 -*-
"""team_random_selection_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QkHeI1OkLDQMhsWZKfy-ONd3hJPTeujL

# Team Random Selection Code :)
"""

import random

# Define the four test lists
level1_list = [1, 2, 3, 4]
level2_list = ['a', 'b', 'c','d']
level3_list = [99, 88, 77,66]
level4_list = ["1$","2&","3%","4©"]

"""Think about a code that help us to have random new mixed lists, each list should have one element from each level lists.

Output may be like that following:
```python
team1 = [1, 'c', 88, '2&']
team2 = [4, 'a', 99, '3%']
team3 = [2, 'b', 77, '4©']
team4 = [3, 'd', 66, '1$']
```


"""

levels = [level1_list,level2_list,level3_list,level4_list]# your code here
teams = []
for i in range(4):
  temp_team = []
  for j in range(4):
    e = random.choice(levels[j])
    levels[j].remove(e)
    temp_team.append(e)
  teams.append(temp_team)
print(teams)