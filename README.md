# Simulation of a Stochastic Pandemic Flu Spread in a Closed Community
This simulation was created to answer the following scenario:
Consider a classroom of 31 elementary school kids. 30 of the kids are healthy (and susceptible to flu) on Day 1. Tommy (the 31st kid) walks in with the flu and starts interacting with his potential victims. Let’s suppose that Tommy comes to school every day (whether or not he’s sick) and will be infectious for 3 days. Thus, there are 3 chances for Tommy to infect the other kids — Days 1, 2, and 3. Suppose that the probability that he infects any individual susceptible kid on any of the three days is p = 0.02; and suppose that all kids and days are independent (so that you have i.i.d. Bern(p) trials). If a kid gets infected by Tommy, he will then become infectious for 3 days as well, starting on the next day.

<p align="center">
  <img src="flu_spread_in_classroom.png" alt="Pandemic Spread in Closed Community" title="Flu Spread in a Classroom" style="text-align:center" width="400px">
  <br>
  <em>Flu Spread in a Classroom</em>
</p>

## Guide to Files

### Reports
* [Report](Stochastic Pandemic Flu Spread in a Closed Community.pdf)

## How to run files

### Packages Required

| Package      | Description                          |
|--------------|--------------------------------------|
| numpy        | Arrays and numerical computing       |
| matplotlib   | Plotting and visualization           |
| scipy        | Scientific computing and statistics  |

```python
# Install required packages if not already installed
pip install numpy matplotlib scipy
```

## Getting Started
1.  **Set up Python Environment & Install Dependencies:** (See **Packages Required** section above).
2.  **Download `"Pandemic_Sim.py"` and place it in the root folder.**
