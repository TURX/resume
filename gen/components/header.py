from env import lang

paper = {
    "en": "letterpaper",
    "ja": "a4paper",
    "zh": "a4paper"
}

page_indicator = {
    "en": r"\thepage \,of 2",
    "ja": r"\thepage / 2",
    "zh": r"第 \thepage 页, 共 2 页"
}

continue_text = {
    "en": "Continued on next page",
    "ja": "次のページに続く",
    "zh": "接下页"
}

template = r"""% !TEX program = xelatex
\documentclass[{insert_paper},11pt]{article}

% \usepackage[utf8]{inputenc}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{multicol}
\usepackage{soul}
\usepackage{fontawesome5}
\usepackage{ifthen}
\usepackage{makecell}
\XeTeXgenerateactualtext=1


%----------FONT OPTIONS----------
% sans-serif
\usepackage[sfdefault]{FiraSans}
\usepackage[fallback]{xeCJK}
\usepackage{pxrubrica}
\rubysizeratio{0.3}
\setCJKmainfont[BoldFont=NotoSansCJKjp-Bold,AutoFakeSlant=0.15]{Noto Sans CJK JP}

% Adjust margins
%\usepackage[
%  top=0.5in,
%  bottom=0.5in,
%  left=0.5in,
%  right=0.5in,
%  includehead,includefoot
%]{geometry}
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\footskip 14pt
\fancyfoot[C]{{insert_page_indicator}}
\fancyfoot[R]{\ifnum \value{page}<2 {{insert_continue_text} →}\fi}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

%-------------------------
% Custom commands
\newcommand{\resumeItem}[2][]{
  \item#1\small{
    {#2 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
    \end{tabular*}
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubheadingCompact}[3]{
    \item
    \begin{tabular*}{0.97\textwidth}{l @{\extracolsep{\fill}} r}
      \textbf{#1} $|$ \textit{\small #3} & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
"""

code = template.replace("insert_paper", paper[lang]).replace("insert_page_indicator", page_indicator[lang]).replace("insert_continue_text", continue_text[lang])
