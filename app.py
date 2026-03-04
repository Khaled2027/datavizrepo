import streamlit as st 
import pandas as pd
import numpy as np

st.title("My Streamlit App")

#st.write("This is sample data: ")

#df=pd.DataFrame({"Country":["India","Turkey","Iran","Oman"],"Population (Mil)":[1400,90,90,5]})



#st.write(df)

#st.table(df)

#x= np.linspace(0,6.28,20)
#y= np.cos(x)
#df2= pd.DataFrame({"x":x, "y":y})

#st.line_chart(df2,x="x",y="y")

#n=st.slider("number of delivery")
#is_blue= st.checkbox("Blue?")
#color=(0,0,255) if is_blue else (255,0,0)

#np.random.seed(10)


#df3=pd.DataFrame(np.random.rand(n,2)/[50,50]+[52.5,13.4],columns=["lat","lon"])

#st.map(df3,color=color)


#st.text_input("My name",key="name")
#st.write(st.session_state["name"].title())


#n=st.slider("number of delivery")
#is_blue= st.checkbox("Blue?")
#color=(0,0,255) if is_blue else (255,0,0)

#np.random.seed(10)

#if st.checkbox("show map"):

    #df3=pd.DataFrame(np.random.rand(n,2)/[50,50]+[52.5,13.4],columns=["lat","lon"])
    #st.map(df3,color=color)

#with st.sidebar:
    #options=st.selectbox("select number",[1,2,3,4,5])

    #st.write(multi_select)

    #slider= st.slider("range:",0,100)

#st.write(slider)


#left, right=st.columns(2)


#with left:
#food= st.radio("food",["pizza","pasta","Burger","Donner"])
#with right:
#st.write(food)


text="""
# this is Khaled's Dashboard 
## this is two hash
### this is 3 hash

- this is a list
"""

st.markdown(text)