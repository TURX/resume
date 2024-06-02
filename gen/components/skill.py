import structure

colon = structure.translate({
    "en": ": ",
    "ja": "：",
    "zh": ": "
})

code = r"""
\section{""" + structure.translate({
    "en": r"Skills",
    "ja": r"スキル",
    "zh": r"技能"
}) + r"}" + "\n" + structure.itemize(
[
    {
        "en": r"\textbf{Computer Science}",
        "ja": r"\textbf{コンピューターサイエンス}",
        "zh": r"\textbf{计算机科学}"
    },
    structure.itemize([
        -2,  # vspace
        structure.translate({
            "en": r"Programming Languages",
            "ja": r"プログラミング言語",
            "zh": r"编程语言"
        }) + colon + r"Python, Java/Kotlin, C/C++, JavaScript/TypeScript (NestJS, React, MUI), Objective-C/Swift, C\# (.NET, Mono, Unity), Bash, Assembly (LC-3, AT\&T), PHP, Visual Basic, Lisp, ASP",
        structure.translate({
            "en": r"Web/Markup Languages",
            "ja": r"Web/Markup言語",
            "zh": r"网页/排版语言"
        }) + colon + r"\LaTeX, Markdown (Pandoc), HTML, CSS",
        structure.translate({
            "en": r"Machine Learning/Data Science",
            "ja": r"機械学習/データ科学",
            "zh": r"机器学习/数据科学"
        }) + colon + r"HuggingFace, PyTorch/TensorFlow/NumPy/Pandas, R, Julia, SQL, MATLAB",
        structure.translate({
            "en": r"Developer Tools",
            "ja": r"デベロッパツール",
            "zh": r"开发工具"
        }) + colon + r"Git, Visual Studio Code, IntelliJ IDEA, Docker, Vim, Visual Studio, Unity Editor, Qt Creator",
        structure.translate({
            "en": r"Operating Systems",
            "ja": r"オペレーティングシステム",
            "zh": r"操作系统"
        }) + colon + r"macOS, Linux (Ubuntu, Debian, OpenWRT, WSL), Windows"
    ], r"leftmargin=0.15in", structure._item_list_item),
    {
        "en": r"\textbf{Natural Languages}",
        "ja": r"\textbf{自然言語}",
        "zh": r"\textbf{自然语言}"
    },
    structure.itemize([
        -2,  # vspace
        {
            "en": r"First Language: Chinese (Mandarin, Gan)",
            "ja": r"ネイティブ：中国語（標準語・贛語）",
            "zh": r"母语: 中文（普通话、赣语）"
        },
        {
            "en": r"Fluent: English (TOEFL 103/120), Japanese (JLPT N1 154/180, 95.4 Percentile)",
            "ja": r"流暢：英語（TOEFL 103/120）、日本語（JLPT N1 154/180、95.4パーセンタイル）",
            "zh": r"流畅: 英文（托福103/120）、日语（日语能力考JLPT N1 154/180，超过95.4\%考生）"
        },
        # {
        #     "en": r"Beginner: Korean",
        #     "ja": r"初心者：韓国語",
        #     "zh": r"入门: 韩文"
        # }
    ], r"leftmargin=0.15in", structure._item_list_item)
], r"leftmargin=0.15in, label={}", structure._item_list_item)
