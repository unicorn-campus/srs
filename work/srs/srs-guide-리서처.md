## S2. 고객사 문제 정의

> RFP 1장 취지의 WHY에서 As-Is 문제·정량 목표(현재값→목표값)를 SRS 문제 정의로 재구성함.  
> 문제→요구→효과 인과 고리를 유지하고, 표면 요구와 실제 니즈를 구분하여 요구의 목표를 바로잡음.  
> 담당(정보수집·초안): 리서처. 근거: `srs정보수집-리서처.md`, 확정 RFP 1-1·1-3·1-4·2-1.

### (a) 작성 원칙

- **WHY First — 문제 정의 최상단에 경영 의도를 재진술함**: RFP 취지의 키 메시지(Why)를 문제 정의 서두에  
  배치하고 개별 문제·요구를 그 아래에 둠. 골든서클 원칙으로 각 요구가 "왜 필요한지"를 잃지 않게 함.[^sinek]  
- **As-Is/To-Be 간극이 곧 문제임**: 현재 상태(As-Is)와 목표 상태(To-Be)의 간극 자체가 문제이며, 간극을  
  메우는 것이 요구사항임. 각 문제를 정량 지표의 현재값→목표값 대비로 표현하여 갭을 측정 가능하게 함  
  (BABOK 전략분석 갭 분석).[^iiba]  
- **근본원인까지 파고들어 표면 요구와 실제 니즈를 구분함**: 고객이 말한 표면 요구를 그대로 명세하지 않고,  
  5 Whys로 근본원인·실제 니즈를 규명함. 실제 니즈를 놓치면 표면 요구만 충족하는 헛 솔루션이 됨.[^lean][^asq]  
- **정량 목표는 측정 가능하게 못 박음**: 모든 목표를 [지표·현재값(baseline)·목표값·기한] 형식으로 명시함.  
  baseline 없는 목표는 검증 불가하므로 부적격임. "빠르게·많이" 정성 표현은 수량화함(SMART).[^smart-wiki][^mdh]  
- **문제→요구→효과 인과 고리 유지(수미상관)**: 각 문제가 어떤 요구로 해결되고 어떤 효과(목표값)로 닫히는지  
  추적 가능하게 연결함. 문제 정의는 경영목표에서 역산하여 IT-비즈니스 정렬을 이룸.[^opengroup]  
- **RFP 취지(설득 서사) → SRS 문제 정의(검증 기준점) 전환**: RFP 취지의 3막 서사적 수사는 걷어내고, 각 문제를  
  요구ID·인수 기준과 1:1 추적되는 검증 명제로 재작성함. SRS 문제 정의는 이해관계자 니즈 정의를 SRS 안으로  
  고정하는 상류 기준점임(ISO/IEC/IEEE 29148).[^iso29148][^moxie]

### (b) 통신사 B2B 예시·문구

- **WHY(키 메시지) 재진술 예시**  
  - "발주사는 MNO 망 사고가 발생해도 가입자를 가장 먼저 안심시키는 알뜰폰 사업자가 되고자 함. 장애·사고에  
    대한 실시간 가시성 확보가 본 시스템의 존재 이유(Why)임."(RFP 1-1 각색)

- **As-Is 문제를 "장면 → 검증 명제"로 재구성한 표(문제ID·근본원인·정량 지표·대응 요구 연결)**

| 문제ID | As-Is 문제(장면) | 근본원인 | 연결 정량 지표(현재값→목표값) | 대응 요구 |
|--------|------------------|----------|-------------------------------|-----------|
| PRB-01 | MNO 사고를 뉴스·SNS로 뒤늦게 인지, 담당자 통지 평균 40분 | 장애 1차 정보가 MNO에 종속·자동 수신 채널 부재 | 인지~통지 40분 → 5분 이내 | REQ-BIZ-01, REQ-TEC-01 |
| PRB-02 | 공식 정보 부재로 상담사가 뉴스 속보 보며 응대, 고객센터 마비 | 검수된 안내 문구·응대 지원 부재 | 선제 안내 수일 → 30분, 월 문의 5,000 → 3,500건(30%↓) | REQ-BIZ-01, REQ-BIZ-05b |
| PRB-03 | 영향 가입자·지역을 수작업·사후 추정 | 영향범위 실시간 조회 수단 부재 | 수작업 → 실시간 조회(P99 3초) | REQ-BIZ-02, REQ-TEC-02 |
| PRB-04 | 보상 안내가 사고 3주 후 개별 공지(2018 국사 화재) | 복구정보·사고 이력의 체계적 관리 부재 | 사후 리포트 3영업일 이내 제공 | REQ-BIZ-03, REQ-BIZ-04 |

