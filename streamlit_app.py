import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import AMV

st.title("Visualizing metastatic lesions in bone")

"""
Authors: Tina Saadat Kia, Alvinsen Japutra, Ilija Lichkovski

Welcome to the webpage for our project report! The four sections of our work can be accessed in the tabs below:
"""

st.write(
    "Link format: [docs.streamlit.io](https://docs.streamlit.io/)."
)

tab1, tab2, tab3, tab4 = st.tabs(["1. Introduction", 
                                  "2. Materials & Methods", 
                                  "3. Results & Discussion", 
                                  "4. Data availability"])
with tab1:
    st.header("What is bone metastasis?")
    """
    In patients with various types of cancers, cancer cells tend to break away from the site of the primary tumor and enter the bloodstream. As a result, they can colonize different tissues in a process called *metastasis*. Bones are a common such region of metastasis due to their unique microenvironment (Espisito et al, 2018).
    
    Different kinds of primary cancers tend to lead to different kinds of secondary cancers in bone (metastases). For example, prostate cancer cells produce proteins that stimulate osteoblasts, while breast cancer cells tend to activate osteoclasts (although this categorization is not as straightforward). As a result of bone metastasis, an incurable form of secondary cancer arises, manifesting in different kinds of lesions.
     
    Our objective in this report is to visualize those lesions that result from bone metastases. We do this by analyzing spinal CT scans in a variety of patients from both sexes who have been diagnosed with dfferent primary tumors (prostate, lung, breast, skin etc.) and suffer from different kinds of bone metastasis, such as osteolytic, osteoblastic and mixed (featuring both).
    
    To understand the different kinds of metastasis, it's important to get acquainted with two kinds of cells in bone:
    * **osteoblasts** are cells responsible for synthesizing bone tissue, so when cancer cells stimulate the activity of osteoblasts, the result is an abnormal formation of dense structures within the bone. These lesions are categorized as **osteoblastic lesions**.
    * **osteoclasts** are involved in bone tissue breakdown, so cancers affecting those lead to **osteolytic lesions**, which appear as regions where the bone quality and density has been significantly compromised.
    """
    
    st.header("Computed Tomography (CT)")

    """
    The patients examined in this report were imaged using Computed Tomography (CT) -- a technique
    """

    st.header("References")
    st.write("Esposito, Mark, et al. ‘The Biology of Bone Metastasis’. Cold Spring Harbor Perspectives in Medicine, vol. 8, no. 6, June 2018, https://doi.org/10.1101/cshperspect.a031252.")
    st.write("Jayarangaiah A, Kemp AK, Theetha Kariyanna P. Bone Metastasis. [Updated 2023 Jul 31]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK507911/")

with tab2:
    st.header("Choice of dataset")

    """
    The dataset was obtained from The Cancer Imaging Archive (https://www.cancerimagingarchive.net/). The topic was chosen due to the high prevalence of bone metastasis, as it occurs in around 1 in 10 cancer patients depending on the cancer type (Zhang et al, 2023), thereby rendering it important to understand its manifestation. The particular dataset contained a favorable number of subjects (55), was publicly available, and included segmentation masks for the individual vertebrae in the spine (which allows for isolating the affected regions). Importantly, the novelty of visualizing lesions in the spine, which we had not encountered in the course, was another important motivator behind analyzing this data.
    
    The data, including demographic information and classification tables, is available at https://www.cancerimagingarchive.net/collection/spine-mets-ct-seg/ (full citation below).
    
    """



    st.header("Patient choice")

    """
    Patients were chosen to maximize the diversity of presentations of the bone metastasis. The patient group consists of 6 males and 9 females with 9 types of primary cancer (prostate, colon, lung, skin, breast, cervical, renal, neuro, skin). The patients were further selected such that 3 patients each come with the following presentations: no metastasis, osteolytic metastasis, osteoblastic metastasis, mixed metastasis, compound metastasis (mixed + osteoblastic/osteolytic), and each of the authors analyzed every kind of presentation, as seen in the table below.
    """
    
    IDs = [13681, 11471, 12196, 12855, 14826, 14293, 14078, 14487, 15040, 13989, 14316, 14912, 13641, 13089, 13843, ]
    lesions = ['none',
               'lytic in T8',
               'blastic in L3',
               'mixed in L3, T12, L4',
               'mixed in L1; blastic in T8',
               'none',
               'lytic in L1',
               'blastic in T10',
               'mixed in L3',
               'mixed in L3, T12; lytic in L2',
               'none',
               'lytic in L1',
               'blastic in L3',
               'mixed in L1:T5, T8:T11, L3',
               'lytic in T7, L1; mixed in L3']
    cancers = ['skin',
               'neuro',
               'prostate',
               'breast',
               'renal',
               'lung',
               'prostate',
               'colon',
               'prostate',
               'breast',
               'prostate',
               'renal',
               'cervical',
               'prostate',
               'lung']
    sexes = ['M','F','M','F','F','F','M','F','M','F','M','F','F','M','F']
    authors = ['Tina','Tina','Tina','Tina','Tina','Alvinsen','Alvinsen','Alvinsen','Alvinsen','Alvinsen','Ilija','Ilija','Ilija','Ilija','Ilija']

    df = pd.DataFrame(columns=['Patient ID', 'Sex', 'Primary cancer', 'Metastasis type', 'Analyzed by'])

    df['Patient ID'] = IDs
    df['Sex'] = sexes
    df['Primary cancer'] = cancers
    df['Metastasis type'] = lesions
    df['Analyzed by'] = authors

    st.dataframe(df, hide_index=True)
    st.caption("Table 1: Information about the patients analyzed in this report")

    st.header("References")
    st.write("Zhang, Jing et al. “Prevalence and prognosis of bone metastases in common solid cancers at initial diagnosis: a population-based study.” BMJ open vol. 13,10 e069908. 21 Oct. 2023, doi:10.1136/bmjopen-2022-069908")
    st.write("Pieper, S., Haouchine, N., Hackney, D.B., Wells, W.M. Sanhinova, M., Balboni, T., Spektor, A., Huynh, M., Tanguturi, S., Kim, E., Guenette, J.P., Kozono, D.E., Czajkowski, B., Caplan, S., Doyle, P., Kang, H., Alkalay, R.N. (2024) **Spine metastatic bone cancer: pre and post radiotherapy CT (Spine-Mets-CT-SEG) [Dataset] (Version 1)**. The Cancer Imaging Archive. https://doi.org/10.7937/kh36-ds04")

with tab3:
    st.header("Key visualizations")

    with st.expander("See explanation"):
        st.write('test')
        col1, col2 = st.columns(2)

        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/cat.jpg")

    st.header("Discussion")


