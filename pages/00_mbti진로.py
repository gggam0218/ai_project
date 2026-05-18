import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🎯",
    page_icon="✨",
    layout="centered"
)

# MBTI 데이터
mbti_data = {
    "INTJ": [
        {
            "job": "🧠 AI 개발자",
            "major": "컴퓨터공학과, 인공지능학과",
            "personality": "논리적이고 혼자 깊게 생각하는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "📊 데이터 분석가",
            "major": "통계학과, 데이터사이언스학과",
            "personality": "분석력 좋고 문제 해결 좋아하는 성격!",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],

    "INFP": [
        {
            "job": "🎨 웹툰 작가",
            "major": "디자인학과, 만화애니메이션학과",
            "personality": "상상력 풍부하고 감수성이 뛰어난 사람!",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "💬 상담사",
            "major": "심리학과, 상담학과",
            "personality": "공감 능력이 좋고 사람 이야기를 잘 들어주는 성격!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ENTP": [
        {
            "job": "🚀 스타트업 CEO",
            "major": "경영학과, 경제학과",
            "personality": "아이디어 많고 도전 좋아하는 타입!",
            "salary": "평균 연봉 약 6,000만원 이상"
        },
        {
            "job": "📢 마케터",
            "major": "광고홍보학과, 미디어학과",
            "personality": "말 잘하고 트렌드에 민감한 성격!",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],

    "ESFP": [
        {
            "job": "🎤 유튜버",
            "major": "방송연예과, 미디어학과",
            "personality": "사람들과 어울리는 걸 좋아하고 에너지 넘치는 성격!",
            "salary": "평균 연봉은 매우 다양해요 💸"
        },
        {
            "job": "✈️ 승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 밝은 분위기의 사람에게 잘 맞아요!",
            "salary": "평균 연봉 약 4,500만원"
        }
    ]
}

# 없는 MBTI용 기본 데이터
default_jobs = [
    {
        "job": "💻 IT 개발자",
        "major": "컴퓨터공학과",
        "personality": "집중력 있고 배우는 걸 좋아하는 사람!",
        "salary": "평균 연봉 약 5,000만원"
    },
    {
        "job": "📚 교사",
        "major": "교육학과",
        "personality": "책임감 있고 사람을 잘 도와주는 성격!",
        "salary": "평균 연봉 약 4,300만원"
    }
]

# 제목
st.title("✨ MBTI 진로 추천 앱")
st.write("나의 MBTI에 어울리는 직업을 알아보자 😆")

# MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox(
    "👇 너의 MBTI를 선택해줘!",
    mbti_list
)

st.divider()

# 데이터 가져오기
jobs = mbti_data.get(selected_mbti, default_jobs)

st.subheader(f"🎯 {selected_mbti} 유형 추천 진로!")

for idx, job in enumerate(jobs, start=1):
    st.markdown(f"""
    ## {idx}. {job['job']}

    ### 📚 추천 학과
    {job['major']}

    ### 😎 잘 맞는 성격
    {job['personality']}

    ### 💰 평균 연봉
    {job['salary']}
    """)

    st.divider()

# 하단 문구
st.success("🔥 진로는 참고용이니까 너무 걱정 말고, 네가 좋아하는 걸 가장 중요하게 생각하자!")
