import structure

code = r"""
\section{""" + structure.translate({
    "en": r"Projects",
    "ja": r"プロジェクト",
    "zh": r"项目"
}) + r"}" + "\n" + structure.projectheading_list([
    {
        "title": {
            "en": r"\textbf{KDE Connect (Apple Continuity-like Experience)} $|$ \emph{Swift, Objective-C, C++ (Qt)}",
            "ja": r"\textbf{KDE Connect（Apple Continuityのような体験）} $|$ \emph{Swift, Objective-C, C++ (Qt)}",
            "zh": r"\textbf{KDE Connect (Apple连续互通体验)} $|$ \emph{Swift, Objective-C, C++ (Qt)}"
        },
        "date": {
            "en": r"KDE, November 2018 - Present",
            "ja": r"（KDE）2018年11月 - 現在",
            "zh": r"KDE, 2018年11月 - 现今"
        },
        "body": structure.item_list([
            structure.itemize([
                {
                    "en": r"Lead Developer of macOS version (new UI, device list, secure connection, plugin ports; GSoC'22 proposal)",
                    "ja": r"KDE ConnectのmacOSバージョンのリードデベロッパ（新しいUI、セキュア接続、プラグイン移植）",
                    "zh": r"macOS版本主要开发者 (新UI、设备列表、加密连接、插件移植; GSoC'22开题报告)"
                },
                {
                    "en": r"Developer and Reviewer of iOS version (About view, background execution with location, trusted networks)",
                    "ja": r"KDE ConnectのiOSバージョンのデベロッパとレビュアー（Aboutビュー、バックグラウンド実行）",
                    "zh": r"iOS版本开发者、审核 (“关于”界面、使用位置的后台执行、网络信任)"
                },
                {
                    "en": r"Maintainer of App Store Connect for release and troubleshooting",
                    "ja": r"App Store Connectのメンテナンス（リリースとトラブルシューティング）",
                    "zh": r"App Store Connect维护者 (版本发布、用户反馈)"
                },
                {
                    "en": r"Contribution to Android and Linux versions (new conversation in Android SMS)",
                    "ja": r"AndroidとLinuxのバージョンへの貢献（Android SMSの新しい会話）",
                    "zh": r"Android和Linux版本贡献者 (Android创建新短信会话)"
                }
            ])
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": r"\textbf{Highlighted Course Projects} $|$ \emph{C, C++, Python, Java}",
            "ja": r"\textbf{授業の課題とプロジェクト} $|$ \emph{C, C++, Python}",
            "zh": r"\textbf{课程项目} $|$ \emph{C, C++, Python}"
        },
        "date": {
            "en": r"February 2022 - Present",
            "ja": r"2022年2月 - 現在",
            "zh": r"2022年2月 - 现今"
        },
        "body": structure.item_list([
            structure.itemize([
                {
                    "en": r"OS: xv6 trace count for syscall; priority-based scheduler, virtual memory extension; threading with spin lock",
                    "ja": r"OS：xv6でsyscallの呼び出し回数、優先度ベースのスケジューラ、仮想メモリ、スピンロックでのスレッド",
                    "zh": r"操作系统：xv6系统调用跟踪计数器; 基于优先级的调度器, 虚拟内存扩展; 基于自旋锁的线程实现"
                },
                {
                    "en": r"OS: distributed network file system with both server and client on idempotent UDP-based protocol",
                    "ja": r"OS：分散ネットワークファイルシステムのサーバとクライアントをUDPプロトコルで実装",
                    "zh": r"操作系统：分布式网络文件系统, 实现了基于幂等UDP协议的服务端和客户端"
                },
                {
                    "en": r"OS: wish -- Unix shell to execute program, supporting \texttt{cd}, \texttt{path}, \texttt{exit}, redirection, error, and \texttt{if} statements",
                    "ja": r"OS：wish -- プログラムを実行できるUnixシェル、\texttt{cd}・\texttt{path}・リダイレクション・エラー・\texttt{if}文のサポート",
                    "zh": r"操作系统：wish -- 用来执行程序的Unix shell, 支持\texttt{cd}, \texttt{path}, \texttt{exit}, 重定向, 错误, 和\texttt{if}语句"
                },
                {
                    "en": r"Database: relational database buffer manager, heapfile manager, operations (\texttt{select}, \texttt{delete}, \texttt{insert})",
                    "ja": r"DB：関係型データベースのバファーマネージャ、ヒープファイルマネージャ、SQLによる操作",
                    "zh": r"数据库：关系数据库缓冲管理器, 堆文件管理器, 用户操作后端 (\texttt{select}, \texttt{delete}, \texttt{insert})"
                },
                # {
                #     "en": r"AI: Principle Component Analysis on Face Dataset; Hierarchical Clustering on Item Statistics",
                #     "ja": r"AI：顔データセットにの主成分分析、アイテム統計に対する階層的クラスタリング",
                #     "zh": r"人工智能: 人脸数据集的主成分分析; 物品统计的层次聚类"
                # },
                # {
                #     "en": r"AI: Heuristic Player for Teeko Board Game and 8-tile Puzzle; Q-Learning Agent to Find Treasure in Environment",
                #     "ja": r"AI：Teeko Board Gameのと8タイルパズルの発見的プレーヤー、宝探しQ学習エージェント",
                #     "zh": r"人工智能: Teeko棋和8方块游戏的启发式玩家; 寻宝环境中的Q学习代理"
                # },
                {
                    "en": r"PL: Compiler for a subset of C Programming Language",
                    "ja": r"PL：C言語の部分のためのコンパイラの実装",
                    "zh": r"程序语言：C语言子集的编译器实现"
                },
                {
                    "en": r"Optimization: Flight Fare Optimization with MIP; Implementation/Analysis of various descent methods",
                    "ja": r"OPT：MIPによるフライト運賃の最適化、様々な降下法の実装と解析",
                    "zh": r"优化：机票价格优化（MIP）；实现和分析各种下降方法"
                },
                {
                    "en": r"Japanese Linguistics: Estimated trends by predictions of origin of words using language model",
                    "ja": r"日本語言語学：言語モデルを使って単語の起源の予測による動向の推定",
                    "zh": r"日语语言学：使用语言模型预测词源、估计趋势"
                }
            ])
        ]),
        "tag": ["resume"]
    },
    {
        "title": {
            "en": r"\textbf{aitc19x/VR-JC} $|$ \emph{C\# (Unity)}",
            "ja": r"\textbf{aitc19x/VR-JC} $|$ \emph{C\# (Unity)}",
            "zh": r"\textbf{aitc19x/VR-JC} $|$ \emph{C\# (Unity)}"
        },
        "date": {
            "en": r"GitHub, August 2019 - December 2020",
            "ja": r"（GitHub）2019年8月 - 2020年12月",
            "zh": r"GitHub, 2019年8月 - 2020年12月"
        },
        "body": structure.item_list([
            {
                "en": r"Mixed reality project for viewing 2D and 3D models in 6DoF collaborated with NIT Akashi College in Japan",
                "ja": r"日本の明石高専との共同プロジェクトで、2D/3Dモデルを6DoFで表示するVRプロジェクト",
                "zh": r"混合现实项目, 在6DoF环境内查看2D和3D模型, 与日本明石高等专门学校合作"
            }
        ]),
        "tag": None
    }
    # TODO: Haiku OS
])
