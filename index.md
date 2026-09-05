---
---

{% include section.html %}

<div class="home-hero">
  <div class="home-hero-left">
    <h1 class="home-title">Healthcare &amp;<br><em>Simulation</em><br>Optimization Lab</h1>
    <p class="home-tagline">
      Simulation, optimization, and digital-twin methods for real decisions in
      healthcare, infectious disease, and bioprocess systems.
    </p>
    <div class="home-buttons">
      <a class="home-btn home-btn-primary" href="{{ "/research/" | relative_url }}">Our Research →</a>
      <a class="home-btn" href="{{ "/team/" | relative_url }}">Meet the Team</a>
    </div>
    <div class="home-recruit">
      <div class="home-recruit-title">학부연구생 · 대학원생 모집중! · Now Recruiting</div>
      <p><strong>모집 대상:</strong> 학부생 3–4학년 (시뮬레이션 수강자 우대), 석·박사 대학원생</p>
      <p><strong>관심 분야:</strong> 바이오·헬스케어 시스템, 시뮬레이션 기반 최적화, 디지털 트윈</p>
      <p><strong>지원 방법:</strong> <a href="mailto:serinlee@inu.ac.kr">serinlee@inu.ac.kr</a> 로 이메일! · <a href="{{ "/join/" | relative_url }}">자세히 보기</a></p>
    </div>
  </div>
  <div class="home-hero-right">
    <h2 class="home-welcome">HelSi 연구실에 오신 것을 환영합니다</h2>
    <p>인천대학교 산업경영공학과 <strong>HelSi 연구실</strong>(헬스케어 및 시뮬레이션 최적화 연구실)은
      <strong>시뮬레이션(Simulation)</strong>과 <strong>최적화(Optimization)</strong>를 기반으로
      감염병, 임상시험, 바이오 공정 등 복잡한 바이오·헬스케어 시스템의 의사결정 문제를 연구합니다.</p>
    <p>우리 연구실은 <strong>Agent-based 시뮬레이션, 수리적 모델링, 디지털 트윈</strong> 등의 기법으로
      시스템의 불확실한 거동을 예측하고, <strong>파라미터 보정(calibration), 설명가능한 AI(XAI),
      시뮬레이션 최적화</strong>를 통해 데이터에 근거한 정책과 운영 전략을 도출하는 것을 목표로 합니다.</p>
    <p>또한 미국 Gilead Sciences, Fred Hutchinson Cancer Center 등 해외 기관과의
      <strong>국제 공동연구</strong>를 활발히 진행하고 있습니다.</p>
    <p class="home-welcome-en">HelSi Lab at Incheon National University studies decision-making in complex
      bio and healthcare systems — infectious disease, clinical trials, and biomanufacturing —
      using agent-based simulation, mathematical modeling, digital twins, model calibration,
      explainable AI, and simulation optimization.</p>
  </div>
</div>

{% include section.html %}

## Research Areas · 연구 분야

We model complex bio and healthcare systems, simulate how they behave under
uncertainty, and optimize the decisions that shape them.
복잡한 바이오·헬스케어 시스템을 모델링하고, 불확실성 하의 거동을 시뮬레이션하며, 의사결정을 최적화합니다.
{:.center}

{% include research-venn.html %}

{% capture col1 %}
#### Bio · Healthcare Systems
바이오 · 헬스케어 시스템

Disease forecasting, hospital resource allocation, clinical trial analysis,
and bioprocess systems.
질병 예측 · 병상 자원 분배 · 임상시험 분석 · 바이오 공정
{% endcapture %}

{% capture col2 %}
#### Simulation & Modeling
시뮬레이션 & 모델링

Agent-based simulation on HPC, mathematical modeling, and surrogate models for
systems too complex to solve directly.
Agent-based 시뮬레이션 · 수리적 모델링 · 근사 모델링
{% endcapture %}

{% capture col3 %}
#### Optimization
최적화

Global optimization, machine learning, and explainable AI — with digital twins
and parameter calibration bridging simulation and optimization.
글로벌 최적화 · 머신 러닝 · 설명가능한 AI (XAI) · 디지털 트윈 · 파라미터 보정
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

{% include button.html text="See our research" link="research" flip=true style="bare" %}
