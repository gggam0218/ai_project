import streamlit as st
import csv
from datetime import datetime

st.set_page_config(page_title="자살 상담건수 분석", page_icon="📊")

# CSV 읽기
data = []

with open("../lele(1).csv", "r", encoding="cp949") as f:
    reader = csv.DictReader(f)

    for row in reader:
        row["연"] = int(row["연"])
        row["월"] = int(row["월"])
        row["일"] = int(row["일"])
        row["상담건수"] = int(row["상담건수"])
        row["날짜"] = datetime(row["연"], row["월"], row["일"])

        data.append(row)

st.title("📞 자살 상담건수 분석")

month = st.selectbox(
    "월을 선택하세요",
    [1, 2, 3, 4],
    format_func=lambda x: f"{x}월"
)

# 선택한 월 데이터
month_data = [x for x in data if x["월"] == month]

# 평균
avg_count = sum(x["상담건수"] for x in month_data) / len(month_data)

# 최고
max_data = max(month_data, key=lambda x: x["상담건수"])

# 최저
min_data = min(month_data, key=lambda x: x["상담건수"])

st.subheader(f"📌 {month}월 분석 결과")

st.metric(
    "평균 상담건수",
    f"{avg_count:.1f}건"
)

st.write(
    f"🔺 최고 상담건수 : {max_data['상담건수']}건 "
    f"({max_data['날짜'].strftime('%Y-%m-%d')})"
)

st.write(
    f"🔻 최저 상담건수 : {min_data['상담건수']}건 "
    f"({min_data['날짜'].strftime('%Y-%m-%d')})"
)

# 증가·감소 경향 분석
first_week_avg = (
    sum(x["상담건수"] for x in month_data[:7])
    / len(month_data[:7])
)

last_week_avg = (
    sum(x["상담건수"] for x in month_data[-7:])
    / len(month_data[-7:])
)

st.subheader("📈 증가·감소 경향")

if last_week_avg > first_week_avg:
    st.success(
        f"{month}월은 초반 평균({first_week_avg:.1f}건)보다 "
        f"후반 평균({last_week_avg:.1f}건)이 높아 증가하는 경향을 보입니다."
    )

elif last_week_avg < first_week_avg:
    st.info(
        f"{month}월은 초반 평균({first_week_avg:.1f}건)보다 "
        f"후반 평균({last_week_avg:.1f}건)이 낮아 감소하는 경향을 보입니다."
    )

else:
    st.warning(
        f"{month}월은 초반과 후반 평균이 비슷하여 큰 변화가 없습니다."
    )

# 월별 평균 비교
st.subheader("📊 월별 평균 상담건수")

month_avg = {}

for m in [1, 2, 3, 4]:
    temp = [x["상담건수"] for x in data if x["월"] == m]
    month_avg[m] = sum(temp) / len(temp)

for m, avg in month_avg.items():
    st.write(f"{m}월 평균 : {avg:.1f}건")
