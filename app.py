import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #F6F9FC 0%, #FFFFFF 100%);
}

/* 기본 여백 */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* 상단 로고 텍스트 */
.logo {
    font-size: 24px;
    font-weight: 900;
    color: #0B1F3A;
    margin-bottom: 20px;
}

/* 히어로 영역 */
.hero {
    background: linear-gradient(135deg, #0B1F3A 0%, #1E4E8C 70%, #3B82F6 100%);
    padding: 64px 56px;
    border-radius: 32px;
    color: white;
    margin-bottom: 42px;
    box-shadow: 0 20px 50px rgba(11, 31, 58, 0.18);
}

.hero-badge {
    display: inline-block;
    background-color: rgba(255,255,255,0.16);
    padding: 8px 16px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 20px;
}

.hero-title {
    font-size: 52px;
    font-weight: 900;
    line-height: 1.2;
    margin-bottom: 18px;
}

.hero-subtitle {
    font-size: 19px;
    line-height: 1.7;
    color: rgba(255,255,255,0.88);
    max-width: 760px;
}

/* 섹션 제목 */
.section-title {
    font-size: 32px;
    font-weight: 900;
    color: #0B1F3A;
    margin-top: 30px;
    margin-bottom: 8px;
}

.section-desc {
    font-size: 16px;
    color: #64748B;
    margin-bottom: 24px;
}

/* 카드 */
.card {
    background-color: #FFFFFF;
    border-radius: 24px;
    padding: 28px;
    min-height: 210px;
    border: 1px solid #E3ECF7;
    box-shadow: 0 12px 30px rgba(15, 31, 58, 0.08);
    transition: all 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 38px rgba(15, 31, 58, 0.12);
}

.card-icon {
    width: 46px;
    height: 46px;
    border-radius: 16px;
    background-color: #EEF5FF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 18px;
}

.card-title {
    font-size: 21px;
    font-weight: 850;
    color: #0B1F3A;
    margin-bottom: 10px;
}

.card-text {
    color: #52616B;
    line-height: 1.65;
    font-size: 15px;
}

/* 이용방법 박스 */
.step-box {
    background-color: #F4F8FF;
    border: 1px solid #DDE7F7;
    border-radius: 22px;
    padding: 22px;
    text-align: center;
    min-height: 145px;
}

.step-num {
    width: 34px;
    height: 34px;
    background-color: #0B1F3A;
    color: white;
    border-radius: 999px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    margin-bottom: 12px;
}

.step-title {
    font-weight: 800;
    color: #0B1F3A;
    margin-bottom: 8px;
}

.step-text {
    color: #52616B;
    font-size: 14px;
}

/* CTA */
.cta {
    background-color: #EEF5FF;
    border-radius: 28px;
    padding: 42px;
    margin-top: 42px;
    text-align: center;
    border: 1px solid #DDE7F7;
}

.cta-title {
    font-size: 30px;
    font-weight: 900;
    color: #0B1F3A;
    margin-bottom: 10px;
}

.cta-text {
    color: #52616B;
    font-size: 16px;
}

/* 푸터 */
.footer {
    margin-top: 56px;
    padding: 28px;
    border-radius: 22px;
    background-color: #0B1F3A;
    color: rgba(255,255,255,0.75);
    text-align: center;
    font-size: 14px;
}

/* 버튼 */
div.stButton > button {
    background-color: #0B1F3A;
    color: white;
    border-radius: 999px;
    padding: 0.75rem 1.4rem;
    border: none;
    font-weight: 800;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #1E4E8C;
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)


# 상단 로고
st.markdown('<div class="logo">🔗 이어질 숙명</div>', unsafe_allow_html=True)

# 히어로 영역
st.markdown("""
<div class="hero">
    <div class="hero-badge">Sookmyung Mentor-Mentee Matching Platform</div>
    <div class="hero-title">숙명의 경험이,<br>나의 내일로 이어집니다.</div>
    <div class="hero-subtitle">
        이어질 숙명은 숙명여대 학생들이 전공, 진로, 학교생활 고민을 나누고
        나에게 맞는 멘토 또는 멘티를 만날 수 있도록 돕는 캠퍼스 멘토링 매칭 서비스입니다.
    </div>
</div>
""", unsafe_allow_html=True)

# CTA 버튼
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("매칭 테스트 시작하기"):
        st.success("매칭 테스트 페이지로 이동할 예정입니다.")

with col2:
    if st.button("서비스 설명 보기"):
        st.info("서비스 설명 페이지로 이동할 예정입니다.")

with col3:
    if st.button("멘토로 함께하기"):
        st.info("멘토 등록 페이지로 이동할 예정입니다.")


# 핵심 기능
st.markdown('<div class="section-title">이어질 숙명에서 할 수 있는 것</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">나에게 맞는 연결을 찾고, 경험을 나누며 함께 성장할 수 있어요.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🧭</div>
        <div class="card-title">맞춤형 매칭</div>
        <div class="card-text">
            관심 분야, 고민 유형, 선호 스타일을 바탕으로
            나와 잘 맞는 멘토 또는 멘티를 추천합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">💬</div>
        <div class="card-title">추천 카드</div>
        <div class="card-text">
            추천된 멘토/멘티를 카드 형식으로 확인하고
            매칭률과 추천 이유를 직관적으로 비교할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🤝</div>
        <div class="card-title">채팅 연결</div>
        <div class="card-text">
            매칭 요청이 수락되면 채팅방이 생성되어
            전공, 진로, 학교생활 고민을 나눌 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)


# 이용 방법
st.markdown('<div class="section-title">이용 방법</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">간단한 단계로 나에게 맞는 연결을 찾아보세요.</div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-title">회원가입</div>
        <div class="step-text">학교 이메일로 안전하게 시작해요.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-title">매칭 테스트</div>
        <div class="step-text">관심사와 고민을 입력해요.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-title">추천 확인</div>
        <div class="step-text">추천 카드를 확인해요.</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="step-box">
        <div class="step-num">4</div>
        <div class="step-title">매칭 요청</div>
        <div class="step-text">마음에 드는 상대에게 요청해요.</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="step-box">
        <div class="step-num">5</div>
        <div class="step-title">채팅 시작</div>
        <div class="step-text">수락되면 대화를 시작해요.</div>
    </div>
    """, unsafe_allow_html=True)


# 안전한 커뮤니티
st.markdown('<div class="section-title">안전한 커뮤니티</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">학생들이 안심하고 소통할 수 있는 환경을 지향합니다.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🏫</div>
        <div class="card-title">학교 이메일 기반</div>
        <div class="card-text">
            숙명여대 학생 인증을 기반으로 신뢰할 수 있는 연결을 제공합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🔒</div>
        <div class="card-title">개인정보 보호</div>
        <div class="card-text">
            필요한 정보만 수집하고, 민감한 정보는 최소화하는 방향으로 설계합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">📢</div>
        <div class="card-title">신고 및 안내</div>
        <div class="card-text">
            부적절한 대화나 불편한 상황을 신고할 수 있는 기능을 고려합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)


# 마지막 CTA
st.markdown("""
<div class="cta">
    <div class="cta-title">나에게 맞는 연결을 찾아볼까요?</div>
    <div class="cta-text">
        간단한 매칭 테스트를 통해 나와 잘 맞는 멘토/멘티를 확인해보세요.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

if st.button("지금 매칭 테스트 시작하기"):
    st.success("매칭 테스트 페이지로 이동할 예정입니다.")


# 푸터
st.markdown("""
<div class="footer">
    이어질 숙명 · 숙명여대 학생들을 위한 멘토·멘티 매칭 서비스<br>
    서비스 소개 · 이용 가이드 · 안전한 커뮤니티 · 문의하기<br><br>
    © 2026 이어질 숙명. All rights reserved.
</div>
""", unsafe_allow_html=True)
