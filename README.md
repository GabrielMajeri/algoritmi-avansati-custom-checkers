# Verificatori personalizați pentru problemele de pe platforma CMS

Începând cu anul universitar 2021-2022, în cadrul cursului de Algoritmi Avansați (curs de anul II, la programul de studiu Informatică de la [FMI-UniBuc](https://fmi.unibuc.ro/)) se folosește [platforma CMS](https://cms.fmi.unibuc.ro/) pentru evaluarea și punctarea automată a problemelor de laborator.

Aplicația este un _fork_ al proiectului [`online-judge`](https://github.com/DMOJ/online-judge), dezvoltat de [DMOJ](https://dmoj.ca/). Pe lângă customizările estetice și funcționale făcute la nivel de aplicație, pentru majoritatea problemelor avem configurați **verificatori personalizați** (_custom checkers_), care oferă un feedback mult mai detaliat și informativ studenților atunci când rezolvarea lor nu afișează soluția corectă.

Un [_custom checker_](](https://docs.dmoj.ca/#/problem_format/custom_checkers)) se implementează definind o funcție Python care este încărcată și apelată de către evaluator după ce termină de executat o submisie. Această funcție are acces la output-ul generat de program și la fișierul cu output-ul „corect” (cel configurat de editor). Ea trebuie să compare cele două output-uri și să verifice dacă cel produs de submisie este conform cu cel așteptat.
