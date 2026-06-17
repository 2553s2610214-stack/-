
import streamlit as st
from google import genai

# API 키 불러오기
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("API 키를 불러오지 못했습니다.")
    st.stop()

st.title("🍔 음식 메뉴 추천 챗봇")

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("오늘 뭐 먹을지 물어보세요!")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # 대화 기록 구성
        history = ""
        for msg in st.session_state.messages:
            role = "사용자" if msg["role"] == "user" else "AI"
            history += f"{role}: {msg['content']}\n"

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
            너는 음식 메뉴 추천 전문가야.
            사용자의 취향, 상황, 날씨 등을 고려해서 메뉴를 추천해줘.

            대화 기록:
            {history}
            """
        )

        answer = response.text

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
