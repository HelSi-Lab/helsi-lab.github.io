---
title: People
nav:
  order: 1
  tooltip: About our team
header-style: urban
header-dark: false
---

<div class="team-page">
  <section class="team-roster team-roster-first">
    <h1 class="team-page-title">OUR TEAM <span>· 연구실 구성원</span></h1>

    {% assign pi = site.members | where_exp: "member", "member.is-pi == true" | first %}
    <p class="team-group-title">PRINCIPAL INVESTIGATOR <span>· 지도교수</span></p>
    <div class="team-card-grid team-card-grid-pi">
      {% include team-card.html member=pi %}
    </div>

    <p class="team-group-title">MEMBERS <span>· 연구원</span></p>

    <div class="team-card-grid">
      {% assign researchers = site.members | where_exp: "member", "member.role != 'pi' and member.role != 'alumni'" | sort: "order" %}
      {% for member in researchers %}
        {% include team-card.html member=member %}
      {% endfor %}
    </div>
  </section>

  {% assign alumni = site.members | where_exp: "member", "member.role == 'alumni'" %}
  {% if alumni.size > 0 %}
    <section class="team-alumni">
      <p class="team-group-title">ALUMNI <span>· 졸업생</span></p>
      {% for member in alumni %}
        <a href="{{ member.url | relative_url }}"><span>{{ member.name }}</span><span>{{ member.description }}</span><span aria-hidden="true">→</span></a>
      {% endfor %}
    </section>
  {% endif %}

</div>
