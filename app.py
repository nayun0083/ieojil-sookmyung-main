import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🔗",
    layout="wide"
)

# -------------------------
# 상태 초기화
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "selected_mentor" not in st.session_state:
    st.session_state.selected_mentor = "김민지 멘티"

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "text": "🎉 매칭에 성공했어요!"},
        {"role": "mentor", "text": "안녕하세요! 만나서 반가워요 😊"}
    ]


def move_page(page):
    st.session_state.page = page


# -------------------------
# 최소 CSS
# -------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

.card {
    border: 1px solid #30363D;
    border-radius: 12px;
    padding: 20px;
    background-color: #111827;
    min-height: 150px;
}

.small-text {
    color: #A0A7B4;
    font-size: 14px;
}

.chat-box {
    background-color: #161B22;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 14px;
}

.notice {
    color: #A0A7B4;
    font-size: 14px;
}

.result-box {
    background-color: #123524;
    color: #6EE7A8;
    padding: 18px;
    border-radius: 10px;
    margin: 20px 0;
}

button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# -------------------------
# 공통 헤더
# -------------------------
def header():
    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("🔗 이어질 숙명")

    with col2:
        st.write("로그인 | 매칭 | 채팅 | 알림 | 공지사항 | 👤")

    st.divider()


# -------------------------
# 메인페이지
# -------------------------
def main_page():
    header()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("선배와 후배를 연결하고")
        st.title("학교 간 교류를 지원하는 플랫폼")
        st.write(
            "이어질 숙명은 숙명여대 학생들이 전공, 진로, 학교생활 고민을 나누고 "
            "나에게 맞는 멘토 또는 멘티를 만날 수 있도록 돕는 멘토·멘티 매칭 서비스입니다."
        )

    with col2:
        with st.container(border=True):
            st.write("관련 이미지 영역")

    st.divider()

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
                st.session_state.q_index = 0
                st.session_state.answers = {}
                move_page("matching")

    with col3:
        with st.container(border=True):
            st.subheader("서비스 설명보기")
            st.write("이어질 숙명이 어떤 서비스인지 자세히 알아보세요.")
            if st.button("서비스 설명보기", use_container_width=True):
                move_page("service")

    st.divider()
    st.caption("문의: campuslink@email.com  © 2026 이어질 숙명. All rights reserved.")


# -------------------------
# 서비스 설명 페이지
# -------------------------
def service_page():
    header()

    st.title("서비스 설명")

    with st.container(border=True):
        st.header("이어질 숙명은 어떤 서비스인가요?")
        st.write(
            "숙명여대 학생들이 전공, 진로, 학교생활 고민을 나눌 수 있도록 "
            "멘토와 멘티를 연결하는 매칭 서비스입니다."
        )

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

    col1, col2 = st.columns(2)

    with col1:
        if st.button("매칭 테스트 시작하기", use_container_width=True):
            st.session_state.q_index = 0
            st.session_state.answers = {}
            move_page("matching")

    with col2:
        if st.button("메인페이지로 돌아가기", use_container_width=True):
            move_page("main")


# -------------------------
# 매칭 테스트
# -------------------------
questions = [
    {
        "title": "Q1",
        "question": "어떤 도움을 받고 싶나요?",
        "type": "radio",
        "options": ["학교생활", "전공", "취업", "대외활동"]
    },
    {
        "title": "Q1-1",
        "question": "현재 가장 고민되는 것은?",
        "type": "text"
    },
    {
        "title": "Q2",
        "question": "관심 분야는?",
        "type": "radio",
        "options": ["AI", "웹개발", "앱개발", "디자인"]
    },
    {
        "title": "Q3",
        "question": "어떤 선배를 만나고 싶나요?",
        "type": "radio",
        "options": ["친절한", "친구 같은", "경험 많은", "꼼꼼한"]
    },
    {
        "title": "Q4",
        "question": "나의 성향은?",
        "type": "radio",
        "options": ["도전형", "계획형", "신중형", "사교형"]
    },
    {
        "title": "Q5",
        "question": "멘토링 가능한 시간은?",
        "type": "radio",
        "options": ["평일", "주말", "저녁", "상관없음"]
    }
]


