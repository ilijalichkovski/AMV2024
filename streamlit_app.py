import streamlit as st

st.title("Visualizing MRI scans of low-grade gliomas in Python")
st.write(
    "Link format: [docs.streamlit.io](https://docs.streamlit.io/)."
)

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", 
                                  "Materials & Methods", 
                                  "Results", 
                                  "Data availability"])
with tab1:
    st.header("What are gliomas?")
    """A tumor affecting glial cells in the brain or spinal cord is called a glioma. 
    Brain tumors are divided into 4 grades to denote the speed with which they spread
    
    
    """
    st.write("Aiman W, Gasalberti DP, Rayi A. Low-Grade Gliomas. [Updated 2023 May 6]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK560668/")
    st.write("Tony J.C. Wang, Minesh P. Mehta, Low-Grade Glioma Radiotherapy Treatment and Trials, Neurosurgery Clinics of North America, Volume 30, Issue 1, 2019, Pages 111-118, ISSN 1042-3680, ISBN 9780323655019, https://doi.org/10.1016/j.nec.2018.08.008.")
    st.header("Magnetic Resonance Imaging (MRI)")

with tab2:
    st.header("Choice of dataset")
    st.header("Patient choice")
