import uuid
from fastapi import Request, HTTPException, Response
from fastapi.responses import JSONResponse

# 로그인
async def login_user(request: Request):
    '''
    return 은 jsonresponse지만
    main의 sessionmiddleware가 request.session에 들어있는 정보들을 암호화(서명, 인코딩)
    서버는 해당 정보를 http헤더에 실어서 보내줌 + return값
    그걸 브라우저는 가지고있다가 접속할때 요청 헤더에 자동으로 실어서 보냄
    어떻게 그걸 같은 도메인인지 알고? -> 애초에 쿠키를 받을 때 어디서 가져왔나를 자동으로 기록함
    
    '''
    body = await request.json()
    email = body.get("email")
    password = body.get("password")

    # 필수값 검증
    if not email or not password:
        raise HTTPException(status_code=400, detail="email_or_password_required")

    # 세션 생성
    session_id = request.session.get("sessionID")
    if not session_id: #처음 로그인한 사람이라면 session id 할당
        session_id = str(uuid.uuid4())
        request.session["sessionID"] = session_id
        request.session["email"] = email

    return JSONResponse(
        status_code=200,
        content={"session_id": session_id, "email": email}
    )


# 로그아웃
async def logout_user(request: Request):
    try:
        request.session.clear()
        return Response(status_code=204)
    except Exception:
        raise HTTPException(status_code=500, detail="logout_failed")