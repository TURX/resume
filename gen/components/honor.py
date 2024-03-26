import type
import structure

code = r"""
\section{""" + structure.translate({
    "en": r"Extracurricular Honors \& Awards",
    "ja": r"受賞歴",
    "zh": r"课外荣誉和奖项"
}) + r"}" + "\n" + r"\small{" + structure.item_list([
    {
        "en": r"\textbf{ACM-ICPC (International Collegiate Programming Contest):} Silver Medal (7\textsuperscript{th} place out of 96 teams) (2021 ICPC NCNA Regional, Team THREE\_PUPILS); Rated (26\textsuperscript{th} place out of 118 teams) (2022 ICPC NCNA Regional, Team GEKOta)",
        "ja": r"\textbf{ACM-ICPC（国際大学対抗プログラミングコンテスト）：} 銀メダル（96チーム中7位・2021年ICPC北中米地区大会・チームTHREE\_PUPILS）、ランキング入り（118チーム中26位）（2021年ICPC北中米地区大会・チームGEKOta）",
        "zh": r"\textbf{ACM-ICPC (国际大学生程序设计竞赛)：} 银奖 (总共96队中第7名) (2021年北美中北部区域赛, THREE\_PUPILS 队)、排名 (总共118队中第26名) (2022年北美中北部区域赛, GEKOta 队)"
    },
    # TODO: ICPC honorable mention
    # -10,  # vspace
    {
        "en": r"\textbf{ACSL (American Computer Science League) Senior Division}",
        "ja": r"\textbf{ACSL（American Computer Science League） 上級コース}",
        "zh": r"\textbf{ACSL (美国计算机科学联赛) 高级组}"
    },
    -4,  # vspace,
    structure.itemize([
        {
            "en": "2020 All-Star: Global Top Score; Personal Gold; Programming Proficiency; Team Silver",
            "ja": "2020 All-Star：グローバルトップスコア、個人金メダル、プログラミング能力賞、チーム銀メダル",
            "zh": "2020全明星赛：国际高分奖、个人金奖、编程技能奖、团队银奖 (总分全国第二、个人分全国第一)"
        },
        {
            "en": "2019 - 2020: Team Bronze; Individual Distinction",
            "ja": "2019 - 2020：チーム銀メダル、個人優秀賞",
            "zh": "2019-2020晋级赛：团队铜奖、个人杰出奖"
        }
    ], "label={}, nosep"),
    {
        "en": r"\textbf{Google Code-in:} Finalist (Top 6) at KDE Community (2018) and Haiku OS (2019)",
        "ja": r"\textbf{Google Code-in：} Finalist（トップ6）、KDE Community（2018）と Haiku OS（2019）より",
        "zh": r"\textbf{Google Code-in：} Finalist (前6名), 从KDE开源社区和Haiku OS中选出 (2018、2019)"
    },
    {
        "en": r"\textbf{China National Olympiad in Informatics in Provinces:} 2\textsuperscript{nd} Prize, Senior Division (2019, 2020); 3\textsuperscript{rd} Prize, Senior Division (2018); 2\textsuperscript{nd} Prize, Junior Division (2017)",
        "ja": r"\textbf{NOIP 中国情報オリンピック省大会：} 上級コース2等賞（2019・2020）、上級コース3等賞（2018）、初級コース2等賞（2017）",
        "zh": r"\textbf{NOIP/CSP (全国信息学奥林匹克联赛)：} 提高组二等奖 (2019、2020)、提高组三等奖 (2018)、普及组二等奖 (2017)"
    },
    {
        "en": r"\textbf{China Adolescents Science and Technology Innovation Contest:} 1\textsuperscript{st} Prize in Province, Finalist of National Contest (2020, Project \textit{Trash Classification System based on CNN of Machine Learning})",
        "ja": r"\textbf{CASTIC 中国青少年科学技術イノベーションコンテスト：} 省大会1等賞、全国大会に出場（2020年・プロジェクト \textit{Trash Classification System based on CNN of Machine Learning}）",
        "zh": r"\textbf{CASTIC (全国青少年科技创新大赛)：} 省一等奖, 晋级全国决赛 (2020, 获奖项目 \textit{基于神经网络机器学习的人工智能垃圾图像分类系统})"
    }
]) + "}"
