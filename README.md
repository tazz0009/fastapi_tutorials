# FastAPI Tutorials

Python FastAPI 사용해서 API 서버 간단 구축

## chap01 Install and Setup

- 가상환경설치

```
python3 -m venv fastapi-env
fastapi-env\Scripts\activate.bat
```

- 아나콘다 가상환경설치

```
python3 -m venv fastapi-env
fastapi-env\Scripts\activate.bat
```

- fastAPI, uvicorn 설치

```
pip3 install fastapi
python -m pip install --upgrade pip
pip install uvicorn
uvicorn --version
```

- main.py 파일 생성
- 서버 start

```
uvicorn main:app --reload
```

## chap02 Break it down

- git 초기화

```
git init
```

- .gitignore 파일 생성
- git commit

```
git add .
git commit -m "let learn fastAPI"
```

## chap03 Path Parameters

## chap04 API Docs

- http://127.0.0.1:8000/docs

## chap05 Query Parameters

## chap06 Request Body

## chap07 Debugging

## chap08 Pydantic Schemas

## chap09 Database Connection

## chap10 Create Model and Tables

## chap11 Store blog to database

## chap12 Get blog from database

## chap13 Exception & Status Code

## chap14 Delete a blog

## chap15 Response Model

## chap16 Create User

## chap17 Hash Password

## chap18 Show User

## chap19 Using Doc Tags

## chap20 Relationship

## chap21 API Router

## chap22 API router path operators

## chap23 Blog & User respository

## chap24 Logn & verify Password

## chap25 JWT Access Token

## chap26 Route behind authentication

## chap27 Deploy fastAPI app
