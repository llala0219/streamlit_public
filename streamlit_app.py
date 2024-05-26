import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame({
    'first column' : [10, 20, 30, 40],
    'second column' : [100, 200, 300, 400]
    })
st.write(df)

df2 = pd.DataFrame(np.random.randn(200, 3),
                   columns=['a','b','c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c'])
st.write(c)
