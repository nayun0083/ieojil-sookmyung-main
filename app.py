import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

st.title("이어질 숙명")
st.subheader("숙명의 경험이, 나의 내일로 이어집니다.")

st.write("""
숙명여대 학생들을 위한 멘토·멘티 매칭 서비스입니다.
전공, 진로, 학교생활 고민을 함께 나눌 수 있는 연결을 만들어갑니다.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 매칭 테스트")
    st.write("간단한 질문을 통해 나에게 맞는 멘토/멘티를 찾아보세요.")
    if st.button("매칭 테스트 시작하기"):
        st.success("매칭 테스트 페이지로 이동할 예정입니다.")

with col2:
    st.markdown("### 서비스 설명")
    st.write("이어질 숙명이 어떤 서비스인지 알아보세요.")
    if st.button("서비스 설명 보기"):
        st.info("서비스 설명 페이지로 이동할 예정입니다.")

st.divider()

st.header("이어질 숙명에서 할 수 있는 것")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 맞춤형 매칭")
    st.write("관심 분야와 고민 유형을 바탕으로 나와 잘 맞는 멘토/멘티를 추천합니다.")

with col2:
    st.markdown("#### 추천 카드")
    st.write("추천된 멘토/멘티를 카드 형식으로 확인할 수 있습니다.")

with col3:
    st.markdown("#### 채팅 연결")
    st.write("매칭 요청이 수락되면 채팅을 통해 대화를 시작할 수 있습니다.")

st.divider()

st.header("이용 방법")

st.write("""
1. 학교 이메일로 회원가입하기  
2. 매칭 테스트 응답하기  
3. 추천 멘토/멘티 카드 확인하기  
4. 매칭 요청 보내기  
5. 수락되면 채팅 시작하기  
""")

st.divider()

st.caption("© 2026 이어질 숙명 | 숙명여대 학생들을 위한 멘토·멘티 매칭 서비스")
