import streamlit as st
import streamlit.components.v1 as components

def codepen_default():
    st.write('codepen embed')

    # CodePen embed HTML
    codepen_html = """
    <p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="qEOvYbQ" data-pen-title="AG GRID 연습" data-user="Plamingo" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
        <span>See the Pen <a href="https://codepen.io/Plamingo/pen/qEOvYbQ">
    AG GRID 연습</a> by Jackson Kim (<a href="https://codepen.io/Plamingo">@Plamingo</a>)
    on <a href="https://codepen.io">CodePen</a>.</span>
        </p>
        <script async src="https://public.codepenassets.com/embed/index.js"></script>
    """
    # html 실행하기
    components.html(codepen_html, height=500)



# 탭으로 구분
tab1, tab2, tab3 = st.tabs(["Button Animation", "CSS Grid", "Custom HTML"])

with tab1:
    st.subheader("버튼 애니메이션")
    components.html("""
    <iframe 
      height="400" 
      style="width: 100%;" 
      src="https://codepen.io/t_afif/embed/bGOYNrO?default-tab=result" 
      frameborder="0">
    </iframe>
    """, height=420)

with tab2:
    st.subheader("CSS Grid 레이아웃")
    components.html("""
    <iframe 
      height="400" 
      style="width: 100%;" 
      src="https://codepen.io/milanraring/embed/preview/KKgGvrK?default-tab=result" 
      frameborder="0">
    </iframe>
    """, height=420)

with tab3:
    # 사용자 입력으로 CodePen URL 받기
    codepen_id = st.text_input("CodePen ID 입력", "abc123")
    username = st.text_input("Username 입력", "username")
    
    if st.button("임베드"):
        embed_url = f"https://codepen.io/{username}/embed/{codepen_id}?default-tab=result"
        components.html(f"""
        <iframe 
          height="500" 
          style="width: 100%;" 
          src="{embed_url}" 
          frameborder="0">
        </iframe>
        """, height=520)