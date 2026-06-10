import streamlit as st
import pandas as pd

st.set_page_config(page_title="자살률 분석", layout="wide")

st.title("📊 자살률 분석")

# CSV 불러오기
df = pd.read_csv("../dog.csv", encoding="cp949")

# 분석할 항목
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

data = df[["년도", col]].dropna()

# 최고값
max_row = data.loc[data[col].idxmax()]

# 최저값
min_row = data.loc[data[col].idxmin()]

# 평균
avg = data[col].mean()

st.header(f"📌 {choice} 분석 결과")

st.subheader("가장 높은 자살률")
st.write(f"연도 : {int(max_row['년도'])}년")
st.write(f"자살률 : {max_row[col]:.2f}")

st.subheader("가장 낮은 자살률")
st.write(f"연도 : {int(min_row['년도'])}년")
st.write(f"자살률 : {min_row[col]:.2f}")

st.subheader("평균 자살률")
st.write(f"{avg:.2f}")

# 자살률 순위
st.subheader("📋 자살률이 높은 순")

sorted_df = data.sort_values(by=col, ascending=False)
sorted_df.columns = ["년도", "자살률"]

st.dataframe(
    sorted_df,
    use_container_width=True
)

# 경향 설명
st.header("📈 자살률 경향")

if choice == "군 자살률":
    st.write(
        """
        - 2011년에 가장 높았으며 이후 전반적으로 감소하는 추세를 보인다.
        - 최근으로 갈수록 자살률이 낮아지는 경향이 나타난다.
        - 전체적으로 개선되는 모습을 보인다.
        """
    )

elif choice == "민간 자살률":
    st.write(
        """
        - 초반에는 감소하는 추세를 보였다.
        - 최근에는 감소세가 둔화되며 일부 증가하는 모습이 나타난다.
        - 전반적으로는 과거보다 낮아졌지만 높은 수준이 유지되고 있다.
        """
    )

else:
    st.write(
        """
        - 초반에는 감소하는 모습을 보였다.
        - 이후 일부 연도에서 다시 증가하는 경향이 나타났다.
        - 최근 몇 년간 비교적 높은 수준이 유지되고 있다.
        """
    )
