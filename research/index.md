---
title: Research
nav:
  order: 2
  tooltip: Research areas, publications, projects, and talks
  dropdown:
    - title: Research areas
      link: research/#areas
    - title: Publications
      link: research/#publication
    - title: Projects
      link: research/#projects
    - title: Presentations
      link: research/#presentation
    - title: Awards
      link: research/#awards
---

{% include section.html %}

<div class="research-page">

  <div class="research-hero" id="areas">
    <p class="research-eyebrow">Research</p>
    <h1>Research Areas</h1>
    <p class="research-lead">
      HelSi Lab develops simulation, optimization, and digital-twin methods to
      support decision-making in complex bio/healthcare systems. Our work spans
      three areas — click each to see what we do.
    </p>
  </div>

  <div class="research-areas">

    <details class="research-area" open>
      <summary>
        <span class="research-area-number">01</span>
        <span class="research-area-title">Bio &amp; Healthcare Systems</span>
        <span class="research-area-sub">Infectious disease · Clinical trials · Biomanufacturing</span>
      </summary>
      <div class="research-area-body">
        <p class="research-area-intro">Where we apply our models: real bio and healthcare systems
          in which decisions must be made under uncertainty.</p>

        <div class="research-topic">
          <img src="{{ "/images/proj-abm.jpg" | relative_url }}" alt="Agent-based model of COVID-19 policy">
          <div>
            <h3>Infectious Disease &amp; Public Health Policy</h3>
            <p>HPC-based agent-based simulation of disease spread (COVID-19, measles,
              seasonal influenza) to forecast outbreaks and evaluate public-health
              interventions — vaccination campaigns, non-pharmaceutical interventions,
              and resource allocation — including how opinion dynamics shape vaccine uptake.</p>
          </div>
        </div>

        <div class="research-topic">
          <img src="{{ "/images/proj-dbs.jpg" | relative_url }}" alt="Pharmacokinetic modeling of HIV PrEP adherence">
          <div>
            <h3>Clinical Trials &amp; Pharmacometrics</h3>
            <p>Pharmacokinetic and mathematical modeling of clinical-trial data to estimate
              drug adherence, protection, and efficacy — e.g., HIV pre-exposure prophylaxis
              (dried blood spot biomarkers, long-acting injectables) — and digital-twin-based
              <em>virtual clinical trials</em> for infectious diseases (NRF, 2026–2029),
              in collaboration with Gilead Sciences.</p>
          </div>
        </div>

        <div class="research-topic">
          <img src="{{ "/images/proj-biomfg.jpg" | relative_url }}" alt="Biomanufacturing process model">
          <div>
            <h3>Biomanufacturing</h3>
            <p>Discrete-event simulation of biopharmaceutical production (e.g., monoclonal
              antibodies) and batch-scheduling optimization to improve yield and
              throughput under process uncertainty.</p>
          </div>
        </div>
      </div>
    </details>

    <details class="research-area">
      <summary>
        <span class="research-area-number">02</span>
        <span class="research-area-title">Agent-Based Modeling &amp; Digital Twins</span>
        <span class="research-area-sub">LLM-persona agents · Synthetic populations · Digital-twin frameworks</span>
      </summary>
      <div class="research-area-body">
        <p class="research-area-intro">How we build models: making agent-based simulations
          more realistic, more data-driven, and reusable across problems.</p>

        <div class="research-topic">
          <div class="research-topic-placeholder">Figure coming soon</div>
          <div>
            <h3>LLM-Persona Agents &amp; Synthetic Populations</h3>
            <p>Agent-based models whose agents are driven by LLM personas, and algorithms
              for building synthetic populations from public data (e.g., household assignment
              using the NVIDIA Persona Korea synthetic population) for general-purpose ABM.</p>
          </div>
        </div>

        <div class="research-topic">
          <div class="research-topic-placeholder">Figure coming soon</div>
          <div>
            <h3>Digital-Twin Frameworks &amp; Surrogate Modeling</h3>
            <p>Digital twins of healthcare and bioprocess systems, and mathematical or
              surrogate models that approximate simulations too expensive to run directly.</p>
          </div>
        </div>
      </div>
    </details>

    <details class="research-area">
      <summary>
        <span class="research-area-number">03</span>
        <span class="research-area-title">Calibration, Simulation Optimization &amp; Explainable AI</span>
        <span class="research-area-sub">Representative calibration · Post-calibration XAI · Optimization under uncertainty</span>
      </summary>
      <div class="research-area-body">
        <p class="research-area-intro">How we make models trustworthy and actionable: fitting
          them to data, explaining what they learned, and optimizing the decisions they inform.</p>

        <div class="research-topic">
          <img src="{{ "/images/proj-xcal.jpg" | relative_url }}" alt="Calibration output">
          <div>
            <h3>Representative Calibration &amp; Explainable AI</h3>
            <p>Calibration algorithms that use black-box optimization and clustering to find
              <em>representative</em> parameter sets for complex simulation models, and
              explainable post-calibration analysis that interprets how calibrated parameters
              drive policy outcomes.</p>
          </div>
        </div>

        <div class="research-topic">
          <div class="research-topic-placeholder">Figure coming soon</div>
          <div>
            <h3>Simulation Optimization under Uncertainty</h3>
            <p>Global optimization and machine learning on top of simulation models to find
              robust policies — e.g., optimal vaccination campaign strategies that account for
              societal characteristics and fairness.</p>
          </div>
        </div>
      </div>
    </details>

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
