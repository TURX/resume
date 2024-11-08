import type
import structure

resumeSubHeadings: type.ResumeSubHeadingList = [
    {
        "title": {
            "en": r"Undergraduate Peer Mentor / Tutor",
            "ja": r"学部生のティーチング・アシスタント",
            "zh": r"本科助教"
        },
        "date": {
            "en": "September 2022 -- Present",
            "ja": "2022年9月 -- 現在",
            "zh": "2022年9月 -- 现今"
        },
        "subtitle": {
            "en": r"Department of Computer Sciences \& University Housing, University of Wisconsin--Madison",
            "ja": r"ウィスコンシン大学マディソン校\ 情報科学科 \& 学生宿舎",
            "zh": r"威斯康星大学麦迪逊校（UW--Madison）\ 计算机科学系 \& 学生宿舎"
        },
        "place": {
            "en": r"Madison, Wisconsin, USA",
            "ja": r"米国\ ウィスコンシン州\ マディソン",
            "zh": r"美国\ 威斯康星州\ 麦迪逊市"
        },
        "body": structure.item_list([
            {
                "en": r"""
                COMP SCI 540 (Intro-Artificial Intelligence): Helping students to learn machine learning, math, game, and search by answering questions during office hours (-- May 2024) \\
                {\faIcon{award}} Received Golden Bricks Award (2023) for service to CS Department \href{https://www.cs.wisc.edu/2023-cs-department-awards-and-thank-yous/\#GOLDEN\%20BRICK\%20AWARDS}{\emph{Post}}
                """,
                "ja": r"""
                COMP SCI 540（人工知能基礎）：オフィスアワーで、機械学習・数学・ゲーム理論・探索法などについての質問を答える (-- 2024年5月) \\
                {\faIcon{award}} 情報科学科への貢献でGolden Bricks Award（2023年）を受賞 \href{https://www.cs.wisc.edu/2023-cs-department-awards-and-thank-yous/\#GOLDEN\%20BRICK\%20AWARDS}{\emph{投稿}}
                """,
                "zh": r"""
                COMP SCI 540（人工智能基础）：在答疑时间帮助学生理解机器学习、数学、博弈论、搜索 (-- 2024年5月) \\
                {\faIcon{award}} 因对计算机科学系的贡献获得金砖奖（2023年） \href{https://www.cs.wisc.edu/2023-cs-department-awards-and-thank-yous/\#GOLDEN\%20BRICK\%20AWARDS}{\emph{文章}}
                """
            },
            {
                "en": "Calculus: providing individual and group tutoring to residents taking Mathematics courses",
                "ja": "微積分：寮で住んでいる学生たちに数学の勉強支援を提供",
                "zh": "微积分：为宿舍学生提供数学相关的课程指导"
            }
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": r"Software Development Engineer Intern",
            "ja": r"ソフトウェアエンジニア\ インターン",
            "zh": r"软件工程师\ 实习生"
        },
        "date": {
            "en": "May 2022 -- September 2022",
            "ja": "2022年5月 -- 2022年9月",
            "zh": "2022年5月 -- 2022年9月"
        },
        "subtitle": {
            "en": r"Textea Inc",
            "ja": r"Textea Inc",
            "zh": r"Textea Inc"
        },
        "place": {
            "en": r"(Remote) Coralville, Iowa, USA",
            "ja": r"（リモート）米国\ アイオワ州\ コーラルビル",
            "zh": r"（远程）美国\ 爱荷华州\ 科拉尔维尔市"
        },
        "body": structure.item_list([
            structure.translate({
                "en": r"Lead Developer of Funix: NodeJS generator from Python functions to serverless web instances",
                "ja": r"Funix\ リードデベロッパ：Python関数をサーバレスWebサービスに変換できるNodeJS生成プログラム",
                "zh": r"Funix项目组长：使用Python生成基于NodeJS的无服务器架构网络实例"
            }) + " \\" +
            structure.itemize([
                r"\footnotesize " + structure.paper_leading + r"F. Bao, M. Qi, \textbf{R. Tu}, E. Wan (2024). Funix - The laziest way to build GUI apps in Python. In Proceedings of the 23rd Python in Science Conference. SciPy. \href{https://proceedings.scipy.org/articles/JFYN3740}{\aiicon{open-access}}"
            ]),
            {
                "en": "Lead Developer of Web Backend: APIs for user auth, permission, admin, RPC and HTTP remote call",
                "ja": r"Webバックエンド\ リードデベロッパ：ユーザー認証・アクセス権・管理者・リモート関数呼び出し用のAPI",
                "zh": "网站后端项目组长：用户认证、鉴权、管理、基于RPC和HTTP的远程调用"
            },
            {
                "en": "Developer of NLP Backend: classical natural language processing task implementation in Python, API migration",
                "ja": "NLPバックエンドデベロッパ：自然言語処理タスクのPython実装、API マイグレーション",
                "zh": "自然语言处理开发：使用Python实现经典自然语言处理任务、API迁移"
            }
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": "Japanese Tutor",
            "ja": "日本語チューター",
            "zh": "日语辅导"
        },
        "date": {
            "en": "October 2021 -- April 2022",
            "ja": "2021年10月 -- 2022年4月",
            "zh": "2021年10月 -- 2022年4月"
        },
        "subtitle": {
            "en": "Greater University Tutoring Service, University of Wisconsin--Madison",
            "ja": r"ウィスコンシン大学マディソン校\ チュータリングサービス",
            "zh": r"威斯康星大学麦迪逊分校\ 大学生辅导服务"
        },
        "place": {
            "en": r"Madison, Wisconsin, USA",
            "ja": r"米国\ ウィスコンシン州\ マディソン",
            "zh": r"美国\ 威斯康星州\ 麦迪逊市"
        },
        "body": {
            "en": "Helped students to improve proficiency through instruction and conversation as an advanced/fluent speaker",
            "ja": "上級/流暢な話者として、指導や会話を通じて学生の言語能力向上を支援した",
            "zh": "作为一位高级/流利的使用者，通过指导和对话帮助学生提高他们的语言能力"
        },
        "tag": None
    },
    {
        "title": {
            "en": "Director",
            "ja": "部長",
            "zh": "社长"
        },
        "date": {
            "en": "August 2018 -- August 2021",
            "ja": "2018年8月 -- 2021年8月",
            "zh": "2018年8月 -- 2021年8月"
        },
        "subtitle": {
            "en": "IT Club, Attached High School to Jiangxi Normal University",
            "ja": r"江西師範大学附属中学\ 情報科学部",
            "zh": r"江西师范大学附属中学\ 信息技术社"
        },
        "place": {
            "en": "Nanchang, Jiangxi, China",
            "ja": r"中国\ 江西省\ 南昌市",
            "zh": r"中国\ 江西省\ 南昌市"
        },
        "body": structure.item_list([
            {
                "en": "AP and competitive programming teaching, website, live stream, partnership with college in Japan",
                "ja": "APと競技プログラミングの講義、ウェブサイト、ライブ配信、明石高専とのコラボ",
                "zh": "AP和竞赛编程教学、网站、直播流、和日本学校合作VR项目"
            }
        ]),
        "tag": None
    }
]

resumeSubHeadings_code = structure.subheading_list(resumeSubHeadings)

code = r"""
\section{""" + r"\faIcon{suitcase} " + structure.translate({
    "en": "Work Experience",
    "ja": "職歴",
    "zh": "工作经历"
}) + r"}" + resumeSubHeadings_code
