---
title: News
nav:
  order: 5
  tooltip: Lab updates
---

{% include section.html %}

# News

{% include list.html data="posts" component="post-excerpt" %}

<!--
How to add a news item:
  1. Create _posts/YYYY-MM-DD-short-title.md with front matter:
       ---
       title: "Headline"
       image: images/news/photo.jpg   # optional; put the photo in images/news/
       ---
       One or two sentences of text (shown in the list). More text is fine — it shows on the post's own page.
-->
