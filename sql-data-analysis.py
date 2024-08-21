import streamlit as st
import pandas as pd
from pandasql import sqldf

st.set_page_config(layout="wide")

st.header("📊 SQL Data Analysis on Sample Superstore data")

df = pd.read_excel("Sample - Superstore (2) (1).xls")
st.dataframe(df)

st.divider()
st.code("SELECT * FROM df limit 5;")
output = sqldf('''SELECT * FROM df limit 5;''')
st.write(output)

st.divider()
st.code("Q1) What percentage of total orders were shipped on the same date?")
st.code("SELECT ROUND((COUNT(DISTINCT Order ID) / (SELECT COUNT(DISTINCT Order ID) AS total_orders FROM df)) * 100, 2) AS Same_Day_Shipping_Percentage FROM df WHERE Order Date = Ship Date;")
output1 = sqldf('''SELECT ROUND((COUNT(DISTINCT `Order ID`) / (SELECT COUNT(DISTINCT `Order ID`) AS total_orders FROM df)) * 100, 2) AS Same_Day_Shipping_Percentage FROM df WHERE `Order Date` = `Ship Date`;''')
st.write(output1)


st.divider()
st.code("Q2) Find the top 5 items with the highest average sales per day?")
st.code("SELECT `Product ID`, ROUND(AVG(Sales), 3) AS Average_Sales FROM df GROUP BY `Product ID` ORDER BY Average_Sales DESC LIMIT 5;")
output2 = sqldf('''SELECT
    `Product ID`,
    ROUND(AVG(Sales), 3) AS Average_Sales
FROM
    df
GROUP BY
    `Product ID`
ORDER BY
    Average_Sales DESC
LIMIT 5;
''')
st.write(output2)

st.divider()
st.code("Q3) Write a query to find the average order value for each customer, and rank the customers by their average order value?")
st.code("SELECT `Customer Name`,ROUND(AVG(Sales), 3) AS avg_order_value, DENSE_RANK() OVER (ORDER BY AVG(Sales) DESC) AS sales_rank FROM df GROUP BY `Customer Name`;")
output3 = sqldf(''' SELECT
    `Customer Name`,
    ROUND(AVG(Sales), 3) AS avg_order_value,
    DENSE_RANK() OVER (ORDER BY AVG(Sales) DESC) AS sales_rank
FROM
    df
GROUP BY
    `Customer Name`;''')
st.write(output3)


st.divider()
st.code("Q4) What is the most demanded sub-category in the west region?")
st.code("SELECT `Sub-Category`,ROUND(SUM(Sales), 3) AS total_quantity FROM df WHERE Region = 'West' GROUP BY `Sub-Category` ORDER BY total_quantity DESC LIMIT 1;")
output4 = sqldf('''SELECT
`Sub-Category`,
    ROUND(SUM(Sales), 3) AS total_quantity
FROM
    df
WHERE
    Region = 'West'
GROUP BY
    `Sub-Category`
ORDER BY
    total_quantity DESC
LIMIT 1;
''')
st.write(output4)


st.divider()
st.code("Q5) Which order has the highest number of items?")
st.code("SELECT `Order ID`,COUNT(`Order ID`) AS num_item FROM df GROUP BY `Order ID` ORDER BY num_item DESC LIMIT 1;")
output5 = sqldf('''SELECT
    `Order ID`,
    COUNT(`Order ID`) AS num_item
FROM
   df
GROUP BY
    `Order ID`
ORDER BY
    num_item DESC
LIMIT 1;''')
st.write(output5)


st.divider()
st.code("Q6) Which order has the highest cumulative value?")
st.code("SELECT  `Order ID`,ROUND(SUM(Sales), 3) AS order_value FROM df GROUP BY `Order ID` ORDER BY order_value DESC LIMIT 1;")
output6 = sqldf('''SELECT  `Order ID`,ROUND(SUM(Sales), 3) AS order_value FROM df GROUP BY `Order ID` ORDER BY order_value DESC LIMIT 1;''')
st.write(output6)

st.divider()
st.code("")
st.code("")
output7 = sqldf('''''')
st.write(output7)


footer="""<style>
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: blue;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #E8E8E8;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://ayushjoshi10.github.io/Portfolio/" target="_blank">Ayush Joshi</a></p>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)
