# Personal-health-dashboard

Dashboard link[https://personal-health-tracking-dashboard-h8bxrvpeuqp3awxbuu9nfb.streamlit.app]


## Objective:
Build an interactive Streamlit dashboard to help individuals track and analyze their daily health habits including steps, sleep, mood, water intake, calories burned, and distance walked.
## Features explainations:
1.steps:The total number of steps taken by a person that day.
2.distance_km:The total distance walked or run in kilometers, often derived from the step count.
3.calories_burned:The estimated number of calories the person burned throughout the day (via walking, exercise, etc.).
4.active_minutes:The number of minutes the person spent doing moderate to vigorous physical activity.
5.sleep_hours:Number of hours the person slept the previous night.
6.water_intake_liters : How many liters of water the person drank that day.
7.mood: Categorical (could be strings like 'happy', 'tired', 'stressed', or numerical scores like 1–5)

## ❓ Problem Statement
Many individuals struggle to maintain healthy habits due to a lack of awareness of how their daily activities, hydration, sleep, and emotional states are connected. Without clear insights, it's difficult to form effective routines that support overall wellbeing.

- There is a need for a simple, interactive tool that can analyze and visualize health patterns to help individuals make smarter decisions about their fitness and lifestyle.

## Key Features:

## 📈 Dynamic KPIs:

Average steps, sleep hours, water intake, calories burned, active minutes, and distance walked are automatically calculated based on user-selected filters.

## 🗓️ Customizable Filters:

Filter the data by mood and date range via a sidebar for personalized analysis.

## 📊 Interactive Visualizations:

Line plots and bar charts showing trends over time (steps, calories burned).

Mood analysis with steps and calories burned relationships.

Custom plots (Line, Bar, Scatter) based on any two selected variables.

## 🔍 Data Explorer:

Users can expand a section to view the raw dataset directly inside the app.

## 💡 Insights Provided:

From the analysis, it is discovered that:
1. On average, a person takes 10,238 steps daily.
2. The average distance covered is 7.6 kilometers.
3. A person is active for 102 minutes on average.
4. A person consumes an average of 2.5 liters of water daily.
5. From the analysis, the more steps and distance you walk, the more calories you burn.
6. You take more steps when you are energetic, and you are likely to be stressed and tired, but take very few steps when you are sad.
7. When you sleep very well (up to 7.5 hours), you wake up energetic, and when you sleep less, you wake up tired.
8. On the days that you are stressed, tired, and sad, you consume more water, and less when you are energetic.


## 📢 Recommendations:

From the above insights, I recommend maintaining good health or losing weight:
1. Consume 2.5L of water daily.
2. Be active for about 107 minutes daily.
3. To lose weight, take about 10,239 steps daily.
4. Sleep at least up to 7 hours a day.

## 🎨 User-Friendly Design:

Light, clean theme (or grey color scheme if preferred).

Responsive two-column layout for insights and recommendations.

## 🛠️ Technical Stack:

- Libraries: Streamlit, Pandas, Seaborn, Matplotlib.

- Caching: Faster performance with @st.cache_data.

- Layout: Wide screen configuration for better data visualization.

