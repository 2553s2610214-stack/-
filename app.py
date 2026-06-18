import streamlit as st
import random

st.set_page_config(
    page_title="날씨 음식 추천",
    page_icon="🍽️",
    layout="wide"
)

food_data = {
    "☀️ 맑음": [
        {"name": "피자", "image": "https://picsum.photos/400/300?1"},
        {"name": "햄버거", "image": "https://picsum.photos/400/300?2"},
        {"name": "샐러드", "image": "https://picsum.photos/400/300?3"},
        {"name": "샌드위치", "image": "https://picsum.photos/400/300?4"},
        {"name": "치킨", "image": "https://picsum.photos/400/300?5"},
        {"name": "파스타", "image": "https://picsum.photos/400/300?6"}
    ],
    "🌧️ 비": [
        {"name": "파전", "image": "https://picsum.photos/400/300?7"},
        {"name": "칼국수", "image": "https://picsum.photos/400/300?8"},
        {"name": "수제비", "image": "https://picsum.photos/400/300?9"},
        {"name": "짬뽕", "image": "https://picsum.photos/400/300?10"},
        {"name": "김치찌개", "image": "https://picsum.photos/400/300?11"},
        {"name": "라면", "image": "https://picsum.photos/400/300?12"}
    ],
    "❄️ 눈": [
        {"name": "어묵", "image": "https://picsum.photos/400/300?13"},
        {"name": "붕어빵", "image": "https://picsum.photos/400/300?14"},
        {"name": "호떡", "image": "https://picsum.photos/400/300?15"},
        {"name": "국밥", "image": "https://picsum.photos/400/300?16"},
        {"name": "떡볶이", "image": "https://picsum.photos/400/300?17"},
        {"name": "순대", "image": "https://picsum.photos/400/300?18"}
    ],
    "🔥 더움": [
        {"name": "냉면", "image": "https://picsum.photos/400/300?19"},
        {"name": "빙수", "image": "https://picsum.photos/400/300?20"},
        {"name": "초밥", "image": "https://picsum.photos/400/300?21"},
        {"name": "물회", "image": "https://picsum.photos/400/300?22"},
        {"name": "샐러드", "image": "https://picsum.photos/400/300?23"},
        {"name": "아이스크림", "image": "https://picsum.photos/400/300?24"}
    ],
    "🥶 추움": [
        {"name": "삼계탕", "image": "https://picsum.photos/400/300?25"},
        {"name": "곰탕", "image": "https://picsum.photos/400/300?26"},
        {"name": "부대찌개", "image": "https://picsum.photos/400/300?27"},
        {"name": "샤브샤브", "image": "https://picsum.photos/400/300?28"},
        {"name": "갈비탕", "image": "https://picsum.photos/400/300?29"},
        {"name": "설렁탕", "image": "https://picsum.photos/400/300?30"}
    ]
}

st.title("🌤️ 날씨와 어울리는 음식 추천")
st.write("오늘 날씨를 선택하면 음식을 추천해드립니다!")

weather = st.selectbox(
    "오늘 날씨를 선택하세요",
    list(food_data.keys())
)

if st.button("🍽️ 음식 추천 받기"):

    foods = random.sample(
        food_data[weather],
        min(4, len(food_data[weather]))
    )

    st.subheader("추천 음식")

    cols = st.columns(2)

    for idx, food in enumerate(foods):

        with cols[idx % 2]:

            st.image(
                food["image"],
                use_container_width=True
            )

            st.markdown(f"### {food['name']}")

            if st.button(
                f"{food['name']} 선택",
                key=f"{food['name']}_{idx}"
            ):

                st.success(
                    f"오늘의 선택은 {food['name']} 입니다! 🎉"
                )

                all_foods = []

                for food_list in food_data.values():
                    all_foods.extend(food_list)

                extra_foods = random.sample(all_foods, 3)

                st.subheader("🎁 추가 추천")

                extra_cols = st.columns(3)

                for i, item in enumerate(extra_foods):

                    with extra_cols[i]:
                        st.image(
                            item["image"],
                            use_container_width=True
                        )
                        st.write(item["name"])
