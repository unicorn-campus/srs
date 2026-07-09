# SRS 가이드 S3 정보수집 — 기능 요구사항(FR)·솔루션 범위 (데모)

> 담당: PoC 엔지니어(데모)  
> 목적: SRS 작성 가이드 S3 섹션(기능 요구사항·솔루션 범위) 초안 작성에 필요한 이론·기법·외부 근거를 정리함.  
> 대상 섹션: 「S3. 기능 요구사항(FR)·솔루션 범위」 — RFP의 REQ-BIZ 업무 요구를 검증 가능한 FR로 정형화하는 방법.  
> 근거 입력: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`,  
> 구조 선례 `rfp/RFP작성가이드.md`(3단 구조), 확정 아젠다 `work/srs/srs-agenda.md`.  
> 출처 표기 원칙: 외부 자료는 WebSearch로 URL을 확인한 것만 기재하며, 확인 못한 URL은 지어내지 않음.

---

## 1. 핵심 질문 (S3가 답해야 할 것)

- RFP의 업무 요구(REQ-BIZ, "무엇을 하고 싶은가")를 SRS의 기능 요구사항(FR, "시스템이 무엇을 하는가")으로  
  어떻게 변환하는가.  
- 기능ID를 어떻게 부여하고 RFP 요구ID와 어떻게 매핑(추적)하는가.  
- 솔루션 범위(In-scope)·제외범위(Out-of-scope)·가정(Assumptions)·제약(Constraints)을 어떻게 구분하는가.  
- 각 FR을 어떻게 검증(PoC 판정 기준)에 연결하여 "측정할 수 없으면 요구사항이 아님" 원칙을 지키는가.

---

## 2. 개념·기법 정리 (근거 포함)

### 2-1. 업무 요구(REQ-BIZ) → 기능 요구(FR) 정형화

- 요구는 3층위로 구분됨: 비즈니스 요구(왜·무엇을) → 기능 요구(시스템이 무엇을 함) → 비기능 요구(얼마나 잘).  
  RFP의 REQ-BIZ는 비즈니스·업무 층위이며, SRS의 FR은 이를 "시스템 관점의 검증 가능한 동작"으로 좁혀 재기술함.  
  (근거: `rfp/RFP작성가이드.md` 3-(a) 요구 표현 구분 원칙 / ISO/IEC/IEEE 29148 요구 층위)  
- 하나의 REQ-BIZ가 복수 FR로 분해될 수 있음(예: "심각도별 자동 통지" = 심각도 판정 FR + 통지 발송 FR).  
- 비기능(성능·가용성·보안 정량치)은 FR이 아니라 NFR(S4)로 이관하되, FR의 PoC 판정 기준에서 상호 참조함.

### 2-2. ISO/IEC/IEEE 29148 기능 요구 명세 기법

- ISO/IEC/IEEE 29148은 개별 요구가 갖춰야 할 **9개 특성**을 규정함: necessary(필요), appropriate(적절),  
  unambiguous(명확), complete(완전), singular(단일), feasible(실현가능), verifiable(검증가능), correct(정확),  
  conforming(준수). FR 작성 시 이 특성을 만족하도록 서술함.  
- **검증가능성(verifiable)**: 요구가 충족되었음을 증명(가능하면 측정)할 수 있는 프로세스가 존재해야 검증 가능함.  
  "검증가능성은 요구가 측정 가능할 때 강화됨"(standard guidance). → S3의 "각 FR에 측정 가능한 PoC 판정 기준 부여"의 근거.  
- **기능 요구 문장 구조(2018)**: [condition(조건) + subject(주체) + action(동작) + object(대상) +  
  constraint of action(동작 제약)] 5요소로 서술하면 명확·검증 가능한 FR이 됨.  
  - 출처: ISO/IEC/IEEE 29148:2011 (ISO 공식) https://www.iso.org/standard/45171.html  
  - 출처: ISO/IEC/IEEE 29148 SRS 템플릿·요구 특성 정리 https://www.reqview.com/doc/iso-iec-ieee-29148-templates/  
  - 출처: 29148 SRS 예시 템플릿 https://www.well-architected-guide.com/documents/iso-iec-ieee-29148-template/

### 2-3. 유스케이스·Given-When-Then 인수기준 형식

- 인수 기준(Acceptance Criteria)은 "요구 의도"와 "인도 결과" 사이의 계약이며, 완료 판정·범위 경계를 명확히 함.  
- **Given-When-Then**(BDD 형식): "Given(전제조건) → When(동작) → Then(기대 결과)"로 서술하면 조건·동작·결과가  
  분리되어 복잡한 기능도 검증 가능한 형태로 고정됨. 기능형 인수기준은 "시스템이 특정 조건에서 무엇을 해야 하는가"를  
  사용자 관점 동작으로 기술함.  
- 유스케이스는 액터·사전조건·주 흐름·대안 흐름으로 기능 맥락을 서술하며, 인수기준은 그 흐름의 판정 기준을 제공함.  
  - 출처: Acceptance Criteria 정의·Given-When-Then https://www.atlassian.com/work-management/project-management/acceptance-criteria  
  - 출처: Acceptance Criteria 형식·베스트프랙티스 https://www.altexsoft.com/blog/acceptance-criteria-purposes-formats-and-best-practices/  
  - 출처: Acceptance Criteria 범위 경계·모호성 제거 https://www.productplan.com/glossary/acceptance-criteria

### 2-4. 범위·제외범위·가정·제약 구분

- 인수기준·범위 명시는 팀을 합의된 기능에 정렬시키고, 개발 중 예기치 못한 추가(scope creep)를 차단함.  
- 4구분 정의(정산 분쟁 예방 목적):  
  - **범위(In-scope)**: 벤더가 구현·책임지는 기능 경계.  
  - **제외범위(Out-of-scope)**: 명시적으로 본 사업에서 제외하는 항목(오해·분쟁 방지 위해 명문화).  
  - **가정(Assumptions)**: 참으로 전제하는 선행 조건(불충족 시 범위·일정 영향).  
  - **제약(Constraints)**: 반드시 지켜야 하는 한계(규제·기술·정책).  
  - 출처: 범위 경계·제약(scope/constraints) 관리 https://www.atlassian.com/work-management/project-management/acceptance-criteria

### 2-5. PoC 판정 기준(성공/합격 기준) 설계

- PoC는 실데이터·실업무로 솔루션이 문제를 해결하는지 구매 전 검증하는 구간이며, 명확한 성공 기준·기간·  
  상호 약속이 성공 전제임(B2B는 통상 30~90일).  
- **성공 기준(Success Criteria)은 측정 가능·문제 직결**이어야 함 — 성능 임계값·비용 목표·사용자 만족도 등  
  합격/불합격을 가르는 벤치마크로 정의함.  
- **SMART 원칙**: Specific(구체) · Measurable(측정가능·KPI 명시) · Attractive/Achievable(사업목표 연관) ·  
  Realistic(PoC 범위 내 검증가능) · Time-bound(수행·평가 시한 명시). FR의 판정 기준 설계에 그대로 적용함.  
- 리스크 근거: **PoC의 약 62%가 목표(성공 기준) 부실 정의로 실패**함(McKinsey 2023, diceus 인용). → 판정 기준을  
  사전에 정량으로 못 박는 것이 S3의 핵심 산출 가치임.  
  - 출처: PoC 성공 기준·SMART·실패율 https://diceus.com/poc-success-criteria/  
  - 출처: PoC 정의·단계 https://asana.com/resources/proof-of-concept  
  - 출처: 엔터프라이즈 세일즈 PoC 성공 기준·상호 약속 https://inaccord.com/blog-posts/what-is-a-proof-of-concept-in-enterprise-sales  
  - 출처: B2B PoC(파일럿)의 비용·성공 확보 https://brixongroup.com/en/proof-of-concept-in-b2b-marketing-when-a-pilot-project-really-saves-costs-and-ensures-success/

### 2-6. AI 기능 요구의 검증 특수성

- AI 예측·생성 기능은 결정론적 기능과 달리 결과가 확률적이므로, 판정 기준을 **통계적 임계값(오차율)·표본·  
  폴백 조건·사람 검수(HITL)**로 설계해야 함.  
- 본 RFP는 이를 이미 반영함: AI 영향예측은 과거 사고 전수 백테스트 오차율 ±15% 이내 합격·룰 기반 폴백,  
  AI 응대지원은 초안 생성 후 상담사(HITL) 검수 후 사용, AI 결과는 참고용으로 최종 문구는 담당자 검수.  
  (근거: RFP REQ-BIZ-05a/05b, REQ-TEC-05, 6-3 AI 재학습 귀속 경계)  
- 따라서 AI FR의 PoC 판정은 "단일 통과/실패"가 아니라 "합격 건수·오차율 리포트 + 폴백 동작 확인 + HITL 게이트  
  통과"로 구성함(SMART의 Measurable을 확률 지표로 구체화).

---

## 3. 본 RFP REQ-BIZ → FR 매핑 근거 (S3 예시 재료)

> 아래는 확정 RFP 2-1 업무 요구(REQ-BIZ)와 확인 기준을 그대로 근거로 삼아 FR 정형화의 재료로 정리한 것임.

| RFP 요구ID | 업무 요구 요지 | RFP 확인 기준(측정) | 도출 FR(그룹) |
|-----------|----------------|----------------------|----------------|
| REQ-BIZ-01 | 심각도별 자동 통지 | 수신(인지) 후 5분 이내 담당자 통지 도달 | FR-통지 |
| REQ-BIZ-02 | 영향 가입자·지역·서비스 범위 실시간 조회 | 평균 2초 & P99 3초, 표본 100건 100% 일치 | FR-조회 |
| REQ-BIZ-03 | 복구 진행률·ETR 갱신 제공 | 15분 주기 갱신, 완료 시점까지 연속 조회 | FR-ETR |
| REQ-BIZ-04 | 사고 종료 후 이력·재발방지 리포트 자동 생성 | 종료 후 3영업일 이내(타임라인·영향범위·MTTR 포함) | FR-리포트 |
| REQ-BIZ-05a | AI 기반 영향범위 예측 | 과거 전수 백테스트 오차율 ±15%·룰 폴백 | FR-AI예측 |
| REQ-BIZ-05b | AI 기반 고객센터 응대 지원 | 통지 후 10분 내 초안·상담사(HITL) 검수 | FR-AI응대 |

- 범위/제외범위/가정/제약의 RFP 근거:  
  - 제외범위: MNO 망 자체 복구(2-2 "MNO 복구 MTTR은 벤더 SLA 제외"), 가입자 개인 식별정보 원문 제공  
    (2-2 보안 "집계·범위 단위 제공, 개인 식별 최소화"), 무검수 자동 발송(2-1 "최종 문구는 HITL 검수").  
  - 가정: MNO가 이벤트를 Webhook/API 규격으로 실시간 제공(REQ-TEC-01), AI 백테스트용 과거 사고 데이터 확보 가능.  
  - 제약: 개인정보보호법 안전성 확보조치 준수, 접근권한 3단계 분리(2-2), AI 결과 참고용·HITL 게이트.

---

## 4. S3 초안 반영 포인트 (요약)

- (a) 작성원칙: REQ-BIZ→FR 정형화, ISO 29148 5요소 문장 구조·9특성, 기능ID 규칙, 범위 4구분, FR→PoC 판정 연결.  
- (b) 예시: 6개 FR 그룹(통지·조회·ETR·리포트·AI예측·AI응대)의 FR 분해표 + 기능ID↔RFP 요구ID 매핑 +  
  측정 가능 인수기준(예: FR-조회-01 평균2초&P99 3초·표본100건 100% 일치) + Given-When-Then 서술.  
- (c) 체크리스트: 망라성·검증가능성·추적성·범위 4구분·PoC 판정·AI 특수 취급 점검.

---

## 5. 출처 목록 (WebSearch 확인 URL)

- ISO/IEC/IEEE 29148:2011 (ISO 공식 표준 페이지): https://www.iso.org/standard/45171.html  
- ISO/IEC/IEEE 29148 SRS 템플릿·요구 9특성 정리(ReqView): https://www.reqview.com/doc/iso-iec-ieee-29148-templates/  
- ISO/IEC/IEEE 29148 SRS 예시 템플릿(Well-Architected Guide): https://www.well-architected-guide.com/documents/iso-iec-ieee-29148-template/  
- Acceptance Criteria 정의·Given-When-Then(Atlassian): https://www.atlassian.com/work-management/project-management/acceptance-criteria  
- Acceptance Criteria 형식·베스트프랙티스(AltexSoft): https://www.altexsoft.com/blog/acceptance-criteria-purposes-formats-and-best-practices/  
- Acceptance Criteria 범위 경계(ProductPlan): https://www.productplan.com/glossary/acceptance-criteria  
- PoC 성공 기준·SMART·실패율(Diceus): https://diceus.com/poc-success-criteria/  
- PoC 정의·단계(Asana): https://asana.com/resources/proof-of-concept  
- 엔터프라이즈 세일즈 PoC(Accord): https://inaccord.com/blog-posts/what-is-a-proof-of-concept-in-enterprise-sales  
- B2B PoC 파일럿 비용·성공(Brixon Group): https://brixongroup.com/en/proof-of-concept-in-b2b-marketing-when-a-pilot-project-really-saves-costs-and-ensures-success/

> 비고: 위 URL은 WebSearch 결과에서 확인한 실제 링크임. McKinsey 62% 통계는 Diceus 문서가 인용한 2차 출처로,  
> 원 보고서 직접 확인은 하지 않았으므로 "Diceus 인용(McKinsey 2023)"으로 표기함.
