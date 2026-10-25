---
layout: page
title: Presentations
permalink: /presentations/
---

Non-exhaustive list of my talks and posters at conferences, invited seminars and workshops.

{% assign talks = site.presentations | sort: "date" | reverse %}
{% assign years = talks | group_by_exp: "pres", "pres.date | date: '%Y'" %}
<div class="timeline">
{% for year in years %}
  <section class="timeline-year">
    <h2 class="year">{{ year.name }}</h2>
    <ul class="talks">
    {% for pres in year.items %}
      {% include presentation.html %}
    {% endfor %}
    </ul>
  </section>
{% endfor %}
</div>
