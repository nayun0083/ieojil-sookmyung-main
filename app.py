import streamlit as st

# =============================
# 페이지 기본 설정
# =============================
st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

# =============================
# 페이지 상태 관리
# =============================
if "page" not in st.session_state:
    st.session_state.page = "main"


def set_page(page_name):
    st.session_state.page = page_name


# =============================
# CSS
# =============================
st.markdown("""
<style>
/* 전체 배경 */
.stApp {
    background-color: #F6F9FC;
}

/* 전체 너비 */
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* 기본 텍스트 */
body {
    color: #111827;
}

/* 상단바 */
.navbar {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 16px;
    padding: 16px 22px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 6px 20px rgba(15, 31, 58, 0.05);
}

.logo-area {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, #0B1F3A, #2563EB);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 22px;
    font-weight: 900;
}

.logo-text {
    font-size: 20px;
    font-weight: 900;
    color: #0B1F3A;
}

.nav-menu {
    color: #374151;
    font-size: 15px;
    font-weight: 700;
}

/* 공통 박스 */
.box {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 30px;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

/* 메인 히어로 */
.hero {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 42px;
    min-height: 250px;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

.hero-title {
    font-size: 36px;
    font-weight: 900;
    line-height: 1.45;
    color: #111827;
    margin-bottom: 18px;
}

.hero-desc {
    font-size: 16px;
    line-height: 1.8;
    color: #52616B;
}

.image-circle {
    width: 190px;
    height: 190px;
    border-radius: 999px;
    border: 2px solid #D7DEE8;
    background: linear-gradient(135deg, #EEF5FF, #FFFFFF);
    display: flex;
    justify-content: center;
    align-items: center;
    color: #64748B;
    font-weight: 800;
    margin: 0 auto;
}

/* 공지 */
.notice-box {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 24px;
    min-height: 210px;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

.notice-title {
    font-size: 18px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 14px;
}

.notice-text {
    font-size: 15px;
    color: #374151;
    line-height: 1.8;
}

/* Streamlit container 박스 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
    border: 1px solid #D7DEE8;
    background-color: #FFFFFF;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

/* 액션 카드 내부 */
.action-inner {
    text-align: center;
    padding: 26px 10px 18px 10px;
    min-height: 150px;
}

.action-title {
    font-size: 25px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 16px;
}

.action-desc {
    font-size: 16px;
    color: #52616B;
    line-height: 1.7;
}

/* 페이지 제목 */
.page-title {
    font-size: 42px;
    font-weight: 900;
    color: #111827;
    text-align: center;
    margin-bottom: 28px;
}

/* 섹션 */
.section-title {
    font-size: 28px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 16px;
}

.section-text {
    font-size: 16px;
    line-height: 1.8;
    color: #374151;
}

/* 기능 카드 */
.feature-card {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 28px;
    min-height: 170px;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

.feature-title {
    font-size: 24px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 14px;
}

.feature-desc {
    font-size: 15px;
    color: #52616B;
    line-height: 1.7;
}

/* 이용 방법 */
.guide-box {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

.guide-title {
    font-size: 20px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 12px;
}

.guide-text {
    font-size: 16px;
    line-height: 1.9;
    color: #374151;
}

/* 매칭 페이지 */
.temp-box {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 24px;
    box-shadow: 0 10px 26px rgba(15, 31, 58, 0.06);
}

/* 푸터 */
.footer {
    background-color: #FFFFFF;
    border: 1px solid #D7DEE8;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    color: #6B7280;
    font-size: 13px;
    margin-top: 30px;
}

/* 버튼 */
div.stButton > button {
    background-color: #0B1F3A;
    color: white;
    border: 1px solid #0B1F3A;
    border-radius: 999px;
    padding: 0.75rem 1.2rem;
    font-weight: 800;
    font-size: 16px;
}

div.stButton > button:hover {
    background-color: #1E3A8A;
    color: white;
    border: 1px solid #1E3A8A;
}

/* 모바일 여백 약간 보정 */
@media screen and (max-width: 768px) {
    .hero-title {
        font-size: 28px;
    }

    .page-title {
        font-size: 32px;
    }

    .nav-menu {
        font-size: 12px;
    }
}
</style>
""", unsafe_allow_html=True)


