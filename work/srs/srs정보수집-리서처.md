# SRS 작성 정보수집 — S2. 고객사 문제 정의 (리서처)

> 목적: SRS 작성 가이드 S2「고객사 문제 정의」섹션 초안 작성에 필요한 정보를 정리함.  
> 담당: 리서처(RFP 분석가) / 작성일: 2026-07-09  
> 근거 입력: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`(1장 취지·정량 목표),  
> 구조 선례 `rfp/RFP작성가이드.md`(2. 취지 섹션), 아젠다 `work/srs/srs-agenda.md`(S2 범위).  
> 원칙: 모든 외부 자료에 출처 URL을 표기함(지어내지 않음). 이론 근거 없는 임의 추가 금지.

---

## 1. S2 정보수집 목적·범위

- S2는 RFP 1장 취지의 WHY에서 As-Is 문제·정량 목표(현재값→목표값)를 SRS 문제 정의로 재구성하는 섹션임.  
- 핵심 관점 3가지를 정보수집 대상으로 함.  
  - 문제 정의 기법: As-Is/To-Be 갭 분석, 근본원인 분석, 정량 목표(SMART) 설정  
  - 정렬 원칙: WHY First, IT-비즈니스 정렬(경영목표 역산)  
  - 표면 요구와 실제 니즈 구분: 고객이 말한 표면 요구를 그대로 명세하지 않고 근본 니즈를 규명함  
- 산출 지향점: S2 초안이 각 문제를 요구ID·인수 기준과 1:1 추적 가능한 검증 명제로 못 박도록 지원함.

---

## 2. 핵심 개념 — RFP 취지(WHY)를 SRS 문제 정의로 재구성

- RFP 취지와 SRS 문제 정의는 목적이 다름. 같은 WHY를 다루되 문서의 기능이 상이함.  
  - RFP 취지(설득 서사): "왜 구축하는가"를 3막 구조(설정→갈등→해결)로 벤더에게 설득하는 글임.[^moxie]  
  - SRS 문제 정의(검증 기준점): 그 WHY를 요구ID·인수 기준과 추적 가능한 검증 명제로 정형화하는 기준점임.  
- 따라서 S2 재구성의 요체는 "서사적 수사는 걷어내고, 문제를 측정 가능한 명제로 다시 못 박음"임.  
- 표준 근거: ISO/IEC/IEEE 29148은 이해관계자 니즈·요구 정의(StRS)를 요구 명세(SRS)의 상류로 규정함.  
  SRS 문제 정의는 이 이해관계자 니즈 정의를 SRS 안으로 끌어와 요구의 출발점을 고정하는 역할임.[^iso29148]  
- 인과 고리 유지 원칙: 문제→요구→효과가 끊기지 않게 연결함(수미상관). RFP 1-4의 "실시간 가시성 확보  
  → 5분 통지 → 30분 선제 안내 → 문의 30% 감소" 고리를 SRS 문제 정의에서도 동일하게 보존함.

---

## 3. 문제 정의 기법 (외부 자료 근거)

### 3-1. WHY First — 골든서클(Golden Circle)

- 사이먼 시넥의 골든서클은 What(무엇)이 아니라 Why(왜)에서 출발하라는 원칙임. 조직의 존재 이유(Why)를  
  먼저 정의하고 How·What을 그 아래 배치함.[^sinek]  
- S2 적용: 문제 정의 최상단에 RFP 키 메시지의 경영 의도(Why)를 재진술하고, 개별 문제·요구를 그 아래 배치함.  
- 효과: 개별 요구가 "왜 필요한지"를 잃지 않게 하여, 표면 기능 나열로 흐르는 것을 방지함.

### 3-2. As-Is/To-Be 갭 분석 (BABOK 전략분석)

- 갭 분석은 현재 상태(As-Is)와 목표 상태(To-Be)를 비교하여 그 간극을 메우기 위한 필요 변화를 도출하는  
  기법임. IIBA BABOK의 전략분석(Strategy Analysis) 지식영역에서 역량 평가(capability assessment)로 다룸.[^iiba]  
- 3단계: ① 목표(To-Be) 정의 → ② 현재(As-Is) 상태·이슈 파악 → ③ 간극 해소 실행계획 수립.[^balearnings]  
- S2 적용: As-Is 문제와 To-Be 목표의 간극 자체가 곧 "문제"이며, 이 간극을 메우는 것이 요구사항임.  
  각 문제를 정량 지표의 현재값→목표값 대비로 표현하면 갭이 측정 가능해짐.

### 3-3. 근본원인 분석 (5 Whys) — 표면 요구와 실제 니즈 구분

- 5 Whys는 "왜?"를 반복(통상 5회)하여 표면적 증상 뒤의 근본원인에 도달하는 기법임. 도요타 오노 다이이치가  
  정립했고 린·식스시그마에서 표준 도구로 사용됨.[^lean]  
- 핵심 효용: "피상적 답을 넘어 근본원인에 도달"하게 함. 분석 전 문제 명제(problem statement)를 명확히 정의함이  
  전제임.[^asq]  
- S2 적용(표면 요구 vs 실제 니즈): 고객의 표면 요구(예: "알림 시스템을 만들어달라")를 그대로 명세하면  
  실제 니즈(예: "가입자를 가장 먼저 안심시켜 이탈 방지")를 놓침. 5 Whys로 근본원인·실제 니즈를 규명하여  
  요구의 목표를 바로잡음.

### 3-4. 정량 목표 설정 (SMART, baseline→target)

- SMART는 Specific·Measurable·Achievable·Relevant·Time-bound의 약어로, 측정 기준과 기한을 갖춘 목표  
  설정 원칙임.[^smart-wiki][^cfi]  
- Measurable은 진척을 측정할 기준을, Time-bound는 시작일·목표일을 요구함. 특히 baseline(현재값) 없는 목표는  
  달성 여부를 검증할 수 없어 부적격으로 봄 — 목표는 baseline 대비 개선폭으로 설정함.[^mdh]  
- S2 적용: 모든 정량 목표를 [지표·현재값(baseline)·목표값·기한] 형식으로 명시함. "빠르게·많이" 같은 정성  
  표현은 금지하고 수량화함(예: "인지~통지 40분 → 5분 이내").

### 3-5. IT-비즈니스 정렬 (경영목표 역산)

- IT 역량을 비즈니스 요구에 정렬하려면 경영목표에서 역산함 — 경영목표 → 필요 비즈니스 역량 → 그 역량을  
  막는 현재 문제점 순으로 도출해야 논리가 이어짐.[^opengroup]  
- S2 적용: 문제 정의가 경영목표("가장 먼저 안심시키는 사업자")에서 역산되어 As-Is 문제와 연결되는지 점검함.  
  문제가 경영목표와 무관하게 나열되면 정렬이 깨진 것임.

---

## 4. 본 RFP 문제·목표 매핑 (S2 초안 입력 데이터)

> 출처: 확정 RFP 1-1(키 메시지)·1-3(As-Is)·1-4(정량 목표)·2-1(엔드유저 상충). 아래는 S2 초안의 근거 데이터임.

### 4-1. WHY(키 메시지)

- "당사는 실시간 장애·사고 가시성을 확보하여, MNO 망 사고가 발생해도 가입자를 가장 먼저 안심시키는  
  알뜰폰 사업자가 되고자 함."(RFP 1-1)  
- 배경: 발주사는 MNO 망을 도매 임차하는 MVNO로, 망 장애·보안사고의 1차 정보가 MNO에 종속됨(RFP 1-2).

### 4-2. As-Is 문제 (RFP 1-3)

- P1(정보 종속): MNO 대규모 장애·보안사고 시 공식 통지를 실시간으로 못 받고 뉴스·SNS·자체 모니터링으로  
  뒤늦게 인지함.  
- P2(고객센터 마비): 2025-04 MNO 유심 정보 유출 사고 시 문의가 평소 수 배로 폭증했으나 공식 정보 부재로  
  상담사가 뉴스 속보를 보며 응대, 고객센터 다수가 마비됨.  
- P3(사후·지연 대응): 2018 MNO 국사 화재 시 알뜰폰 가입자 보상 안내가 사고 약 3주 후에야 개별 공지됨.  
- 악순환: "장애·사고 인지 지연 → 고객센터 응대 마비 → 가입자 이탈"이 반복됨.

### 4-3. 정량 목표 (RFP 1-4, 현재값 → 목표값)

| 지표 | 현재값(As-Is) | 목표값(To-Be) | 성격 |
|------|---------------|----------------|------|
| 장애 인지 ~ MVNO 담당자 통지(평균) | 약 40분 | 5분 이내 | 내부 |
| 가입자 선제 안내 발송 시점 | 사후·수시간~수일 | 사고 인지 후 30분 이내 | 대가입자 |
| 장애 발생 시 고객센터 문의량(월) | 약 5,000건 | 3,500건(30% 감소) | 대가입자 |
| 영향범위(가입자·지역) 파악 방식 | 수작업·사후 추정 | 실시간 조회(P99 3초) | 내부 |

### 4-4. 인과 고리 (수미상관, RFP 1-4)

- 실시간 가시성 확보(WHY) → 담당자 5분 통지 → 검수된 안내 문구로 가입자 30분 내 선제 안내 → 문의 폭주 전  
  가입자 안심(문의 30% 감소). 헤드라인의 "가장 먼저 안심" 약속이 대가입자 지표로 닫힘.

### 4-5. 표면 요구 vs 실제 니즈 (5 Whys 적용 예)

- 표면 요구: "장애 알림 시스템을 만들어달라."  
- Why1 왜 알림이 필요? → 사고를 늦게 인지함(평균 40분).  
- Why2 왜 늦나? → 장애 1차 정보가 MNO에 종속되고 자동 수신 채널이 없음.  
- Why3 늦으면 왜 문제? → 고객센터가 문의 폭주로 마비됨.  
- Why4 마비되면 왜 문제? → 가입자가 불안·불신으로 이탈함.  
- Why5 이탈하면 왜 문제? → 신뢰·매출 훼손, "가장 먼저 안심시키는 사업자" 목표가 실패함.  
- 실제 니즈: 단순 알림봇이 아니라 ① 5분 내 담당자 인지 ② 검수된 정확한 안내로 30분 내 가입자 선제 안심  
  ③ 영향범위 실시간 파악 ④ 상담 응대 부담 경감임. 실제 니즈를 놓치면 알림봇만 만들고 이탈은 못 막음.

### 4-6. 엔드유저 관점 상충 (RFP 2-1)

- 사내 운영자(고객센터·상황실): "정확·신속 통지와 응대 부담 경감"을 원함.  
- 경영진: "가입자 이탈 방지·신뢰 유지"를 원함.  
- 상충 시 우선순위: 가입자 보호(통지 신속성)를 최우선으로 함. 문제 정의에 이 우선순위를 반영함.

---

## 5. 출처 목록

> 재활용(가이드 섹션 2 각주)과 신규 확인(WebSearch)을 구분 표기함. 신규 항목은 2026-07-09 검색으로 URL 확인함.

### 재활용 (rfp/RFP작성가이드.md 각주)

[^sinek]: Start With Why / Golden Circle (Simon Sinek) - https://simonsinek.com/golden-circle/
[^opengroup]: Developing IT strategy — aligning IT capabilities with business requirements (The Open Group) - https://blog.opengroup.org/2011/11/22/developing-it-strategy-aligning-it-capabilities-business-requirements/
[^moxie]: How to Structure a Story: 7 Frameworks (Moxie Institute) - https://www.moxieinstitute.com/how-to-structure-story-business-frameworks/
[^iso29148]: ISO/IEC/IEEE 29148:2018 Requirements engineering - https://www.iso.org/standard/72089.html

### 신규 확인 (WebSearch, 2026-07-09)

[^lean]: 5 Whys — What is it? (Lean Enterprise Institute, 도요타 오노 다이이치 정립) - https://www.lean.org/lexicon-terms/5-whys/
[^asq]: Five Whys and Five Hows (ASQ, American Society for Quality) - https://asq.org/quality-resources/five-whys
[^iiba]: A Guide to the Business Analysis Body of Knowledge (BABOK, IIBA) - https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/
[^balearnings]: An Introduction To Gap Analysis (Business Analyst Learnings) - https://www.businessanalystlearnings.com/ba-techniques/2016/11/22/an-introduction-to-gap-analysis
[^smart-wiki]: SMART criteria (Wikipedia) - https://en.wikipedia.org/wiki/SMART_criteria
[^cfi]: SMART Goal — Definition, Guide, and Importance of Goal Setting (Corporate Finance Institute) - https://corporatefinanceinstitute.com/resources/management/smart-goal/
[^mdh]: Writing Meaningful Goals and SMART Objectives — baseline·target (Minnesota Dept. of Health) - https://www.health.state.mn.us/communities/practice/resources/phqitoolbox/objectives.html
