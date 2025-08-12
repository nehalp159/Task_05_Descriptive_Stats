# Task 05: Descriptive Statistics and Large Language Models

## Project Description
This repository investigates the potential rewards and drawbacks of using LLMs (Large Language Models) to analyze data related to sports statistics. The aim is to determine if AI can reliably respond to queries regarding datasets in natural language and offer insightful information for making decisions.

## Author
Nehal Pawar  
July-August 2025

## Objectives
1. Assess LLM reliability on fundamental statistical queries
2. Examine LLM's performance on challenging analytical problems.
3. Record quick engineering techniques
4. Assess the visualizations produced by LLM
5. Evaluate the usefulness of coaching decisions

## Dataset
- **Type**: Women's Lacrosse Cumulative Statistics
- **Size**: 34 players, 19 games
- **Source**: https://cuse.com/sports/2013/1/16/WLAX_0116134638
- **Time Period**: 2025

## Methodology
1. Created validation scripts to verify correct answers
2. Developed 20 test questions across 4 complexity levels
3. Tested with multiple LLMs
4. Documented accuracy and prompt strategies
5. Analyzed patterns in successes and failures

## Project Structure
```
Task_05_Descriptive_Stats/
├── README.md                                  # This file
├── .gitignore                                 # Excludes data files
├── data/                                      
│   └── syracuse_wlax_stats_2025.csv           # Dataset (not in repo)
├── scripts/
│   └── validate_stats.py                      # Validation script
├── prompts/
│   └── questions.md                           # Test questions
└── results/
    ├── chatgpt_results.md                     # Results from ChatGPT
    ├── claude_results.md                      # Results from Claude
    ├── copilot_results.md                     # Results from Copilot
    ├── gemini_results.md                      # Results from Gemini
    ├── python_output.md                       # Results from Python validation script
    ├── summary_Python vs ChatGPT.md           # Overall findings
    ├── summary_Python vs Claude.md            # Overall findings
    ├── summary_Python vs Copilot.md           # Overall findings
    └── summary_Python vs Gemini.md            # Overall findings
```

## Key Findings
### Python vs ChatGPT
- All statistical results from Python were accurately matched by ChatGPT.
- It included useful coaching insights like strategy, places for improvement, and MVP recommendations.

### Python vs Gemini
- Gemini included reasoning utilizing measures like shooting efficiency as well as MVP scores, and it matched all Python statistics.
- More innovative assessment techniques were introduced by Gemini's analysis, which were helpful for coaching insights.

### Python vs Claude
- Claude provided thorough tactical thinking and matched all Python statistics reports.
- Suggested lineup optimization, player development, and focused defensive enhancements.

### Python vs Copilot
- Copilot included non-player rows like "Team" and "Totals Opponents," which led to an incorrect count of players and points, although it matched the majority of Python's player-specific statistics.
- Despite occasional errors in dataset interpretation, it provided rational coaching recommendations, optimal lineups, and opportunities for improvement.

## How to Reproduce
1. Make a clone of this repository
2. Include your dataset in the folder `data/`
3. Execute the validation script: `python3 scripts/validate_stats.py`
4. With any LLM, use the questions from `prompts/questions.md`
5. Review the results against the validation output

## Tools Used
- VS Code for development
- Python 3.x for validation
- Gemini, ChatGPT, Claude, Copilot

## Overall Conclusion
Python provided precise statistical computations, guaranteeing accuracy in numerical findings. ChatGPT typically produced similar results and provided clear, strategic coaching advice. Gemini incorporated novel measurements and evaluation methods while matching the calculations as well. Claude was as precise as Python and had the most practical, strategic reasoning. Although Copilot frequently misread the dataset design by inserting non-player rows, it was still able to match a large number of Python results while offering helpful coaching advice and recommendations for improvement. When combined, these tools demonstrate how combining the qualitative knowledge of LLMs with the quantitative precision of Python results in more comprehensive and practical sports data analysis.

## Contact
For inquiries about this analysis, please contact: nepawar@syr.edu

## Acknowledgments
Under Professor Jonathan's guidance, the project is part of Syracuse University's research requirements.