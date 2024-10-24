import streamlit as st
import matplotlib.pyplot as plt

import AMV

st.title("Visualizing metastatic lesions in bone")
st.write(
    "Link format: [docs.streamlit.io](https://docs.streamlit.io/)."
)

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", 
                                  "Materials & Methods", 
                                  "Results & Discussion", 
                                  "Data availability"])
with tab1:
    st.header("What is bone metastasis?")
    """
    In patients with various types of cancers, cancer cells tend to break away from the site of the primary tumor and enter the bloodstream. As a result, **Osteoblasts** are cells responsible for synthesizing bone tissue, while **osteoclasts** are involved in bone tissue breakdown. 
    
    This report aims to visualize bone metastases as manifested in spinal CT scans in a variety of patients. We analyzed patients from both sexes who have been diagnosed with dfferent primary tumors (prostate, lung, breast, skin etc.) and suffer from different kinds of bone metastasis, such as osteolytic, osteoblastic and mixed (featuring both). 
    """
    
    st.header("Computed Tomography (CT)")

    """
    
    """

    st.header("References")
    st.write("Jayarangaiah A, Kemp AK, Theetha Kariyanna P. Bone Metastasis. [Updated 2023 Jul 31]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK507911/")
    st.write("Dataset: Pieper, S., Haouchine, N., Hackney, D.B., Wells, W.M. Sanhinova, M., Balboni, T., Spektor, A., Huynh, M., Tanguturi, S., Kim, E., Guenette, J.P., Kozono, D.E., Czajkowski, B., Caplan, S., Doyle, P., Kang, H., Alkalay, R.N. (2024) Spine metastatic bone cancer: pre and post radiotherapy CT (Spine-Mets-CT-SEG) [Dataset] (Version 1). The Cancer Imaging Archive. https://doi.org/10.7937/kh36-ds04")

with tab2:
    st.header("Choice of dataset")

    "The dataset was obtained from The Cancer I"
    st.header("Patient choice")
    
    """
    sdl
    """

with tab3:
    st.header("Key visualizations")

    st.header("Discussion")