def matching_page():
    q = questions[st.session_state.q_index]

    st.title(q["title"])
    st.subheader(q["question"])

    if q["type"] == "radio":
        answer = st.radio(
            "선택해주세요.",
            q["options"],
            key=f"q_{st.session_state.q_index}",
            label_visibility="collapsed"
        )
    else:
        answer = st.text_area(
            "답변을 입력해주세요.",
            key=f"q_{st.session_state.q_index}",
            label_visibility="collapsed"
        )

    st.write("")

    if st.session_state.q_index < len(questions) - 1:
        if st.button("다음"):
            st.session_state.answers[q["title"]] = answer
            st.session_state.q_index += 1
            st.rerun()
    else:
        if st.button("결과 보기"):
            st.session_state.answers[q["title"]] = answer
            move_page("result")
            st.rerun()


# -------------------------
# 매칭 결과
# -------------------------
def result_page():
    st.title("🎉 매칭 결과")
    st.header("당신은 열정송이입니다!")

    st.write("목표가 생기면 끝까지 도전하는 열정적인 유형입니다.")

    st.divider()

    st.header("🌱 나와 잘 맞는 선배를 찾았습니다!")

    with st.container(border=True):
        st.markdown(
            """
            <div class="result-box">
                김송이 선배에게 매칭 신청하시겠습니까?
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("**학과:** 컴퓨터과학과")
        st.write("**학번:** 20학번")
        st.write("**관심 분야:** AI · 웹개발 · 프로젝트")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("프로필 보기", use_container_width=True):
                st.info("프로필 상세 페이지는 이후 구현 예정입니다.")

        with col2:
            if st.button("매칭 신청하기", use_container_width=True):
                st.success("매칭 신청이 완료되었습니다!")
                st.session_state.selected_mentor = "김송이 선배"

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("채팅으로 이동", use_container_width=True):
            move_page("chat")

    with col2:
        if st.button("메인페이지로 이동", use_container_width=True):
            move_page("main")


# -------------------------
# 채팅 페이지
# -------------------------
def chat_page():
    st.title("이어질 숙명")

    col1, col2, col3 = st.columns([1.2, 1.2, 2])

    # 왼쪽: 채팅 목록
    with col1:
        st.header("💬 나의 채팅 목록")

        mentors = [
            {"name": "김민지 멘티", "last": "😊 친해져요!"},
            {"name": "박지훈 멘토", "last": "학교생활이 궁금하면 편하게 물어보세요!"},
            {"name": "이서연 멘티", "last": "📚 같이 공부해요!"}
        ]

        for mentor in mentors:
            if st.button(f"👩 {mentor['name']}", key=mentor["name"], use_container_width=True):
                st.session_state.selected_mentor = mentor["name"]

            st.caption(mentor["last"])
            st.divider()

        if st.button("➕ 새로운 매칭 시작하기", use_container_width=True):
            st.session_state.q_index = 0
            st.session_state.answers = {}
            move_page("matching")

    # 가운데: 추천 주제
    with col2:
        st.header("💡 이런 주제는 어때요?")

        topics = [
            "학교에서 가장 좋아하는 수업은 무엇인가요?",
            "MT와 축제 중 하나만 간다면 무엇을 선택하시겠어요?",
            "방학 때 가장 하고 싶은 것은 무엇인가요?",
            "과제 VS 시험! 하나만 선택한다면?"
        ]

        for topic in topics:
            if st.button(topic, key=f"topic_{topic}", use_container_width=True):
                st.session_state.messages.append({"role": "me", "text": topic})
                st.rerun()

        st.divider()
        st.caption("원하는 메시지를 누르면 대화 상대에게 전송됩니다.")

    # 오른쪽: 채팅창
    with col3:
        st.header(f"👤 {st.session_state.selected_mentor}")

        st.write("🎉 매칭에 성공했어요!")

        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "system":
                st.info(msg["text"])
            elif msg["role"] == "mentor":
                st.markdown(
                    f"""
                    <div class="chat-box">
                        🤖 {msg["text"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div class="chat-box">
                        🧑 {msg["text"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        message = st.chat_input("메시지를 입력하세요.")

        if message:
            st.session_state.messages.append({"role": "me", "text": message})
            st.rerun()


# -------------------------
# 페이지 실행
# -------------------------
if st.session_state.page == "main":
    main_page()

elif st.session_state.page == "service":
    service_page()

elif st.session_state.page == "matching":
    matching_page()

elif st.session_state.page == "result":
    result_page()

elif st.session_state.page == "chat":
    chat_page()
