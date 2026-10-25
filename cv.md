---
layout: page
title: CV
permalink: /cv/
---

<p class="cv-actions">
  <a class="btn" href="{{ '/assets/files/Alice_Lacan_CV.pdf' | relative_url }}" target="_blank">Download CV (PDF)</a>
  <span>Publications, talks and teaching have their own pages:
  <a href="{{ '/publications/' | relative_url }}">Publications</a> ·
  <a href="{{ '/presentations/' | relative_url }}">Presentations</a> ·
  <a href="{{ '/teaching/' | relative_url }}">Teaching</a></span>
</p>

{% for s in site.data.cv %}
<section class="cv-section">
  <h2 class="list-heading">{{ s.section }}</h2>
  {% for e in s.entries %}
  <div class="cv-entry">
    <span class="cv-date">{{ e.date }}</span>
    <div class="cv-body">
      <span class="cv-title">{{ e.title }}</span>{% if e.link %} <a class="cv-link" href="{{ e.link }}" target="_blank" rel="noopener">link&nbsp;↗</a>{% endif %}
      {%- if e.org %}<span class="cv-org">{{ e.org }}{% if e.place %}, {{ e.place }}{% endif %}</span>{% endif %}
      {%- if e.details %}<span class="cv-details">{{ e.details }}</span>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endfor %}
