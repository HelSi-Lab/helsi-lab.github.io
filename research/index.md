---
title: Research
nav:
  order: 2
  tooltip: Research areas, publications, projects, and talks
---

{% include section.html %}

<div class="research-page">

  <div class="research-hero">
    <p class="research-eyebrow">Research</p>
    <h1>Research Areas</h1>
    <p class="research-lead">
      HelSi Lab develops simulation, optimization, and digital-twin methods to
      support decision-making in complex bio/healthcare systems.
    </p>
  </div>

  <div class="research-areas">
    <div class="research-area-row">
      <div class="research-area-number">01</div>
      <div class="research-area-text">
        <h2>Healthcare Systems &amp; Policy Modeling</h2>
        <p>Simulation and mathematical modeling for disease forecasting, health
          policy evaluation, and resource allocation in healthcare systems.</p>
      </div>
      <div class="research-area-img"><img src="images/proj-abm.jpg" alt="Agent-based disease model"></div>
    </div>

    <div class="research-area-row">
      <div class="research-area-number">02</div>
      <div class="research-area-text">
        <h2>Clinical Trial Analytics</h2>
        <p>Data-driven analysis of clinical trials using pharmacokinetic models,
          simulation, and real-world behavioral data.</p>
      </div>
      <div class="research-area-img"><img src="images/proj-dbs.jpg" alt="DBS clinical trial pipeline"></div>
    </div>

    <div class="research-area-row">
      <div class="research-area-number">03</div>
      <div class="research-area-text">
        <h2>Digital Twin &amp; Biomanufacturing</h2>
        <p>Digital-twin models for bio/healthcare operations, including virtual
          clinical trials, biomanufacturing processes, and batch optimization.</p>
      </div>
      <div class="research-area-img"><img src="images/proj-biomfg.jpg" alt="Bioprocess digital twin"></div>
    </div>

    <div class="research-area-row">
      <div class="research-area-number">04</div>
      <div class="research-area-text">
        <h2>Simulation Optimization &amp; Explainable AI</h2>
        <p>Optimization under uncertainty, surrogate modeling, parameter
          calibration, and explainable AI for complex simulation models.</p>
      </div>
      <div class="research-area-img"><img src="images/proj-xcal.jpg" alt="Calibration analysis"></div>
    </div>
  </div>

  <div class="research-list" style="margin-bottom:2.5rem">
    <div class="research-list-item">
      <strong>2026–2029</strong>
      <span>가상 임상시험을 활용한 감염병 약물 유효성 예측 및 임상 프로토콜 최적화 (Digital Twin-based Virtual Clinical Trial for Infectious Diseases: Effectiveness Prediction and Protocol Optimization). <em>National Research Foundation of Korea (NRF), PI.</em></span>
    </div>
    <div class="research-list-item">
      <strong>2026–2027</strong>
      <span>공공데이터를 활용한 에이전트 기반 시뮬레이션 연구. <em>Incheon National University (INU), PI.</em></span>
    </div>
    <div class="research-list-item">
      <strong>2025–2027</strong>
      <span>데이터 기반 시뮬레이션 및 모델링 기법 연구. <em>Incheon National University (INU), PI.</em></span>
    </div>
  </div>

  <nav class="research-tabs" aria-label="Research sections">
    <a href="#publication">Publication</a>
    <a href="#presentation">Presentation</a>
    <a href="#awards">Awards</a>
  </nav>

  <section id="publication" class="research-section">
    <h2>Publication</h2>
    <h3>Under review &amp; in preparation</h3>
    {% include list.html data="citations" component="citation" filter="d.group == 'review'" %}

    <h3>Journal papers</h3>
    {% include list.html data="citations" component="citation" filter="d.group == 'journal'" %}

    <h3>Peer-reviewed conference proceedings</h3>
    {% include list.html data="citations" component="citation" filter="d.group == 'proceedings'" %}
  </section>

  <section id="presentation" class="research-section">
    <h2>Presentation</h2>
    <h3>Invited talks</h3>
    {% include list.html data="citations" component="citation" filter="d.group == 'talk'" %}

    <h3>Conference presentations</h3>
    {% include list.html data="citations" component="citation" filter="d.group == 'oral'" %}

    <h3>Posters</h3>
    {% include list.html data="citations" component="citation" filter="d.group == 'poster'" %}

  </section>

  <section id="awards" class="research-section">
    <h2>Awards</h2>
    <!-- <div class="research-list">
      <div class="research-list-item">
        <strong>2020 &amp; 2021</strong>
        <span>Lee B. Lusted Prize Finalist. <em>Society for Medical Decision Making.</em></span>
      </div>
    </div> -->
  </section>

</div>