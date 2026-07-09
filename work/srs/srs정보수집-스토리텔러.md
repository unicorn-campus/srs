# SRS 정보수집 — S1. SRS 개요·목적·범위·독자 (담당: 스토리텔러)

> 목적: 「SRS 작성 가이드」 S1 섹션(문서 메타: 목적·범위·제외범위·독자·용어) 초안 작성에 필요한  
> 근거를 본인 지식 + 신뢰성 있는 외부 자료로 정리함. 외부 자료는 출처 URL을 반드시 표기함.  
> 근거 입력: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`,  
> 구조 선례 `rfp/RFP작성가이드.md`, 아젠다 `work/srs/srs-agenda.md`.  
> 작성: 스토리텔러(제안서 작성자) / 표준 기준: ISO/IEC/IEEE 29148:2018.

---

## 1. 왜 S1(개요·목적·범위·독자)이 SRS의 첫 관문인가 (WHY First)

- SRS의 첫 섹션은 "이 문서가 무엇을·왜·누구를 위해 작성되었는가"를 못 박는 계약적 서문임.  
  범위(scope)가 모호하면 이후 FR·NFR·인수 기준이 아무리 정밀해도 정산·검수 분쟁의 근원이 됨.  
- ISO/IEC/IEEE 29148은 SRS 첫머리에 목적(Purpose)·범위(Scope)·제품 조망(Product overview)·  
  정의(Definitions)를 두어, 본론 요구사항을 읽기 전에 독자가 시스템 경계와 이해관계자를 인지하도록 규정함.[^iso29148][^obp29148]  
- 실무 모범사례도 SRS 작성의 출발점을 두 질문으로 요약함 — "이 소프트웨어는 왜 존재하는가",  
  "무엇이 범위 안이고 무엇이 범위 밖인가". 이 지점의 모호성이 프로젝트 전체를 흔든다고 경고함.[^perforce][^apriorit]

---

## 2. ISO/IEC/IEEE 29148:2018 — SRS 문서 개요 요소 (핵심 근거)

### 2-1. 표준의 3계층 요구사항 문서 체계

- ISO/IEC/IEEE 29148:2018은 요구공학 전 주기(도출→분석→명세→검증)를 다루며, 요구사항 문서를  
  3계층으로 정의함.[^iso29148][^jama]  
  - StRS(Stakeholder Requirements Specification): 이해관계자가 시스템에 기대하는 바(요구의 원천).  
  - SyRS(System Requirements Specification): 이해관계자 요구를 시스템 수준 요구로 번역.  
  - SRS(Software Requirements Specification): 개발자가 설계하고 시험자가 검증할 수 있을 만큼 상세한  
    소프트웨어 수준 요구.  
- 본 사업 SRS는 확정 RFP(발주사 요구의 원천, StRS에 상응)를 근거로 작성하는 SRS 계층 문서임.

### 2-2. SRS 표준 목차와 개요(Introduction) 절 구성

- 29148의 SRS 권고 목차(Annex/Clause 9.5.x)는 아래 구조이며, 이 중 개요(1장)가 S1 담당 범위임.[^obp29148][^reqview-tmpl]  

| 목차 | 절 | S1 담당 여부 |
|------|-----|:---:|
| 1. Introduction(개요) | 1.1 Purpose(목적) | ● |
| | 1.2 Scope(범위·제외범위) | ● |
| | 1.3 Product overview(제품 조망: perspective·functions·user characteristics·limitations) | ● |
| | 1.4 Definitions(정의·용어) | ● (위치 지정) |
| 2. References(참조) | — | ● (근거 문서 지정) |
| 3. Specific requirements | 외부 인터페이스·기능·성능·DB·설계제약·품질속성 | S3~S5 |
| 4. Verification(검증) | 요구별 검증 방법 | S6 |
| 5. Appendices | 가정·의존성, 약어 | S7 |

### 2-3. 목적(Purpose) 절이 담아야 할 요소

- 29148은 목적 절에 (1) SRS 문서 자체의 목적을 기술하고 (2) **의도된 독자(intended audience)를  
  명시**할 것을 요구함.[^obp29148][^reqview-example]  
- 즉 "무엇을 만드는가"뿐 아니라 "이 문서를 누가 어떤 목적으로 읽는가"를 서문에서 규정해야 함.

### 2-4. 범위(Scope) 절이 담아야 할 요소

- 29148 Scope 절 요구사항.[^obp29148][^reqview-example][^wikipedia]  
  - 산출될 소프트웨어 제품을 **이름으로 식별**함.  
  - 제품이 **할 것(what it will do)과 하지 않을 것(what it will not do)**을 설명함.  
  - 응용의 효익·목표·목적을 기술함.  
  - 상위 명세(사업계획·시스템명세 등)의 유사 진술과 **일관**되게 유지함.  
- 핵심: "하지 않을 것"의 명문화가 표준이 요구하는 필수 요소임(범위 경계 = 포함 + 제외).

### 2-5. 정의·용어(Definitions) 위치

- 29148은 SRS에서 사용하는 용어·약어·두문자어의 정의를 제공하도록 요구하며, 통상 개요 절(1.4) 또는  
  부록(Acronyms and abbreviations)에 배치함.[^obp29148][^reqview-tmpl]  
- 본 가이드 체계에서는 용어집 본체를 S7(추적성·운영이행·용어)에 두고, S1에서는 **위치를 지정·참조**함.

---

## 3. 범위/제외범위(Scope / Out-of-Scope) 서술 모범사례

- **포함·제외 동시 명시 원칙**: 시스템이 할 일과 하지 않을 일을 함께 나열함. RFP·SRS에 적히지 않은  
  기능은 자동으로 제외범위이며 별도 명세·변경(CR) 대상임을 명확히 함.[^perforce][^melsatar]  
- **제외범위 커뮤니케이션**: 제외 항목은 단순 나열이 아니라 "왜 제외인지·구현 시 어떤 영향인지"를  
  이해관계자에게 설명하여 범위 확장(scope creep)과 기대 불일치를 예방함.[^apriorit][^melsatar]  
- **이해관계자 검토·검증**: 범위 진술은 이해관계자(개발·영업·법무 등)와 공유·검증하여 초기에 인식  
  차이를 제거함. 범위 정렬 실패는 후반 정산 분쟁으로 전이됨.[^perforce][^apriorit]  
- **상위 문서 일관성**: SRS 범위는 상위 RFP·계약의 요구ID·SLA·계약조건과 수치·경계가 일치해야 함  
  (29148의 "상위 명세와 일관" 요구와 동일 취지).[^obp29148]

---

## 4. 독자(이해관계자)별 관점 — 개발·영업·법무

- 29148은 SRS 독자로 개발자·관리자·시험자·사용자 등을 예시하며, 각자 다른 목적으로 문서를 읽음.[^jama][^reqview-example]  
- 본 사업 SRS의 3대 독자와 관심사(RFP 근거).  

| 독자 | 읽는 목적 | 주로 참조하는 RFP 근거 |
|------|-----------|------------------------|
| 개발(수주 벤더·구축 사업자) | 기능·NFR·연동 규격을 설계·구현·시험 | REQ-BIZ/TEC 전체, Capacity 수치표, Webhook/API 규격 |
| 영업 | 제안 범위·가격·SLA 협상 기준 확정 | 제안서 구성(5장), 예산 NRC/MRC(3장), 배점 매핑(부록A) |
| 법무 | 규제·계약 리스크 검토 | 개인정보 안전성 확보조치, NDA 2회, 저작권 분리귀속, 서비스 크레딧·하자/유지 경계(6장) |

- 통신 RFP·SRS 응답은 엔지니어링·상품·법무·컴플라이언스·재무·영업 다부서 기여가 필요하므로,  
  독자를 서문에 명시해 각 부서가 "자기 절"을 빠르게 찾도록 설계함(가이드 섹션 9-b 오너십 원칙과 정합).

---

## 5. 본 RFP(MVNO 시스템)에 대한 S1 적용 매핑

### 5-1. 대상 시스템 식별(제품명)

- 「MVNO향 통신 장애·보안사고 실시간 통지 및 영향범위 조회 시스템」. 발주사 OO모바일(MVNO)이  
  MNO 망 사고 시 가입자를 가장 먼저 보호하기 위해 구축하는 시스템(RFP 0·1장).

### 5-2. 범위(포함) — RFP 요구ID 기반

- 업무: 심각도별 자동 통지(REQ-BIZ-01), 영향범위 실시간 조회(REQ-BIZ-02), 복구 ETR 갱신(REQ-BIZ-03),  
  사고 리포트 자동생성(REQ-BIZ-04), AI 영향예측(REQ-BIZ-05a)·응대지원(REQ-BIZ-05b).  
- 기술: Webhook/API 실시간 푸시(REQ-TEC-01), 대규모 동시 조회(REQ-TEC-02), 다중 채널 이중화  
  (REQ-TEC-03), 인증·전송보안·위변조 방지(REQ-TEC-04), AI 모델 서비스화(REQ-TEC-05), 인프라·  
  MNO 연동 구성(REQ-TEC-06).  
- 운용: 가용성 보장(REQ-OPS-01), 통지 SLA 준수율 관리(REQ-OPS-02), 24x365 공동 대응·합동 훈련  
  (REQ-OPS-03), 월간 리포트(REQ-OPS-04). → 총 16개 요구ID.

### 5-3. 제외범위(Out-of-Scope) — RFP가 명시적으로 벤더 책임 밖으로 규정한 항목

- **MNO 망 복구 자체**: 실제 망 복구 주체는 MNO이므로 MNO 복구 MTTR은 벤더 SLA에서 제외,  
  월간 리포트의 관찰 지표로만 제공(RFP 2-2·2-3). 벤더 책임은 ETR 15분 주기 갱신 성실성에 한정.  
- **개인 식별정보 개별 제공**: 영향범위 조회는 집계·범위 단위로 제공하고 개인 식별을 최소화(RFP 2-2 보안).  
- **AI 예측·생성 결과의 자동 확정**: AI 결과는 참고용이며 최종 통지·안내 문구는 담당자 검수(HITL)  
  필수(RFP 2-1). 무인 자동 발송은 범위 밖.  
- **구체 이중화 아키텍처·배포형태**: Active-Active/Standby 등 이중화 방식과 클라우드/온프레미스 배포는  
  가용성 목표 달성을 전제로 벤더 제안에 위임(RFP 2-2·REQ-TEC-06). SRS는 목표만 명세, 수단은 비고정.

### 5-4. 용어 정의 위치

- RFP 약어표(MNO/MVNO/NRC/MRC/NFR/TPS/P99/MTTR/ETR/RTO/RPO/HITL/PM/CR/SLA)를 승계하되,  
  SRS 용어집 본체는 S7에 배치하고 S1에서는 위치를 참조 지정함.

### 5-5. 측정 가능한 인수 기준(범위 정의 완전성) — 서술 예시

- 지표: 범위 정의 완전성 = (SRS 범위 항목에 매핑된 RFP 요구ID 수 / RFP 확정본 전체 요구ID 수) × 100.  
- 목표값: 100%(요구ID 16개 전부 SRS 범위 항목으로 1:1 매핑, 누락 0건) **그리고** 제외범위 절에 명시  
  항목 3개 이상 존재(MNO 망 복구·개인식별정보 개별제공·AI 자동확정 등).  
- 측정조건(Given-When-Then): RFP 확정본 요구ID 16개가 주어졌을 때(Given), SRS S1 범위 절과 S3~S7을  
  대조하면(When), 전 요구ID가 매핑되고 제외범위 명시 항목이 존재함(Then). 판정: RTM(S7) 교차 확인.

---

## 6. 출처 목록 (외부 자료 URL)

[^iso29148]: ISO/IEC/IEEE 29148:2018 Systems and software engineering — Requirements engineering (ISO 표준 페이지) - https://www.iso.org/standard/72089.html
[^obp29148]: ISO/IEC/IEEE 29148:2018(en) 온라인 브라우징 플랫폼(SRS 목차·Purpose·Scope 절 원문) - https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29148:ed-2:v1:en
[^reqview-tmpl]: ISO/IEC/IEEE 29148 Requirements Specification Templates (ReqView) - https://www.reqview.com/doc/iso-iec-ieee-29148-templates/
[^reqview-example]: Example Software Requirements Specification (SRS) — 29148 기반 예제 (ReqView) - https://www.reqview.com/doc/iso-iec-ieee-29148-srs-example/
[^jama]: How to Write a System Requirements Specification (SRS) Document (Jama Software) - https://www.jamasoftware.com/requirements-management-guide/writing-requirements/system-requirements-specification/
[^wikipedia]: Software requirements specification (Wikipedia) - https://en.wikipedia.org/wiki/Software_requirements_specification
[^perforce]: How to Write a Software Requirements Specification (SRS) Document (Perforce) - https://www.perforce.com/blog/alm/how-write-software-requirements-specification-srs-document
[^apriorit]: Crafting a Clear Software Requirements Specification (SRS) (Apriorit) - https://www.apriorit.com/white-papers/706-srs-development
[^melsatar]: Software Scope vs. Requirement specifications (Mohamed Sami) - https://melsatar.blog/2017/05/14/software-scope-vs-requirement-specifications/

> 비고: [^iso29148]의 ISO 표준 페이지는 `rfp/RFP작성가이드.md` 각주와 동일 URL로, 본 SRS 가이드에서도  
> 동일 근거를 승계함. 표준 원문 전문은 유료이며, 목차·절 요구사항은 [^obp29148](공식 OBP 미리보기)·  
> [^reqview-tmpl]·[^reqview-example](표준 기반 공개 템플릿·예제)로 교차 확인함.
