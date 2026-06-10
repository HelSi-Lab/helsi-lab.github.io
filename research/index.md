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
    {% include list.html data="citations" component="citation" filters="group: review" %}

    <h3>Journal papers</h3>
    {% include list.html data="citations" component="citation" filters="group: journal" %}

    <h3>Conference proceedings</h3>
    {% include list.html data="citations" component="citation" filters="group: proceedings" %}

  </section>

  <section id="presentation" class="research-section">
    <h2>Presentation</h2>

    <h3>Invited talks</h3>
    <div class="research-list">
      <div class="research-list-item"><strong>2026.02</strong><span>Data-driven approaches to support clinical trials. <em>Korea Research Institute of Bioscience &amp; Biotechnology (KRIBB).</em></span></div>
      <div class="research-list-item"><strong>2026.01</strong><span>Data-driven approaches to support clinical trials. <em>Seoul National University (SNU).</em></span></div>
      <div class="research-list-item"><strong>2020.09</strong><span>Introduction to agent-based modelling. <em>Industrial &amp; Mathematical Data Analytics Research Center, SNU.</em></span></div>
    </div>

    <h3>Conference presentations</h3>
    <div class="research-list compact">
      <div class="research-list-item"><strong>2025</strong><span>Dried blood spots measurements as indicator of HIV PrEP adherence and protection among MSM in HPTN067. <em>Epidemics, San Diego, CA.</em></span></div>
      <div class="research-list-item"><strong>2025</strong><span>Optimizing Vaccination Campaign Considering Societal Characteristics. <em>Korean Institute of Industrial Engineers, Daejeon.</em></span></div>
      <div class="research-list-item"><strong>2024</strong><span>Optimizing vaccination campaign strategies considering societal characteristics. <em>INFORMS Annual Meeting, Seattle, WA.</em></span></div>
      <div class="research-list-item"><strong>2023</strong><span>Optimal vaccine promotion campaigns considering disease transmission and opinion propagation with fairness. <em>INFORMS Annual Meeting, Phoenix, AZ.</em></span></div>
      <div class="research-list-item"><strong>2023</strong><span>Optimal budget allocation to vaccine promotion campaigns considering disease transmission and opinion propagation. <em>INFORMS Healthcare Conference, Toronto, Canada.</em></span></div>
      <div class="research-list-item"><strong>2023</strong><span>Advancing simulation methodology for identifying optimal healthcare policy during COVID-19 pandemic. <em>IDM Annual Symposium, Seattle, WA.</em></span></div>
      <div class="research-list-item"><strong>2022</strong><span>Optimal vaccination campaigns under opinion and physical networks. <em>INFORMS Annual Meeting, Indianapolis, IN.</em></span></div>
      <div class="research-list-item"><strong>2021</strong><span>Impact of vaccination and relaxation of NPIs on controlling COVID-19 using agent-based simulation. <em>43rd SMDM Annual Meeting.</em> <strong style="color:var(--helsi-gold)">Finalist, Lee B. Lusted Award</strong></span></div>
      <div class="research-list-item"><strong>2021</strong><span>Using agent-based simulation to optimize vaccination schedules and NPIs to control COVID-19 outbreaks. <em>INFORMS Annual Meeting, Anaheim, CA.</em></span></div>
      <div class="research-list-item"><strong>2021</strong><span>Using agent-based simulation to analyze how to achieve herd immunity to SARS-CoV-2 with vaccination and NPIs. <em>INFORMS Healthcare Conference.</em></span></div>
      <div class="research-list-item"><strong>2020</strong><span>Impact of population health interventions for a measles outbreak in a low vaccination area. <em>INFORMS Annual Meeting.</em></span></div>
      <div class="research-list-item"><strong>2020</strong><span>Agent-based simulation of COVID-19 society reopening plans in an urban setting. <em>INFORMS Annual Meeting.</em></span></div>
      <div class="research-list-item"><strong>2020</strong><span>Agent-based simulation study of reopening scenarios for COVID-19 in a large urban area. <em>42nd SMDM Annual Meeting.</em> <strong style="color:var(--helsi-gold)">Finalist, Lee B. Lusted Award</strong></span></div>
    </div>

    <h3>Posters</h3>
    <div class="research-list compact">
      <div class="research-list-item"><strong>2022</strong><span>Optimal vaccination campaigns under disease transmission and opinion propagation. <em>44th SMDM Annual Meeting, Seattle, WA.</em></span></div>
      <div class="research-list-item"><strong>2021</strong><span>Optimizing COVID-19 vaccine prioritization policies with NPIs using agent-based simulation. <em>MIDAS Network Annual Meeting.</em></span></div>
      <!-- <div class="research-list-item"><strong>2018</strong><span>Dimensionality reduction model for common eligibility criteria in EMR: a pilot study. <em>Korean Society of Medical Informatics Spring Conference, Seoul.</em></span></div> -->
    </div>
  </section>

  <section id="awards" class="research-section">
    <h2>Awards</h2>
  </section>

</div>