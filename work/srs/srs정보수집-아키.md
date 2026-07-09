# SRS 정보수집 — 아키 (S4 기술 요건 NFR · S5 데이터 요건)

> 목적: 「SRS 작성 가이드」 S4(기술 요건 NFR)·S5(데이터 요건) 초안 작성에 필요한 정보를  
> 본인 지식 + 신뢰성 있는 외부 자료(표준·법령 우선)로 정리함. 모든 외부 근거는 출처 URL을 표기함.  
> 근거 입력: 확정 RFP `work/rfp/RFP-MVNO장애보안사고_실시간통지_영향범위조회시스템.md`,  
> 구조 선례 `rfp/RFP작성가이드.md`(4. 기술 요구 작성), 아젠다 `work/srs/srs-agenda.md`.  
> 작성: 아키(솔루션 아키텍트) / 담당 섹션: S4·S5.

---

## 1. S4 기술 요건(비기능 요구 NFR) 정보수집

### 1-1. NFR 정량화 원칙 — [지표 + 목표값 + 측정조건] 3요소

- NFR(비기능 요구)은 "얼마나 잘"에 해당하며, 기능 요구(FR)와 달리 정량 임계값이 없으면 제안·검수·  
  정산에서 분쟁이 발생함. 따라서 모든 NFR은 **[지표(무엇을 잰다) + 목표값(임계값) + 측정조건(부하·기간·  
  방법)]** 3요소로 기술해야 SRS↔인수기준↔SLA 연계가 성립함.  
- "빠르다·안정적·안전함" 같은 정성 표현은 요구가 아님 — "측정할 수 없으면 요구사항이 아님"(아젠다 S0 원칙).  
- 3요소가 갖춰지면 인수 기준(AC)이 자동 도출됨. 예: 지표=조회 응답시간 / 목표=P99 3초 / 측정=피크  
  300 TPS 부하 → AC "피크 300 TPS 부하 시 조회 응답 P99 3초 이내".

### 1-2. ISO/IEC 25010 소프트웨어 품질 모델 매핑

- ISO/IEC 25010은 소프트웨어 제품 품질을 8~9개 품질특성으로 정의함(기능적합성·성능효율성·호환성·  
  사용성·신뢰성·보안성·유지보수성·이식성). NFR을 이 특성에 매핑하면 누락 없이 망라 가능함.  
- 본 RFP NFR↔품질특성 매핑(요지)  
  - 성능효율성(Performance efficiency): 통지 지연 1분, 조회 응답 평균2초·P99 3초, 300 TPS(REQ-TEC-01/02)  
  - 신뢰성(Reliability): 가용성 99.95%, 채널 자동 전환 30초, DR RTO 1h/RPO 15m(REQ-TEC-03, 장해대책)  
  - 보안성(Security): OAuth 2.0 인증·TLS 1.2+·위변조 방지 로그(REQ-TEC-04)  
- 출처: ISO/IEC 25010 System and software quality models (ISO) - https://www.iso.org/standard/35733.html  
- 출처: ISO/IEC 25010 Quality Model (arc42) - https://quality.arc42.org/standards/iso-25010

### 1-3. 성능·용량 지표 (응답시간·TPS·백분위수)

- **응답시간 백분위수(P99)**: 평균만으로는 꼬리 지연(tail latency)을 숨김. P99=하위 99% 요청이 만족하는  
  응답시간으로, "평균 2초 & P99 3초 동시 충족"은 평균과 최악 사용자 경험을 함께 통제하는 방식임.  
- **TPS(초당 처리건수)**: 용량 지표. Little's Law(동시사용자 N = TPS × 평균응답시간 R)로 목표 TPS를  
  산정·역산함. 예: 300 TPS × 2초 = 동시 처리 약 600건 수준의 자원 설계 근거가 됨.  
- 측정조건 명시가 필수 — "정상부하 시"와 "장애 피크 시"는 다른 목표가 적용됨(본 RFP는 장애 피크 부하 기준).  
- 출처: Little's Law 활용 성능 계산 (SKCC Engineering) - https://engineering-skcc.github.io/performancetest/LittlesLaw/

### 1-4. 가용성·이중화·재해복구(DR)

