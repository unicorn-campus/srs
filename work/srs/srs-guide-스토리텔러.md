## S1. SRS 개요·목적·범위·독자

> 담당: 스토리텔러(제안서 작성자) / 표준 기준: ISO/IEC/IEEE 29148:2018 SRS 개요 요소.  
> 다루는 SRS 항목: 문서 목적 진술·대상 시스템 범위·제외범위·독자(개발/영업/법무)·용어 정의 위치.  
> 근거: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`.

### (a) 작성 원칙

- S1은 SRS 본론(FR·NFR·데이터·인수기준)을 읽기 전에 독자가 **시스템 경계·목적·이해관계자**를 인지하도록  
  하는 계약적 서문임. 범위가 모호하면 이후 명세가 정밀해도 정산·검수 분쟁의 근원이 됨.[^perforce]  
- ISO/IEC/IEEE 29148은 SRS 개요(Introduction)에 목적(Purpose)·범위(Scope)·제품 조망(Product overview)·  
  정의(Definitions)를 두도록 규정함. S1은 이 4요소를 담당함.[^iso29148][^obp29148]  
- **목적(Purpose) 절**: 문서 자체의 목적과 함께 **의도된 독자(intended audience)를 명시**함 — "무엇을  
  만드는가"에 더해 "누가 어떤 목적으로 읽는가"를 서문에서 규정함.[^obp29148]  
- **범위(Scope) 절**: 산출 제품을 이름으로 식별하고, 제품이 **할 것과 하지 않을 것**을 함께 기술함.  
  "하지 않을 것(제외범위)"의 명문화는 표준이 요구하는 필수 요소이며, 상위 문서(RFP·계약)와 일관되게 유지함.[^obp29148][^melsatar]  
- **제외범위 서술 원칙**: 제외 항목은 단순 나열이 아니라 "왜 제외인지·구현 시 영향"을 함께 적어 범위  
  확장(scope creep)과 기대 불일치를 예방함. RFP·SRS에 없는 기능은 자동으로 제외이며 변경(CR) 대상임.[^apriorit][^melsatar]  
- **독자 정의 원칙**: 개발·영업·법무 등 독자를 서문에 명시해 각 부서가 "자기 절"을 빠르게 찾도록 함.  
  통신 SRS는 다부서 기여가 필요하므로 독자별 관심사를 연결해 섹션 오너십을 명확히 함.[^jama]  
- **용어 정의 위치 원칙**: 용어·약어 정의는 개요 또는 부록에 배치함. 본 가이드는 용어집 본체를 S7에 두고  
  S1에서 위치를 참조 지정하여 중복을 방지함.[^obp29148]  
- **측정 가능성 원칙**: 범위 정의도 검증 가능해야 함 — "범위가 명확함" 같은 정성 표현 대신 "요구ID  
  100% 매핑·제외범위 명시 항목 존재"처럼 측정 가능한 완전성 기준으로 서술함(측정할 수 없으면 요구가 아님).

### (b) 통신사 B2B 예시·문구 (본 RFP 맥락 각색)

- **목적 진술 예시**: "본 SRS는 「MVNO향 통신 장애·보안사고 실시간 통지 및 영향범위 조회 시스템」의  
  기능·비기능·데이터 요구를 확정 RFP에 근거해 명세하여, 발주사(OO모바일)와 수주 벤더가 동일 기준으로  
  설계·구축·검수·정산하도록 함을 목적으로 함. 독자는 개발(수주 벤더)·영업·법무임."  
- **대상 시스템 식별 예시**: "대상 제품은 MNO 망 장애·보안사고 이벤트를 수신하여 MVNO 담당자에게  
  심각도별 자동 통지하고, 영향 가입자 규모·지역을 실시간 조회하며, 복구정보(ETR)·사고 리포트·AI  
  영향예측을 제공하는 시스템임."  
- **범위(포함) 예시**: 심각도별 자동 통지(REQ-BIZ-01), 영향범위 실시간 조회(REQ-BIZ-02), 복구 ETR  
  갱신(REQ-BIZ-03), 사고 리포트 자동생성(REQ-BIZ-04), AI 영향예측·응대지원(REQ-BIZ-05a/05b),  
  Webhook/API 실시간 푸시·다중 채널 이중화·보안·MNO 연동(REQ-TEC-01~06), 가용성·SLA·공동대응·  
  월간 리포트(REQ-OPS-01~04). → RFP 요구ID 16개 전체.  
- **제외범위(Out-of-Scope) 예시 문구**  
  - "MNO 망 복구 자체는 본 시스템 범위에서 **제외**함 — 복구 주체는 MNO이며, MNO 복구 MTTR은 벤더  
    SLA 대상이 아닌 월간 리포트 관찰 지표로만 제공함. 벤더 책임은 ETR 15분 주기 갱신 성실성에 한정."  
  - "가입자 개인 식별정보의 개별 제공은 **제외**함 — 영향범위 조회는 집계·범위 단위로만 제공하고 개인  
    식별을 최소화함(개인정보보호법 안전성 확보조치 준수)."  
  - "AI 예측·생성 결과의 무인 자동 확정·발송은 **제외**함 — AI 결과는 참고용이며 최종 통지·안내 문구는  
    담당자 검수(HITL)를 거침."  
  - "구체 이중화 아키텍처(Active-Active/Standby)·배포형태(클라우드/온프레미스)는 SRS에서 고정하지  
    **않음** — 가용성 목표(99.95%/월) 달성을 전제로 벤더 제안에 위임함."  
- **독자별 관심사 매핑 문구**  
  - 개발(수주 벤더): 기능·NFR·연동 규격 구현 근거(REQ-BIZ/TEC, Capacity 수치표, Webhook/API 규격).  
  - 영업: 제안 범위·가격(NRC/MRC)·SLA 협상 기준(제안서 구성·예산·배점 매핑).  
  - 법무: 개인정보 안전성 확보조치, NDA 2회, 저작권 분리귀속, 서비스 크레딧·하자/유지 경계(6장).  
- **용어 정의 위치 문구**: "본 SRS의 용어·약어(MNO·MVNO·NRC·MRC·NFR·TPS·P99·MTTR·ETR·RTO/RPO·  
  HITL·PM·CR·SLA)는 RFP 약어표를 승계하며, 용어집 본체는 S7(추적성·운영이행·용어)에 배치함."  
- **측정 가능한 인수 기준 서술 예시**(범위 정의 완전성)  
  - 지표: 범위 정의 완전성 = (SRS 범위 항목에 매핑된 RFP 요구ID 수 / RFP 전체 요구ID 수) × 100.  
  - 목표값: **100%**(요구ID 16개 전부 1:1 매핑, 누락 0건) **그리고** 제외범위 명시 항목 **3개 이상** 존재.  
  - Given-When-Then: RFP 확정본 요구ID 16개가 주어졌을 때(Given), SRS S1 범위 절과 S3~S7을 대조하면  
    (When), 전 요구ID가 범위 항목으로 매핑되고 제외범위 명시 항목이 존재함(Then). 판정: RTM(S7) 교차 확인.

### (c) 작성 체크리스트

- [ ] 목적 절에 문서 목적과 **의도된 독자(개발·영업·법무)**를 함께 명시했는가 (29148 Purpose 요구)  
- [ ] 대상 시스템(제품)을 **이름으로 식별**하고 상위 RFP와 명칭이 일치하는가  
- [ ] 범위 절에 **할 것(포함)**을 RFP 요구ID로 열거했는가(16개 매핑)  
- [ ] 범위 절에 **하지 않을 것(제외범위)**을 명시하고 각 항목에 "제외 사유·영향"을 붙였는가  
- [ ] 제외범위가 RFP의 벤더 책임 경계(MNO 복구·개인식별정보·AI 자동확정·이중화 위임)와 일치하는가  
- [ ] 독자별 관심사(참조 절)를 매핑해 각 부서가 자기 절을 찾도록 했는가  
- [ ] 용어·약어 정의 **위치(S7)**를 지정·참조하고 RFP 약어표를 승계했는가  
- [ ] 범위 정의 완전성을 **측정 가능한 인수 기준**(요구ID 100% 매핑·제외범위 명시)으로 서술했는가  
- [ ] S1 범위·경계 수치가 상위 RFP·계약(SLA·서비스 크레딧)과 상호 일관되는가

[^iso29148]: ISO/IEC/IEEE 29148:2018 Systems and software engineering — Requirements engineering (ISO) - https://www.iso.org/standard/72089.html
[^obp29148]: ISO/IEC/IEEE 29148:2018(en) 온라인 브라우징 플랫폼(SRS 목차·Purpose·Scope 절 원문) - https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29148:ed-2:v1:en
[^jama]: How to Write a System Requirements Specification (SRS) Document (Jama Software) - https://www.jamasoftware.com/requirements-management-guide/writing-requirements/system-requirements-specification/
[^perforce]: How to Write a Software Requirements Specification (SRS) Document (Perforce) - https://www.perforce.com/blog/alm/how-write-software-requirements-specification-srs-document
[^apriorit]: Crafting a Clear Software Requirements Specification (SRS) (Apriorit) - https://www.apriorit.com/white-papers/706-srs-development
[^melsatar]: Software Scope vs. Requirement specifications (Mohamed Sami) - https://melsatar.blog/2017/05/14/software-scope-vs-requirement-specifications/
