import datetime
import calendar
from env import lang

name = {
    "en": "Ruixuan Tu",
    "zh": r"\scshape 涂睿轩 Ruixuan Tu",
    "ja": r"\scshape Ruixuan Tu\, \ruby{涂}{トゥ}\ \ruby{睿}{ルイ}\ruby{轩}{シュェン}"
}

link = {
    "en": "Website: ",
    "zh": "网站：",
    "ja": "HP："
}

resume_line = {
    "en": r"Résumé: \href{https://direct.turx.asia/resume.pdf}{EN} \href{https://direct.turx.asia/resume-ja.pdf}{日} \href{https://direct.turx.asia/resume-zh.pdf}{中}",
    "zh": r"简历：\href{https://direct.turx.asia/resume-zh.pdf}{中} \href{https://direct.turx.asia/resume.pdf}{EN} \href{https://direct.turx.asia/resume-ja.pdf}{日}",
    "ja": r"履歴書：\href{https://direct.turx.asia/resume-ja.pdf}{日} \href{https://direct.turx.asia/resume.pdf}{EN} \href{https://direct.turx.asia/resume-zh.pdf}{中}"
}

today = datetime.date.today()

date_line = {
    "en": "Updated on {} {} {}".format(today.day, calendar.month_name[today.month], today.year),
    "zh": "更新于 {}年 {}月 {}日".format(today.year, today.month, today.day),
    "ja": "{}年 {}月 {}日現在".format(today.year, today.month, today.day)
}

phone_line = {
    "en": r"+1 608-977-4951",
    "zh": r"+1 608-977-4951 $\land$ +86 139-7090-5245",
    "ja": r"+1 608-977-4951 $\land$ +81 090-7347-2311"
}

template = r"""
\begin{center}
    \textbf{\Huge {insert_name}} \\ \vspace{1pt}
    \small \faIcon{phone-alt} {insert_phone} $|$ \faIcon{envelope} \href{mailto:ruixuan@cs.wisc.edu}{ruixuan@cs.wisc.edu} $\land$ \href{mailto:turx2003@gmail.com}{turx2003@gmail.com}
    $|$ \small \href{https://turx.asia}{{\faIcon{link}} {insert_link}{turx.asia}} \\
    \small {\aiicon{cv}} {insert_resume_line}
    $|$ \small \href{https://github.com/TURX}{{\faIcon{github}} {TURX}}
    $|$ \small \href{https://linkedin.com/in/rxtu}{\faIcon{linkedin} {rxtu}}
    $|$ \small \href{https://scholar.google.com/citations?user=V6hzHoQAAAAJ}{\aiicon{googlescholar}}
    $|$ {insert_date_line}
\end{center}
"""

code = template.replace("{insert_name}", name[lang]).replace("{insert_link}", link[lang]).replace("{insert_resume_line}", resume_line[lang]).replace("{insert_date_line}", date_line[lang]).replace("{insert_phone}", phone_line[lang])
