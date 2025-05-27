import streamlit as st
import calendar
from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Title of the app
st.title("📅 400-Year Gregorian Calendar Viewer")
st.markdown(f"Explore the Gregorian calendar from **{current_year - 399} to {current_year}**")

# Year selector
selected_year = st.slider("Select a year:", min_value=current_year - 399, max_value=current_year, value=current_year)

# Check for leap year
def is_leap(year):
    return calendar.isleap(year)

# Display year header
st.header(f"Calendar for {selected_year} {'(Leap Year)' if is_leap(selected_year) else ''}")

# Display the calendar month-by-month
for month in range(1, 13):
    month_name = calendar.month_name[month]
    st.subheader(month_name)
    month_calendar = calendar.month(selected_year, month)
    st.code(month_calendar, language="text")

# Summary note
st.markdown("---")
st.markdown("✅ This app displays each month of the selected year using the **Gregorian calendar rules**.")
st.markdown("Leap years are determined according to standard rules: divisible by 4, but not 100 unless also divisible by 400.")
