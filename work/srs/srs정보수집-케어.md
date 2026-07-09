# SRS 정보수집 — S7 추적성·운영이행·용어 (케어)

> 목적: SRS 작성 가이드 S7 섹션 초안 작성을 위한 정보 수집.  
> 담당: 케어(고객 운영 매니저) / 대상 섹션: S7 추적성·운영이행·용어  
> 근거 입력: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`,  
> 아젠다 `work/srs/srs-agenda.md`, 구조·출처 선례 `rfp/RFP작성가이드.md`(케어 섹션 5 이행·SLA 각주 재사용).  
> 외부 URL 출처 원칙: RFP작성가이드.md 검증 각주 재사용 + WebSearch로 신규 확인분 표기(지어내지 않음).

---

## 1. 요구사항 추적성 매트릭스(RTM)

### 1-1. 표준 근거 — ISO/IEC/IEEE 29148

- ISO/IEC/IEEE 29148:2018은 요구공학(Requirements Engineering) 국제표준으로, 요구사항 추적성을  
  시스템·SW 생애주기 전반의 정합 확보를 위한 필수 요소로 규정함.  
- 표준은 추적성 매트릭스를 통해 요구 간 의존관계·변경 이력을 추적하도록 명시하며, RTM은 모든 사용자  
  요구를 검증 케이스·설계 요소·검증 단계에 매핑하도록 요구됨.  
- SRS 문서 구성 요소로 "요구사항 추적성" 항목을 별도로 두어 상·하위 요구 및 검증 산출물 연결을 기술함.  
- 출처: ISO/IEC/IEEE 29148:2018 Requirements engineering — https://www.iso.org/standard/72089.html  
- 출처: ISO/IEC/IEEE 29148 SRS Example Template(추적성·용어 정의 섹션 포함) —  
  https://www.well-architected-guide.com/documents/iso-iec-ieee-29148-template/

### 1-2. 양방향 추적성(Bidirectional Traceability)

- 양방향 추적성 = 전방(forward: 요구 → 설계 → 코드 → 테스트/검증)과 후방(backward: 결함·테스트·  
  배포 기능 → 원 요구) 양쪽으로 추적 가능한 상태를 의미함.  
- 링크 유형: 만족 링크(상세 요구 → 상위 원천 요구), 검증/확인 링크(V&V 테스트 케이스 → 요구),  
  완화 링크(요구 → 완화 대상 리스크). RTM은 이 링크들을 표로 고정함.  
- 실무 효과: 요구 누락(원천 요구에 대응 SRS 항목 부재)과 고아 항목(원천 요구 없는 SRS 항목)을  
  기계적으로 검출 가능 → 감점·범위 분쟁 사전 차단.  
- 출처: Requirements Traceability Matrix(Perforce) — https://www.perforce.com/resources/alm/requirements-traceability-matrix  
- 출처: RTM for Systems Engineers(ReqView) — https://www.reqview.com/blog/requirements-traceability-matrix/

### 1-3. RTM 컬럼 구성(실무)

- 권장 컬럼: 요구ID / 분류 / 내용 / 우선순위(필수·권장·선택) / 출처 조항 / 배점 매핑 /  
  제안서 대응 / 검증방법 / 계약·SLA 반영.  
- RTM은 요구사항을 요구정의 → 설계 → 개발 → 시험 → 인수까지 단계별로 연결해 커버리지를 가시화함.  
- 출처: How to Make a Requirements Traceability Matrix(ProjectManager) —  
  https://www.projectmanager.com/blog/requirements-traceability-matrix  
- 출처: How to Create and Use a Requirements Traceability Matrix(Jama Software) —  
  https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/how-to-create-and-use-a-requirements-traceability-matrix-rtm/

### 1-4. 본 RFP 추적성 근거(부록 A RTM)

- 본 RFP 부록 A는 요구ID·분류·우선순위·확인/검증 방법·배점 매핑·계약·SLA 반영 6개 컬럼으로 구성됨.  
- 대상 요구 16건: 업무 REQ-BIZ-01~05b(6건), 기술 REQ-TEC-01~06(6건), 운용 REQ-OPS-01~04(4건).  
- 예: REQ-BIZ-01 → 검증 "PoC 수신~담당자 통지 5분 이내 측정" → 배점 "기능 적합성" → 계약 "통지  
  SLA 준수율(6-1)"으로 요구부터 계약까지 한 행에 연결됨.  
- SRS의 S7 추적 매트릭스는 이 RFP 요구ID를 SRS 기능ID(FR)·인수기준(AC)과 1:1로 재연결함.

---

## 2. 운영 이행/전환(Transition·Knowledge Transfer)

### 2-1. 3단계 지식 이전(Shadow → 분담 → 독립)

- 지식 이전은 단계적(Shadow: 관찰 → 역할 분담: 공동 수행 → 독립: 인수 조직 단독 운영)으로 수행할 때  
  빅뱅 인계 대비 지식 격차를 크게 줄임(RFP작성가이드 케어 섹션 근거).  
- 인계 후 30/60/90일 리뷰, 전환 리스크 레지스터 운영이 모범사례로 제시됨.  
- 출처: The Complete Guide to Project Handover — Best Practice(Adapt Consulting) —  
  https://www.adaptconsultingcompany.com/2025/11/17/the-complete-guide-to-project-handover-purpose-process-risks-and-best-practice/  
- 출처: IT Outsourcing Transition Plan Guide(Opsio) —  
  https://opsiocloud.com/in/knowledge-base/it-outsourcing-transition-plan-guide/

### 2-2. 운영 런북(Runbook)

- 런북은 일상 운용·장애 대응 절차를 표준화한 문서로, 구축 기간 중 동시 작성할 때 가치가 가장 큼.  
- 통지 시스템 특성상 채널 전환·에스컬레이션·ETR 갱신 등 반복 절차를 런북으로 고정해 담당자 교체와  
  무관하게 동일 대응을 보장함.  
- 출처: 7 Reasons You Need a Managed Services Operational Runbook(Hitachi Solutions) —  
  https://global.hitachi-solutions.com/blog/why-you-need-an-it-operational-runbook/

### 2-3. 롤백(Rollback)·전환 실패 대비

- 전환(컷오버) 실패에 대비한 롤백 계획은 이행 요구의 필수 항목임. 데이터 이행 정합성·리허설·롤백  
  절차를 사전 정의하고, 병행 운영·컷오버 창을 확보함.  
- 롤백 발동 기준(트리거)과 원복 목표시간을 사전 합의해 판단 지연을 방지함.

---

## 3. Hypercare(안정화 지원)

- Hypercare는 컷오버 직후 프로젝트 실행 체계에서 운영 체계로 전환하는 안정화 기간으로, 격상된 지원·  
  집중 모니터링·신속 에스컬레이션·일일 거버넌스(스탠드업)를 운영함.  
- 통상 기간: go-live 후 2~4주(복잡도·연동·데이터 이행 규모에 따라 가변), 프로젝트팀 → 운영팀으로  
  4~6주에 걸쳐 책임을 점진 이관함.  
- 종료 기준(exit criteria): 심각 이슈 0건, 핵심 프로세스 정상 가동, SLA 충족, 운영팀이 추가 지원  
  없이 대다수 이슈 해결 가능 등 명확한 조건으로 종료를 판정함.  
- 출처: ERP Hypercare Checklist and Post-Go-Live Support Plan(Panorama Consulting) —  
  https://www.panorama-consulting.com/erp-hypercare-checklist/  
- 출처: What Is Hypercare? Benefits & Best Practices(Salesforce) — https://www.salesforce.com/service/hypercare/  
- 출처: Plan your support operations / Transition to support operations(Microsoft Dynamics 365) —  
  https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/transition-to-support-operations  
- 출처: Hypercare(Atlassian Success Central) —  
  https://success.atlassian.com/solution-paths/solution-guides/itsm-solution-delivery-guide/hypercare

### 본 RFP hypercare·운영 근거

- 본 RFP 일정: 안정화(hypercare) 2027-03-02 ~ 03월말, "SLA 적용"으로 명시(4장).  
- 본 RFP 운용 요구(2-3): 교육·연수(상담사·상황실 운영자·관리자), 이행(런북·3단계 지식 이전·hypercare  
  1개월 SLA·롤백 계획)을 명문화함.  
- REQ-OPS-03: 24x365 공동 대응 핫라인·분기 1회 합동 장애대응 모의훈련(결과 리포트 제출).  
- REQ-OPS-04: 월간 장애대응 리포트(통지 소요시간·MNO 복구 MTTR 관찰지표·재발률) + 정기 리뷰 미팅.

---

## 4. 용어·약어집 관리

- ISO/IEC/IEEE 29148 SRS 구성은 "용어 정의(Definitions)" 섹션을 표준 요소로 포함해 문서 내 용어  
  해석 일관성을 확보하도록 함(출처: 1-1의 29148 템플릿 링크).  
- 용어·약어집 관리 원칙: (1)단일 출처(문서 1곳에 집약 후 상호 참조), (2)측정 기준어의 시각 정의 명문화,  
  (3)변경 시 버전·일자 표기.  
- 본 RFP 약어표 근거: MNO/MVNO, NRC/MRC/TCO, NFR/TPS/P99, MTTR/ETR/RTO/RPO, HITL/PM/CR/SLA.  
- 본 RFP 시각 기준 정의(혼동 방지 핵심): "발생/수신" = MNO 이벤트 수신(Webhook 수신) 시각,  
  "인지" = 수신 시각으로 정렬. 통지 목표 "5분(종단)" ⊃ "1분(시스템 전송 구간, REQ-TEC-01)"의 상·하위  
  관계를 용어로 못 박아 정산 분쟁을 예방함.

---

## 5. S7 초안 반영 포인트(요약)

- 추적성: RFP 요구ID ↔ SRS 기능ID(FR) ↔ 인수기준(AC) 1:1 매핑을 강제하고, 미매핑·고아 항목 0건을  
  완전성 기준으로 정량화함(부록 A RTM 컬럼을 SRS용으로 확장).  
- 운영이행: 교육(3대상)·3단계 지식이전(Shadow→분담→독립)·hypercare 1개월(SLA 적용·종료기준)·런북·  
  롤백을 이행 요건으로 정의하고 REQ-OPS(핫라인·분기 훈련·월간 리포트)와 연결함.  
- 용어: 29148 용어 정의 섹션 준거 단일 용어집 + 시각 기준 정의(수신/인지, 5분⊃1분)를 명문화함.

---

## 6. 출처 목록(본 파일 인용 URL)

- ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html [RFP작성가이드 각주 재사용]  
- ISO/IEC/IEEE 29148 SRS Template — https://www.well-architected-guide.com/documents/iso-iec-ieee-29148-template/ [WebSearch 신규]  
- Perforce RTM — https://www.perforce.com/resources/alm/requirements-traceability-matrix [WebSearch 신규]  
- ReqView RTM — https://www.reqview.com/blog/requirements-traceability-matrix/ [WebSearch 신규]  
- ProjectManager RTM — https://www.projectmanager.com/blog/requirements-traceability-matrix [RFP작성가이드 각주 재사용]  
- Jama Software RTM — https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/how-to-create-and-use-a-requirements-traceability-matrix-rtm/ [RFP작성가이드 각주 재사용]  
- Adapt Consulting Project Handover — https://www.adaptconsultingcompany.com/2025/11/17/the-complete-guide-to-project-handover-purpose-process-risks-and-best-practice/ [RFP작성가이드 각주 재사용]  
- Opsio IT Outsourcing Transition Plan — https://opsiocloud.com/in/knowledge-base/it-outsourcing-transition-plan-guide/ [RFP작성가이드 각주 재사용]  
- Hitachi Solutions Operational Runbook — https://global.hitachi-solutions.com/blog/why-you-need-an-it-operational-runbook/ [RFP작성가이드 각주 재사용]  
- Panorama Consulting ERP Hypercare Checklist — https://www.panorama-consulting.com/erp-hypercare-checklist/ [WebSearch 신규]  
- Salesforce Hypercare — https://www.salesforce.com/service/hypercare/ [WebSearch 신규]  
- Microsoft Dynamics 365 Transition to Support Operations — https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/transition-to-support-operations [WebSearch 신규]  
- Atlassian Hypercare — https://success.atlassian.com/solution-paths/solution-guides/itsm-solution-delivery-guide/hypercare [WebSearch 신규]
