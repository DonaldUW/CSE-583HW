# CSE 583 作业 1：自行车数据分析
# CSE 583 Homework 1: Bicycle Data Analysis

## 数据集
## Dataset

本作业使用从 2012 年开始记录的 Fremont Bridge 每小时自行车通行数量数据。
This homework uses hourly bicycle counts recorded at the Fremont Bridge beginning in 2012.

- 数据集介绍：<https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k>
- Dataset description: <https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k>
- CSV 下载地址：<https://data.seattle.gov/api/views/65db-xm6k/rows.csv>
- CSV download: <https://data.seattle.gov/api/views/65db-xm6k/rows.csv>

## 要求的文件夹结构
## Required Folder Structure

```text
hw1/
├── pyproject.toml
├── README.md
└── src/
    └── hw1_data_analysis/
        ├── __init__.py
        ├── hw1.py
        └── bicycle_data.csv
```

`pyproject.toml` 中的项目名称使用连字符 `hw1-data-analysis`。
The project name in `pyproject.toml` uses hyphens: `hw1-data-analysis`.

Python 包的文件夹名称使用下划线 `hw1_data_analysis`。
The Python package directory uses underscores: `hw1_data_analysis`.

## 作业要求
## Assignment Requirements

所有数据分析代码都应在 `src/hw1_data_analysis/hw1.py` 中完成。
Complete all data-analysis work in `src/hw1_data_analysis/hw1.py`.

- [x] 将 CSV 文件读取到 Pandas DataFrame 中。**（1 分）**
  Read the CSV file into a Pandas DataFrame. **(1 point)**
- [x] 在代码注释中描述 DataFrame 的各个列，以及这些列应当使用的数据类型；如果实际类型不符合预期，需要进行转换。**（1 分）**
  In a code comment, describe the DataFrame columns and their expected data types; correct any types that do not match. **(1 point)**
- [x] 添加一列，存储 East 和 West 两侧自行车数量之和。**（1 分）**
  Add a column containing the sum of the East and West bicycle counts. **(1 point)**
- [x] 添加一列，存储一天中的小时数。**（1 分）**
  Add a column containing the hour of the day. **(1 point)**
- [x] 添加一列，存储年份。**（1 分）**
  Add a column containing the year. **(1 point)**
- [x] 创建一个只包含 2016 年数据的新 DataFrame。**（1 分）**
  Create a new DataFrame containing only observations from 2016. **(1 point)**
- [x] 检查 2016 年 DataFrame 中是否存在数据缺失的时间点，确保缺失值不会影响绘图和最繁忙时段计算，并在代码注释中写出缺失数据点的数量。**（1 分）**
  Check the 2016 DataFrame for time points with missing data, prevent missing values from affecting the plot and busiest-hour calculation, and record the number of missing points in a code comment. **(1 point)**
- [x] 使用 Pandas 和 Matplotlib 绘制 2016 年各小时的自行车数量，添加合适的标题和坐标轴名称，并将图片保存为 `counts_by_hour.png`。**（1 分）**
  Use Pandas and Matplotlib to plot the 2016 bicycle counts by hour, add a suitable title and axis labels, and save the figure as `counts_by_hour.png`. **(1 point)**
- [x] 通过 Python 和 Pandas 计算平均而言一天中最繁忙的小时，并将结果写在代码注释中。**（1 分）**
  Use Python and Pandas to calculate the busiest hour of the day on average, and write the result in a code comment. **(1 point)**
- [x] 在 README 中描述完成作业的过程；如果使用了 AI 辅助，需要如实说明。**（1 分）**
  Describe the homework process in the README and disclose any AI assistance. **(1 point)**
- [ ] 将完成的作业推送到 GitHub，但不要上传 CSV 数据文件。
  Push the completed homework to GitHub without uploading the CSV data file.
- [ ] 在 Canvas 中提交 GitHub 仓库链接。
  Submit the GitHub repository link on Canvas.

## 当前准备进度
## Current Setup Progress

- [x] 已创建 `hw1` 文件夹。
  Created the `hw1` directory.
- [x] 已创建 `src/hw1_data_analysis` 文件夹。
  Created the `src/hw1_data_analysis` directory.
- [x] 已创建包含指定项目信息和依赖项的 `pyproject.toml`。
  Created `pyproject.toml` with the required project information and dependencies.
- [x] 已创建空的 `src/hw1_data_analysis/__init__.py`。
  Created an empty `src/hw1_data_analysis/__init__.py`.
- [x] 已创建并完成 `src/hw1_data_analysis/hw1.py`。
  Created and completed `src/hw1_data_analysis/hw1.py`.
- [x] 已下载 CSV，并保存为 `src/hw1_data_analysis/bicycle_data.csv`。
  Downloaded the CSV as `src/hw1_data_analysis/bicycle_data.csv`.
- [x] 已添加 `.gitignore`，避免将下载的 CSV 上传到 GitHub。
  Added `.gitignore` so the downloaded CSV is not uploaded to GitHub.
- [x] 已在 `hw1/.venv` 的 Python 3.13 环境中安装项目依赖。
  Installed the project dependencies in the Python 3.13 environment at `hw1/.venv`.
