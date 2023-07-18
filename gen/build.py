import components.header as header
import components.heading as heading
import components.edu as edu
import components.work as work
import components.acad as acad
import components.honor as honor
import components.proj as proj
import components.skill as skill

doc = header.code + r"""
\begin{document}
""" + heading.code + edu.code + work.code + acad.code + honor.code + proj.code + skill.code + r"""
\end{document}
"""

with open("gen/doc.tex", "w") as f:
    f.write(doc)
