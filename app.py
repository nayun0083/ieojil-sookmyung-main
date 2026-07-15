import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"


def move_page(page_name):
    st.session_state.page = page_name


# 공통 상단바
def render_header():
    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("🔗 이어질 숙명")

    with col2:
        st.write("로그인   |   매칭   |   채팅   |   알림   |   공지사항   |   👤")

    st.divider()


# 메인페이지
def render_main_page():
    render_header()

    # 히어로 영역
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("선배와 후배를 연결하고")
        st.title("학교 간 교류를 지원하는 플랫폼")
        st.write(
            "이어질 숙명은 숙명여대 학생들이 전공, 진로, 학교생활 고민을 나누고 "
            "나에게 맞는 멘토 또는 멘티를 만날 수 있도록 돕는 멘토·멘티 매칭 서비스입니다."
        )

    with col2:
        st.info("관련 이미지 영역")

    st.divider()

    # 공지 + 버튼 카드
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("공지사항 >")
            st.write("📢 이벤트 결과 발표")
            st.write("...")

    with col2:
        with st.container(border=True):
            st.subheader("매칭 시작하기")
            st.write("나에게 맞는 멘토/멘티를 찾기 위한 매칭 테스트를 시작해보세요.")

            if st.button("매칭 시작하기", use_container_width=True):
                move_page("matching")

    with col3:
        with st.container(border=True):
            st.subheader("서비스 설명보기")
            st.write("이어질 숙명이 어떤 서비스인지 자세히 알아보세요.")

            if st.button("서비스 설명보기", use_container_width=True):
                move_page("service")

    st.divider()

    st.caption("문의: campuslink@email.com  © 2026 이어질 숙명. All rights reserved.")


# 서비스 설명 페이지
def render_service_page():
    render_header()

    st.title("서비스 설명")

    with st.container(border=True):
        st.header("이어질 숙명은 어떤 서비스인가요?")
        st.write(
            "숙명여대 학생들이 전공, 진로, 학교생활 고민을 나눌 수 있도록 "
            "멘토와 멘티를 연결하는 매칭 서비스입니다."
        )

        if st.button("매칭 테스트 시작하기", key="service_top_matching"):
            move_page("matching")

    st.write("")

    with st.container(border=True):
        st.header("왜 필요할까요?")
        st.write("① 선배와 연결될 기회 부족")
        st.write("② 전공/진로 정보 격차")
        st.write("③ 누구에게 물어봐야 할지 모르는 어려움")

    st.write("")

    st.subheader("[핵심 기능 소개]")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("매칭 테스트")
            st.write("질문 기반으로 유형을 분석합니다.")

    with col2:
        with st.container(border=True):
            st.subheader("추천 카드")
            st.write("맞춤 멘토/멘티를 추천합니다.")

    with col3:
        with st.container(border=True):
            st.subheader("채팅 연결")
            st.write("매칭 후 대화가 가능합니다.")

    st.write("")

    st.subheader("[이용방법 안내]")

    with st.container(border=True):
        st.write("1. 학교 이메일로 로그인/가입")
        st.write("2. 매칭 테스트 응답")
        st.write("3. 추천 멘토/멘티 카드 확인")
        st.write("4. 매칭 요청 후 수락되면 채팅 시작")

    st.write("")

    st.write("나에게 맞는 연결을 찾아볼까요?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("매칭 테스트 시작하기", key="service_bottom_matching", use_container_width=True):
            move_page("matching")

    with col2:
        if st.button("메인페이지로 돌아가기", use_container_width=True):
            move_page("main")


# 임시 매칭 테스트 페이지
def render_matching_page():
    render_header()

    st.title("매칭 테스트")

    st.write("나에게 맞는 멘토/멘티를 찾기 위한 질문에 답해주세요.")

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

    if st.button("결과 보기"):
        st.success("당신은 성장형 연결송이입니다!")
        st.write("추천 카드 페이지로 연결될 예정입니다.")

    st.write("")

    if st.button("메인페이지로 돌아가기"):
        move_page("main")


# 페이지 실행
if st.session_state.page == "main":
    render_main_page()

elif st.session_state.page == "service":
    render_service_page()

elif st.session_state.page == "matching":
    render_matching_page()
