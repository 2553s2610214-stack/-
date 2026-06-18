import streamlit as st
import random

st.set_page_config(
    page_title="날씨 음식 추천",
    page_icon="🍽️",
    layout="wide"
)

food_data = {
    "☀️ 맑음": [
        {
            "name": "햄버거",
            "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA1MTNfMTUg%2FMDAxNzQ3MTA2OTE4Njcz.FcbiYb4JTunhuITOQotTidDJDqqsKQxw_38-CaLosZ8g.9bpZnYoACnUZVjtPv3HZd90MPmIU2aickFaYzBkqGOkg.PNG%2Fimage.png&type=sc960_832"
        },
        {
            "name": "피자",
            "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
        },
        {
            "name": "치킨",
            "image": "https://images.unsplash.com/photo-1562967916-eb82221dfb92"
        },
        {
            "name": "파스타",
            "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9"
        }
    ],

    "🌧️ 비": [
        {
            "name": "파전",
            "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836"
        },
        {
            "name": "칼국수",
            "image": "https://images.unsplash.com/photo-1516684732162-798a0062be99"
        },
        {
            "name": "수제비",
            "image": "https://images.unsplash.com/photo-1544025162-d76694265947"
        },
        {
            "name": "짬뽕",
            "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19"
        }
    ],

    "❄️ 눈": [
        {
            "name": "붕어빵",
            "image": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543"
        },
        {
            "name": "어묵",
            "image": "https://images.unsplash.com/photo-1547592180-85f173990554"
        },
        {
            "name": "국밥",
            "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836"
        },
        {
            "name": "호떡",
            "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288"
        }
    ],

    "🔥 더움": [
        {
            "name": "냉면",
            "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"
        },
        {
            "name": "빙수",
            "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
        },
        {
            "name": "초밥",
            "image": "https://images.unsplash.com/photo-1579584425555-c3ce17fd4351"
        },
        {
            "name": "물회",
            "image": "https://images.unsplash.com/photo-1553621042-f6e147245754"
        }
    ],

    "🥶 추움": [
        {
            "name": "삼계탕",
            "image": "https://images.unsplash.com/photo-1544025162-d76694265947"
        },
        {
            "name": "곰탕",
            "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836"
        },
        {
            "name": "부대찌개",
            "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b"
        },
        {
            "name": "샤브샤브",
            "image": "https://images.unsplash.com/photo-1515003197210-e0cd71810b5f"
        }
    ]
}

st.title("🌤️ 날씨와 어울리는 음식 추천")
st.markdown("### 오늘 날씨에 딱 맞는 음식을 골라보세요!")

weather = st.selectbox(
    "오늘 날씨를 선택하세요",
    list(food_data.keys())
)

if st.button("🍽️ 음식 추천 받기"):

    foods = random.sample(
        food_data[weather],
        min(4, len(food_data[weather]))
    )

    st.subheader(f"{weather} 추천 음식")

    cols = st.columns(2)

    for idx, food in enumerate(foods):

        with cols[idx % 2]:

            st.image(
                food["image"],
                use_container_width=True
            )

            st.markdown(f"### 🍴 {food['name']}")

            if st.button(
                f"{food['name']} 선택",
                key=f"{food['name']}_{idx}"
            ):

                st.success(
                    f"오늘의 선택은 '{food['name']}' 입니다! 😋"
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
