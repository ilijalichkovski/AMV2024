import streamlit as st

st.title("Visualizing MRI scans of low-grade gliomas in Python")
st.write(
    "Link format: [docs.streamlit.io](https://docs.streamlit.io/)."
)

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", 
                                  "Materials & Methods", 
                                  "Results", 
                                  "Data availability"])
tab1.header("Glioma")
tab1.write("Lorem ipsum")
tab1.header("Computed tomography (CT)")
tab2.header("Choice of dataset")
tab2.header("Patient choice")

st.sidebar.write('hello')
