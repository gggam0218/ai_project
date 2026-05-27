# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(page_title="연령별 인구 그래프", layout="wide")

st.title("행정구별 연령 인구 그래프")

# ---------------------------
# 한글 폰트 설정
# ---------------------------
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# ---------------------------
# CSV 파일 업로드
# ---------------------------
uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("데이터 미리보기")
    st.dataframe(df.head())

    # ---------------------------
    # 컬럼 예시
    # 행정구 / 나이 / 인구수
    # ---------------------------

    region_col = "행정구"
    age_col = "나이"
    pop_col = "인구수"

    # 숫자 변환
    df[age_col] = pd.to_numeric(df[age_col], errors="coerce")
    df[pop_col] = pd.to_numeric(df[pop_col], errors="coerce")

    # 결측 제거
    df = df.dropna(subset=[age_col, pop_col])

    # ---------------------------
    # 행정구 선택
    # ---------------------------
    regions = sorted(df[region_col].unique())

    selected_region = st.selectbox(
        "행정구 선택",
        regions
    )

    filtered_df = df[df[region_col] == selected_region]

    # 나이순 정렬
    filtered_df = filtered_df.sort_values(age_col)

    # ---------------------------
    # 그래프 생성
    # ---------------------------
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        filtered_df[age_col],
        filtered_df[pop_col],
        color="hotpink",
        linewidth=3
    )

    # 제목
    ax.set_title(
        f"{selected_region} 연령별 인구",
        fontsize=18,
        fontweight="bold"
    )

    # 축 이름
    ax.set_xlabel("나이", fontsize=13)
    ax.set_ylabel("인구 수", fontsize=13)

    # ---------------------------
    # 10살 단위 구분선
    # ---------------------------
    min_age = int(filtered_df[age_col].min())
    max_age = int(filtered_df[age_col].max())

    xticks = list(range((min_age // 10) * 10, max_age + 10, 10))

    ax.set_xticks(xticks)

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.5
    )

    # 전체 그리드
    ax.grid(
        True,
        linestyle="--",
        alpha=0.3
    )

    st.pyplot(fig)

else:
    st.info("CSV 파일을 업로드해주세요.")
