import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
  st.write("Here's our first attempt at using data to create a table:")
  st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
  )

if __name__ == "__main__":
    run()
