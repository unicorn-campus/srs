# SRS 작성 가이드 정보수집 — S6 인수 기준(Acceptance Criteria) [딜]

> 목적: 「SRS 작성 가이드」 S6(인수 기준) 섹션 초안 작성을 위한 정보 수집·정리.  
> 담당: 딜(가격·계약 매니저). 근거 입력: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`,  
> 구조 선례 `rfp/RFP작성가이드.md`(딜 담당 섹션 6·7·8, 케어 담당 섹션 5).  
> 원칙: "측정할 수 없으면 요구사항이 아님" — 인수 기준은 기간·임계값·판정방법을 갖춘 검증 가능 서술이어야 함.  
> 외부 자료는 출처 URL을 명기하며, 이론 근거 없는 임의 추가는 배제함.

---

## 1. S6 담당 범위·핵심 질문

- S6는 FR·NFR을 "언제 완료·합격으로 판정하는가"의 측정 가능한 기준으로 못 박는 섹션임.  
- 핵심 질문 3가지  
  - 인수 기준을 어떤 형식으로 서술해야 모호성 없이 검증 가능한가 → Given-When-Then·SMART  
  - SLA·서비스 크레딧을 인수 기준·계약과 어떻게 연계해 정산 분쟁을 예방하는가  
  - 하자보수(무상)와 유지관리(유상)의 경계를 어떻게 인수 기준으로 판정하는가  
- 본 시스템의 정산 리스크 지점: 통지 SLA 준수율(REQ-OPS-02)·가용성(REQ-OPS-01),  
  AI 백테스트 오차율(REQ-BIZ-05a) 기인 하자/유지 귀속 판정.

## 2. Acceptance Criteria 작성 기법

### 2-1. AC의 정의·목적

- 인수 기준(Acceptance Criteria)은 사용자 스토리·요구가 완료·수용 가능으로 인정되기 위해  
  충족해야 할 조건을 사전 정의한 명세임. 개발 전 합의하여 범위·판정 기준을 고정함.  
- AC는 구현이 아닌 "관찰 가능한 행위(behavior)"에 초점을 둠. 판정 주체가 바뀌어도 동일하게 해석되어야 함.  
- (출처: Acceptance Criteria — Purposes, Formats and Best Practices, altexsoft -  
  https://www.altexsoft.com/blog/acceptance-criteria-purposes-formats-and-best-practices/)

### 2-2. Given-When-Then(Gherkin/BDD) 형식

- 형식: Given(선행 조건·상태) → When(행위·이벤트) → Then(관찰 가능한 결과). BDD의 Gherkin 자연어  
  구문으로, 시나리오당 3~5스텝을 권장함.  
- Then 절은 반드시 측정 가능한 결과(임계값·시간·건수)로 서술해야 검증·자동화가 가능함.  
- 각 시나리오는 상호 독립·단독 실행 가능해야 하며, 시나리오 간 의존을 배제함.  
- (출처: Gherkin Reference, Cucumber 공식 문서 - https://cucumber.io/docs/gherkin/reference/)

### 2-3. SMART 기준

- SMART = Specific(구체)·Measurable(측정 가능)·Achievable(달성 가능)·Relevant(관련성)·  
  Time-bound(기한 명시). 요구·목표를 명확·검증 가능하게 만드는 프레임워크임.  
- 요구사항 적용: Measurable은 진척·충족 여부를 추적할 판정 기준을 포함함을 뜻함.  
- 변환 예: "빠르게 로그인" → "이메일·비밀번호로 10초 이내 로그인 후 환영 메시지 표시".  
- (출처: SMART criteria, Wikipedia - https://en.wikipedia.org/wiki/SMART_criteria)  
- (출처: Writing SMART Requirements, JAF Consulting -  
  https://jafconsulting.com/writing-smart-requirements-specific-measurable-achievable-relevant-time-bound/)

### 2-4. 검증가능성(testability)

- 모호어("빠름·많음·안정적")를 수량화해 재작성해야 함. INVEST의 Testable·Small 속성과 직결됨.  
- 측정 3요소: [지표 + 임계값 + 측정조건·판정방법]. 본 RFP NFR 서술 규칙(2-2)과 동일 구조임.  
- (출처: Ten Attributes of a Testable Requirement, Prolifics -  
  https://www.prolifics-testing.com/news/ten-attributes-of-a-testable-requirement)  
- (출처: Testable requirements — how to write good acceptance criteria, EITT -  
  https://eitt.academy/management/testable-requirements-how-to-write-good-acceptance-criteria/)

## 3. SLA·서비스 크레딧 설계

### 3-1. SLA 지표 3요소·조건

- SLA는 요구·기대 서비스 수준을 문서화한 합의임(ITIL 4). 지표는 [지표+목표값+측정방식]으로 명시함.  
- SLA 조건: 측정 방식 명확·자동 반복 측정·장애 시 즉시 적용·담당자 교체와 무관하게 동일 해석.  
- (출처: ITIL 4 SLA·SLM Best Practices, Alloy Software -  
  https://www.alloysoftware.com/blog/itil-service-level-management/)  
- (출처: SLA란 무엇인가, 이랜서 - https://www.elancer.co.kr/blog/detail/1004)  
- (출처: 서비스수준협약(SLA) 기술동향, ETRI - https://ettrends.etri.re.kr/ettrends/90/0905000544/19-6_055_065.pdf)

### 3-2. 가용성 산식

- Availability = MTBF / (MTBF + MTTR). 나인 하나 증가 시 허용 다운타임이 약 1/10로 감소함.  
- 99.95%/월 = 월 약 21.6분 다운타임 허용. 4나인 이상은 이중화·자동 failover를 전제로 함.  
- (출처: Reliability targets — MTBF/MTTR, Microsoft Azure Well-Architected -  
  https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics)  
- (출처: Three/Four nines 다운타임·SLA 계산기, Hyperping - https://hyperping.com/three-nines)

### 3-3. 서비스 크레딧(인센티브 균형)

- 크레딧은 징벌이 아닌 개선 유인으로 설계함. 기대목표치·최소목표치 이원화, 월별 산정·연 누적 상한 설정.  
- 벤더 통제 가능 지표만 크레딧 대상으로 함(예: MNO 망 복구 MTTR은 관찰 지표로 제외).  
- (출처: 요식적 관행도 징벌 수단도 아니다 — IT 조직을 위한 SLA 안내서, CIO Korea -  
  https://www.cio.com/article/3524897/)  
- (출처: 공공 SLA 표준, 아이티데일리 - http://www.itdaily.kr/news/articleView.html?idxno=232653)

## 4. SW사업 대가·하자보수 vs 유지관리 경계

### 4-1. 하자보수(무상) vs 유지관리(유상)

- 무상 하자보수: 사업 완료일로부터 통상 1년, "오류·결함 수정"에 한정됨.  
- 유상 유지관리: 추가개발·기능개선·환경변경·추가 교육 등. 경계 모호 시 정산 분쟁이 발생함.  
- (출처: 소프트웨어 용역계약일반조건, 국가법령정보센터 -  
  https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2000000010572)  
- (출처: '공공SW 하자보수' 막무가내식 관행 없앤다, 전자신문 - https://www.etnews.com/20210308000203)  
- (출처: SW사업 하자보수·유지관리제도, 소프트웨어 중심사회 -  
  http://www.software.kr/um/um01/um0106/um010605/um01060504/um0106050401.do)

### 4-2. SW사업 대가산정·유지관리 요율

- 유지관리 요율은 통상 개발비의 10~15%, 상용SW는 등급별 최대 20%. 산정 근거는 KOSA 대가산정 가이드 준거.  
- (출처: SW사업 대가산정 가이드 2024 개정판, KOSA - https://www.sw.or.kr/site/sw/ex/board/List.do?cbIdx=276)  
- (출처: 상용SW 유지관리요율 1등급 최대 20%로, 아이티데일리 -  
  http://www.itdaily.kr/news/articleView.html?idxno=203454)

### 4-3. AI 재학습 귀속 경계(본 RFP 특수 항목)

- 정상 운영 중 성능저하(drift) 기인 정기 재학습 = MRC 유상. 구현결함 기인 성능오류 = 무상 하자.  
- 판정 기준: REQ-BIZ-05a 백테스트 오차율(±15%) 초과 원인이 구현결함인지 여부(RFP 6-3).  
- 인수 기준으로 백테스트 오차율 임계값·판정 절차를 명문화해야 귀속 분쟁을 예방함.

### 4-4. 지체상금

- 요율 1000분의 1.5(SW 물품+용역 일괄), 산식 = 기준금액 × 요율 × 지체일수.  
- 기준금액은 NRC 중 미완료·미검수 부분에 한정, 총액 cap = NRC의 30%. 발주사 귀책·불가항력은 면책.  
- (출처: 계약이행의 지체 > 지체상금, 찾기쉬운 생활법령정보 -  
  https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=519&ccfNo=6&cciNo=2&cnpClsNo=1)

## 5. 본 RFP 근거 매핑 (S6 인수 기준 반영 대상)

| RFP 근거 | 지표·임계값 | 측정·판정 | 계약 연계 |
|----------|-------------|-----------|-----------|
| REQ-OPS-02 | 통지 SLA 준수율 ≥ 98%/월 | (준수건/전체통지건), 자동 타임스탬프 | 서비스 크레딧(6-1) |
| REQ-OPS-01 | 가용성 ≥ 99.95%/월(≤ 21.6분) | MTBF/(MTBF+MTTR), 월 집계 | 서비스 크레딧(6-1) |
| REQ-TEC-01 | 수신~통지 ≤ 1분, 성공률 ≥ 99.9% | 이벤트 타임스탬프 자동 측정 | 통지 준수율 반영 |
| REQ-TEC-03 | 채널 자동 전환 ≤ 30초 | 채널 강제 차단 후 전환 시험 | 통지 준수율 반영 |
| REQ-BIZ-03 | ETR 15분 주기 갱신 준수율 ≥ 98% | 갱신 타임스탬프 자동 측정 | 통지 준수율 반영 |
| REQ-BIZ-02 | 조회 평균 2초 & P99 3초 | 300 TPS 부하, 표본 100건 대사 100% 일치 | — |
| REQ-BIZ-05a | 백테스트 오차율 ±15% 이내 | 과거 사고 전수 백테스트 | 하자/유지 경계(6-3) |
| REQ-TEC-05 | 추론 ≤ 3초, 누적 10건 재학습 | 추론 부하·재학습 로그 | AI 재학습 귀속(6-3) |

- 서비스 크레딧 표(RFP 6-1): 98%↑ 없음 / 97~98% 5% / 95~97% 10% / 93~95% 15% / 93%↓ 20%(월 상한).  
  연간 누적 크레딧 상한 = 연 MRC의 15%.  
- 비(非)SLA 관찰 지표: MNO 망 복구 MTTR은 월간 리포트 기재용이며 벤더 페널티 대상이 아님(인수 기준에서 배제).

## 6. 통합 출처 목록

(원천 각주는 `rfp/RFP작성가이드.md` 딜 섹션 6·7·8 및 케어 섹션 5, S6 신규 확인분은 WebSearch로 검증)

- Given-When-Then / Gherkin(Cucumber): https://cucumber.io/docs/gherkin/reference/  
- Acceptance Criteria formats(altexsoft): https://www.altexsoft.com/blog/acceptance-criteria-purposes-formats-and-best-practices/  
- SMART criteria(Wikipedia): https://en.wikipedia.org/wiki/SMART_criteria  
- Writing SMART Requirements(JAF): https://jafconsulting.com/writing-smart-requirements-specific-measurable-achievable-relevant-time-bound/  
- Testable requirement(Prolifics): https://www.prolifics-testing.com/news/ten-attributes-of-a-testable-requirement  
- Acceptance criteria 작성(EITT): https://eitt.academy/management/testable-requirements-how-to-write-good-acceptance-criteria/  
- ITIL 4 SLA(Alloy Software): https://www.alloysoftware.com/blog/itil-service-level-management/  
- SLA 가이드(이랜서): https://www.elancer.co.kr/blog/detail/1004  
- SLA 기술동향(ETRI): https://ettrends.etri.re.kr/ettrends/90/0905000544/19-6_055_065.pdf  
- 가용성 MTBF/MTTR(Azure): https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics  
- nines 계산기(Hyperping): https://hyperping.com/three-nines  
- SLA 안내서(CIO Korea): https://www.cio.com/article/3524897/  
- 공공 SLA 표준(아이티데일리): http://www.itdaily.kr/news/articleView.html?idxno=232653  
- SW 용역계약일반조건(국가법령정보센터): https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2000000010572  
- 공공SW 하자보수(전자신문): https://www.etnews.com/20210308000203  
- 하자보수·유지관리제도(SW중심사회): http://www.software.kr/um/um01/um0106/um010605/um01060504/um0106050401.do  
- SW 대가산정 가이드 2024(KOSA): https://www.sw.or.kr/site/sw/ex/board/List.do?cbIdx=276  
- 유지관리요율(아이티데일리): http://www.itdaily.kr/news/articleView.html?idxno=203454  
- 지체상금(생활법령): https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=519&ccfNo=6&cciNo=2&cnpClsNo=1
