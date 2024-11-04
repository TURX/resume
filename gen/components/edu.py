import type
import structure

resumeSubHeadings: type.ResumeSubHeadingList = [
    {
        "title": {
            "en": "University of Wisconsin--Madison",
            "ja": "ウィスコンシン大学マディソン校（University of Wisconsin--Madison）",
            "zh": "威斯康星大学麦迪逊校（University of Wisconsin--Madison）"
        },
        "date": {
            "en": "September 2021 -- Present",
            "ja": "2021年9月 -- 現在",
            "zh": "2021年9月 -- 现今"
        },
        "subtitle": {
            "en": r"\makecell[lt]{\textit{\small Bachelor of Science in Computer Sciences (Honors), Mathematics (Honors), \&} \\ \textit{\small \hspace{99pt} Data Science, Statistics, Japanese}}",
            "ja": r"\makecell[lt]{\textit{\small 学士（理学）：情報科学（Honors）・数学（Honors）・} \\ \textit{\small \hspace{70pt} データ科学・統計学・日本学\, 専攻}}",
            "zh": r"\makecell[lt]{\textit{\small 理学学士：计算机科学（荣誉）、数学（荣誉）、数据科学、统计学、日本学}}"
        },
        "place": {
            "en": r"\makecell[rt]{\textit{\small Madison, Wisconsin, USA}}",
            "ja": r"\makecell[rt]{\textit{\small 米国\ ウィスコンシン州\ マディソン}}",
            "zh": r"\makecell[rt]{\textit{\small 美国\ 威斯康星州\ 麦迪逊市}}"
        },
        "body": structure.item_list([
            {
                "en": r"""
                \begin{tabular*}{0.94\textwidth}[t]{l @{\extracolsep{\fill}} c @{\extracolsep{\fill}} r}
                    \textbf{GPA}: 3.864/4.0 & \textbf{Credits}: 229 (2 times of graduation requirement) &
                \end{tabular*}
                """,
                "ja": r"""
                \begin{tabular*}{0.94\textwidth}[t]{l @{\extracolsep{\fill}} c @{\extracolsep{\fill}} r}
                    \textbf{GPA}：3.864/4.0 & \textbf{単位}：229（二回分の卒業単位数） &
                \end{tabular*}
                """,
                "zh": r"""
                \begin{tabular*}{0.94\textwidth}[t]{l @{\extracolsep{\fill}} c @{\extracolsep{\fill}} r}
                    \textbf{GPA}：3.864/4.0 & \textbf{学分}：229（毕业要求的两倍）
                \end{tabular*}
                """
            },
            {
                "en": r"""
                \textbf{Honors}: Dean's List (Fall 2021 -- Fall 2022), Undergraduate Scholarship for Summer Study (2023, 2024)
                """,
                "ja": r"""
                \textbf{賞}：学部長表彰者（2021秋・2022春・2022秋）、学部生夏学期奨学金（2023・2024）
                """,
                "zh": r"""
                \textbf{荣誉}：院长嘉许名单（2021年秋季、2022年春季、2022年秋季）、本科生暑期奖学金（2023、2024）
                """
            },
            r"\faIcon{chalkboard-teacher} " + structure.translate({
                "en": "Taking PhD-level (graduate only) courses generally not allow undergraduate students to take",
                "ja": "原則学部生が履修できない、博士課程かつ最難関の700-899番の授業を履修している",
                "zh": "正在修读最难的博士难度（仅研究生）700-899号课程，通常不允许本科生修读"
            }),
            # {
            #     "en": r"""
            #     \textbf{Computer Sciences Courses}: Intro-Discrete Mathematics, Intro-Computer Engineering, Machine Organization \& Programming, Programming II/III, Intro-Artificial Intelligence, Intro-Operating Systems, Database Management Systems, Intro-Algorithms (Honors), Intro-Programming Languages \& Compilers, Intro-Optimization, Linear Optimization, Data Science Programming II, Intro-Theory of Computing, Nonlinear Optimization I (Grad), Mathematical Foundations of Machine Learning (Grad)
            #     """,
            #     "ja": r"""
            #     \textbf{コンピューターサイエンスの授業}：離散数学基礎、コンピューターエンジニアリング基礎、計算機構成とプログラミング、プログラミング II/III、人工知能基礎、オペレーティングシステム基礎、データベース管理システム、アルゴリズム基礎（Honors）、プログラミング言語とコンパイラ基礎、最適化基礎、線形最適化、データ科学プログラミング II、計算理論基礎、非線形最適化 I（院）、機械学習の数学（院）
            #     """,
            #     "zh": r"""
            #     \textbf{计算机科学课程}：离散数学基础、计算机工程基础、机器组成和编程、编程二/三、人工智能基础、操作系统基础、数据库管理系统、算法基础（荣誉）、编程语言和编译器基础、最优化基础、线性优化、数据科学编程二、计算理论基础、非线性优化一（研）、机器学习的数学基础（研）
            #     """
            # },
            {
                "en": r"\footnotesize \textbf{Machine Learning-Related Computer Sciences Courses}: Artificial Intelligence, Linear Optimization, Nonlinear Optimization I (Grad), Mathematical Machine Learning (Grad), Game Theory and Learning",
                "ja": r"\textbf{機械学習関連のコンピューターサイエンスの授業}：人工知能、線形最適化、非線形最適化 I（院）、機械学習の数学（院）、ゲーム理論とメカニズムデザイン",
                "zh": r"\textbf{机器学习相关的计算机科学课程}：人工智能、线性优化、非线性优化一（研）、机器学习的数学（研）、博弈论和机制设计"
            },
            {
                "en": r"""
                \footnotesize \textbf{Other Computer Sciences Courses}: Operating Systems, Database Management Systems, Programming Languages \& Compilers, Algorithms (Honors), Theory of Computing
                """,
                "ja": r"""
                \textbf{コンピューターサイエンスの授業}：オペレーティングシステム、データベース管理システム、プログラミング言語とコンパイラ、アルゴリズム（Honors）、計算理論
                """,
                "zh": r"""
                \textbf{计算机科学课程}：操作系统基础、数据库管理系统、编程语言和编译器、算法（荣誉）、计算理论
                """
            },
            {
                "en": r"""
                \footnotesize \textbf{Mathematics Courses}: Linear Algebra (Honors), Combinatorics, Analysis I (Honors)/II (Honors), Modern Algebra I (Honors)/II (Honors), Topology (Honors), Real Analysis I (Measure Theory, Grad)/II (Functional Analysis, Grad, 50\% complete), Stochastic Processes (Honors), Theory of Probability I (Grad)
                """,
                "ja": r"""
                \textbf{数学の授業}：線型代数（Honors）、組合せ数学、解析 I（Honors）/II（Honors）、現代代数 I（Honors）/II（Honors）、位相幾何学（Honors）、実解析 I（測度論/院）/II（関数解析/院/半分）、確率過程（Honors）、確率論（院）
                """,
                "zh": r"""
                \textbf{数学课程}：线性代数（荣誉）、组合数学、数学分析一（荣誉）/二（荣誉）、近世代数一（荣誉）/二（荣誉）、基础拓扑学（荣誉）、实变函数一（测度论/研）/二（泛函分析/研/一半）、随机过程（荣誉）、概率论（研）
                """
            },
            {
                "en": r"""
                \footnotesize \textbf{Selected Other Major Courses}: Classical Japanese, The Tale of Genji, Japanese Linguistics, Japanese Sociolinguistics, Probability and Mathematical Statistics II
                """,
                "ja": r"""
                \textbf{他専攻の授業}：日本文語、日本古典文学--源氏物語、日本語言語学、日本語社会言語学、数理統計学 II
                """,
                "zh": r"""
                \textbf{其他专业课程}：古典日语、日本古典文学--源氏物语、日语语言学、日语社会语言学、数理统计学二
                """
            }
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": "Attached High School to Jiangxi Normal University",
            "ja": "江西師範大学附属中学",
            "zh": "江西师范大学附属中学"
        },
        "date": {
            "en": "September 2018 -- June 2021",
            "ja": "2018年9月 -- 2021年6月",
            "zh": "2018年9月 -- 2021年6月"
        },
        "subtitle": {
            "en": r"Honors Senior High School Diploma",
            "ja": r"高等学校卒業証明書",
            "zh": r"普通高中毕业证"
        },
        "place": {
            "en": r"Nanchang, Jiangxi, China",
            "ja": r"中国\ 江西省\ 南昌市",
            "zh": r"中国\ 江西省\ 南昌市"
        },
        "body": structure.item_list([
            {
                "en": r"""
                \begin{tabular*}{0.94\textwidth}[t]{l @{\extracolsep{\fill}} c @{\extracolsep{\fill}} r}
                    Weighted GPA: 4.325/4.0 & Unweighted GPA: 3.816/4.0 & Cumulative Credits: 28.500
                \end{tabular*}
                """,
                "ja": r"""
                \begin{tabular*}{0.94\textwidth}[t]{l @{\extracolsep{\fill}} c @{\extracolsep{\fill}} r}
                    加重GPA：4.325/4.0 & 加重なしGPA：3.816/4.0 & 修得単位数：28.500
                \end{tabular*}
                """,
                "zh": r"""
                \begin{tabular*}{0.94\textwidth}[t]{l @{\extracolsep{\fill}} c @{\extracolsep{\fill}} r}
                    加权GPA：4.325/4.0 & 非加权GPA：3.816/4.0 & 学分：28.500
                \end{tabular*}
                """
            },
            {
                "en": r"""
                Honors: School Role Model (2021), Sino-U.S. Program Scholar (2020), Outstanding School Club Leader (2020)
                """,
                "ja": r"""
                賞：校模範生（2021）、中米プログラム優等卒業生（2020）、優秀学生部長（2020）
                """,
                "zh": r"""
                荣誉：青春榜样（2021）、中美班荣誉毕业生（2020）、优秀学生社团社长（2020）
                """
            }
        ]),
        "tag": ["resume-zh", "resume-ja"]
    }
]

resumeSubHeadings_code = structure.subheading_list(resumeSubHeadings)

code = r"""
\section{""" + r"\faIcon{university} " + structure.translate({
    "en": "Education",
    "ja": "学歴",
    "zh": "教育"
}) + r"}" + resumeSubHeadings_code
