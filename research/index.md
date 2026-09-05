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

  <div class="research-grid research-grid-3">
    <div class="research-card">
      <img class="research-card-img" src="{{ "/images/proj-dbs.jpg" | relative_url }}" alt="Bio and healthcare systems modeling">
      <div class="research-card-body">
        <div class="research-card-number">01</div>
        <h2>Bio &amp; Healthcare Systems Modeling</h2>
        <p>Simulation and mathematical modeling of real bio/healthcare systems to
          forecast outcomes and evaluate decisions.</p>
        <ul class="research-card-topics">
          <li><strong>Infectious disease</strong> — HPC-based agent-based simulation for
            disease-spread forecasting and public-health policy evaluation.</li>
          <li><strong>Clinical trials</strong> — Pharmacokinetic modeling and clinical-trial
            data analysis (e.g., HIV PrEP adherence), in collaboration with Gilead Sciences.</li>
          <li><strong>Bioprocess</strong> — Digital-twin models of biomanufacturing
            (monoclonal antibody production) for yield optimization under uncertainty.</li>
        </ul>
      </div>
    </div>
    <div class="research-card">
      <img class="research-card-img" src="{{ "/images/proj-abm.jpg" | relative_url }}" alt="Simulation methodology">
      <div class="research-card-body">
        <div class="research-card-number">02</div>
        <h2>Simulation Methodology</h2>
        <p>New ways to build simulation models that are more realistic, more
          data-driven, and cheaper to run.</p>
        <ul class="research-card-topics">
          <li><strong>LLM-persona agents</strong> — Agent-based models whose agents are driven
            by LLM personas, and LLM-based synthetic population generation.</li>
          <li><strong>Surrogate &amp; mathematical modeling</strong> — Approximate models for
            systems too complex to simulate directly.</li>
        </ul>
      </div>
    </div>
    <div class="research-card">
      <img class="research-card-img" src="{{ "/images/proj-xcal.jpg" | relative_url }}" alt="Simulation optimization and explainable AI">
      <div class="research-card-body">
        <div class="research-card-number">03</div>
        <h2>Simulation Optimization &amp; Explainable AI</h2>
        <p>Turning simulation models into decisions: fitting them to data and
          optimizing the policies they inform.</p>
        <ul class="research-card-topics">
          <li><strong>Calibration</strong> — Algorithms for representative parameter
            calibration of complex simulation models.</li>
          <li><strong>Explainable AI (XAI)</strong> — Explaining calibrated models and
            post-calibration analysis for policy evaluation.</li>
          <li><strong>Global optimization</strong> — Simulation optimization under
            uncertainty, machine learning, and digital twins.</li>
        </ul>
      </div>
    </div>
  </div>

  <nav class="research-tabs" aria-label="Research sections">
    <a href="#publication">Publication</a>
    <a href="#projects">Projects</a>
    <a href="#presentation">Presentation</a>
    <a href="#awards">Awards</a>
  </nav>

</div>

## Publication
{: #publication}

### Under review & in preparation

{% include list.html data="citations" component="citation" filter="group == 'review'" %}

### Journal papers

{% include list.html data="citations" component="citation" filter="group == 'journal'" %}

### Conference proceedings

{% include list.html data="citations" component="citation" filter="group == 'proceedings'" %}

## Projects
{: #projects}

- **2026 – 2029 · PI** — 가상 임상시험을 활용한 감염병 약물 유효성 예측 및 임상 프로토콜 최적화 (Digital Twin-based Virtual Clinical Trial for Infectious Diseases). *한국연구재단 (NRF)*
- **2026 – 2027 · PI** — 공공데이터를 활용한 에이전트 기반 시뮬레이션 연구. *인천대학교 (INU)*
- **2025 – 2027 · PI** — 데이터 기반 시뮬레이션 및 모델링 기법 연구. *인천대학교 (INU)*

## Presentation
{: #presentation}

### Invited talks

- **2026.02** — Data-driven approaches to support clinical trials. *Korea Research Institute of Bioscience & Biotechnology (KRIBB).* **Lee, S.**
- **2026.01** — Data-driven approaches to support clinical trials. *Seoul National University.* **Lee, S.**

### Conference presentations

- **2026** — Discrete-Event Simulation Modeling of​ Monoclonal Antibody Production under Uncertainty​. *대한산업공학회 (Korean Institute of
Industrial Engineers), Gyeongju. <u>Kang, H.</u>, **Lee, S.**.
- **2025** — Dried blood spots measurements as indicator of HIV PrEP adherence and protection among MSM in HPTN067. *Epidemics, San Diego, CA.* **Lee, S.**, Dimitrov, D., Anderson, P., Moore, M.
- **2025** — Optimizing Vaccination Campaign Considering Societal Characteristics. *대한산업공학회 (Korean Institute of
Industrial Engineers), Daejeon.* **Lee, S.**, Zabinsky, Z.B., Liu, S.

## Awards
{: #awards}

Lab awards and honors will be listed here.
