import streamlit as st
import pandas as pd

st.set_page_config(page_title="자살률 분석", layout="wide")

st.title("📊 자살률 분석")

try:
    df = pd.read_csv("dog.csv", encoding="cp949")
except Exception as e:
    st.error(f"CSV 파일을 불러올 수 없습니다.\n{e}")
    st.stop()

items = {
    "군 자살률": "군자살률(10만명당)",
    "민간 자살률": "민간자살률(10만명당)",
    "20대 남성 자살률": "20대 자살율(10만명당_남자)"
}

choice = st.radio(
    "자살률 종류를 선택하세요.",
    list(items.keys())
)

col = items[choice]

if col not in df.columns:
    st.error(f"'{col}' 컬럼이 CSV에 없습니다.")
    st.write("현재 컬럼명:", df.columns.tolist())
    st.stop()

data = df[["년도", col]].copy()

data[col] = pd.to_numeric(data[col], errors="coerce")
data = data.dropna()

if data.empty:
    st.error("분석할 데이터가 없습니다.")
    st.stop()

max_row = data.loc[data[col].idxmax()]
min_row = data.loc[data[col].idxmin()]
avg = data[col].mean()

st.header(f"📌 {choice} 분석 결과")

st.subheader("가장 높은 자살률")
st.write(f"연도 : {max_row['년도']}년")
st.write(f"자살률 : {max_row[col]:.2f}")

st.subheader("가장 낮은 자살률")
st.write(f"연도 : {min_row['년도']}년")
st.write(f"자살률 : {min_row[col]:.2f}")

st.subheader("평균 자살률")
st.write(f"{avg:.2f}")

st.subheader("📋 자살률이 높은 순")

sorted_df = data.sort_values(by=col, ascending=False)
sorted_df.columns = ["년도", "자살률"]

st.dataframe(sorted_df, use_container_width=True)
