抓取B站视频排行榜
这是一个用于抓取B站视频排行榜的Python程序。该程序可以从指定的B站排行榜页面抓取视频的标题和链接，并将其保存到Excel文件中。

依赖
Python 3.x
requests
BeautifulSoup4
pandas
XlsxWriter
可以通过以下命令安装所需的依赖：

Copy code
pip install requests BeautifulSoup4 pandas XlsxWriter
如何使用
打开 config.py 文件，修改 URL 变量为你想要抓取的B站排行榜页面链接。
打开终端或命令行，进入程序所在的目录。
输入以下命令来运行程序：
css
Copy code
python main.py
程序将自动抓取排行榜页面的数据，并将结果保存为名为 bilibili_rankings-<当前日期时间>.xlsx 的Excel文件，该文件将保存在程序所在的目录中。
注意事项
Excel文件名将包括当前日期时间的信息，例如 bilibili_rankings-2022-04-04 16:30:00.xlsx。
Excel文件中将不会有任何框线，第一列将显示当前的实际时间，表格内所有字体将为微软雅黑。
