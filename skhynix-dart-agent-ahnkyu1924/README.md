# SK하이닉스 OpenDART 재무분석 Agent
대상: SK하이닉스 / DART 고유번호 `00164779` / 종목코드 `000660`

## API 키
OpenDART에서 키를 발급한 뒤 GitHub Repository → Settings → Secrets and variables → Actions → New repository secret 에서 `DART_API_KEY` 이름으로 저장하세요. 키를 코드에 직접 넣지 마세요.

## Pages
Settings → Pages → Build and deployment → Source → GitHub Actions.
그 뒤 Actions → Update DART and deploy dashboard → Run workflow.

## 자동화
매일 07:15 KST에 공시 목록과 최근 5개 사업연도 연결 전체재무제표를 다시 받아 `data/`와 `docs/index.html`을 갱신합니다.

## 분석
첨부 가이드에 맞춰 금액과 비율을 함께 표시하고, ROA/ROE/총자산회전율은 평균 잔액을 사용할 수 있을 때 계산합니다. 계정/주석/시장가격이 추가로 필요한 CAPEX·FCF·EBITDA·ROIC·CCC·PER/PBR 등은 근거 없이 추정하지 않습니다.

## 로컬 실행
`pip install -r requirements.txt` → `.env.example`을 `.env`로 복사 → API 키 입력 → `python run.py`
