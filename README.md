# 여기이슈

> 개발 기간 : 2021/01/04 ~ 2021/02/19

#### 🖐 Developer

* 강구원 
* 안동규 
* 이대헌 
* 이혜진 
* 조현섭 



-----

### 📍여기이슈란?

> 최신 이슈를 빠르게 파악하고, 의견공유를 하고 싶은 사람들을 위한
>
>  SNS 커뮤니티 & 디베이팅 서비스



#### # 기획 배경 

* 최신 이슈를 접하는 경로를 파악해본 결과, SNS , 언론사 사이트, 각종 포털사이트 등이 있었습니다. SNS는 사람들의 이목을 끌만한 주제들만 제공하였으며, 언론사 사이트 및 포털사이트에서는 최신 이슈를 한눈에 파악하지 못한다는 문제점이 있었습니다. 

  따라서, 최신 이슈를 `키워드`로 제공하고, 키워드와 관련된 `뉴스기사 및 유튜브 영상`을 제공하여 손쉽게 정보를 파악할 수 있는 서비스를 자공하고자 하였습니다. 

* 보통 최신 이슈를 각종 포털 사이트의 뉴스 기사로 접하고, 댓글로 의견공유를 합니다. 그러나 댓글의 특성상 한줄평이 많고, 악성 댓글도 많아 심도 깊은 토의 및 토론을 하고 싶은 사람들에게는 아쉬움이 많습니다. 

  따라서, 의견공유하기에 적합한 각종 `디베이팅 서비스`를 제공하고자 하였습니다. 



#### # 서비스 목적

* 이슈 키워드 추출 및 제공
* 다양한 의견 공유 방법 제공



#### # 주요 기능

* 이슈 키워드 제공 기능
  * 자동 이슈 요약 api로 대표 주제 기사를 선별한 후, 키워드 api를 활용해 키워드를 추출하여 매일매일 업데이트 합니다.
* 이슈 키워드 관련 정보 제공 기능
  * 뉴스 api, 유튜브 api를 활용해 이슈 키워드와 관련된 뉴스기사 및 유튜브 동영상을 무한 스크롤로 제공합니다.
* 댓글 타입 선택 기능
  * 작성한 의견 게시물의 성격에 따라 토론 및 토의를 할 수 있도록 두가지 댓글 타입을 제공합니다.
* 댓글 감정 분석 기능
  * 댓글을 8가지 감정으로 분류하여 악성 댓글일 가능성이 높은 혐오, 분노의 감정 댓글을 관리합니다. 



## 🔧 Install

* Django 실행

  1. 패키지 설치

  ```text
  $ pip install -r requirements.txt
  ```

  2. Django 실행

  ```text
  $ python manage.py runserver
  ```

* Vue.js 실행

  1. 패키지 설치

  ```text
  $ npm i
  ```

  2. Vue 실행

  ```text
  $ npm run serve
  ```





## 📑 Project Construction

> 해당 프로젝트는 BackEnd(`Django`), FrontEnd(`Vue.js`), DataBase(`SQLite`)로 구성되어 있습니다.





##  📂Tech Stack

### Tools

| Tool          | 기술                                                 |
| ------------- | ---------------------------------------------------- |
| GitLab        | 기능별 branch를 나눠서 코드 버전 관리                |
| Jira          | Issue 관리를 위해 Git과 연동하여 사용                |
| Scrum Poker   | Jira Issue 별 스프린트 시간 관리를 위한 어플리케이션 |
| VS Code       | code 구현을 위한 Tool                                |
| Google Chrome | 구현한 화면을 출력하기 위한 브라우저                 |

### ◾ Library

| Library | 내용                                      |
| ------- | ----------------------------------------- |
| Django  | Backend 구현을 위한 python web framework  |
| Vue.js  | Frontend 구현을 위한 JavaScript framework |

### ◾ Software Language

| Language   | 기술                             |
| ---------- | -------------------------------- |
| Python     | Backend 및 이미지 처리 구현 언어 |
| JavaScript | Frontend 구현 언어               |
| HTML/CSS   | Frontend 구현 언어               |



## 📖 기술 설명

* ERD 
  * 상세 보기 : https://www.erdcloud.com/d/HonMGuMMNZuuPfgrA

