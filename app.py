import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

# 페이지 이동 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_main():
    st.session_state.page = "main"

def go_service():
    st.session_state.page = "service"

def go_matching():
    st.session_state.page = "matching"



# CSS 디자인
st.markdown("""
<style>
.stApp {
    background-color: #F7F9FC;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* 공통 카드 */
.box {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 26px;
    box-shadow: 0 8px 24px rgba(13, 27, 61, 0.06);
}

/* 상단바 */
.navbar {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 16px 22px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo-area {
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 900;
    font-size: 20px;
    color: #0B1F3A;
}

.logo-icon {
    width: 42px;
    height: 42px;
    border-radius: 10px;
    background: linear-gradient(135deg, #0B1F3A, #2F6FED);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
}

/* 히어로 */
.hero {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 34px;
    margin-bottom: 24px;
}

.hero-title {
    font-size: 34px;
    font-weight: 900;
    line-height: 1.45;
    color: #111827;
}

.hero-desc {
    margin-top: 14px;
    color: #52616B;
    font-size: 16px;
    line-height: 1.7;
}

.image-circle {
    width: 180px;
    height: 180px;
    border-radius: 999px;
    border: 2px solid #D7DEE8;
    background: linear-gradient(135deg, #EEF5FF, #FFFFFF);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #64748B;
    font-weight: 700;
    margin-left: auto;
}

/* 공지 */
.notice {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 22px;
    min-height: 150px;
}

.notice-title {
    font-weight: 800;
    color: #111827;
    margin-bottom: 12px;
}

/* 작은 기능 버튼 카드 */
.action-card {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 24px;
    text-align: center;
    min-height: 150px;
}

.action-title {
    font-size: 20px;
    font-weight: 850;
    color: #111827;
    margin-bottom: 8px;
}

.action-desc {
    color: #52616B;
    font-size: 15px;
    line-height: 1.6;
}

/* 서비스 설명 페이지 */
.page-title {
    font-size: 36px;
    font-weight: 900;
    text-align: center;
    color: #111827;
    margin-bottom: 26px;
}

.section-title {
    font-size: 26px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 14px;
}

.section-text {
    font-size: 16px;
    line-height: 1.8;
    color: #374151;
}

.feature-card {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 24px;
    min-height: 150px;
}

.feature-title {
    font-size: 24px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 12px;
}

.feature-desc {
    color: #52616B;
    font-size: 15px;
    line-height: 1.6;
}

.guide-box {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 24px;
    margin-top: 18px;
    width: 100%;
}

.cta-box {
    background-color: #ECFDF3;
    border: 1px solid #86EFAC;
    color: #14532D;
    border-radius: 999px;
    padding: 14px 28px;
    text-align: center;
    font-weight: 800;
    margin-top: 14px;
}

/* 푸터 */
.footer {
    background-color: white;
    border: 1px solid #D7DEE8;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    color: #6B7280;
    font-size: 13px;
    margin-top: 28px;
}

/* Streamlit 버튼 */
div.stButton > button {
    border-radius: 999px;
    border: 1px solid #0B1F3A;
    background-color: #0B1F3A;
    color: white;
    font-weight: 800;
    padding: 0.7rem 1.2rem;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #1E3A8A;
    color: white;
    border: 1px solid #1E3A8A;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 상단바 함수
# -----------------------------
def render_navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo-area">
            <div class="logo-icon">✦</div>
            <div>이어질 숙명</div>
        </div>
        <div style="color:#64748B; font-size:14px;">
            로그인 · 매칭 · 채팅 · 알림 · 공지사항
        </div>
    </div>
    """, unsafe_allow_html=True)



