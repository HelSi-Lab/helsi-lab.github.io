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
      <article>
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
        <div>
          <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          <p>{{ post.content | markdownify | remove: "<p>" | remove: "</p>" | strip_html }}</p>
        </div>
      </article>
    {% endfor %}
  </section>
</div>
