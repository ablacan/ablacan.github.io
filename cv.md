---
layout: page
title: CV
permalink: /cv/
intro: >-
  [Download CV (PDF)](/assets/files/Alice_Lacan_CV.pdf){: .btn target="_blank"}
illustration: /assets/img/illustrations/cv.webp
illustration_alt: Cartoon of Alice unrolling a long scroll
illustration_style: yellow
illustration_offset: orange
---

{% for s in site.data.cv %}
<section class="cv-section">
  <h2 class="list-heading">{{ s.section }}</h2>
  {% for e in s.entries %}
  <div class="cv-entry">
    <span class="cv-date">{{ e.date }}</span>
    <div class="cv-body">
      <span class="cv-title">{{ e.title }}</span>{% if e.link %} <a class="cv-link arrow-link" href="{{ e.link }}" target="_blank" rel="noopener">Link</a>{% endif %}
      {%- if e.org %}<span class="cv-org">{{ e.org }}{% if e.place %}, {{ e.place }}{% endif %}</span>{% endif %}
      {%- if e.details %}<span class="cv-details">{{ e.details }}</span>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endfor %}
