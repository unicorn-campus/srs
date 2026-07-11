# 완료 산출물 복사 방법

이 가이드는 Claude Code를 이용한 솔루션요구사항정의서(이하 SRS) 작성 실습을 위해    
샘플 완료 산출물을 본인의 프로젝트 디렉토리에 복사하는 방법을 안내하기 위해 제작되었습니다.

## 사전작업
- 프로젝트 셋업
  프로젝트 디렉토리와 공통지침을 먼저 구성해야 합니다. -> [프로젝트 셋업 가이드](https://github.com/unicorn-campus/ai-automation/blob/main/homework/00.%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EC%85%8B%EC%97%85%20%EA%B0%80%EC%9D%B4%EB%93%9C.md)

- 필수 프로그램 Claude Desktop, vscode, Git 설치: [설치 가이드](https://github.com/unicorn-plugins/npd/blob/main/resources/guides/setup/prepare.md)

## 샘플 프로젝트 다운로드
- 터미널 오픈: Windows 사용자는 PowerShell, Mac 사용자는 Terminal을 실행
  ![](images/2026-07-11-17-11-26.png)    
  ※ 자주 사용하므로 작업표시줄(Mac은 Dock)에 고정하세요.  
  
- Workspace 디렉토리로 이동
  ```
  cd ~/workspace
  ```

- 샘플 저장소 다운로드
  ```
  git clone https://github.com/unicorn-campus/srs.git
  ```

- vscode에서 열기
  ```
  cd srs
  code .
  ```

## 샘플 산출물 복사  
- SRS 프로젝트 디렉토리 vscode에서 오픈   
  ```
  cd ~/workspace/incident-alert
  code .
  ```
- 산출물 복사  
  다운로드한 샘플 저장소의 아래 파일을 `incident-alert` 디렉토리로 복사

  | Phase | 소스 디렉토리 | 타겟 디렉토리 | 파일명 |
  |-------|--------------|--------------|--------|
  | 1. RFP수령 | output | rfp | RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.docx |
  | 2. RFP분석 | work/rfp | rfp | rfp-analyze.md |

  **복사방법**        
  - `incident-alert` 프로젝트에 디렉토리 생성: rfp, guides, prompts
  - 소스 디렉토리에서 복사할 파일을 멀티 선택하고 복사(CTRL-C 또는 Cmd+C)   
    ![](images/2026-07-11-17-29-45.png)  
  - `incident-alert` 프로젝트에서 대상 디렉토리 선택하고 붙여넣기(CTRL-V 또는 Cmd+V)  

  ※ 디렉토리 전체를 복사할 때는 디렉토리명만 복사하고 붙여넣기 하세요.     

## 기타 문서 복사 

| 목적 | 소스 디렉토리 | 타겟 디렉토리 | 파일명 |
|-------|--------------|--------------|--------|
| SRS 작성 가이드 | guides | guides | srs-guide.md |
| 스킬 개발 프롬프트 | prompts | prompts | skill.txt |




