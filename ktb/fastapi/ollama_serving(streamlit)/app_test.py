import streamlit as st
import ollama
from PIL import Image

'''
streamlit에서 ollama서버로 채팅과 같은 데이터를 보내서 주고 받고 사용자에게 보여주는 형식
fastapi와는 차원이 다른 편리함.. 하지만 표현이 제한적임..

+++++++++++++++++++++++++++++++++++++=
우리는 postman을 사용해서 api로 요청을 쏠때는 base64로 encoding이 필요했음
여기서는 Raw bytes로만 변환해서 보내주면 ollama라이브러리가 http요청을 보내기 전 인코딩을 수행해 json본문에 포함
'''


#1. 페이지 설정
st.set_page_config(page_title="내 컴퓨터 속 GPT", page_icon="💬")
st.title("💬 나만의 로컬 GPT (with Gemma3)")

#모델 id
model_id = "gemma3:4b"

#2. 이미지 올릴 사이드바 설정
with st.sidebar:
    st.header('이미지 업로드')

    st.caption(f"Runs on {model_id}")

    uploaded_file = st.file_uploader("이미지를 분석하려면 업로드하쇼", type = ['png', 'jpg', 'jpeg'])

    if uploaded_file:
        st.info("이미지 분석")
        image = Image.open(uploaded_file)
        st.image(image, caption = 'uploaded image', use_container_width = True)

#3. 세션 상태 초기화 (대화 기록 저장소)
# Streamlit은 매번 코드를 다시 실행하므로, 대화 기록이 날아가지 않게 session_state에 저장해야 합니다.
if "messages" not in st.session_state:
    st.session_state["messages"] = []

#4. 이전 대화 기록을 화면에 출력
# (새로고침 되어도 이전 대화가 남아있게 함)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#5. 사용자 입력 처리
if prompt := st.chat_input("무엇이든 물어보세요..."):
    #5-1. 사용자의 입력을 화면에 표시하고 기록에 저장
    with st.chat_message("user"):
        st.markdown(prompt)
        if uploaded_file:
            st.image(uploaded_file,width = 200)
    
    #payload가 되겠지?
    text_message = {"role": "user", "content": prompt}

    #5-2. AI의 답변을 생성하고 화면에 표시 (스트리밍 방식)
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # 빈 공간을 미리 만듦
        full_response = ""
        
        if uploaded_file:
            text_message['images'] = [uploaded_file.getvalue()]
            #image가 있을 때 현재 질문만
            #우선 image 데이터(base64)는 용량이 텍스트와 비교가 안될정도로 큼
            #멀티턴 상황시 이미지, 텍스트와 같은 데이터가 너무 쌓여 모델이 제대로 기억못하거나 이상해지는 문제가 생길 수 있음
            #우리는 현재 입력한 대화와 이미지에만 집중해 해결..
            #gemini와 같은 모델들은 Long Context Window(많은 토큰 처리가능), 그 안에서 정보를 찾는 정확도(Attention/Retrieval)를 높이는 방식으로 해결


        st.session_state.messages.append(text_message)

        messages_to_send = st.session_state.messages

        #Ollama에게 대화 기록 전체를 보내서 답변 요청
        #stream=True: 글자를 한 글자씩 타자기처럼 받기 위함
        response = ollama.chat(
            model=model_id,
            messages=messages_to_send,
            stream=True
        )
        
        #Ollama의 답변
        #한 글자씩 받아서 화면에 업데이트
        for chunk in response:
            token = chunk['message']['content']
            full_response += token
            message_placeholder.markdown(full_response + "▌") # 커서 효과

        #완료되면 커서 제거하고 최종 텍스트 표시
        message_placeholder.markdown(full_response)
    
    #5-3. AI의 답변도 기록에 저장 (그래야 다음 대화 때 기억함)
    st.session_state.messages.append({"role": "assistant", "content": full_response})