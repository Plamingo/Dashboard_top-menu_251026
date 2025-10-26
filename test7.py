# top-bar 구현 테스트

import streamlit as st
# from PIL import Image

st.set_page_config(layout='wide')

with open('css/style.css',encoding='UTF-8') as f:
  css = f'<style>{f.read()}</style>'

st.html('''
        <style>
        .stAppHeader {
          display:none;
        }
        .stMainBlockContainer {
          padding:0;
        }
        .stImage {
          display: block;
          position: relative;
          z-index:1;
        }
        </style>
        ''')

html_code = '''
<!-- 폰트어썸 불러오기 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">

<header class="top-bar">
  <div class="tob-bar__container">
    <div class="top-bar-left">
      <a href="http://localhost:8501" class="logo"></a>
    </div>
    <div class="top-bar-right">
      <nav class="util-nav">
        <ul class="util-nav-list">
          <li class="util-nav-item"><a href="#" class="util-nav-link">Sign In</a></li>
          <li class="util-nav-item"><a href="#" class="util-nav-link">My Information</a></li>
          <li class="util-nav-item"><a href="#" class="util-nav-link">Temporary</a></li>
          <li class="util-nav-item"><a href="#" class="util-nav-link">Temporary</a></li>
        </ul>
        <div class="search-btn-box">
          <button class="search-btn">
            <i class="fa-solid fa-magnifying-glass"></i>
          </button>
        </div>
      </nav>
      <nav class="top-bar__depth1-menu">
        <ul>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">대시보드</a>

          </li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">프로젝트관리</a>
            <div class="mega-menu">
              <div class="mega-menu-inner">
                <ul class="depth2-list">
                  <li class="depth2-list-item">
                    <a href="#" class="depth2-list-link">2차 메뉴</a>
                    <ul class="depth3-list">
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                    </ul>
                  </li>
                  <li class="depth2-list-item">
                    <a href="#" class="depth2-list-link">2차 메뉴</a>
                    <ul class="depth3-list">
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                    </ul>
                  </li>
                  <li class="depth2-list-item">
                    <a href="#" class="depth2-list-link">2차 메뉴</a>
                    <ul class="depth3-list">
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                      <li class="depth3-list-item"><a href="#" class="depth3-list-link">3차 메뉴아이템</a></li>
                    </ul>
                  </li>

                </ul>
              </div>
            </div>
          </li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">작업관리</a></li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">일정관리</a></li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">문서관리</a></li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">시험DB관리</a></li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">리포트&통계</a></li>
          <li class="depth1-list-item"><a href="#" class="depth1-list-link">MyPage</a></li>
        </ul>
      </nav>
    </div>
  </div>
</header>
'''
    
# topbar_cols= st.columns((1,5))
# with topbar_cols[0]:
#   
# with topbar_cols[1].container():
with st.container(height=120,border=False):
  
  st.html(css+html_code)

  # img = Image.open("Images/TRANSYS_logo.png")
  # st.image(img, width=400)
st.write('test')
st.image(image="Images/TRANSYS_logo.png",width=200,clamp=True)

