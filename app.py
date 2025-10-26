import streamlit as st

test_page1 = st.Page(page="test1.py",title="test1")
test_page5 = st.Page(page="test5.py",title="test5")
test_page6 = st.Page(page="test6.py",title="test6")
test_page6 = st.Page(page="test7.py",title="test7")

pg = st.navigation([test_page1,test_page5,test_page6])

pg.run()
