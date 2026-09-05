---
title: Research
nav:
  order: 2
  tooltip: Research outline and selected topics
header-style: urban
header-dark: false
---

<div class="research-reference-page">
  <nav class="research-subnav" aria-label="Research navigation">
    <a href="#area" class="active" data-research-tab="area" role="tab" aria-selected="true">Research Area <span>· 연구 분야</span></a>
    <a href="#international" data-research-tab="international" role="tab" aria-selected="false">International Articles <span>· 국제학술지</span></a>
    <a href="#korean" data-research-tab="korean" role="tab" aria-selected="false">Korean Articles <span>· 국내학술지</span></a>
    <a href="#conference" data-research-tab="conference" role="tab" aria-selected="false">Conference <span>· 학술대회</span></a>
    <a href="#projects" data-research-tab="projects" role="tab" aria-selected="false">Projects <span>· 연구과제</span></a>
  </nav>

  <section class="research-reference-content" id="research-area" data-research-panel="area" role="tabpanel">
    <h1>Research Area <span>· 연구 분야</span></h1>

    <article id="healthcare-systems" class="research-reference-item">
      <h2>Health Policy &amp; Disease Modeling <span>· 보건정책 및 질병 모델링</span></h2>
      <div class="research-reference-body">
        <figure><img src="{{ '/images/proj-abm.png' | relative_url }}" alt="Agent-based simulation of infectious disease policy"></figure>
        <div>
          <h3>Developing simulation models for vaccination, prevention, and infectious-disease policy</h3>
          <p>백신, 예방, 감염병 대응 정책을 위한 시뮬레이션 모델을 개발</p>
          <h3>Examining how population behavior and intervention strategies shape health outcomes</h3>
          <p>인구집단의 행동과 개입 전략이 건강 결과에 미치는 영향을 분석</p>
        </div>
      </div>
    </article>

    <article id="clinical-trials" class="research-reference-item">
      <h2>Clinical Trials &amp; Pharmacometrics <span>· 임상시험 및 약리계량학</span></h2>
      <div class="research-reference-body">
        <figure><img src="{{ '/images/proj-dbs.jpg' | relative_url }}" alt="Pharmacokinetic modeling of clinical-trial data"></figure>
        <div>
          <h3>Developing simulation-based evidence for clinical-trial design and treatment evaluation</h3>
          <p>임상시험 설계와 치료 효과 평가를 위한 시뮬레이션 기반 근거를 개발</p>
          <h3>Connecting pharmacometric models and virtual trials to practical healthcare decisions</h3>
          <p>약리계량학 모델과 가상 임상시험을 실제 헬스케어 의사결정에 연결</p>
        </div>
      </div>
    </article>

    <article id="biomanufacturing" class="research-reference-item">
      <h2>Biomanufacturing Digital Twins <span>· 바이오공정 디지털 트윈</span></h2>
      <div class="research-reference-body">
        <figure><img src="{{ '/images/proj-biomfg.png' | relative_url }}" alt="Discrete-event simulation of a biomanufacturing process"></figure>
        <div>
          <h3>Making biopharmaceutical production systems visible, testable, and more resilient</h3>
          <p>바이오의약품 생산 시스템을 가시화하고, 가상 환경에서 검증하며, 불확실성에 강한 공정을 설계</p>
          <h3>Improving yield and throughput through process simulation and scheduling optimization</h3>
          <p>공정 시뮬레이션과 스케줄링 최적화를 통해 수율과 생산성을 향상</p>
        </div>
      </div>
    </article>

    <article id="simulation-methods" class="research-reference-item">
      <h2>Simulation Research <span>· 시뮬레이션 연구</span></h2>
      <div class="research-reference-body">
        <figure><img src="{{ '/images/proj-xcal.png' | relative_url }}" alt="Representative calibration and explainable AI output"></figure>
        <div>
          <h3>Agent-based modeling methods</h3>
          <p>에이전트 기반 모델의 설계, 가상 인구 구성, 상호작용 및 개입 전략 분석 방법론을 연구</p>
          <h3>Calibration, optimization, and explainable analysis</h3>
          <p>복잡한 시뮬레이션 모델의 보정·최적화와 결과 해석을 위한 설명가능 분석 방법론을 개발</p>
        </div>
      </div>
    </article>
  </section>

  <section class="research-output-panel" data-research-panel="international" role="tabpanel" hidden>
    <h1>International Articles <span>· 국제학술지</span></h1>
    <h2>Journal Articles <span>· 학술지 논문</span></h2>
    {% include research-output-list.html group="journal" %}
    <h2>Forthcoming and Ongoing Work <span>· 게재 예정 및 진행 중인 연구</span></h2>
    {% include research-output-list.html group="review" %}
  </section>

  <section class="research-output-panel" data-research-panel="korean" role="tabpanel" hidden>
    <h1>Korean Articles <span>· 국내학술지</span></h1>
    <p class="research-empty">국내학술지 논문을 준비하고 있습니다.</p>
  </section>

  <section class="research-output-panel" data-research-panel="conference" role="tabpanel" hidden>
    <h1>Conference <span>· 학술대회</span></h1>
    <h2>WSC Proceedings <span>· Winter Simulation Conference 논문</span></h2>
    {% include research-output-list.html group="proceedings" %}
    <h2>Invited Talks <span>· 초청 강연</span></h2>
    {% include research-output-list.html group="talk" %}
    <h2>Oral Presentations <span>· 구두 발표</span></h2>
    {% include research-output-list.html group="oral" %}
    <h2>Poster Presentations <span>· 포스터 발표</span></h2>
    {% include research-output-list.html group="poster" %}
  </section>

  <section class="research-output-panel" data-research-panel="projects" role="tabpanel" hidden>
    <h1>Projects <span>· 연구과제</span></h1>
    {% include research-output-list.html group="project" %}
  </section>
</div>