# =============================
# 공통 상단바
# =============================
def render_navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo-area">
            <div class="logo-icon">✦</div>
            <div class="logo-text">이어질 숙명</div>
        </div>
        <div class="nav-menu">
            로그인 &nbsp;&nbsp; 매칭 &nbsp;&nbsp; 채팅 &nbsp;&nbsp; 알림 &nbsp;&nbsp; 공지사항 &nbsp;&nbsp; 👤
        </div>
    </div>
    """, unsafe_allow_html=True)


# =============================
# 메인페이지
# =============================
def render_main_page():
    render_navbar()

    # 히어로 영역
    col1, col2 = st.columns([2.2, 1])

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

    st.write("")

    # 공지 + 매칭 + 서비스 설명
    col1, col2, col3 = st.columns([1.1, 1, 1])

    with col1:
        st.markdown("""
        <div class="notice-box">
            <div class="notice-title">공지사항 &gt;</div>
            <div class="notice-text">
                📢 이벤트 결과 발표<br><br>
                ...
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        with st.container(border=True):
            st.markdown("""
            <div class="action-inner">
                <div class="action-title">매칭 시작하기</div>
                <div class="action-desc">
                    나에게 맞는 멘토/멘티를 찾기 위한<br>
                    매칭 테스트를 시작해보세요.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.button(
                "매칭 시작하기",
                key="main_matching_btn",
                use_container_width=True,
                on_click=set_page,
                args=("matching",)
            )

    with col3:
        with st.container(border=True):
            st.markdown("""
            <div class="action-inner">
                <div class="action-title">서비스 설명보기</div>
                <div class="action-desc">
                    이어질 숙명이 어떤 서비스인지<br>
                    자세히 알아보세요.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.button(
                "서비스 설명보기",
                key="main_service_btn",
                use_container_width=True,
                on_click=set_page,
                args=("service",)
            )

    # 푸터
    st.markdown("""
    <div class="footer">
        문의: campuslink@email.com &nbsp;&nbsp; © 2026 이어질 숙명. All rights reserved.
    </div>
    """, unsafe_allow_html=True)


# =============================
# 서비스 설명 페이지
# =============================
def render_service_page():
    render_navbar()

    st.markdown('<div class="page-title">서비스 설명</div>', unsafe_allow_html=True)

    # 서비스 소개
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

    st.button(
        "매칭 테스트 시작하기",
        key="service_matching_top",
        use_container_width=True,
        on_click=set_page,
        args=("matching",)
    )

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

    # 핵심 기능
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

    # 이용 방법
    st.markdown("### [이용방법 안내]")

    st.markdown("""
    <div class="guide-box">
        <div class="guide-title">이용 방법</div>
        <div class="guide-text">
            1. 학교 이메일로 로그인/가입<br>
            2. 매칭 테스트 응답<br>
            3. 추천 멘토/멘티 카드 확인<br>
            4. 매칭 요청 후 수락되면 채팅 시작
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="section-text" style="font-weight:900; color:#111827;">
        나에게 맞는 연결을 찾아볼까요?
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "매칭 테스트 시작하기",
            key="service_matching_bottom",
            use_container_width=True,
            on_click=set_page,
            args=("matching",)
        )

    with col2:
        st.button(
            "메인페이지로 돌아가기",
            key="service_back_main",
            use_container_width=True,
            on_click=set_page,
            args=("main",)
        )


# =============================
# 임시 매칭 테스트 페이지
# =============================
def render_matching_page():
    render_navbar()

    st.markdown('<div class="page-title">매칭 테스트</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="temp-box">
        <div class="section-title">나에게 맞는 연결을 찾아보세요</div>
        <div class="section-text">
            이 페이지는 이후 매칭 테스트 질문 화면으로 연결될 예정입니다.
            현재는 페이지 이동이 잘 되는지 확인하기 위한 임시 화면입니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    interest = st.multiselect(
        "관심 분야를 선택해주세요.",
        ["전공 공부", "진로 탐색", "취업 준비", "공모전", "대외활동", "학교생활"]
    )

    concern = st.selectbox(
        "현재 가장 고민되는 부분은 무엇인가요?",
        ["선택해주세요", "전공 공부", "진로", "수강신청", "학교생활", "대외활동"]
    )

    style = st.radio(
        "어떤 스타일의 멘토/멘티를 선호하나요?",
        ["친절한 설명형", "현실 조언형", "경험 공유형", "함께 성장형"]
    )

    if st.button("결과 보기", use_container_width=True):
        st.success("당신은 성장형 연결송이입니다!")
        st.write("추천 카드 페이지로 연결될 예정입니다.")

    st.write("")

    st.button(
        "메인페이지로 돌아가기",
        key="matching_back_main",
        use_container_width=True,
        on_click=set_page,
        args=("main",)
    )


# =============================
# 페이지 실행
# =============================
if st.session_state.page == "main":
    render_main_page()

elif st.session_state.page == "service":
    render_service_page()

elif st.session_state.page == "matching":
    render_matching_page()
