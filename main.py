import pandas as pd
import streamlit as st

from recommender import SkuRecommender

rec = SkuRecommender()
rec.read_stock()

get_key = lambda sku: [ind for ind, k in enumerate(rec.stock.keys()) if k == sku][0]

sku = st.sidebar.selectbox('Select your Sku:', rec.keys(), get_key('sku-123'))
n_rec = st.sidebar.slider('Number of similar skus', 1, 20, 10)
make_rec = st.sidebar.button('Make Recommendations')

st.subheader('View Sku')
st.write(rec.view(sku))

if make_rec:
    rec.set_main(sku)
    rec_skus = rec.make_recommendations(n_rec)
    df = pd.DataFrame(rec_skus, columns=['sku', 'scoring'])
    max_score = float(df['scoring'].max())
    st.header('Similar Skus')
    st.subheader(f"{round(max_score, 4)}: {int(max_score)} is the number of attributes shared with {sku} and "
                 f"{round(max_score - int(max_score), 4)} measure how similar are those attributes (0-1)")
    st.write(df)
