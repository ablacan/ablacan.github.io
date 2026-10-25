---
layout: page
title: Publications
permalink: /publications/
---

Research articles published in journals and conferences, and papers under review.
Click the paper icon to access an article. Full list on [Google Scholar](https://scholar.google.com/citations?user=9G7453EAAAAJ&hl=fr).

{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign sections = "submitted:Under review|journal:Journal articles|conference:Conference papers" | split: "|" %}
<div class="pubs">
{% for section in sections %}
  {% assign key = section | split: ":" | first %}
  {% assign heading = section | split: ":" | last %}
  {% assign group = pubs | where: "type", key %}
  {% if group.size > 0 %}
  <h2 class="list-heading">{{ heading }}</h2>
  {% for pub in group %}{% include publication.html %}{% endfor %}
  {% endif %}
{% endfor %}
</div>
