import streamlit as st
import json

st.set_page_config(layout='wide')


# JSON 데이터 예제
json_data = '''
[
    {"id": 1, "title": "2024-11-10", "description": "이것은 첫 번째 박스입니다."},
    {"id": 2, "title": "박스 2", "description": "이것은 두 번째 박스입니다."},
    {"id": 3, "title": "박스 3", "description": "이것은 세 번째 박스입니다."},
    {"id": 4, "title": "박스 4", "description": "이것은 네 번째 박스입니다."},
    {"id": 5, "title": "박스 5", "description": "이것은 다섯 번째 박스입니다."}
]
'''

# JSON 데이터를 파싱
data = json.loads(json_data)
lists = ["트레킹", "일지", "분석"]
# CSS 코드 삽입
def app():
    Expander(data, lists[0])
    Report_Expander(data, lists[1])
    Expander(data, lists[2])

@st.fragment
def Expander(data, list_name):
    with st.expander("📈"+list_name, expanded=True):
        st.markdown("""
            <style>
                    #box1 { text-align: left;}
                    
            /* 컨테이너 스타일 */
            .scroll-container {
                display: flex;
                overflow-x: auto; /* 가로 스크롤 활성화 */
                padding: 10px;
                gap: 10px; /* 박스 간격 */
            }

            /* 박스 스타일 */
            .scroll-box {
                flex: 0 0 auto; /* 크기 고정 */
                width: 300px; /* 박스 너비 */
                height: 300px; /* 박스 높이 */
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                display: flex;
                flex-direction: column; /* 세로 방향 정렬 */
                font-size: 16px;
                font-weight: bold;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                padding: 10px;
                text-align: left;
                justify-content: left;
            }
            /* 텍스트 스타일 (추가) */
            .left-align {
                text-align: left; /* 텍스트 왼쪽 정렬 */
                font-size: 16px;
                font-weight: normal;
                margin-bottom: 10px;
                line-height: 1.5; /* 줄 간격 */
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

        
        boxes_html = "".join(
            [f'''
            <div class="scroll-box">
                <div>
                    <strong style="text-align:left;">일시: {item["title"]}</strong>
                    <div id = "box1">{item["description"]}</div>
                </div>
                
            </div>
            ''' for item in data]
        )
        
        # 스크롤 가능한 컨테이너 추가
        st.markdown(f"""
            <div class="scroll-container">
                {boxes_html}
            </div>
        """, unsafe_allow_html=True)

@st.fragment
def Report_Expander(data, list_name):
    with st.expander("📈"+list_name, expanded=True):
        st.markdown("""
            <style>
                    #box1 { text-align: left;}
                    
            /* 컨테이너 스타일 */
            .scroll-container {
                display: flex;
                overflow-x: auto; /* 가로 스크롤 활성화 */
                padding: 10px;
                gap: 10px; /* 박스 간격 */
            }

            /* 박스 스타일 */
            .scroll-box {
                flex: 0 0 auto; /* 크기 고정 */
                width: 300px; /* 박스 너비 */
                height: 300px; /* 박스 높이 */
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                display: flex;
                flex-direction: column; /* 세로 방향 정렬 */
                font-size: 16px;
                font-weight: bold;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                padding: 10px;
                text-align: left;
                justify-content: left;
            }
            /* 텍스트 스타일 (추가) */
            .left-align {
                text-align: left; /* 텍스트 왼쪽 정렬 */
                font-size: 16px;
                font-weight: normal;
                margin-bottom: 10px;
                line-height: 1.5; /* 줄 간격 */
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

        
        boxes_html = "".join(
            [f'''
            <div class="scroll-box">
                <div>
                    <strong style="text-align:left;">일시: {item["title"]}</strong>
                    <div id = "box1">{item["description"]}</div>
                </div>
                
            </div>
            ''' for item in data]
        )
        
        # 스크롤 가능한 컨테이너 추가
        st.markdown(f"""
            <div class="scroll-container">
                {boxes_html}
            </div>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    app()