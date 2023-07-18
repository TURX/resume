import datetime
import calendar
from env import lang

name = {
    "en": "Ruixuan Tu",
    "zh": r"\scshape 涂睿轩 Ruixuan Tu",
    "ja": r"\scshape Ruixuan Tu\, \ruby{涂}{トゥ}\ \ruby{睿}{ルイ}\ruby{轩}{シュェン}"
}

link = {
    "en": "Website",
    "zh": "网站",
    "ja": "ウェブサイト"
}

resume_line = {
    "en": r"Résumé: \href{https://direct.turx.asia/resume.pdf}{\underline{EN}} \href{https://direct.turx.asia/resume-ja.pdf}{\underline{日}} \href{https://direct.turx.asia/resume-zh.pdf}{\underline{中}}",
    "zh": r"简历: \href{https://direct.turx.asia/resume-zh.pdf}{\underline{中}} \href{https://direct.turx.asia/resume.pdf}{\underline{EN}} \href{https://direct.turx.asia/resume-ja.pdf}{\underline{日}}",
    "ja": r"履歴書: \href{https://direct.turx.asia/resume-ja.pdf}{\underline{日}} \href{https://direct.turx.asia/resume.pdf}{\underline{EN}} \href{https://direct.turx.asia/resume-zh.pdf}{\underline{中}}"
}

today = datetime.date.today()

date_line = {
    "en": "Updated on {} {} {}".format(today.day, calendar.month_name[today.month], today.year),
    "zh": "更新于 {}年 {}月 {}日".format(today.year, today.month, today.day),
    "ja": "{}年 {}月 {}日現在".format(today.year, today.month, today.day)
}

template = r"""
\begin{center}
    \textbf{\Huge {insert_name}} \\ \vspace{1pt}
    \small \faIcon{phone-alt} +1 (608) 977-4951 $\land$ +86 13970905245 $|$ \faIcon{envelope} \href{mailto:ruixuan.tu@wisc.edu}{\underline{ruixuan.tu@wisc.edu}} $\land$ \href{mailto:turx2003@gmail.com}{\underline{turx2003@gmail.com}}
    $|$ \small \faIcon{linkedin} \href{https://linkedin.com/in/rxtu}{\underline{rxtu}} 
    $|$ \small \faIcon{github} \href{https://github.com/TURX}{\underline{TURX}} \\
    \small \faIcon{link} {insert_link}: \href{https://turx.asia}{\underline{turx.asia}} $|$
    \small \faIcon{file} {insert_resume_line} $|$
    {insert_date_line}
\end{center}
"""

code = template.replace("{insert_name}", name[lang]).replace("{insert_link}", link[lang]).replace("{insert_resume_line}", resume_line[lang]).replace("{insert_date_line}", date_line[lang])
