import streamlit as st
import pandas as pd
import time
from engine import start_sniffing

st.set_page_config(page_title="Net-Pulse Detector", layout="wide")
st.title("📡 Net-Pulse: Real-Time Anomaly Detector")