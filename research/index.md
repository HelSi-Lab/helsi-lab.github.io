---
title: Research
nav:
  order: 2
  tooltip: Research outline and selected topics
---

{% include section.html %}

<div class="research-page">

  <div class="research-hero" id="outline">
    <p class="research-eyebrow">Research</p>
    <h1>Research Outline <span class="research-kr">연구 개요</span></h1>
    <p class="research-lead">
      HelSi Lab develops simulation, optimization, and digital-twin methods to
      support decision-making in complex bio/healthcare systems. We model real
      systems, simulate how they behave under uncertainty, and optimize the
      decisions that shape them.
    </p>
    <p class="research-lead research-lead-kr">
      HelSi 연구실은 감염병·임상시험·바이오 공정 등 복잡한 바이오·헬스케어 시스템의 의사결정을 돕기 위해
      시뮬레이션, 최적화, 디지털 트윈 방법론을 연구합니다.
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


</div>