# 메인페이지
def render_main_page():
    render_navbar()

    # 히어로 영역
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="hero">
            <div class="hero-title">
                선배와 후배를 연결하고<br>
                학교 간 교류를 지원하는 플랫폼
            </div>
            <div class="hero-desc">
                이어질 숙명은 숙명여대 학생들이 전공, 진로, 학교생활 고민을 나누고
                나에게 맞는 멘토 또는 멘티를 만날 수 있도록 돕는 멘토·멘티 매칭 서비스입니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="hero" style="display:flex; align-items:center; justify-content:center;">
            <div class="image-circle">관련 이미지</div>
        </div>
        """, unsafe_allow_html=True)

    # 공지 + 버튼 카드
    col1, col2, col3 = st.columns([1.2, 1, 1])

    with col1:
        st.markdown("""
        <div class="notice">
            <div class="notice-title">공지사항 &gt;</div>
            <div>📢 이벤트 결과 발표</div>
            <br>
            <div style="color:#6B7280;">...</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="action-card">
            <div class="action-title">매칭 시작하기</div>
            <div class="action-desc">나에게 맞는 멘토/멘티를 찾기 위한 매칭 테스트를 시작해보세요.</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("매칭 시작하기", key="main_matching_btn"):
            go_matching()

    with col3:
        st.markdown("""
        <div class="action-card">
            <div class="action-title">서비스 설명보기</div>
            <div class="action-desc">이어질 숙명이 어떤 서비스인지 자세히 알아보세요.</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("서비스 설명보기", key="main_service_btn"):
            go_service()

    # 푸터
    st.markdown("""
    <div class="footer">
        문의: campuslink@email.com &nbsp;&nbsp; © 2026 이어질 숙명. All rights reserved.
    </div>
    """, unsafe_allow_html=True)


# 서비스 설명 페이지
def render_service_page():
    render_navbar()

    st.markdown('<div class="page-title">서비스 설명</div>', unsafe_allow_html=True)

    # 소개 박스
    st.markdown("""
    <div class="box">
        <div class="section-title">이어질 숙명은 어떤 서비스인가요?</div>
        <div class="section-text">
            숙명여대 학생들이 전공, 진로, 학교생활 고민을 나눌 수 있도록
            멘토와 멘티를 연결하는 매칭 서비스입니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("매칭 테스트 시작하기", key="service_matching_top"):
        go_matching()

    st.write("")

    # 왜 필요한가요
    st.markdown("""
    <div class="box">
        <div class="section-title">왜 필요할까요?</div>
        <div class="section-text">
            ① 선배와 연결될 기회 부족<br>
            ② 전공/진로 정보 격차<br>
            ③ 누구에게 물어봐야 할지 모르는 어려움
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 핵심 기능 소개
    st.markdown("### [핵심 기능 소개]")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">매칭 테스트</div>
            <div class="feature-desc">
                질문 기반으로 사용자의 고민과 선호 스타일을 분석합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">추천 카드</div>
            <div class="feature-desc">
                나와 잘 맞는 멘토/멘티를 카드 형식으로 추천합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">채팅 연결</div>
            <div class="feature-desc">
                매칭 후 서로 대화할 수 있는 채팅 연결을 제공합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # 이용 방법 안내
    st.markdown("### [이용방법 안내]")

    st.markdown("""
    <div class="guide-box">
        <b>이용 방법</b><br><br>
        1. 학교 이메일로 로그인/가입<br>
        2. 매칭 테스트 응답<br>
        3. 추천 멘토/멘티 카드 확인<br>
        4. 매칭 요청 후 수락되면 채팅 시작
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div style="font-weight:800; color:#111827; margin-top:20px;">
        나에게 맞는 연결을 찾아볼까요?
    </div>
    """, unsafe_allow_html=True)

    if st.button("매칭 테스트 시작하기", key="service_matching_bottom"):
        go_matching()

    if st.button("메인페이지로 돌아가기", key="back_main"):
        go_main()



# 임시 매칭 페이지
def render_matching_page():
    render_navbar()

    st.markdown('<div class="page-title">매칭 테스트</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
        <div class="section-title">나에게 맞는 연결을 찾아보세요</div>
        <div class="section-text">
            이 페이지는 이후 매칭 테스트 질문 화면으로 연결될 예정입니다.
            현재는 페이지 이동이 잘 되는지 확인하기 위한 임시 화면입니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    interest = st.multiselect(
        "관심 분야를 선택해주세요.",
        ["전공 공부", "진로 탐색", "취업 준비", "공모전", "대외활동", "학교생활"]
    )

    concern = st.selectbox(
        "현재 가장 고민되는 부분은 무엇인가요?",
        ["선택해주세요", "전공 공부", "진로", "수강신청", "학교생활", "대외활동"]
    )

    if st.button("결과 보기"):
        st.success("당신은 성장형 연결송이입니다!")
        st.write("추천 카드 페이지로 연결될 예정입니다.")

    if st.button("메인페이지로 돌아가기", key="matching_back_main"):
        go_main()


# 페이지 렌더링
if st.session_state.page == "main":
    render_main_page()

elif st.session_state.page == "service":
    render_service_page()

elif st.session_state.page == "matching":
    render_matching_page()
