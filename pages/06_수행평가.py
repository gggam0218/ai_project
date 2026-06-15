import streamlit as st
import pandas as pd

st.set_page_config(page_title="자살 상담건수 분석", page_icon="📊")

# CSV 파일 읽기
df = pd.read_csv("lele.csv")

# 날짜 만들기
df["날짜"] = pd.to_datetime(df[["연", "월", "일"]])

# 월별 평균 계산
monthly_avg = df.groupby("월")["상담건수"].mean()

# 최고, 최저 날짜 찾기
max_row = df.loc[df["상담건수"].idxmax()]
min_row = df.loc[df["상담건수"].idxmin()]

st.title("📞 자살 상담건수 분석")

# 월 선택
month = st.selectbox(
    "월을 선택하세요",
    [1, 2, 3, 4],
    format_func=lambda x: f"{x}월"
)

st.subheader(f"{month}월 평균 상담건수")
st.metric(
    label=f"{month}월 평균",
    value=f"{monthly_avg[month]:.1f}건"
)

st.divider()

# 최고 날짜
st.subheader("📈 최고 상담건수")
st.write(
    f"**{int(max_row['연'])}년 {int(max_row['월'])}월 {int(max_row['일'])}일**"
)
st.write(f"상담건수 : **{int(max_row['상담건수'])}건**")

# 최저 날짜
st.subheader("📉 최저 상담건수")
st.write(
    f"**{int(min_row['연'])}년 {int(min_row['월'])}월 {int(min_row['일'])}일**"
)
st.write(f"상담건수 : **{int(min_row['상담건수'])}건**")

st.divider()

# 증가 감소 경향 분석
st.subheader("📊 증가·감소 경향 분석")

jan = monthly_avg[1]
feb = monthly_avg[2]
mar = monthly_avg[3]
apr = monthly_avg[4]

analysis = []

if feb > jan:
    analysis.append("• 1월보다 2월의 평균 상담건수가 증가했습니다.")
else:
    analysis.append("• 1월보다 2월의 평균 상담건수가 감소했습니다.")

if mar > feb:
    analysis.append("• 2월보다 3월의 평균 상담건수가 증가했습니다.")
else:
    analysis.append("• 2월보다 3월의 평균 상담건수가 감소했습니다.")

if apr > mar:
    analysis.append("• 3월보다 4월의 평균 상담건수가 증가했습니다.")
else:
    analysis.append("• 3월보다 4월의 평균 상담건수가 감소했습니다.")

for text in analysis:
    st.write(text)

st.write("")
st.write("### 종합 분석")

if jan == monthly_avg.max():
    highest_month = 1
elif feb == monthly_avg.max():
    highest_month = 2
elif mar == monthly_avg.max():
    highest_month = 3
else:
    highest_month = 4

if jan == monthly_avg.min():
    lowest_month = 1
elif feb == monthly_avg.min():
    lowest_month = 2
elif mar == monthly_avg.min():
    lowest_month = 3
else:
    lowest_month = 4

st.write(
    f"""
- 평균 상담건수가 가장 높은 달은 **{highest_month}월**입니다.
- 평균 상담건수가 가장 낮은 달은 **{lowest_month}월**입니다.
- 1월부터 3월까지는 전반적으로 감소하는 경향을 보였습니다.
- 4월에는 상담건수가 다시 증가하는 모습을 보였습니다.
- 전체적으로 상담건수는 증가와 감소를 반복하며 변동하는 경향을 나타냅니다.
"""
)