![image-20210403224517409](https://user-images.githubusercontent.com/42925284/114342969-dd4b5200-9b97-11eb-8e8c-9f7594254944.png)



* Wire Frame
  * Tool : Figma
  * 상세 보기 : https://www.figma.com/proto/wzRcxL6gBvTedlRG3ditq2/%EC%97%AC%EA%B8%B0%EC%9D%B4%EC%8A%88_%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%84?node-id=11%3A532&scaling=min-zoom

![와이어 프레임_여기이슈](https://user-images.githubusercontent.com/42925284/114342999-ecca9b00-9b97-11eb-8c22-5fb89cdf0737.JPG)



## 💡여기이슈 기능
### 메인 페이지
![메인](https://user-images.githubusercontent.com/42925284/116516954-3988d280-a909-11eb-84f2-70be5e248899.gif)


#### ◾ 회원가입 & 로그인

* 이메일 주소 중복 여부 확인 기능을 통해 중복된 아이디를 가지지 않도록 회원 관리 함.



### 1. 이슈모음 Page



#### ◾ 이슈 키워드 제공


* '정치','해외','사회/생활','스포츠','경제','IT/과학','연예' 7가지 카테고리별로 매일매일 상위 10개의 HOT 키워드를 제공함
* 날짜별로 검색 가능함.
* 키워드 추출 방법
  * 자동 이슈 요약 api로 대표 주제 기사를 선별한 후, 키워드 api로 키워드 추출
![이슈랭킹](https://user-images.githubusercontent.com/42925284/116517090-6806ad80-a909-11eb-831c-8b3c9e557620.gif)



#### ◾ 이슈 키워드 관련 정보 제공

* 이슈 키워드와 관련된 최신 뉴스 기사 및 유튜브 동영상을 제공함.

* 최신순 / 정확도순으로 배열 가능함. 

* 정보 제공 방법

  * 뉴스 api, 유튜브 api를 활용해 실시간으로 crawling하여 제공함.

![이슈디테일](https://user-images.githubusercontent.com/42925284/116517131-79e85080-a909-11eb-87cc-9357f03f25c2.gif)

  

-------------

### 2. 의견 나눔 Page

> 글쓰기 기능을 통해 이슈에 대한 자신의 의견을 작성할 수 있으며, 댓글로 다른 사람들과 소통할 수 있습니다.



#### ◾ 해시태그 추천 기능

* 의견 게시물 작성시 해시태그 입력 가능
* 해시태그 입력 시, 해시태그 추천 버튼을 누르면 사용자가 작성한 글을 분석하여 핵심 키워드를 해시태그로 추천해줌.

![해시태그](https://user-images.githubusercontent.com/42925284/116517190-94bac500-a909-11eb-9be4-1ea0f6a8ea4a.gif)


#### ◾ 해시태그 검색 기능

* 해시태그는 의견 게시물 리스트에 노출됨
* 단어를 입력하면 해당 단어가 해시태그 및 제목에 포함된 게시물을 필터링 해줌.

![태그 검색](https://user-images.githubusercontent.com/42925284/116517201-98e6e280-a909-11eb-8481-325d5b50b997.gif)


#### ◾ 댓글 타입 선택 기능

* 게시물 작성시 작성자가 원하는 댓글의 형태를 토의/토론 중 선택 가능함.
* 댓글의 형태에 따라 다른 댓글 폼을 보여줌.

![타입 선택](https://user-images.githubusercontent.com/42925284/116517208-9b493c80-a909-11eb-864e-eafab9a62cd1.gif)


#### ◾ 댓글 감정 분석 기능

* 댓글 작성시 '작성'버튼을 누르면 작성된 댓글을 8가지의 감정으로 분류함.
* 악성 댓글일 확률이 높은 '분노','혐오'로 분류된 댓글은 작성자에게 경고창이 뜸.
  * 경고창에서 해당 댓글의 감정이 '분노', '혐오' 이므로 작성자에게 수정을 권함.
  * 수정을 누를 시, 댓글 수정 기능
  * 확인을 누를시, 댓글이 등록되지만, 관리자가 겸열할 수 있음

![댓글등록](https://user-images.githubusercontent.com/42925284/116517221-9e442d00-a909-11eb-9149-fb117fe15e63.gif)


------------------------

### 3. 클럽Page

> 관심사가 같은 사람들끼리 클럽을 형성하여 자료 공유 및 의견 공유를 할 수 있음



#### ◾ 클럽 관리 기능

* 클럽 생성자가 클럽의 공개 여부를 결정 할 수 있음
* 공개 클럽으로 생성시 의견 나눔 Page에 클럽 내에서 작성된 글이 노출됨

![클럽](https://user-images.githubusercontent.com/42925284/116517238-a43a0e00-a909-11eb-9786-af18f1048661.gif)


--------------

### 4. 매거진 Page

> 우리 서비스 이용자들의 활동 통계를 제공함.

![매거진](https://user-images.githubusercontent.com/42925284/116517506-08f56880-a90a-11eb-810a-15972b353c94.gif)



#### ◾ 해시태그 별 댓글 감정 그래프 제공

* 의견 게시물 작성시 함께 작성된 해시태그를 한눈에 볼 수 있도록 워드클라우드 형태로 제공함

* 워드 클라우드에서 해시태그를 클릭하면, 해당 해시태그가 포함된 게시글에 달린 댓글 감정을 버블 그래프로 제공함.

  



