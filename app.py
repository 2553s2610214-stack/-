import streamlit as st
import random
from foods import food_data

st.set_page_config(
    page_title="날씨 음식 추천",
    page_icon="🍽️",
    layout="wide"
)

st.title("🌤️ 날씨와 어울리는 음식 추천")
st.write("오늘 날씨를 선택하면 다양한 음식을 추천해드립니다!")

weather = st.selectbox(
    "오늘 날씨는 어떤가요?",
    list(food_data.keys())
)

if st.button("추천 받기"):
    foods = random.sample(
        food_data[weather],
        min(4, len(food_data[weather]))
    )

    st.subheader(f"{weather} 날씨 추천 음식")

    cols = st.columns(2)

    for idx, food in enumerate(foods):

        with cols[idx % 2]:
            st.image(
                food["image"],
                use_container_width=True
            )

            st.markdown(
                f"### 🍴 {food['name']}"
            )

            if st.button(
                f"{food['name']} 선택",
                key=food["name"]
            ):
                st.success(
                    f"{food['name']} 선택 완료!"
                )

                all_foods = []

                for food_list in food_data.values():
                    all_foods.extend(food_list)

                extra = random.sample(all_foods, 3)

                st.subheader("🎁 추가 추천")

                extra_cols = st.columns(3)

                for i, item in enumerate(extra):

                    with extra_cols[i]:
                        st.image(
                            item["image"],
                            use_container_width=True
                        )
                        st.write(item["name"])
