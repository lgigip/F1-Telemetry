# F1 Telemetry Analysis - Verstappen vs Piastri (Bahrain GP Qualifying 2024)
#
With the aim to develop abilities in **motorsport data analysis and visualisation**, I built this project to extract and compare F1 data; exploring correlations between performance and driving technique. 
#
This project compares the fastest laps of **Max Verstappen**🔵 and **Oscar Piastri**🟠 during the **2024 Bahrain Grand Prix Qualifying Session**, using the *FastF1 Python Library*.
#
#### Plot 1 - Speed Comparison
This plot visualises speed comparison against lap distance for Verstappen and Piastri's fatsers qualifying laps, revealing differences in straight-line speed, minimum corner speed and acceleration profile. The traces show that Verstappen most notably exceeds Piastri's speed on the opening straight, compared to marginal differences between the two traces for other sectors. This indicates where performance differs around the circuit. Overall analysis cannot be attributed to the speed trace in isolation; factors such as corner exit performance, vehicle set-up, energy depolyoment and driver input must also be considered.

#
#### Plot 2 - Throttle and Brake Comparison
This plot, an overlay of throttle and brake application across each driver's fastest lap, visualises the differences in braking application timing, brake release and throttle application. Several braking zones show minor differences between the drivers' braking application, while the throttle traces reveal differences in the speed at which each driver returns to full throttle from corner entry.
This analysis does not attempt to compare braking force, as the brake channel of FastF1 is a binary application signal, rather than a brake-pressure measurement.
#
**In conclusion**, this comparison between Verstappen and Piastri's fastest laps during the 2024 Bahrain Qualifying demonstrates how telemetry at lap-level can be used to localise performance differences that hide behind lap time alone. The speed, throttle and brake traces identify where driver approach differs, providing a basis for more detailed investigation of braking points, corner-exit, speed-development and, ultimately, performance.
#
#### Future Adaptations
- Use a common interpolated distance axis to more precisely quantify differences 
- Expand comparison to multiple laps (not solely the drivers' fastest laps)
- Integrate tyre/weather data for further data analysis
- Compare a greater number of drivers
#
#### Motivation Behind the Project
This was built as an independent passion project; an exploration of **real-world motorsport telemetry and performance data** that demonstrates **practical application of software and data analysis** and my interest in data-analysis and motorsport technology.
