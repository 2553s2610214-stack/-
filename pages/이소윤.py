1
import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 (바다 테마 이모지 및 와이드 레이아웃)
st.set_page_config(
    page_title="OceanBreeze - AI 바다 힐링 도감",
    page_icon="🌊",
    layout="wide"
)

# API 키 및 Gemini 모델 초기화 예외 처리
try:
    # Streamlit Cloud Secrets에서 API 키 로드
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("⚠️ API 키가 설정되지 않았습니다. Streamlit Cloud의 Secrets 설정을 확인해주세요.")
    st.info("로컬 테스트 시 사이드바에 직접 입력할 수도 있습니다.")
    api_key = None

# 2. 사이드바 구성
with st.sidebar:
    st.title("🌊 OceanBreeze")
    st.write("바다의 신비로움과 평온함을 전하는 AI 공간입니다.")
    st.markdown("---")
    
    # 비밀키 수동 입력 예외 처리 (로컬/디버깅용)
    if not api_key:
        user_key = st.text_input("Gemini API Key 입력", type="password")
        if user_key:
            genai.configure(api_key=user_key)
            api_key = user_key
            st.success("API 키가 임시 적용되었습니다.")
            
    st.caption("제작: Streamlit Cloud 배포 가이드 샘플")

# 3. 메인 화면 헤더
st.title("🐋 OceanBreeze: AI 바다 힐링 도감 & 가이드")
st.subheader("푸른 바다가 주는 평온함과 신비로운 생태계를 탐험해 보세요.")
st.markdown("---")

# 탭 구조 설계 (차별화된 두 가지 기능 제공)
tab1, tab2 = st.tabs(["🧬 AI 신비한 해양 생물 도감", "🧘 바다 사운드스케이프 명상"])

# --- 탭 1: AI 신비한 해양 생물 도감 ---
with tab1:
    st.markdown("### 🗺️ 내가 탐험하고 싶은 바다 선택")
    
    col1, col2 = st.columns(2)
    with col1:
        ocean_zone = st.selectbox(
            "바다 수심/구역",
            ["햇빛이 비치는 표층 (0~200m)", "빛이 희미한 중심해 (200~1000m)", "암흑의 심해 (1000m 이상)", "화려한 숲 산호초 지대", "얼어붙은 극지방 바다"]
        )
    with col2:
        creature_type = st.radio(
            "관심 있는 생물 분류",
            ["거대 포유류 (고래, 돌고래 등)", "독특한 어류 (심해어, 상어 등)", "발광 생물 및 무척추동물", "신비로운 해조류 및 미생물"],
            horizontal=True
        )

    if st.button("🔍 AI 해양 생물 도감 발행하기", key="btn_encyclopedia"):
        if not api_key:
            st.warning("Gemini API Key가 필요합니다. Secrets 설정을 먼저 완료해 주세요.")
        else:
            with st.spinner("AI 학자가 바다 깊은 곳에서 생물 정보를 가져오고 있습니다... 🤿"):
                try:
                    # 안정적이고 가벼운 gemini-2.5-flash-lite 사용
                    model = genai.GenerativeModel("gemini-2.5-flash-lite")
                    
                    prompt = f"""
                    다음 조건에 맞는 가상의 혹은 실제 존재하는 흥미로운 해양 생물 도감 1가지를 작성해줘.
                    - 선택한 구역: {ocean_zone}
                    - 생물 분류: {creature_type}

                    출력은 반드시 읽기 쉬운 마크다운 형식을 사용하고, 구조는 아래 틀을 엄격히 지켜줘:
                    ## 🏷️ 생물 이름: [생물 명칭 (국문/영문)]
                    
                    - **주요 서식지**: {ocean_zone}
                    - **위험도 및 희귀도**: ⭐️⭐️⭐️⭐️⭐️ (별점으로 표현)

                    ### 📝 생태 및 특징
                    [여기에 해당 생물의 외형, 사냥 방식, 혹은 생존 방식에 대한 흥미로운 설명을 3줄 이내로 작성]

                    ### 💡 신비로운 사실 (Fun Fact)
                    - [사람들이 잘 모르는 놀라운 비밀 한 가지를 적어줘]

                    ### 🌊 환경 보존 한마디
                    [이 생물이 살아가는 바다를 지키기 위해 우리가 기억해야 할 점 작성]
                    """
                    
                    response = model.generate_content(prompt)
                    st.success("도감 생성이 완료되었습니다! 📝")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {str(e)}")

# --- 탭 2: 바다 사운드스케이프 명상 ---
with tab2:
    st.markdown("### 🎧 나만의 바다 분위기 설계하기")
    st.write("원하는 환경을 선택하면 AI가 그 장소의 소리, 풍경, 그리고 마인드풀니스(명상) 가이드를 텍스트로 생생하게 묘사해 드립니다.")
    
    col3, col4, col5 = st.columns(3)
    with col3:
        beach_type = st.selectbox("해변 종류", ["부드러운 흰색 모래사장", "파도가 거칠게 치는 절벽 기암괴석", "자갈이 굴러가는 몽돌해변", "조용한 열대섬 맹그로브 숲"])
    with col4:
        time_of_day = st.select_slider("시간대", options=["새벽녘", "한낮", "해질녘", "깊은 밤"])
    with col5:
        weather = st.selectbox("날씨", ["맑고 화창한 날", "안개가 자욱한 신비로운 날", "가벼운 비가 내리는 날", "폭풍우가 지나간 직후"])

    if st.button("🧘 바다 힐링 가이드 시작", key="btn_soundscape"):
        if not api_key:
            st.warning("Gemini API Key가 필요합니다. Secrets 설정을 먼저 완료해 주세요.")
        else:
            with st.spinner("눈을 감고 잠시 기다려 주세요. 바다의 소리를 텍스트로 시각화하는 중입니다... 🌊"):
                try:
                    model = genai.GenerativeModel("gemini-2.5-flash-lite")
                    
                    prompt = f"""
                    사용자가 선택한 환경 정보를 바탕으로, 마음이 편안해지는 ASMR 풍경 묘사와 1분 명상 가이드를 작성해줘.
                    - 해변: {beach_type}
                    - 시간대: {time_of_day}
                    - 날씨: {weather}

                    출력 구조는 다음과 같이 마크다운으로 해줘:
                    ## 🌅 {time_of_day}의 {beach_type} ({weather})
                    
                    ### 🎧 사운드 스케이프 (주변 소리 묘사)
                    [귀로 들리는 파도 소리, 바람 소리, 생물들의 소리를 생생하고 문학적으로 묘사]

                    ### 👁️ 시각적 풍경
                    [눈앞에 펼쳐진 색감과 바다의 모습을 회화적으로 설명]

                    ### 🧘 호흡 가이드 (Mindfulness)
                    1. **들이쉬기**: 파도가 밀려오듯 숨을 깊게 들이쉬세요... (4초)
                    2. **내쉬기**: 파도가 모래사장을 빠져나가듯 천천히 숨을 내쉬세요... (4초)
                    [선택한 분위기에 어울리는 따뜻한 위로의 문장 한 줄로 마무리]
                    """
                    
                    response = model.generate_content(prompt)
                    st.balloons() # 시각적 효과 추가
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {str(e)}")
