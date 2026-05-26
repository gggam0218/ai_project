import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(
    page_title="MBTI Country Analyzer",
    layout="wide"
)

st.title("🌍 국가별 MBTI 비율 분석기")
st.markdown("국가를 선택하면 MBTI 비율을 그래프로 보여줍니다.")

# ----------------------------
# CSV 불러오기
# ----------------------------
df = pd.read_csv("countriesMBTI_16types.csv")

# 첫 번째 컬럼 = 국가명
country_col = df.columns[0]

# MBTI 컬럼
mbti_cols = df.columns[1:]

# ----------------------------
# 국가 선택
# ----------------------------
selected_country = st.selectbox(
    "국가 선택",
    sorted(df[country_col].unique())
)

# 선택 국가 데이터
country_data = df[df[country_col] == selected_country].iloc[0]

# 값 추출
values = country_data[mbti_cols].astype(float)

# 내림차순 정렬
values = values.sort_values(ascending=False)

# ----------------------------
# 색상 만들기
# 1등 = 노란색
# 나머지 = 하늘색 → 흐려지는 그라데이션
# ----------------------------
colors = []

for i in range(len(values)):

    # 1등
    if i == 0:
        colors.append("#FFD700")  # gold

    # 나머지
    else:
        # 점점 연해지도록
        fade_ratio = i / (len(values) - 1)

        # 하늘색 RGB
        blue = np.array([135, 206, 250]) / 255

        # 흰색
        white = np.array([1, 1, 1])

        # 혼합
        mixed = blue * (1 - fade_ratio) + white * fade_ratio

        colors.append(mixed)

# ----------------------------
# 그래프
# ----------------------------
fig, ax = plt.subplots(figsize=(13, 6))

bars = ax.bar(
    values.index,
    values.values,
    color=colors,
    edgecolor="black"
)

# 값 표시
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.15,
        f"{height:.1f}%",
        ha='center',
        fontsize=9
    )

# 스타일
ax.set_title(
    f"{selected_country} MBTI Distribution",
    fontsize=20,
    pad=20
)

ax.set_ylabel("Percentage (%)", fontsize=12)
ax.set_xlabel("MBTI Type", fontsize=12)

plt.xticks(rotation=0)

# 배경 살짝 밝게
ax.set_facecolor("#F8F9FA")

# 위쪽 여백
ax.set_ylim(0, values.max() + 3)

plt.tight_layout()

# 출력
st.pyplot(fig)

# ----------------------------
# 최고 MBTI
# ----------------------------
top_mbti = values.idxmax()
top_value = values.max()

st.success(
    f"🏆 {selected_country}에서 가장 높은 MBTI는 "
    f"{top_mbti} ({top_value:.1f}%) 입니다."
)
