---
title: Research
nav:
  order: 2
  tooltip: Research areas, publications, projects, and talks
  dropdown:
    - title: Research Outline
      link: research/#outline
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

  <div class="research-hero" id="outline">
    <p class="research-eyebrow">Research</p>
    <h1>Research Outline</h1>
    <p class="research-lead">
      HelSi Lab develops simulation, optimization, and digital-twin methods to
      support decision-making in complex bio/healthcare systems. We model real
      systems, simulate how they behave under uncertainty, and optimize the
      decisions that shape them.
    </p>
  </div>

  <div class="research-outline">
    <div class="research-outline-col">
      <h2>Bio &amp; Healthcare Systems</h2>
      <p>Infectious disease &amp; public-health policy · Clinical trials &amp; pharmacometrics · Biomanufacturing</p>
    </div>
    <div class="research-outline-col">
      <h2>Simulation &amp; Modeling</h2>
      <p>Agent-based simulation on HPC · LLM-persona agents &amp; synthetic populations · Digital twins · Surrogate &amp; mathematical models</p>
    </div>
    <div class="research-outline-col">
      <h2>Optimization &amp; Explainable AI</h2>
      <p>Representative calibration · Post-calibration XAI · Simulation optimization under uncertainty · Machine learning</p>
    </div>
  </div>

  {% include research-venn.html %}

  <hr class="research-rule">

  <h2 class="research-h2">Selected Topics: Infectious Disease &amp; Public Health Policy</h2>
  <figure class="research-figure">
    <img src="{{ "/images/proj-abm.jpg" | relative_url }}" alt="Agent-based simulation of COVID-19 policy">
    <figcaption><strong>Figure.</strong> HPC-based agent-based simulation of disease spread (COVID-19, measles,
      seasonal influenza) used to forecast outbreaks and evaluate interventions — vaccination campaigns,
      non-pharmaceutical interventions, and resource allocation — including how opinion dynamics
      shape vaccine uptake.</figcaption>
  </figure>

  <h2 class="research-h2">Selected Topics: Clinical Trials &amp; Pharmacometrics</h2>
  <figure class="research-figure">
    <img src="{{ "/images/proj-dbs.jpg" | relative_url }}" alt="Pharmacokinetic modeling of HIV PrEP adherence in HPTN 067">
    <figcaption><strong>Figure.</strong> Pharmacokinetic modeling of clinical-trial data (HPTN 067) to evaluate
      dried-blood-spot biomarkers as indicators of HIV PrEP adherence and protection. Related work:
      long-acting injectable PrEP impact modeling and digital-twin-based <em>virtual clinical trials</em>
      for infectious diseases (NRF, 2026–2029), in collaboration with Gilead Sciences.</figcaption>
  </figure>

  <h2 class="research-h2">Selected Topics: Biomanufacturing Digital Twins</h2>
  <figure class="research-figure">
    <img src="{{ "/images/proj-biomfg.jpg" | relative_url }}" alt="Discrete-event simulation of a biomanufacturing process">
    <figcaption><strong>Figure.</strong> Discrete-event simulation of biopharmaceutical production (e.g., monoclonal
      antibodies, cell therapy) and batch-scheduling optimization to improve yield and throughput under
      process uncertainty.</figcaption>
  </figure>

  <h2 class="research-h2">Selected Topics: Representative Calibration &amp; Explainable AI</h2>
  <figure class="research-figure">
    <img src="{{ "/images/proj-xcal.jpg" | relative_url }}" alt="Representative calibration output">
    <figcaption><strong>Figure.</strong> Calibration of complex simulation models using black-box optimization and
      clustering to find <em>representative</em> parameter sets, and explainable post-calibration analysis
      that interprets how calibrated parameters drive policy outcomes.</figcaption>
  </figure>

  <h2 class="research-h2">Selected Topics: LLM-Persona Agents &amp; Synthetic Populations</h2>
  <p class="research-topic-text">Agent-based models whose agents are driven by LLM personas, and algorithms for
    building synthetic populations from public data (e.g., household assignment using the NVIDIA Persona
    Korea synthetic population) for general-purpose agent-based modeling. <em>Figures coming soon.</em></p>

  <nav class="research-tabs" aria-label="Research sections">
    <a href="#publication">Publication</a>
    <a href="#projects">Projects</a>
    <a href="#presentation">Presentation</a>
    <a href="#awards">Awards</a>
  </nav>

</div>

## Publication
{: #publication}

### Work in progress

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
