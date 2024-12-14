import streamlit as st
import json

st.set_page_config(layout='wide')

# JSON 데이터 예제
json_data = '''
[
    {"id": 1, "title": "박스 1", "description": "이것은 첫 번째 박스입니다."},
    {"id": 2, "title": "박스 2", "description": "이것은 두 번째 박스입니다."},
    {"id": 3, "title": "박스 3", "description": "이것은 세 번째 박스입니다."},
    {"id": 4, "title": "박스 4", "description": "이것은 네 번째 박스입니다."},
    {"id": 5, "title": "박스 5", "description": "이것은 다섯 번째 박스입니다."},
    {"id": 6, "title": "박스 6", "description": "이것은 여섯 번째 박스입니다."},
    {"id": 7, "title": "박스 7", "description": "이것은 일곱 번째 박스입니다."},
    {"id": 8, "title": "박스 8", "description": "이것은 여덟 번째 박스입니다."},
    {"id": 9, "title": "박스 9", "description": "이것은 아홉 번째 박스입니다."},
    {"id": 10, "title": "박스 10", "description": "이것은 열 번째 박스입니다."}
]
'''

# JSON 데이터를 파싱
data = json.loads(json_data)

# CSS 스타일 정의
st.markdown("""
    <style>
    /* 컨테이너 스타일 */
    .scroll-container {
        display: flex;
        flex-wrap: nowrap; /* 가로 스크롤 유지 */
        overflow-x: auto; /* 가로 스크롤 활성화 */
        gap: 10px; /* 행 간 간격 */
        padding: 10px;
        white-space: nowrap;
    }

    /* 행 컨테이너 스타일 */
    .row-container {
        display: flex;
        flex-direction: row; /* 행 방향으로 박스 정렬 */
        gap: 10px; /* 박스 간 간격 */
    }

    /* 박스 스타일 */
    .grid-box {
        flex: 0 0 200px; /* 고정 크기 */
        height: 150px; /* 박스 높이 */
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }

    /* 스크롤바 스타일 */
    .scroll-container::-webkit-scrollbar {
        height: 8px; /* 스크롤바 높이 */
    }
    .scroll-container::-webkit-scrollbar-thumb {
        background: #888; /* 스크롤바 색상 */
        border-radius: 10px;
    }
    .scroll-container::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    </style>
""", unsafe_allow_html=True)

# Expander 시작
with st.expander("📈 분석 데이터", expanded=True):
    st.markdown("#### 스크롤 가능한 2행 5열 레이아웃")
    
    # 데이터를 두 행으로 나눔
    rows = [data[i:i+5] for i in range(0, len(data), 5)]  # 5개씩 분리

    # HTML 행 생성
    rows_html = "".join(
        [
            f'''
            <div class="row-container">
                {''.join([f'''
                <div class="grid-box">
                    <strong>{item["title"]}</strong><br><br>
                    {item["description"]}
                </div>
                ''' for item in row])}
            </div>
            '''
            for row in rows
        ]
    )

    # 스크롤 가능한 컨테이너 추가
    st.markdown(f"""
        <div class="scroll-container">
            {rows_html}
        </div>
    """, unsafe_allow_html=True)