- **가용성 산식**: Availability = MTBF / (MTBF + MTTR). 나인(9) 하나가 늘 때마다 허용 다운타임이 약  
  1/10로 감소함.  
- **가용성 등급별 월 허용 다운타임**  
  - 99.9%(3-nines): 월 약 43.8분  
  - **99.95%: 월 약 21.6분**(본 RFP 목표 — 연 환산 약 4시간 22분)  
  - 99.99%(4-nines): 월 약 4.3분  
- 4-nines 이상은 수동 대응이 불가하여 네트워크·스토리지·DB·DNS까지 이중화 + 자동 페일오버가 전제됨.  
  본 RFP 99.95%도 "이중화 전제 하에 단일 컴포넌트 장애가 서비스 중단으로 전이되지 않음"을 가정함.  
- **가용성→이중화→SLA 배상 3단 연계**: 가용성 목표(정량)를 못 박고 이중화 방식(Active-Active/Standby)은  
  벤더 제안에 위임하면 더 나은 아키텍처를 유도함. 이 목표는 운용(REQ-OPS-01)·계약(6-1)과 수치 일치.  
- **DR(재해복구)**: RTO(목표 복구시간)·RPO(목표 복구시점)로 정량화. 본 RFP는 RTO 1시간·RPO 15분,  
  DR 전환 훈련 포함.  
- 출처: 다운타임·SLA 계산(three/four nines) (Hyperping) - https://hyperping.com/three-nines  
- 출처: 신뢰성 목표 정의 MTBF/MTTR (Microsoft Azure Well-Architected) - https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics  
- 출처: 서버 이중화와 가용성 99.9% vs 99.99% 차이 (스피디) - https://www.speedykorea.com/blog/server-redundancy-availability-sla-difference

### 1-5. 보안 — 인증·전송 암호화·위변조 방지

- **OAuth 2.0**: 제3자 애플리케이션이 자원 소유자를 대신해 HTTP 서비스에 제한적 접근을 얻는 인가  
  프레임워크(RFC 6749). MNO↔MVNO 시스템 간 API 접근 인증에 적용. 서버 간 연동은 client credentials  
  grant가 적합함.  
- **TLS(전송계층보안)**: 전송구간 암호화 표준. 본 RFP는 **TLS 1.2 이상** 요구. TLS 1.2=RFC 5246,  
  TLS 1.3=RFC 8446(2018, TLS 1.2 대비 핸드셰이크 단순화·전방향비밀성 강화). 신규 구축은 1.3 권장.  
- **접근통제 3단계**: 관리자 / 운영자 / 조회자 권한 분리(REQ-TEC-04). 최소권한 원칙 적용.  
- **위변조 방지 로그(무결성 검증)**: 통지 이력이 사후 SLA 준수율 산정·분쟁의 증거가 되므로 위·변조를  
  탐지·차단해야 함. 수단: 해시체인(각 로그에 직전 로그 해시 포함)·전자서명·WORM(Write Once Read Many)  
  저장. 무결성 검증은 로그 재계산 해시 대사로 확인함.  
- 출처: RFC 6749 The OAuth 2.0 Authorization Framework (IETF) - https://datatracker.ietf.org/doc/html/rfc6749  
- 출처: RFC 8446 TLS Protocol Version 1.3 (IETF) - https://datatracker.ietf.org/doc/html/rfc8446  
- 출처: RFC 5246 TLS Protocol Version 1.2 (IETF) - https://datatracker.ietf.org/doc/rfc5246/

### 1-6. 개인정보보호법 안전성 확보조치 기준

- 「개인정보의 안전성 확보조치 기준」(개인정보보호위원회 고시)은 접근권한 관리(최소권한·지체없는 말소),  
  접근통제, **개인정보 전송 시 암호화**, **접근기록 보관·위변조 방지**, 재해·재난 대비 등을 규정함.  
- 본 RFP 적용점: 영향범위 조회 시 접근권한 3단계·전송 암호화(TLS)·접근기록 보관은 이 고시의 직접 근거임.  
- 출처: 개인정보의 안전성 확보조치 기준(행정규칙) (국가법령정보센터) - https://www.law.go.kr/LSW//admRulInfoP.do?admRulSeq=2100000265956&chrClsCd=010201  
- 출처: 개인정보의 안전성 확보조치 기준 안내서(2024.10) (CISP) - https://www.cisp.or.kr/13097/