- **5 Whys 예시 — 표면 요구 vs 실제 니즈**  
  - 표면 요구: "장애 알림 시스템을 만들어달라." → Why1 사고를 늦게 인지(40분) → Why2 장애 1차 정보가 MNO에  
    종속·자동 수신 없음 → Why3 고객센터가 문의 폭주로 마비 → Why4 가입자가 불안·불신으로 이탈 → Why5 신뢰·  
    매출 훼손으로 "가장 먼저 안심시키는 사업자" 목표 실패.  
  - 실제 니즈: 단순 알림봇이 아니라 ① 5분 내 담당자 인지 ② 검수된 정확한 안내로 30분 내 가입자 선제 안심  
    ③ 영향범위 실시간 파악 ④ 상담 응대 부담 경감임. 실제 니즈를 놓치면 알림봇만 만들고 이탈은 못 막음.

- **정량 목표 재진술 규칙(나쁨 → 좋음)**  
  - 나쁨(정성): "장애를 빠르게 알리고 문의를 줄여야 함."  
  - 좋음(현재값→목표값): "장애 인지~담당자 통지를 40분에서 5분 이내로 단축하고, 월 고객센터 문의를 5,000건에서  
    3,500건으로 30% 감소함."

- **문제→요구→효과 인과 고리 서술 예시**  
  - "인지 지연(PRB-01) → 실시간 자동 통지·Webhook 푸시 요구(REQ-BIZ-01·REQ-TEC-01) → 인지~통지 5분 달성  
    → 고객센터 마비(PRB-02) 완화 → 월 문의 30% 감소(효과)." 헤드라인 "가장 먼저 안심" 약속이 효과 지표로 닫힘.

- **엔드유저 상충 반영 예시**  
  - 사내 운영자(응대 부담 경감)와 경영진(이탈 방지·신뢰)의 요구가 상충 시, 가입자 보호(통지 신속성)를  
    최우선으로 명시함(RFP 2-1).

- **측정 가능한 인수 기준 서술 예시**(문제 정의의 완료 판정 기준)  
  - 예1(1:1 연결성): "문제 정의 타당성 = 각 문제 항목(PRB-xx)이 RFP 정량 목표(현재값→목표값)와 1:1 연결되고  
    대응 요구ID(REQ-xx)가 부여됨. 미연결 문제 0건일 때 합격."  
  - 예2(정량화 완결성): "As-Is 정량화 완결성 = 모든 문제가 [지표·현재값(baseline)·목표값] 3요소를 갖춤.  
    baseline 누락 항목 0건일 때 합격."

### (c) 작성 체크리스트

- [ ] RFP 1장 키 메시지의 WHY를 문제 정의 최상단에 재진술했는가 (WHY First)  
- [ ] 각 As-Is 문제를 추상어가 아닌 구체적 장면·간극으로 서술했는가  
- [ ] 각 문제에 5 Whys 등으로 근본원인을 규명하고 표면 요구와 실제 니즈를 구분했는가  
- [ ] 모든 정량 목표를 [지표·현재값(baseline)·목표값·기한] 형식으로 명시했는가 (SMART)  
- [ ] 각 문제(PRB)–요구(REQ)–효과(목표값)가 인과 고리로 연결되고 추적 가능한가  
- [ ] 문제 정의가 경영목표에서 역산되어 IT-비즈니스 정렬을 이루는가  
- [ ] RFP 취지의 서사적 수사를 걷어내고 검증 가능한 명제로 재작성했는가  
- [ ] 엔드유저(고객센터·상황실·경영진) 상충을 식별하고 우선순위(가입자 보호 최우선)를 명시했는가

---

### 출처 (S2)

[^sinek]: Start With Why / Golden Circle (Simon Sinek) - https://simonsinek.com/golden-circle/
[^iiba]: A Guide to the Business Analysis Body of Knowledge (BABOK, IIBA) - https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/
[^lean]: 5 Whys — What is it? (Lean Enterprise Institute) - https://www.lean.org/lexicon-terms/5-whys/
[^asq]: Five Whys and Five Hows (ASQ) - https://asq.org/quality-resources/five-whys
[^smart-wiki]: SMART criteria (Wikipedia) - https://en.wikipedia.org/wiki/SMART_criteria
[^mdh]: Writing Meaningful Goals and SMART Objectives (Minnesota Dept. of Health) - https://www.health.state.mn.us/communities/practice/resources/phqitoolbox/objectives.html
[^opengroup]: Aligning IT capabilities with business requirements (The Open Group) - https://blog.opengroup.org/2011/11/22/developing-it-strategy-aligning-it-capabilities-business-requirements/
[^iso29148]: ISO/IEC/IEEE 29148:2018 Requirements engineering - https://www.iso.org/standard/72089.html
[^moxie]: How to Structure a Story: 7 Frameworks (Moxie Institute) - https://www.moxieinstitute.com/how-to-structure-story-business-frameworks/
