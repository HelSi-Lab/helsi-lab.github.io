---
title: People
nav:
  order: 1
  tooltip: About our team
header-style: urban
header-dark: false
---

<div class="team-page">
  <section class="team-hero">
    <p class="team-kicker">HEALTHCARE &amp; SIMULATION OPTIMIZATION LAB</p>
    <h1>HELSI LAB PEOPLE</h1>
    <p class="team-tagline">We build better healthcare decisions through<br>simulation, optimization, and digital twins.</p>
    <p class="team-tagline-kr">시뮬레이션·최적화·디지털 트윈으로 더 나은 헬스케어 의사결정을 만듭니다.</p>

    <div class="team-image-wall" aria-label="HelSi Lab members">
      {% assign people = site.members | where_exp: "member", "member.role != 'alumni'" %}
      {% for member in people %}
        <a href="{{ member.url | relative_url }}" class="team-image-wall-item" aria-label="{{ member.name }} profile">
          <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" loading="{% if forloop.first %}eager{% else %}lazy{% endif %}">
          <span>{{ member.name }}</span>
        </a>
      {% endfor %}
    </div>
  </section>

  <section class="team-roster">
    <p class="team-section-label">OUR TEAM</p>

    {% assign pi = site.members | where_exp: "member", "member.is-pi == true" | first %}
    <article class="team-pi">
      <a href="{{ pi.url | relative_url }}" class="team-pi-image" aria-label="{{ pi.name }} profile">
        <img src="{{ pi.image | relative_url }}" alt="{{ pi.name }}">
      </a>
      <div class="team-pi-content">
        <p class="team-role">PRINCIPAL INVESTIGATOR</p>
        <h2>{{ pi.name }}</h2>
        <p class="team-pi-title">{{ pi.description }}</p>
        <p>HelSi Lab develops models and decision tools for complex healthcare, infectious-disease, and biomanufacturing systems.</p>
        <div class="team-pi-links">
          {% if pi.links.google-scholar %}<a href="https://scholar.google.com/citations?user={{ pi.links.google-scholar }}" target="_blank" rel="noopener">Google Scholar</a>{% endif %}
          {% if pi.links.cv %}<a href="{{ pi.links.cv | relative_url }}">CV</a>{% endif %}
          {% if pi.links.email %}<a href="mailto:{{ pi.links.email }}">Email</a>{% endif %}
        </div>
      </div>
    </article>

    <div class="team-members-heading">
      <p class="team-section-label">RESEARCH TEAM</p>
      <p>Researchers working across healthcare systems, public health, and biomanufacturing.</p>
    </div>

    <div class="team-card-grid">
      {% assign researchers = site.members | where_exp: "member", "member.role != 'pi' and member.role != 'alumni'" %}
      {% for member in researchers %}
        <a href="{{ member.url | relative_url }}" class="team-person-card">
          <div class="team-person-photo">
            <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" loading="lazy">
          </div>
          <p class="team-role">{{ member.description }}</p>
          <h3>{{ member.name }}</h3>
          <span class="team-person-more">View profile <span aria-hidden="true">→</span></span>
        </a>
      {% endfor %}
    </div>
  </section>

  {% assign alumni = site.members | where_exp: "member", "member.role == 'alumni'" %}
  {% if alumni.size > 0 %}
    <section class="team-alumni">
      <p class="team-section-label">ALUMNI</p>
      {% for member in alumni %}
        <a href="{{ member.url | relative_url }}"><span>{{ member.name }}</span><span>{{ member.description }}</span><span aria-hidden="true">→</span></a>
      {% endfor %}
    </section>
  {% endif %}

  <section class="team-join">
    <p class="team-section-label">WORK WITH US</p>
    <h2>Interested in joining HelSi Lab?</h2>
    <a href="{{ '/join/' | relative_url }}">Explore opportunities <span aria-hidden="true">→</span></a>
  </section>
</div>
