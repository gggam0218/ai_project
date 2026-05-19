import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("### Folium 지도로 서울 인기 관광지를 확인해보세요!")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 클러스터
marker_cluster = MarkerCluster().add_to(m)

# 관광지 데이터
tourist_spots = [
    {
        "rank": 1,
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 왕조의 대표 궁궐"
    },
    {
        "rank": 2,
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.982193,
        "desc": "쇼핑과 길거리 음식 명소"
    },
    {
        "rank": 3,
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "rank": 4,
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "rank": 5,
        "name": "홍대",
        "lat": 37.556350,
        "lon": 126.922672,
        "desc": "젊음과 예술의 거리"
    },
    {
        "rank": 6,
        "name": "강남",
        "lat": 37.497942,
        "lon": 127.027621,
        "desc": "트렌디한 쇼핑 중심지"
    },
    {
        "rank": 7,
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "서울 대표 랜드마크"
    },
    {
        "rank": 8,
        "name": "인사동",
        "lat": 37.574187,
        "lon": 126.985417,
        "desc": "전통 문화 거리"
    },
    {
        "rank": 9,
        "name": "롯데월드타워",
        "lat": 37.512462,
        "lon": 127.102544,
        "desc": "서울 최고층 전망대"
    },
    {
        "rank": 10,
        "name": "한강공원",
        "lat": 37.520694,
        "lon": 126.939894,
        "desc": "서울 시민들의 휴식 공간"
    }
]

# 마커 추가
for spot in tourist_spots:
    popup_html = f"""
    <h4>TOP {spot['rank']} - {spot['name']}</h4>
    <p>{spot['desc']}</p>
    """

    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=popup_html,
        tooltip=spot["name"],
        icon=folium.Icon(
            color="red",
            icon="star"
        )
    ).add_to(marker_cluster)

# 지도 출력
st_folium(m, width=1400, height=700)

# 관광지 리스트 출력
st.subheader("📍 관광지 목록")

for spot in tourist_spots:
    st.markdown(
        f"""
        **TOP {spot['rank']}. {spot['name']}**  
        - {spot['desc']}
        """
    )
