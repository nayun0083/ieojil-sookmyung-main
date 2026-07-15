import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

st.title("이어질 숙명")
st.subheader("나에게 맞는 멘토와 이어지는 캠퍼스 연결 플랫폼")

st.markdown("""
숙명여대 학생들이 전공, 진로, 학교생활 고민을 나누고  
나에게 맞는 멘토 또는 멘티를 만날 수 있도록 돕는 멘토·멘티 매칭 서비스입니다.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="
        background-color: #F4F8FF;
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #DDE7F7;
    ">
        <h3 style="color:#102A43;">나의 연결 유형 찾기</h3>
        <p>간단한 매칭 테스트를 통해 나와 잘 맞는 멘토/멘티를 찾아보세요.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("매칭 테스트 시작하기"):
        st.success("매칭 테스트 페이지로 이동할 예정입니다.")

with col2:
    st.markdown("""
    <div style="
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #DDE7F7;
    ">
        <h3 style="color:#102A43;">서비스 알아보기</h3>
        <p>이어질 숙명이 어떤 서비스인지, 어떻게 이용하는지 확인해보세요.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("서비스 설명 보기"):
        st.info("서비스 설명 페이지로 이동할 예정입니다.")

st.divider()

st.header("이어질 숙명에서 할 수 있는 것")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 맞춤형 매칭")
    st.write("관심 분야, 고민 유형, 선호 스타일을 바탕으로 잘 맞는 멘토/멘티를 추천합니다.")

with col2:
    st.markdown("### 추천 카드")
    st.write("추천된 멘토/멘티를 카드 형식으로 확인하고 비교할 수 있습니다.")

with col3:
    st.markdown("### 채팅 연결")
    st.write("매칭 요청이 수락되면 채팅을 통해 대화를 시작할 수 있습니다.")

st.divider()

st.header("이용 방법")

st.markdown("""
1. 학교 이메일로 회원가입하기  
2. 매칭 테스트 응답하기  
3. 추천 멘토/멘티 카드 확인하기  
4. 매칭 요청 보내기  
5. 수락되면 채팅 시작하기  
""")

st.divider()

st.caption("© 2026 이어질 숙명 | 숙명여대 학생들을 위한 멘토·멘티 매칭 서비스")
