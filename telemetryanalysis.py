# F1 Telemetry Analysis: Verstappen vs Piastri
# Requires: fastf1, matplotlib
from pathlib import Path
import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

# Enable matplotlib and cache
fastf1.plotting.setup_mpl(misc_mpl_mods=False)
cache_dir = Path("cache")
cache_dir.mkdir(exist_ok=True)
fastf1.Cache.enable_cache(str(cache_dir))

# Load a session (2024 Bahrain GP, Qualifying as an example)
session = fastf1.get_session(2024, 'Bahrain', 'Q')
session.load()

# Pick two drivers
verstappen = session.laps.pick_drivers('VER').pick_fastest() 
piastri = session.laps.pick_drivers('PIA').pick_fastest()

# Get telemetry
ver_tel = verstappen.get_car_data().add_distance()
pia_tel = piastri.get_car_data().add_distance()

# Plot Speed Comparison
plt.figure(figsize=(12, 6))
plt.plot(ver_tel['Distance'], ver_tel['Speed'], label='Verstappen', color='blue')
plt.plot(pia_tel['Distance'], pia_tel['Speed'], label='Piastri', color='orange')
plt.title("Fastest Lap Comparison – Speed (Bahrain GP 2024 Quali)")
plt.xlabel("Lap Distance (m)")
plt.ylabel("Speed (km/h)")
plt.legend()
plt.grid(True)
plt.show()

# Plot Throttle & Brake Overlay
fig, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(ver_tel['Distance'], ver_tel['Throttle'], label="Verstappen Throttle", color='blue')
ax1.plot(pia_tel['Distance'], pia_tel['Throttle'], label="Piastri Throttle", color='orange', linestyle='--')
ax1.set_xlabel("Lap Distance (m)")
ax1.set_ylabel("Throttle (%)")

ax2 = ax1.twinx()
ax2.step(ver_tel['Distance'], ver_tel['Brake'], label="Verstappen Brake", color='navy')
ax2.step(pia_tel['Distance'], pia_tel['Brake'], label="Piastri Brake", color='orange', linestyle='--')
ax2.set_ylabel("Brake Application")
ax2.set_yticks([0, 1])
ax2.set_yticklabels(["Off", "On"])

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right')

ax1.set_title("Throttle & Brake Overlay – Fastest Laps")
fig.tight_layout()
plt.show()