import streamlit as st
import csv
from pathlib import Path
from datetime import datetime

# 현재 파일 위치 기준으로 프로젝트 폴더 찾기
BASE_DIR = Path(__file__).resolve().parent.parent

# CSV 파일 경로
csv_path = BASE_DIR / "lele(1).csv"

# CSV 읽기
data = []

with open(csv_path, "r", encoding="cp949") as f:
    reader = csv.DictReader(f)

    for row in reader:
        row["연"] = int(row["연"])
        row["월"] = int(row["월"])
        row["일"] = int(row["일"])
        row["상담건수"] = int(row["상담건수"])
        row["날짜"] = datetime(row["연"], row["월"], row["일"])

        data.append(row)