- [x] 完成并测试数据分析。
  Completed and tested the data analysis.
- [x] 检查生成的图表。
  Inspected the generated plot.
- [x] 完成下面的作业过程描述和 AI 使用声明。
  Finished the process description and AI disclosure below.
- [ ] 提交并推送作业。
  Commit and push the homework.

## 重要提示
## Important Hints

日期字段包含年、月、日和小时，可以将其转换成 datetime 类型，或者通过 Python 分别提取年份和小时。
The date field contains the year, month, day, and hour; convert it to a datetime value or extract the year and hour with Python.

创建初始目录时，下载的 CSV 包含以下列：
When the initial setup was created, the downloaded CSV contained these columns:

- `Date`
- `Fremont Bridge Sidewalks, south of N 34th St Total`
- `Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk`
- `Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk`

可以参考 Pandas 文档和示例，学习读取 CSV、转换日期时间、处理缺失值、数据分组以及使用 Matplotlib 绘图。
Consult the Pandas documentation and examples for reading CSV files, converting datetimes, handling missing values, grouping data, and plotting with Matplotlib.

可以使用 Jupyter Notebook 进行探索，但老师要求的全部内容最终都必须出现在纯 Python 文件 `hw1.py` 中。
A Jupyter Notebook may be used for exploration, but every required part must also appear in the pure Python file `hw1.py`.

## Bonus 加分项
## Bonus

将完整的 `Date` 列转换为日期时间格式，例如 Python 的 `datetime.datetime`、NumPy 的 `datetime64` 或 Pandas 默认的 datetime 格式。
Convert the complete `Date` column to a datetime representation such as Python `datetime.datetime`, NumPy `datetime64`, or Pandas' default datetime format.

在 README 中解释这些日期时间格式之间的区别；使用多种 Markdown 语法也可能获得额外的学习加分。
Explain the differences among these datetime formats in the README; using several kinds of Markdown syntax may also earn additional learning credit.

Python 的 `datetime.datetime` 表示单个日期时间对象，适合一般 Python 程序中的日期操作。
Python's `datetime.datetime` represents one date-time object and is useful for general date operations in Python programs.

NumPy 的 `datetime64` 适合高效保存和计算日期时间数组。
NumPy's `datetime64` is designed for efficiently storing and calculating arrays of date-time values.

Pandas 的 datetime 列建立在 NumPy 日期时间类型之上，并提供 `.dt.year`、`.dt.hour` 等方便的表格数据操作。
Pandas datetime columns build on NumPy date-time types and provide convenient tabular operations such as `.dt.year` and `.dt.hour`.

## 作业过程描述
## Process Description

我首先使用 Pandas 将 CSV 文件读取为 DataFrame，并检查列名和数据类型。自行车计数列是 `float64`，因为其中可能包含缺失值；我将 `Date` 列转换为 Pandas datetime 类型。
I first used Pandas to read the CSV file into a DataFrame and inspected the column names and data types. The bicycle-count columns were `float64` because they could contain missing values, and I converted the `Date` column to Pandas datetime.

随后，我将 East 和 West 两侧的自行车数量相加生成 `total` 列，并从 `Date` 中提取 `Hour` 和 `Year`。我筛选出 2016 年的 8,784 条记录，发现其中有一个自行车计数缺失的时间点，并在后续分析前排除了该行。
Next, I added the East and West bicycle counts to create the `total` column and extracted `Hour` and `Year` from `Date`. I filtered the 8,784 observations from 2016, found one time point with missing bicycle counts, and excluded that row before the remaining analysis.

我按小时对 2016 年的自行车数量分组并求和，使用 Matplotlib 创建带有标题和坐标轴标签的折线图，并将其保存为 `counts_by_hour.png`。我还计算了各小时的平均自行车数量，并使用 `idxmax()` 确定平均最繁忙的小时是 17:00。
I grouped and summed the 2016 bicycle counts by hour, used Matplotlib to create a line plot with a title and axis labels, and saved it as `counts_by_hour.png`. I also calculated the average bicycle count for each hour and used `idxmax()` to determine that the busiest hour on average was 17:00.

最后，我重新运行了完整脚本，确认缺失数据数量为 1、最繁忙小时为 17，并实际检查了生成图表的标题、坐标轴和曲线。
Finally, I reran the complete script, confirmed that the missing-data count was 1 and the busiest hour was 17, and visually inspected the generated plot's title, axes, and curve.

## AI 辅助使用声明
## AI Assistance Disclosure

Codex 被用于解释作业要求、创建初始文件夹结构、配置文件、`.gitignore` 和双语 README。它还用于讲解 Pandas 和 Matplotlib、协助排查语法和变量错误，以及验证程序输出和图表。数据分析代码由学生本人编写并运行。
Codex was used to interpret the assignment, create the initial folder structure, configuration files, `.gitignore`, and bilingual README. It was also used to explain Pandas and Matplotlib, help diagnose syntax and variable errors, and verify the program output and plot. The student wrote and ran the data-analysis code.
