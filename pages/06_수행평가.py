import streamlit as st
import pandas as pd

st.set_page_config(page_title="자살률 분석", layout="wide")

st.title("📊 자살률 분석")

# 1. 파일 읽기 (인코딩 문제 해결을 위한 순차적 시도)
@st.cache_data
def load_data(file_path):
    try:
        # cp949로 먼저 시도하고, 실패 시 utf-8-sig(BOM 처리)로 시도
        return pd.read_csv(file_path, encoding="cp949")
    except:
        return pd.read_csv(file_path, encoding="utf-8-sig")

try:
    df = load_data("dog.csv")
except Exception as e:
    st.error(f"CSV 파일을 불러올 수 없습니다. 파일명과 인코딩을 확인해주세요.\n오류 내용: {e}")
    st.stop()

# 2. 분석 항목 설정
items = {
    "군 자살률": "군자살률(10만명당)",
    "민간 자살률": "민간자살률(10만명당)",
    "20대 남성 자살률": "20대 자살율(10만명당_남자)"
}

choice = st.radio("자살률 종류를 선택하세요.", list(items.keys()), horizontal=True)
col = items[choice]

# 3. 데이터 확인 및 전처리
if col not in df.columns:
    st.error(f"CSV 파일에 '{col}' 컬럼이 존재하지 않습니다.")
    st.info(f"찾은 컬럼 목록: {df.columns.tolist()}")
    st.stop()

# 데이터 복사 및 타입 변환
data = df[["년도", col]].copy()

# '년도'와 '값' 모두 숫자형으로 변환 (콤마나 문자열 포함 대비)
data[col] = pd.to_numeric(data[col].astype(str).str.replace(',', ''), errors="coerce")
data["년도"] = pd.to_numeric(data["년도"].astype(str).str.replace('년', ''), errors="coerce")
data = data.dropna()

if data.empty:
    st.error("분석 가능한 유효 데이터가 없습니다. (숫자 형식이 맞는지 확인하세요)")
    st.stop()

# 4. 분석 지표 계산
max_row = data.loc[data[col].idxmax()]
min_row = data.loc[data[col].idxmin()]
avg = data[col].mean()

# 5. 결과 시각화
st.header(f"📌 {choice} 분석 결과")

# 메트릭 카드로 깔끔하게 표시
c1, c2, c3 = st.columns(3)
c1.metric("최고 기록 연도", f"{int(max_row['년도'])}년", f"{max_row[col]:.2f}")
c2.metric("최저 기록 연도", f"{int(min_row['년도'])}년", f"{min_row[col]:.2f}")
c3.metric("평균 자살률", f"{avg:.2f}")

# 차트 추가 (추세 확인용)
st.subheader("📈 연도별 추세")
st.line_chart(data.set_index("년도")[col])

# 데이터프레임 내림차순 정렬 표시
st.subheader("📋 자살률이 높은 순")
sorted_df = data.sort_values(by=col, ascending=False).copy()
sorted_df.columns = ["년도", f"{choice}(10만명당)"]
st.dataframe(sorted_df.style.highlight_max(axis=0, color='lightcoral'), use_container_width=True)
