---
title: People
nav:
  order: 4
  tooltip: About our team
---

{% include section.html %}

# People

## Principal Investigator

{% include portrait.html lookup="serin-lee" %}

{% include section.html %}

## Members

{% include portrait.html lookup="haeun-kang" %}
{% include portrait.html lookup="minjae-kang" %}
{% include portrait.html lookup="jehwang-jeong" %}
{% include portrait.html lookup="gwanhyeon-lee" %}

{% include section.html %}

## Alumni

{% include list.html data="members" component="portrait" filter="role == 'alumni'" %}

<!-- To add an alumnus: set `role: alumni` in the member's file in _members/ (they will appear here automatically). -->
