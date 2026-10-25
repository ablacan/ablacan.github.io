---
layout: page
title: Teaching
permalink: /teaching/
intro: >-
  I teach statistics, mathematics and machine learning, from first-year Bachelor students to Master students and professionals.
illustration: /assets/img/illustrations/teaching.webp
illustration_alt: Cartoon of Alice writing on a blackboard
illustration_style: yellow
illustration_offset: green
---

{% assign current = site.data.teaching | where: "current", true %}
{% assign past = site.data.teaching | where_exp: "c", "c.current != true" %}
{% assign total_hours = 0 %}
{% for c in site.data.teaching %}{% assign total_hours = total_hours | plus: c.hours %}{% endfor %}

<h2 class="list-heading">This year</h2>
<ul class="courses">
{% for c in current %}{% include course.html %}{% endfor %}
</ul>

<h2 class="list-heading">Previously</h2>
<ul class="courses">
{% for c in past %}{% include course.html %}{% endfor %}
</ul>

<p class="note">{{ total_hours }} hours of teaching in total.</p>
