---
title: News
nav:
  order: 6
  tooltip: Lab updates
header-style: urban
header-dark: false
---

<div class="lab-inner-page news-reference-page">
  <section class="lab-page-heading">
    <h1>News <span>· 소식</span></h1>
  </section>

  <section class="news-reference-list">
    {% for post in site.posts %}
      <article{% if post.images and post.images.size > 0 %} class="has-image"{% endif %}>
        {% if post.images and post.images.size > 0 %}
          <a class="news-reference-image" href="{{ post.url | relative_url }}" aria-label="{{ post.title }}">
            <img src="{{ post.images.first | relative_url }}" alt="{{ post.title }}" loading="lazy">
          </a>
        {% endif %}
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
        <div>
          <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          <p>{{ post.content | markdownify | remove: "<p>" | remove: "</p>" | strip_html }}</p>
        </div>
      </article>
    {% endfor %}
  </section>
</div>
