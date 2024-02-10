# **Final Capstone Project**

## Task
Analyze Fitbit Fitness Tracker App data to gain insights into how consumers use the Fitbit app and discover trends and insights for the marketing team.

## Content 
Respondents generated this dataset to a distributed survey via Amazon Mechanical Turk between 03.12.2016 and 05.12.2016. Thirty eligible Fitbit users consented to submit personal tracker data, including minute-level output for physical activity, heart rate, and sleep monitoring. Individual reports can be parsed by export session ID or timestamp. Variation between output represents using different Fitbit trackers and individual tracking behaviours.<br>
This dataset contains 18 different files like dailyActivity, dailyCalories, hourlySteps, etc.

## Tools
MS Excel for Data Cleaning<br>
Python for EDA ([Daily_stats](https://github.com/tyagi-mansi11/PrepInsta_Internship/blob/4b004ab17ab8a33d21cc67afdf7944e6008e8edb/Week-8/Daily_stats.ipynb), [Hourly_stats](https://github.com/tyagi-mansi11/PrepInsta_Internship/blob/4b004ab17ab8a33d21cc67afdf7944e6008e8edb/Week-8/Hourly_stats.ipynb), [Minute_stats](https://github.com/tyagi-mansi11/PrepInsta_Internship/blob/4b004ab17ab8a33d21cc67afdf7944e6008e8edb/Week-8/Minute_stats.ipynb))<br>
Pandas Profiling

## Insights of EDA
<h3>📌Part-1: Daily_stats</h3>

<h3>✅Bar plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/feb8dabefa14984663024807168ec3033e72f380/Screenshot%202024-02-10%20171239.png/>
👉Analysis of the data revealed no significant abnormalities in heart rate. All heart rates fell within the established normative parameters.

<h3>✅Scatter Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/f51f952c42981049fb78c3b576de097e21dd925e/Screenshot%202024-02-10%20171320.png/>
👉The step count and total distance seem reasonable, based on the assumption of typical walking paces.

<h3>✅Pair Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/a4a0c126801303338a376db76083855b0e06cc07/Screenshot%202024-02-10%20171338.png/>
👉Scatterplots exploring the connections between individual step counts, distances travelled, and active minutes recorded.

<h3>✅Stacked Bar Chart</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/a4a0c126801303338a376db76083855b0e06cc07/Screenshot%202024-02-10%20171408.png/>
👉The spectrum of physical activity levels includes lightly active, while a smaller but significant portion engages in vigorous activity, and another segment participates in less regular or moderate activity.

<h3>✅Correlation Matrix</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/a4a0c126801303338a376db76083855b0e06cc07/Screenshot%202024-02-10%20171433.png/>
👉Visualizing the combined patterns of distance covered and steps taken across the entire dataset with a heatmap.

<h3>📌Part-2: Hourly_stats</h3>

<h3>✅Bar Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/811b764bcac6daba7a9f020aad0e0cb44ddab081/Screenshot%202024-02-10%20171729.png/>
👉As pulse slows with the setting sun, suggesting work patterns dictate peak activity during daylight hours.

<h3>✅Scatter Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/811b764bcac6daba7a9f020aad0e0cb44ddab081/Screenshot%202024-02-10%20171751.png/>
👉The number of steps people take in an hour varies from 0 to 4,000, resulting in a calorie burn of 0 to 200. 

<h3>✅Pair Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/811b764bcac6daba7a9f020aad0e0cb44ddab081/Screenshot%202024-02-10%20171813.png/>
👉Scatterplots exploring the connections between Calories burnt, Total Intensity and Total Steps recorded.

<h3>✅Correlation Matrix</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/811b764bcac6daba7a9f020aad0e0cb44ddab081/Screenshot%202024-02-10%20171832.png/>
👉Visualizing the combined patterns of calories, intensity and steps taken across the entire dataset with a heatmap.

<h3>📌Part-3: Minute_stats</h3>

<h3>✅Bar Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/72886ac1ad2c2271391a69dd8346c2cf3bb904c6/Screenshot%202024-02-10%20171958.png/>

<h3>✅Scatter Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/72886ac1ad2c2271391a69dd8346c2cf3bb904c6/Screenshot%202024-02-10%20172015.png/>

<h3>✅Pair Plot</h3>
<img src = https://github.com/tyagi-mansi11/img/blob/72886ac1ad2c2271391a69dd8346c2cf3bb904c6/Screenshot%202024-02-10%20172044.png/>
