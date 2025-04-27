# health_dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Personal Health Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df=pd.read_csv(r'C:\Users\USER\Documents\dataset\steps_tracker_dataset.csv')
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    return df

df = load_data()

# --- Title ---
st.title("🏃‍♂️ Personal Health Tracking Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
selected_mood = st.sidebar.multiselect("Select Mood", options=df['mood'].unique(), default=df['mood'].unique())
date_range = st.sidebar.date_input("Select Date Range", [df['date'].min(), df['date'].max()])

# --- Filter Data ---
df_filtered = df[
    (df['mood'].isin(selected_mood)) &
    (df['date'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))
]

# --- KPIs (Key Numbers) ---
st.subheader("📊 Summary Metrics")
col1, col2, col3,col4,col5 ,col6= st.columns(6)

with col1:
    st.metric("Average Steps", f"{df_filtered['steps'].mean():,.0f}")

with col2:
    st.metric("Average Sleep Hours daily", f"{df_filtered['sleep_hours'].mean():.1f} hrs")

with col3:
    st.metric("Average Water Intake daily", f"{df_filtered['water_intake_liters'].mean():.1f} L")
with col4:
    st.metric('Average calory burned daily', f"{df_filtered['calories_burned'].mean():.1f}")
with col5:
    st.metric('Average active minutes daily',f"{df_filtered['active_minutes'].mean():.1f} mins")
with col6:
    st.metric('Average distance walked daily',f"{df_filtered['distance_km'].mean():.1f} km")

# --- Charts ---

with st.expander('View dataset',expanded=False):
    st.dataframe(df)

st.subheader("📈 Trends Over Time")

col1,col2=st.columns(2)
with col1:
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_filtered, x='date', y='steps', marker='o', markerfacecolor='green',ax=ax1)
    plt.title('Steps Over Time')
    st.pyplot(fig1,ax1)

with col2:
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_filtered, x='date', y='calories_burned', marker='o', color='red', ax=ax2)
    plt.title('calories burned Over Time')
    st.pyplot(fig2,ax2)



# --- Mood Analysis ---
col1,col2=st.columns(2)
with col1:
     st.subheader("😃 steps walked and calories burned ")

     fig3, ax3 = plt.subplots(figsize=(5, 5))
     sns.lineplot(data=df_filtered, x='steps', y='calories_burned',marker='D' , markerfacecolor='grey',color='brown', ax=ax3)
     plt.title('steps and calory burned')
     plt.xticks(rotation=45)
     st.pyplot(fig3,ax3)

with col2:
    st.subheader('mood and steps taken')
    fig3, ax3 = plt.subplots(figsize=(5, 5))
    sns.barplot(data=df_filtered, x='mood', y='steps', palette='pastel', ax=ax3,ci=None)
    plt.title('steps and mood')
    plt.xticks(rotation=45)
    st.pyplot(fig3,ax3)


#--- filtering by columns

st.sidebar.subheader('Filter by Two columns')

column_choices=df.columns.tolist() # to get the list of columns



# multi select columns
selected_columns=st.sidebar.multiselect('select 2 columns', options=column_choices, default=column_choices[:2])


# rules on the columns
if len(selected_columns)==2:
    st.write(f'showing relationship between **{selected_columns[0]}** and ** {selected_columns[1]}**')

    df_columns=df[[selected_columns[0],selected_columns[1]]] # combining the both columns. df_columns becomes the new df

    
    
    plot_type=st.sidebar.selectbox('select plot type', options=['Line plot','Bar plot', 'Scatter plot']) # list of plotto select from

    # put a conditon
    if plot_type == 'Line plot':
        fig_1=plt.figure(figsize=(10,5))
        sns.lineplot(x=selected_columns[0],y=selected_columns[1], data=df_columns,marker='o', markerfacecolor='red')
        plt.title(f'lineplot of {selected_columns[0]} vs {selected_columns[1]}')
        plt.xticks(rotation='vertical')
        st.pyplot(fig_1)


    elif plot_type == 'Bar plot':
        fig2=plt.figure(figsize=(10,5))
        sns.barplot(x=selected_columns[0],y=selected_columns[1], data=df_columns,ci=None, palette='magma')
        plt.title(f'Bar plot of {selected_columns[0]} vs {selected_columns[1]}')
        plt.xticks(rotation='vertical')
        st.pyplot(fig2)

    elif plot_type == 'Scatter plot':
        fig3=plt.figure(figsize=(10,5))
        sns.scatterplot(x=selected_columns[0],y=selected_columns[1], data=df_columns)
        plt.title(f'scatter plot of {selected_columns[0]} vs {selected_columns[1]}')
        plt.xticks(rotation='vertical')
        st.pyplot(fig3)


else:
    st.write('select exactly two columns')


col1,col2=st.columns(2)


with col1:
    st.title('Insights')
    st.markdown("""
From the analysis, it is discovered that:
1. On average, a person takes 10,238 steps daily.
2. The average distance covered is 7.6 kilometers.
3. A person is active for 102 minutes on average.
4. A person consumes an average of 2.5 liters of water daily.
5. From the analysis, the more steps and distance you walk, the more calories you burn.
6. You take more steps when you are energetic, and you are likely to be stressed and tired, but take very few steps when you are sad.
7. When you sleep very well (up to 7.5 hours), you wake up energetic, and when you sleep less, you wake up tired.
8. On the days that you are stressed, tired, and sad, you consume more water, and less when you are energetic.
""")

with col2:
    st.title('Recommendations')
    st.markdown("""
From the above insights, I recommend maintaining good health or losing weight:
1. Consume 2.5L of water daily.
2. Be active for about 107 minutes daily.
3. To lose weight, take about 10,239 steps daily.
4. Sleep at least up to 7 hours a day.
""")









# --- Footer ---
st.caption("Built with love | Powered by your health data 🚀")


