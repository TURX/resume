import type
import structure

resumeSubHeadings: type.ResumeSubHeadingList = [
    r"\normalsize " + structure.translate({
        "en": r"\normalsize \textbf{Research Interests}: natural language processing (NLP) with human alignment and digital humanities",
        "ja": r"\textbf{研究分野}: 人間へのアライメントと人文情報学における自然言語処理（NLP）",
        "zh": r"\textbf{研究方向}: 与人类对齐的自然语言处理（NLP）以及自然语言处理（NLP）在数字人文学中的应用"
    }),
    {
        "title": {
            "en": "Research Assistant",
            "ja": "リサーチアシスタント",
            "zh": "研究助理"
        },
        "date": {
            "en": "June 2022 -- Present",
            "ja": "2022年6月 -- 現在",
            "zh": "2022年6月 -- 现今"
        },
        "subtitle": {
            "en": "Prof. Forrest Sheng Bao, Vectara Inc / Iowa State University",
            "ja": r"Vectara Inc・アイオワ州立大学\ Forrest Sheng Bao 教授",
            "zh": r"Vectara Inc、爱荷华州立大学 (Iowa State University) \ 鲍盛 (Forrest Sheng Bao) 教授"
        },
        "place": {
            "en": "(Remote) USA",
            "ja": r"（リモート）米国",
            "zh": r"（远程）美国"
        },
        "body": structure.item_list([
            {
                "en": r"NLP Research in Summary Evaluation (DocAsRef) and Hallucination Reduction (RAG and \href{https://github.com/TexteaInc/mercury}{Mercury})",
                "ja": r"NLP研究：要約評価（DocAsRef）と幻覚軽減技術（RAGと\href{https://github.com/TexteaInc/mercury}{Mercury}）",
                "zh": r"NLP研究：摘要评估（DocAsRef）和幻觉克服（RAG 和 \href{https://github.com/TexteaInc/mercury}{Mercury}）",
            },
            structure.itemize([
                r"\footnotesize " + structure.paper_leading + r"F. Bao*, \textbf{R. Tu}*, G. Luo, Y. Yang, H. Li, M. Qiu, C. Chen (2022). DocAsRef: A Pilot Empirical Study on Repurposing Reference-based Summary Quality Metrics as Reference-free Metrics. In Findings of the Association for Computational Linguistics: EMNLP 2023 (pp. 1226–1235). \href{https://arxiv.org/abs/2212.10013}{\aiicon{arxiv}} \href{https://aclanthology.org/2023.findings-emnlp.87/}{\emph{ACL}} " + structure.translate({
                    "en": r"\emph{(*: equal contribution, presented in poster and short talk sessions of NewSumm Workshop of EMNLP 2023)}",
                    "ja": r"\emph{（共同第一著者、NewSumm Workshopのポスターと短い講演セッションにて発表）}",
                    "zh": r"\emph{（共一，在EMNLP 2023 NewSumm Workshop的海报展示和短汇报中发表）}"
                }),
                r"\footnotesize " + structure.paper_leading + r"R. Qu, \textbf{R. Tu}, F. Bao (2024). Is Semantic Chunking Worth the Computational Cost? arXiv. \href{https://arxiv.org/abs/2410.13070}{\aiicon{arxiv}} " + structure.translate({
                    "en": r"\emph{(in submission to NAACL 2025)}",
                    "ja": r"\emph{（NAACL 2025 に投稿中）}",
                    "zh": r"\emph{（提交至 NAACL 2025）}"
                }),
                r"\footnotesize " + structure.paper_leading + r"F. Bao, M. Li, R. Qu, G. Luo, E. Wan, Y. Tang, W. Fan, M. Tamber, S. Kazi, V. Sourabh, M. Qi, \textbf{R. Tu}, C. Xu, M. Gonzales, O. Mendelevitch, A. Ahmad (2024). FaithBench: A Diverse Hallucination Benchmark for Summarization by Modern LLMs. arXiv. \href{https://arxiv.org/abs/2410.13210}{\aiicon{arxiv}} " + structure.translate({
                    "en": r"\emph{(in submission to NAACL 2025)}",
                    "ja": r"\emph{（NAACL 2025 に投稿中）}",
                    "zh": r"\emph{（提交至 NAACL 2025）}"
                })
            ])
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": "Independent Researcher",
            "ja": "独立研究者",
            "zh": "独立研究者"
        },
        "date": {
            "en": "November 2023 -- Present",
            "ja": "2023年11月 -- 現在",
            "zh": "2023年11月 -- 现今"
        },
        "subtitle": {
            "en": r"On Japanese NLP",
            "ja": r"日本語のための自然言語処理",
            "zh": r"针对日语的自然语言处理"
        },
        "place": {
            "en": r"Madison, Wisconsin, USA",
            "ja": r"米国\ ウィスコンシン州\ マディソン",
            "zh": r"美国\ 威斯康星州\ 麦迪逊市"
        },
        "body": structure.item_list([
            structure.translate({
                "en": r"Linguistics: Post-Meiji Word Origins in Japanese Literature",
                "ja": r"言語学：明治以降の日本文学における語源分析",
                "zh": r"语言学：日本文学中明治时代以来的词源分析"
            }) + r" \href{https://direct.turx.asia/as434_paper.pdf}{\faIcon[regular]{file-pdf}} \href{https://direct.turx.asia/as434_slide.pdf}{\faIcon[regular]{file-powerpoint}} " + structure.translate({
                "en": "and Role Language Usage in Anime",
                "ja": "とアニメにおける役割語の使用",
                "zh": "和动漫中的角色语言使用"
            }),
            structure.translate({
                "en": r"Classical Japanese: Waka generation",
                "ja": r"古典日本語：和歌生成",
                "zh": r"古典日语：和歌生成"
            }) + r" \href{https://direct.turx.asia/wakagpt.pdf}{\faIcon[regular]{file-pdf}} \href{https://direct.turx.asia/wakagpt_slide.pdf}{\faIcon[regular]{file-powerpoint}} " + structure.translate({
                "en": "and Kuzushiji recognition",
                "ja": "とくずし字認識",
                "zh": "和古文字识别"
            })
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": "Research Assistant (Senior Honors Thesis)",
            "ja": "リサーチアシスタント（Honors 卒業論文）",
            "zh": "研究助理（荣誉毕业论文）"
        },
        "date": {
            "en": "July 2024 -- Present",
            "ja": "2024年7月 -- 現在",
            "zh": "2024年7月 -- 现今"
        },
        "subtitle": {
            "en": r"Prof. Ramya Korlakai Vinayak \& Daiwei Chen, University of Wisconsin--Madison",
            "ja": r"ウィスコンシン大学マディソン校\ Ramya Korlakai Vinayak 教授",
            "zh": r"威斯康星大学麦迪逊校（UW--Madison）\ Ramya Korlakai Vinayak 教授"
        },
        "place": {
            "en": r"Madison, Wisconsin, USA",
            "ja": r"米国\ ウィスコンシン州\ マディソン",
            "zh": r"美国\ 威斯康星州\ 麦迪逊市"
        },
        "body": structure.item_list([
            {
                "en": r"Machine Learning + NLP Research: Generalizability of In-Context Learning for Transformers and Its Applications to Pluralistic Alignment in NLP (main contributor, and sole contributior except for advisors)",
                "ja": r"機械学習+NLP研究：コンテキスト学習のためのトランスフォーマーの汎化性および自然言語処理における多元的アライメントへの応用（主要貢献者）",
                "zh": r"机器学习+NLP研究：Transformer 在上下文学习中的泛化性及其在自然语言处理中的多元对齐应用（主要贡献者）"
            }
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": "Research Assistant (Directed Study)",
            "ja": "リサーチアシスタント（指導研究）",
            "zh": "研究助理（定向研究）"
        },
        "date": {
            "en": "August 2024 -- Present",
            "ja": "2024年8月 -- 現在",
            "zh": "2024年8月 -- 现今"
        },
        "subtitle": {
            "en": r"Prof. Junjie Hu \& Dr. Sean Yun-Shiuan Chuang, University of Wisconsin--Madison",
            "ja": r"ウィスコンシン大学マディソン校\ Junjie Hu 教授・Sean Yun-Shiuan Chuang博士",
            "zh": r"威斯康星大学麦迪逊校（UW--Madison）\ 胡俊杰（Junjie Hu）教授 \& Sean Yun-Shiuan Chuang 博士"
        },
        "place": {
            "en": r"Madison, Wisconsin, USA",
            "ja": r"米国\ ウィスコンシン州\ マディソン",
            "zh": r"美国\ 威斯康星州\ 麦迪逊市"
        },
        "body": structure.item_list([
            {
                "en": r"NLP Research: Opinion Alignment in LLM Agents (analysis and modeling part)",
                "ja": r"NLP研究：LLMエージェントにおける意見アライメント（分析とモデリング部分）",
                "zh": r"NLP研究：LLM Agent的观点对齐（分析和建模部分）"
            }
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": "Research Assistant (WISCERS Program)",
            "ja": "リサーチアシスタント（WISCERS プログラム）",
            "zh": "研究助理（WISCERS 项目）"
        },
        "date": {
            "en": "June 2022 -- August 2023",
            "ja": "2022年6月 -- 2023年8月",
            "zh": "2022年6月 -- 2023年8月"
        },
        "subtitle": {
            "en": "Prof. Xiaojin Jerry Zhu, University of Wisconsin--Madison",
            "ja": r"ウィスコンシン大学マディソン校\ Xiaojin Jerry Zhu教授",
            "zh": r"威斯康星大学麦迪逊校（UW--Madison）\ 朱晓瑾（Xiaojin Jerry Zhu）教授"
        },
        "place": {
            "en": r"Madison, Wisconsin, USA",
            "ja": r"米国\ ウィスコンシン州\ マディソン",
            "zh": r"美国\ 威斯康星州\ 麦迪逊市"
        },
        "body": structure.item_list([
            structure.translate({
                "en": r"Machine teaching research on supervised learning (linear and k-NN)",
                "ja": r"教師あり学習で機械教示を研究",
                "zh": r"研究在监督学习中的机器教学"
            }) + r" \href{https://pages.cs.wisc.edu/~ruixuan/wiscers-23}{\faIcon[regular]{file-code}} \href{https://github.com/TURX/machine-teaching-23sp}{\faIcon{github}}",
            structure.translate({
                "en": "Participant in Reinforcement Learning Theory and Game Theory Reading Groups (Led Chapter of Imitation Learning)",
                "ja": "強化学習理論とゲーム理論輪読の参加者（模倣学習の章を担当）",
                "zh": "强化学习理论和博弈论读书会的参与者（模仿学习章节领读）"
            })
        ]),
        "tag": ["resume"]
    },
    # {
    #     "title": {
    #         "en": "Research Assistant",
    #         "ja": "リサーチアシスタント",
    #         "zh": "研究助理"
    #     },
    #     "date": {
    #         "en": "August 2023 -- June 2024",
    #         "ja": "2023年8月 -- 2024年6月",
    #         "zh": "2023年8月 -- 2024年6月"
    #     },
    #     "subtitle": {
    #         "en": r"Prof. Yiqiao Zhong \& Prof. Junjie Hu, University of Wisconsin--Madison",
    #         "ja": r"ウィスコンシン大学マディソン校\ Yiqiao Zhong教授とJunjie Hu教授",
    #         "zh": r"威斯康星大学麦迪逊校（UW--Madison）\ Yiqiao Zhong和胡俊杰（Junjie Hu）教授"
    #     },
    #     "place": {
    #         "en": r"Madison, Wisconsin, USA",
    #         "ja": r"米国\ ウィスコンシン州\ マディソン",
    #         "zh": r"美国\ 威斯康星州\ 麦迪逊市"
    #     },
    #     "body": structure.item_list([
    #         {
    #             "en": r"NLP Research in LLM representation of toxic tweets and analysis of inter-layer relations",
    #             "ja": r"自然言語処理研究：大規模言語モデル有害なツイートにおいての表現と層間関係の分析",
    #             "zh": r"自然语言处理研究: 大语言模型有害推文的表示和层间关系分析"
    #         }
    #     ]),
    #     "tag": ["resume"]
    # },
    # {
    #     "title": {
    #         "en": "Participant, Computer Science Seminars",
    #         "ja": r"コンピューターサイエンスゼミナー\ 参加者",
    #         "zh": r"计算机科学研讨班\ 参加者"
    #     },
    #     "date": {
    #         "en": "June 2022 -- Present",
    #         "ja": "2022年6月 -- 現在",
    #         "zh": "2022年6月 -- 现今"
    #     },
    #     "subtitle": {
    #         "en": "Department of Computer Sciences, University of Wisconsin--Madison",
    #         "ja": r"ウィスコンシン大学マディソン校\ 情報科学科",
    #         "zh": r"威斯康星大学麦迪逊校（UW--Madison）\ 计算机科学系"
    #     },
    #     "place": {
    #         "en": r"Madison, Wisconsin, USA",
    #         "ja": r"米国\ ウィスコンシン州\ マディソン",
    #         "zh": r"美国\ 威斯康星州\ 麦迪逊市"
    #     },
    #     "body": structure.item_list([
    #         structure.itemize([
    #         # {
    #         #     "en": "LLM Geometry and Interprebility Reading Group by Prof. Yiqiao Zhong (June 2024 -- August 2024)",
    #         #     "ja": "大規模言語モデルの幾何学と解釈性輪読（Yiqiao Zhong教授が主催、2024年6月 -- 2024年8月）",
    #         #     "zh": "大语言模型几何与可解释性读书会 (由 Yiqiao Zhong 教授主持，2024年6月 -- 2024年8月)"
    #         # },
    #         {
    #             "en": "Reinforcement Learning Theory and Game Theory Reading Groups by Prof. Xiaojin Jerry Zhu (June 2022 -- September 2023)",
    #             "ja": "強化学習理論とゲーム理論輪読（Xiaojin Jerry Zhu教授が主催、2022年6月 -- 2023年9月）",
    #             "zh": "强化学习理论和博弈论读书会 (由 Xiaojin Jerry Zhu 教授主持，2022年6月 -- 2023年9月)"
    #         },
    #         {
    #             "en": "Graph Neural Network (Directed Reading Program, Department of Mathematics) by PhD student Karan Srivastava (February 2023 -- April 2023)",
    #             "ja": "グラフニューラルネットワーク（数学科の指導読書プログラム）（PhD学生Karan Srivastavaが主催、2023年2月 -- 2023年4月）",
    #             "zh": "图神经网络 (数学系导读项目) (由博士生Karan Srivastava主持，2023年2月 -- 2023年4月)"
    #         },
    #         # {
    #         #     "en": "Reinforcement Learning Empirical Applications Reading Group by Prof. Josiah Hanna (July 2022 -- February 2023)",
    #         #     "ja": "強化学習応用読書会（Josiah Hanna教授が主催、2022年7月 -- 2023年2月）",
    #         #     "zh": "强化学习应用读书会 (由 Josiah Hanna 教授主持，2022年7月 -- 2023年2月)"
    #         # },
    #         {
    #             "en": "Machine Learning Lunch Meeting by Prof. Xiaojin Jerry Zhu and Machine Learning Group (February 2023 -- March 2023)",
    #             "ja": "機械学習ランチミーティング（Xiaojin Jerry Zhu教授と機械学習研究グループが共催、2023年2月 -- 2023年3月）",
    #             "zh": "机器学习午餐会 (由 Xiaojin Jerry Zhu 教授和机器学习研究组主持，2023年2月 -- 2023年3月)"
    #         }
    #         ])
    #     ]),
    #     "tag": ["resume"]
    # },
    # {
    #     "title": {
    #         "en": "Mentee, Directed Reading Program",
    #         "ja": r"指導読書プログラム\ 聴講生",
    #         "zh": r"导读项目\ 学生"
    #     },
    #     "date": {
    #         "en": "February 2023 -- April 2023",
    #         "ja": "2023年2月 -- 2023年4月",
    #         "zh": "2023年2月 -- 2023年4月"
    #     },
    #     "subtitle": {
    #         "en": "Department of Mathematics, University of Wisconsin--Madison",
    #         "ja": r"ウィスコンシン大学マディソン校\ 数学科",
    #         "zh": r"威斯康星大学麦迪逊校 (UW--Madison)\ 数学系"
    #     },
    #     "place": {
    #         "en": r"Madison, Wisconsin, USA",
    #         "ja": r"米国\ ウィスコンシン州\ マディソン",
    #         "zh": r"美国\ 威斯康星州\ 麦迪逊市"
    #     },
    #     "body": structure.item_list([
    #         {
    #             "en": "Learned Graph Neural Network along with combinatorics and graph theory under PhD student Karan Srivastava.",
    #             "ja": "博士課程の大学院生のKaran Srivastavaの指導で、組み合わせ数学とグラフ理論においてグラフニューラルネットワークを学んだ",
    #             "zh": "在博士生Karan Srivastava的指导下，学习了组合数学和图论以及图神经网络"
    #         },
    #         # {
    #         #     "en": "This program pairs undergraduate students with graduate mentors for semester-long independent studies. During the semester, the student will work through a mathematical text and meet weekly to discuss it with their mentor.",
    #         #     "ja": "本プログラムは、大学生と大学院生のメンターを1学期間の独立した研究にペアリングするものです。学期中、学生は数学のテキストを通して取り組み、週に1度メンターとのディスカッションを行います",
    #         #     "zh": "该项目将本科生与研究生导师配对，进行为期一个学期的独立学习。在学期期间，学生将通过数学课本进行学习，并每周与导师讨论"
    #         # }
    #     ]),
    #     "tag": ["resume"]
    # },
    # TODO: ICPC
    {
        "title": {
            "en": "Tencent Rhino-Bird High School Scholars Program/Industry-Academia Camp",
            "ja": "テンセントRhino-Bird高校学者プログラム",
            "zh": r"腾讯犀牛鸟中学科学人才培养计划\& 犀牛鸟研学营"
        },
        "date": {
            "en": "April 2021 -- August 2021",
            "ja": "2021年4月 -- 2021年8月",
            "zh": "2021年4月 -- 2021年8月"
        },
        "subtitle": {
            "en": r"Tsinghua University \& China Computer Federation \& Tencent University Relations",
            "ja": r"清華大学\&中国計算機学会\&テンセント産学連携課",
            "zh": r"清华大学 \& 中国计算机学会 \& 腾讯高校合作"
        },
        "place": {
            "en": "(Remote) China",
            "ja": "（リモート）中国",
            "zh": "（远程）中国"
        },
        "body": structure.item_list([
            structure.itemize([
                {
                    "en": "Certificates: Rhino-Bird Scholar Award, Outstanding Student, Certificates of Completion",
                    "ja": "賞：Rhino-Bird学者賞、優秀生徒、修了証書",
                    "zh": "证书: 犀牛鸟小学者、优秀营员、结营证书"
                },
                {
                    "en": r"Proposal: \textit{An Improved Approach of Speaking Proficiency Evaluation of English as a Second Language}",
                    "ja": r"提案：\textit{An Improved Approach of Speaking Proficiency Evaluation of English as a Second Language}",
                    "zh": r"开题报告: \textit{An Improved Approach of Speaking Proficiency Evaluation of English as a Second Language}"
                },
                {
                    "en": r"Report: \textit{Models in Natural Language Understanding Tasks}",
                    "ja": r"レポート：\textit{Models in Natural Language Understanding Tasks}",
                    "zh": r"结营报告: \textit{自然语言处理技术在语言理解任务的模型的调研报告}"
                }
            ])
        ]),
        "tag": ["resume-zh"]
    }
    # TODO: CIS
]

resumeSubHeadings_code = structure.subheading_list(resumeSubHeadings)

code = r"""
\section{""" + r"\faIcon{vial} " + structure.translate({
    "en": "Academic Experience",
    "ja": "学術",
    "zh": "学术经历"
}) + r"}" + resumeSubHeadings_code
