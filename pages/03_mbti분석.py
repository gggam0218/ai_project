import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(page_title="Country MBTI Analyzer", layout="wide")

st.title("🌍 국가별 MBTI 비율 분석")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 컬럼 자동 찾기
country_col = df.columns[0]

# MBTI 컬럼만 추출
mbti_columns = df.columns[1:]

# 국가 선택
selected_country = st.selectbox(
    "국가를 선택하세요",
    df[country_col].unique()
)

# 선택 국가 데이터
country_data = df[df[country_col] == selected_country].iloc[0]

# MBTI 값 가져오기
values = country_data[mbti_columns].astype(float)

# 내림차순 정렬
values = values.sort_values(ascending=False)

# 색상 생성
# 1등 = 노란색
# 나머지 = 하늘색 -> 매우 연한 하늘색 그라데이션

colors = []

for i in range(len(values)):
    if i == 0:
        colors.append("#FFD700")  # gold
    else:
        alpha = 1 - (i / len(values)) * 0.7
        
        # 하늘색 RGB
        base = np.array([135, 206, 235]) / 255
        
        # 흰색과 섞기
        color = base * alpha + np.array([1, 1, 1]) * (1 - alpha)
        
        colors.append(color)

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(values.index, values.values, color=colors)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.2,
        f"{height:.1f}%",
        ha='center',
        fontsize=9
    )

# 스타일
ax.set_title(f"{selected_country} MBTI Distribution", fontsize=18)
ax.set_ylabel("Percentage (%)", fontsize=12)
ax.set_xlabel("MBTI Type", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

# 출력
st.pyplot(fig)

# 최고 MBTI 표시
top_mbti = values.idxmax()
top_value = values.max()

st.success(f"🏆 가장 높은 MBTI: {top_mbti} ({top_value:.1f}%)")