---

## 2. S5 데이터 요건 정보수집

### 2-1. 데이터 모델·수집

- 본 시스템 핵심 데이터 도메인(RFP 요구에서 도출)  
  - 사고 이벤트(MNO 수신): 이벤트ID·수신시각·심각도(긴급/높음/보통)·사고유형·영향 대상 원천정보  
  - 영향범위(집계): 영향 가입자 규모·지역·서비스 범위 — **집계·범위 단위**로만 산출(개인 식별 배제)  
  - 통지 이력: 통지ID·채널(API/이메일/SMS)·발송시각·수신확인·SLA 판정 결과  
  - 복구정보(ETR): 복구 진행률·예상 복구시각, 15분 주기 갱신 이력(연속 조회 가능)  
  - 사고 리포트: 통지 타임라인·영향범위·MTTR(관찰 지표)·재발방지대책  
  - 담당자 계정: 통지 대상 500 계정 이상(개통 1년차), 권한 등급  
  - AI 학습 데이터: 과거 사고 전수(REQ-BIZ-05a 백테스트·재학습용)  
- **수집 방식**: MNO 이벤트는 Webhook 푸시 수신이 1차 경로(REQ-TEC-01), 조회는 API. "발생/수신" 시각  
  기준은 **MNO 이벤트(Webhook) 수신 시각**으로 정렬함(RFP 2장 시각 기준 정의).

### 2-2. 보관 기간·무결성

- **보관 기간**: 통지 이력 **3년 이상**(RFP Capacity표). 사후 SLA 준수율 산정·감사 근거로 사용됨.  
- **무결성(위변조 방지)**: 통지 이력은 위변조 방지 로그로 보관(REQ-TEC-04). 해시체인·전자서명·WORM 등으로  
  사후 변경 불가를 보장하고, 무결성 검증(해시 대사)으로 확인함.  
- 보관 만료 데이터는 파기 정책 필요 — 개인정보 포함 데이터는 보유기간 경과 시 지체없이 파기(안전성 확보조치).

### 2-3. 개인정보 취급 — 집계·범위 단위·가명·암호화

- **핵심 원칙**: 영향범위 조회 결과에는 **개인 식별자를 포함하지 않고, 집계·범위 단위로만 제공**함  
  (RFP 2-2 보안·규제). 예: "서울 강남구 LTE 가입자 약 12,000명 영향"처럼 개인 특정 불가 형태.  
- **법적 근거**: 통계작성 등 목적의 가명정보 처리, 제3자 제공 시 특정 개인을 알아볼 수 있는 정보 포함  
  금지(개인정보 보호법 가명정보 조항). 집계·범위 단위 제공은 개인 식별 최소화 원칙에 부합함.  
- **암호화·접근통제**: 개인정보 전송 시 암호화(TLS), 접근권한 최소화·접근기록 보관(안전성 확보조치).  
- 출처: 개인정보 보호법 (국가법령정보센터) - https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357&ancYnChk=0  
- 출처: 가명정보의 처리 등 (찾기쉬운 생활법령정보) - https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1257&ccfNo=2&cciNo=4&cnpClsNo=1  
- 출처: 가명처리·가명정보 결합제도 (개인정보보호위원회) - https://www.pipc.go.kr/np/default/page.do?mCode=D040010000

### 2-4. 연동 데이터 규격 (Webhook / API)

- **Webhook(수신)**: MNO→시스템 이벤트 푸시. 규격 정의 항목 — 엔드포인트·인증(OAuth 2.0)·페이로드  
  스키마(이벤트ID·수신시각·심각도·사고유형·영향 원천)·재전송(retry)·중복 제거·서명 검증.  
- **API(조회/제공)**: 영향범위·복구정보·통지이력 조회. 규격 항목 — 인증(OAuth 2.0)·전송(TLS 1.2+)·요청/  
  응답 스키마·오류 코드·응답시간 목표(조회 P99 3초).  
