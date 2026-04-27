Reflective Report
1. Analytical Problem and Target Audience
This interactive data analysis project focuses on exploring the annual sales performance and industry distribution of leading global listed corporations. The core analytical problem is to compare corporate sales scale, classify enterprises by industry, and extract intuitive business insights from corporate financial sales data. This interactive dashboard is designed for business students, entry-level business analysts and finance practitioners. It enables users without professional coding skills to filter data, check statistics and view visual charts easily, so they can quickly understand the sales gap and industry composition of major global companies.
2. Dataset Selection and Rationale
The dataset I applied includes 5 representative top international enterprises, with 3 core variables: company name, industry classification and annual sales revenue. The dataset is obtained from public financial reports and industry rankings, ensuring data credibility. I chose this dataset because it is clean, complete and highly suitable for basic business data analysis. There are no missing values or abnormal data inside, which can fully show the complete process of data inspection, filtering, statistical analysis and visualization. In addition, the small dataset size guarantees the Streamlit dashboard runs smoothly and responds fast to all interactive user operations.
3. Main Python Methods and Workflow
The whole analysis tool is developed with Python programming language. Three key Python libraries are used in this project: Pandas for data loading, missing value checking, descriptive statistics and data filtering; Matplotlib for generating bar charts and pie charts; and Streamlit for building the interactive web interface with selectbox, slider, data table and chart display. The workflow follows a clear logical order: dataset overview - data quality check - statistical analysis - interactive filtering - visualization output.
4. Key Findings and Outputs
From the analysis results, clear insights can be concluded. Amazon has the highest sales volume among all sampled companies. Most enterprises belong to the technology industry, while Amazon is in the retail industry. Users can filter companies by industry and sales range to locate target firms quickly. The bar chart shows the sales differences between companies, and the pie chart directly presents the industry proportion structure.
5. Difficulties Encountered
The main difficulty I faced was chart display issues. In the early testing stage, the labels on the bar chart overlapped, and the visualization could not update synchronously with the filtered data, which affected the user experience and interactivity of the tool.
6. Solutions Implemented
I fixed the problems by adjusting the figure size and rotating the x-axis labels by 45 degrees in Matplotlib to avoid text overlap. I also optimized the data logic to ensure the chart updates in real time with user interactions. I tested the program repeatedly to ensure stability and correctness.
7. Limitations and Improvements
The project has limitations: the dataset is small with only 5 companies, and the analysis only covers single-year sales data. The visualization style is basic. For improvements, I can expand the dataset with more firms and multi-year data, add more analysis functions such as growth rate and profit comparison, and optimize the interface design.
8. Key Learnings
Through this assignment, I mastered the full workflow of Python data analysis and Streamlit interactive tool development. I improved my skills in data processing, code debugging and visualization design. I also gained a clearer understanding of how to turn data analysis into a user-friendly product and strengthened my programming and logical thinking abilities.

AI Disclosure
1. AI tool used: Doubao
2. Purpose: Polishing English writing, organizing report structure, ensuring all required points are covered, and adjusting word count to meet the assignment requirements.
3. Usage statement: I reviewed, revised and verified all AI-generated content. All core project information, code logic and personal reflections are my original work. AI was only used for language improvement and structure optimization.
4. Access date: 26 April 2026
