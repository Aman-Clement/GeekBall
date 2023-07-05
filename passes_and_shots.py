
# Function to draw the pitch
from matplotlib.patches import Arrow
from FCPython import createPitch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json


# Size of the pitch in yards
pitchLengthX = 120
pitchWidthY = 80

# ID for World Cup
match_id_required = 7545
home_team_required = "Argentina"
away_team_required = "Croatia"
# Match ID can be obtained from StatsBomb Data 'its a huge data set' so I have not uploaded it to github

file_name = str(match_id_required)+'.json'

with open('StatsbombData/data/events/'+file_name, 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)

df = pd.json_normalize(data, sep="_").assign(match_id=file_name[:-5])

shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
print(shots)

# Draw the pitch
(fig, ax) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')

# plot shots
for i, shot in shots.iterrows():
    x = shot['location'][0]
    y = shot['location'][1]

    goal = shot['shot_outcome_name'] == 'Goal'
    team_name = shot['team_name']

    circleSize = np.sqrt(shot['shot_statsbomb_xg'])*5

    if (team_name == home_team_required):
        if goal:
            shotCircle = plt.Circle(
                (x, pitchWidthY-y), circleSize, color="red")
            plt.text((x+1), pitchWidthY-y+1, shot['player_name'])
        else:
            shotCircle = plt.Circle(
                (x, pitchWidthY-y), circleSize, color="red")
            shotCircle.set_alpha(.2)
    elif (team_name == away_team_required):
        if goal:
            shotCircle = plt.Circle(
                (pitchLengthX-x, y), circleSize, color="blue")
            plt.text((pitchLengthX-x+1), y+1, shot['player_name'])
        else:
            shotCircle = plt.Circle(
                (pitchLengthX-x, y), circleSize, color="blue")
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)

plt.text(5, 75, away_team_required + ' shots')
plt.text(80, 75, home_team_required + ' shots')

fig.set_size_inches(10, 7)

# Pass Plot
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

(fig, ax) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')

for i, passe in passes.iterrows():
    x = passe['location'][0]
    y = passe['location'][1]

    team_name = passe['team_name']

    circleSize = 1

    if (team_name == home_team_required):
        passCircle = plt.Circle((x, pitchWidthY-y), circleSize, color="blue")
        # plt.text((x+1),pitchWidthY-y+1,passe['player_name'])
    elif (team_name == away_team_required):
        passCircle = plt.Circle((pitchLengthX-x, y),
                                circleSize, color="orange")
        # plt.text((pitchLengthX-x+1),y+1,passe['player_name'])
    ax.add_patch(passCircle)

fig.set_size_inches(10, 7)


# Argentina Pass Plot
Arg_passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

(fig2, ax2) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')


for i, passe in Arg_passes.iterrows():
    x = passe['location'][0]
    y = passe['location'][1]

    x_end = passe['pass_end_location'][0]
    y_end = passe['pass_end_location'][1]

    team_name = passe['team_name']

    circleSize = 1

    if (team_name == home_team_required):
        if (x_end >= x and passe['period'] == 1):
            argPassCircle = plt.Circle(
                (x, pitchWidthY-y), circleSize, color="blue")
            ax2.add_patch(argPassCircle)
fig2.set_size_inches(10, 7)

# Messi's Passes
(fig3, ax3) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')

player_name_required = 'Lionel Andrés Messi Cuccittini'
for i, passe in passes.iterrows():
    x = passe['location'][0]
    y = passe['location'][1]

    player_name = passe['player_name']

    circleSize = 1

    if (player_name == player_name_required):
        MessiPassCircle = plt.Circle(
            (x, pitchWidthY-y), circleSize, color="blue")
        ax3.add_patch(MessiPassCircle)
fig3.set_size_inches(10, 7)


# Direction of Passes by Leo
(fig4, ax4) = createPitch(pitchLengthX, pitchWidthY, 'yards', 'gray')

player_name_required = 'Lionel Andrés Messi Cuccittini'
for i, passe in passes.iterrows():
    player_name = passe['player_name']
    if (player_name == player_name_required):
        x = passe['location'][0]
        y = passe['location'][1]
        passCircle = plt.Circle((x, pitchWidthY-y), circleSize, color="blue")
        passCircle.set_alpha(.2)
        ax4.add_patch(passCircle)
        dx = passe['pass_end_location'][0]-x
        dy = passe['pass_end_location'][1]-y
        passArrow = Arrow(x, pitchWidthY-y, dx, dy, width=4, color='red')
        ax4.add_patch(passArrow)

fig4.set_size_inches(10, 7)


fig.savefig('Output/shots.pdf', dpi=100)
fig2.savefig('Output/Arg_passes.pdf', dpi=100)
fig3.savefig('Output/Arg_passes.pdf', dpi=100)

plt.show()
