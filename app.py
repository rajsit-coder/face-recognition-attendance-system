import streamlit as st
import pandas as pd
import os

st.title("📄 Attendance Dashboard")

if not os.path.exists("Attendance"):

    st.warning("Attendance Folder Not Found")

else:

    files = os.listdir("Attendance")

    csv_files = [
        file for file in files
        if file.endswith(".csv")
    ]

    if len(csv_files) == 0:

        st.warning("No Attendance Files Found")

    else:

        selected_file = st.selectbox(
            "Select Attendance File",
            csv_files
        )

        df = pd.read_csv(
            f"Attendance/{selected_file}"
        )
        
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            "Download CSV",
            csv,
            selected_file,
            "text/csv"
        )