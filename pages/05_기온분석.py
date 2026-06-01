import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

st.set_page_config(page_title="서울 기온 분석", layout="wide")

st.title("서울 연도별 기온 비교")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    df["날짜"] = pd.to_datetime(df["날짜"])
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# 월, 일 선택
col1, col2 = st.columns(2)

with col1:
    month = st.selectbox("월 선택", sorted(df["월"].unique()))

with col2:
    days = sorted(df[df["월"] == month]["일"].unique())
    day = st.selectbox("일 선택", days)

# 데이터 필터링
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

st.subheader(f"{month}월 {day}일의 연도별 최고·최저기온")

fig, ax = plt.subplots(figsize=(12, 6))

# 최고기온 무지개색 선
x = filtered["연도"].values
y = filtered["최고기온(℃)"].values

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(
    segments,
    cmap="rainbow",
    norm=plt.Normalize(0, len(segments))
)

lc.set_array(np.arange(len(segments)))
lc.set_linewidth(3)

ax.add_collection(lc)

# 범례용 최고기온 더미선
ax.plot([], [], color="red", linewidth=3, label="최고기온")

# 최저기온
ax.plot(
    filtered["연도"],
    filtered["최저기온(℃)"],
    color="#A7D8FF",
    linewidth=2.5,
    marker="o",
    label="최저기온"
)

ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")
ax.set_title(f"{month}월 {day}일의 연도별 최고·최저기온")

ax.grid(True, alpha=0.3)

ax.set_xlim(filtered["연도"].min(), filtered["연도"].max())

y_min = min(
    filtered["최저기온(℃)"].min(),
    filtered["최고기온(℃)"].min()
)
y_max = max(
    filtered["최저기온(℃)"].max(),
    filtered["최고기온(℃)"].max()
)

ax.set_ylim(y_min - 2, y_max + 2)

ax.legend()

plt.tight_layout()

st.pyplot(fig)

st.dataframe(
    filtered[
        ["연도", "최저기온(℃)", "최고기온(℃)"]
    ],
    use_container_width=True
)
