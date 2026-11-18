import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

total_weeks = 12

swims_m = [400, 600, 800, 1000, 0.0, 0.0]
cycles_km = [8.64, 13.23, 16.27, 18.56, 0.0, 18.56]
runs_km = [3.77, 4.17, 4.86, 5.16, 0.0,]
bricks_km = [0.0, 11.0, 12.82, 0.0, 0.0]

def pad_to_weeks(data, total_length = total_weeks):
    return data + [np.nan]*(total_length - len(data))

df = pd.DataFrame({'Week': np.arange(1, total_weeks + 1), 'Swim_m': pad_to_weeks(swims_m), 'Cycle_km': pad_to_weeks(cycles_km), 'Run_km': pad_to_weeks(runs_km), 
                'Brick_km': pad_to_weeks(bricks_km)})

df['Total_km'] = (df['Swim_m']/1000.0 + df['Cycle_km'] + df['Run_km'] + df['Brick_km'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = [12, 4])
fig.suptitle('NYD Triathlon Progress', fontsize = 14, fontweight = 'bold')
ax1.plot(df['Week'], df['Total_km'], 'o-', color = 'red', label = 'Total Distance')
ax1.plot(df['Week'], df['Cycle_km'], 'o-', color = 'orange', label = 'Cycles')
ax1.plot(df['Week'], df['Run_km'],  'o-', color = 'green', label = 'Runs')
ax1.plot(df['Week'], df['Brick_km'], 'o-', color = 'darkblue', label = 'Bricks')
ax1.axhline(23.73, linestyle = '--', color = 'red', label = 'Target Total (23.73 km)')
ax1.axhline(17.70, linestyle = '--', color = 'orange', label = 'Target Cycle (17.70km)')
ax1.axhline(5.63, linestyle = '--', color = 'green', label = 'Target Run (5.63km)')
ax1.set_xlabel('Week')
ax1.set_ylabel('Distance (km)')
ax1.set_xticks(df['Week'])
ax1.grid(True)
ax1.legend(loc = 'center right')

ax2.plot(df['Week'], df['Swim_m'], 'o-', label = 'Swims')
ax2.axhline(400, linestyle = '--', color = 'gray', label = 'Target Swim  (400m)')
ax2.set_xlabel('Week')
ax2.set_ylabel('Swim Distance (m)')
ax2.set_xticks(df['Week'])
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()