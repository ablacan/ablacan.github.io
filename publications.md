---
layout: page
title: Publications
permalink: /publications/
---
Here's a list of my recent publications:

{% for pub in site.publications reversed %}
  {% include publication.html %}
{% endfor %}