- **시각 동기화**: 이벤트 타임스탬프는 통지 SLA(수신~통지 1분) 자동 측정의 기준이므로 시각 정합성(NTP  
  동기 등)이 데이터 요건에 포함됨.  
- **다중 채널 전송 데이터**: API+이메일+SMS 다중화(REQ-TEC-03), 채널별 전송 상태·전환 이력 기록.

---

## 3. 본 RFP 근거 매핑 (S4·S5 ↔ REQ-TEC / 데이터 요건)

| SRS 섹션 | 근거 요구ID / RFP 항목 | 핵심 수치·기준 |
|----------|------------------------|----------------|
| S4 성능 | REQ-TEC-01 | 수신~통지 1분 이내, 전송 성공률 99.9% 이상(월·피크) |
| S4 성능 | REQ-TEC-02 | 300 TPS 이상, 평균 2초 & P99 3초(동시 충족, 피크 부하) |
| S4 이중화 | REQ-TEC-03 | 채널 자동 전환 30초 이내(강제 차단 시험) |
| S4 보안 | REQ-TEC-04 | OAuth 2.0, TLS 1.2+, 위변조 방지 로그(무결성 검증) |
| S4 인프라 | REQ-TEC-06 | 배포형태 벤더 제안, MNO 연동 전용선/VPN, 네트워크·DB·DNS 이중화 |
| S4 가용성·DR | 장해대책·Capacity표·REQ-OPS-01 | 가용성 99.95%/월(약 21.6분), DR RTO 1h/RPO 15m |
| S5 데이터 모델 | REQ-BIZ-02/03/04 | 영향범위(집계)·복구정보(15분 갱신)·사고 리포트 |
| S5 보관·무결성 | Capacity표·REQ-TEC-04 | 통지 이력 3년 이상, 위변조 방지 로그 |
| S5 개인정보 | 2-2 보안·규제 | 집계·범위 단위 제공, 개인 식별자 미포함, 전송 암호화 |
| S5 연동 규격 | REQ-TEC-01/06 | Webhook/API, OAuth 2.0 인증, TLS, 시각 정합성 |

---

## 참고자료 출처 목록

### 표준·품질 모델·성능

- ISO/IEC 25010 System and software quality models (ISO) - https://www.iso.org/standard/35733.html  
- ISO/IEC 25010 Quality Model (arc42) - https://quality.arc42.org/standards/iso-25010  
- Little's Law 활용 성능 계산 (SKCC Engineering) - https://engineering-skcc.github.io/performancetest/LittlesLaw/

### 가용성·이중화·DR

- 다운타임·SLA 계산 three/four nines (Hyperping) - https://hyperping.com/three-nines  
- 신뢰성 목표 정의 MTBF/MTTR (Microsoft Azure Well-Architected) - https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics  
- 서버 이중화와 가용성 99.9% vs 99.99% 차이 (스피디) - https://www.speedykorea.com/blog/server-redundancy-availability-sla-difference

### 보안 (인증·전송 암호화)

- RFC 6749 The OAuth 2.0 Authorization Framework (IETF) - https://datatracker.ietf.org/doc/html/rfc6749  
- RFC 8446 TLS Protocol Version 1.3 (IETF) - https://datatracker.ietf.org/doc/html/rfc8446  
- RFC 5246 TLS Protocol Version 1.2 (IETF) - https://datatracker.ietf.org/doc/rfc5246/

### 개인정보보호 법령

- 개인정보 보호법 (국가법령정보센터) - https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357&ancYnChk=0  
- 개인정보의 안전성 확보조치 기준(행정규칙) (국가법령정보센터) - https://www.law.go.kr/LSW//admRulInfoP.do?admRulSeq=2100000265956&chrClsCd=010201  
- 개인정보의 안전성 확보조치 기준 안내서(2024.10) (CISP) - https://www.cisp.or.kr/13097/  
- 가명정보의 처리 등 (찾기쉬운 생활법령정보) - https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1257&ccfNo=2&cciNo=4&cnpClsNo=1  
- 가명처리·가명정보 결합제도 (개인정보보호위원회) - https://www.pipc.go.kr/np/default/page.do?mCode=D040010000
