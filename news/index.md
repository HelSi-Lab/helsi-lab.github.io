---
title: News
nav:
  order: 6
  tooltip: Lab updates
---

{% include section.html %}

# News · 소식

<div class="news-list">
{% for post in site.posts %}
  <article class="news-item">
    {% assign imgs = post.images %}
    {% if imgs == nil and post.image %}
      {% assign imgs = post.image | split: "," %}
    {% endif %}
    {% if imgs and imgs.size > 0 %}
      <div class="news-media" data-carousel>
        <div class="news-slides">
          {% for img in imgs %}
            <img src="{{ img | strip | relative_url | uri_escape }}" alt="{{ post.title | regex_strip }}" loading="lazy" class="news-slide{% if forloop.first %} is-active{% endif %}">
          {% endfor %}
        </div>
        {% if imgs.size > 1 %}
          <button class="news-nav news-prev" type="button" aria-label="Previous photo">‹</button>
          <button class="news-nav news-next" type="button" aria-label="Next photo">›</button>
          <div class="news-dots">
            {% for img in imgs %}<span class="news-dot{% if forloop.first %} is-active{% endif %}"></span>{% endfor %}
          </div>
        {% endif %}
      </div>
    {% endif %}
    <div class="news-text">
      <h2 class="news-title">[{{ post.date | date: "%Y.%m.%d" }}] {{ post.title }}</h2>
      {{ post.content | markdownify }}
    </div>
  </article>
{% endfor %}
</div>

<!--
How to add a news item: create _posts/YYYY-MM-DD-short-title.md
  ---
  title: "제목"
  images:                       # optional; one or more photos in images/news/
    - images/news/photo-1.jpg
    - images/news/photo-2.jpg
  ---
  본문 (한 줄씩 문단으로 씁니다)
-->
