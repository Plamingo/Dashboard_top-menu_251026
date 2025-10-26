import streamlit as st

st.set_page_config(layout="wide")

st.title("시험 불만족 내역")
st.title("수정되었음")

left, right = st.columns([1, 2])

with left:
    st.subheader("시험 사진")
    img_file = st.file_uploader("시험 이미지 업로드", type=["jpg", "png", "jpeg"])
    if img_file:
        st.image(img_file, use_column_width=True, caption="시험품 사진")

with right:
    st.subheader("시험 정보 입력")
    spec = st.text_input("SPEC (규격/모델명)")
    test_result = st.text_area("시험결과")
    test_item = st.text_input("시험품명")
    # 추가 입력 항목
    etc = st.text_area("기타 불만족 내용(선택)")
    if st.button("저장"):
        st.success("저장되었습니다!")

# 스타일 개선: 중앙 분리선과 padding 추가 (CSS)
st.markdown("""
    <style>
    .block-container {
        padding-top: 40px;
        padding-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)        