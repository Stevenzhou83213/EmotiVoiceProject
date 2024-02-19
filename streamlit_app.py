
import os

def run_project():
    # 运行项目
    os.system("streamlit run demo_page.py --server.port 6006 --logger.level debug")

if __name__ == "__main__":
    run_project()

import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Hello, world!")

if __name__ == "__main__":
    main()
