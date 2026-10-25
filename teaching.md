---
layout: page
title: Teaching
permalink: /teaching/
---

I teach statistics, mathematics and machine learning, from first-year Bachelor students to Master students and professionals.

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
