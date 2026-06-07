# Project Requirements and Specifications Document
## Python Virtual Environments, CI/CD Simulation, and AI Demo Projects for FDP Hands-On Session

This document defines the use cases, scope, functional requirements, non-functional requirements, architecture, and execution expectations for the Python demo projects used in the Faculty Development Programme hands-on session. It is intended to act as a concise project specification document for the working code samples already prepared for demonstration. [cite:1]

## Document purpose

The purpose of this specification is to provide a structured project definition for the demo artifacts so that participants can understand not only how to run the code, but also why the code exists, what problem it solves, and how each module fits into an industry-style software delivery workflow. [cite:1]

The document is intentionally designed for academic delivery, where the goal is to simulate real software engineering practices for AI projects using lightweight Python scripts that can run on personal laptops without cloud infrastructure. [cite:1]

## Program alignment

The projects defined here align with the FDP purpose of combining theoretical understanding, practical exposure, and industry-oriented insights through hands-on Python activities in AI, data science, and smart solution development. [cite:1]

They also support the stated objectives of developing Python skills, introducing AI application workflows, enhancing problem-solving ability, and promoting the use of AI tools in teaching and research. [cite:1]

## Project portfolio

The hands-on session includes two primary demonstration projects and two supporting automation modules. [cite:1]

| Project/Module | Purpose | Primary Technology | Demonstration Value |
|---|---|---|---|
| Student Risk Predictor | Simulate an AI-based scoring application that behaves differently in DEV and TEST environments | Python, environment variables | Explains config-driven deployment behavior [cite:1] |
| Academic FAQ Bot | Simulate a lightweight NLP-based academic assistant with adjustable confidence threshold | Python, scikit-learn TF-IDF, cosine similarity | Explains how environment configuration affects answer strictness [cite:1] |
| Test Suite | Validate correctness of the predictor logic before deployment | Python, pytest | Demonstrates automated quality gates [cite:1] |
| Pipeline and Deployment Simulation | Simulate CI/CD execution and promotion to TEST | Python subprocess, JSON output | Demonstrates staged automation without cloud setup [cite:1] |

## Stakeholders

The primary stakeholders are faculty members attending the FDP, the industry resource person demonstrating the session, and institutions that may later adapt the demo projects for teaching, student labs, or introductory AI engineering practice. [cite:1]

A secondary stakeholder is the learner community, because the same projects can be extended into student mini-projects or internal laboratory exercises. [cite:1]

## Project context

The session assumes a Windows 11 laptop-based demonstration environment with Python installed locally, VS Code as the editor, and terminal-based execution using Command Prompt or PowerShell. [cite:1]

The project design deliberately avoids dependence on Docker, cloud deployment, remote servers, or hosted machine learning services so that the entire workflow remains accessible during a short FDP session. [cite:1]

## Use case 1: Student Risk Predictor

### Use case summary

The Student Risk Predictor is a simplified AI-style analytics script that calculates a normalized student performance score from attendance, internal assessment marks, and assignment marks, then classifies the student as either `safe` or `at_risk`. [cite:1]

The same script must produce different outcomes in different environments based on a configurable threshold so that participants clearly understand how DEV and TEST deployments may behave differently without changing core application logic. [cite:1]

### Problem statement

In academic and industry settings, the same code often behaves differently when configuration changes across development, testing, and deployment environments. [cite:1]

This project uses a relatable educational scenario to demonstrate that environment variables and runtime configuration can alter system behavior even when the source code remains the same. [cite:1]

### Intended users

- Faculty members learning environment-aware Python application setup. [cite:1]
- Students who will later use the model as a classroom lab activity. [cite:1]
- Instructors demonstrating configuration-driven AI behavior. [cite:1]

### Functional requirements

| ID | Requirement |
|---|---|
| FR-SRP-01 | The system shall accept three numeric inputs: attendance, internal score, and assignment score. [cite:1] |
| FR-SRP-02 | The system shall compute a weighted normalized score using predefined weights. [cite:1] |
| FR-SRP-03 | The system shall read `APP_ENV` and `MODEL_THRESHOLD` from environment variables. [cite:1] |
| FR-SRP-04 | The system shall classify the result as `safe` if the normalized score is greater than or equal to the threshold, otherwise `at_risk`. [cite:1] |
| FR-SRP-05 | The system shall return output as a Python dictionary containing environment, score, threshold, and label. [cite:1] |
| FR-SRP-06 | The system shall be executable from the command line using a local Python interpreter. [cite:1] |
| FR-SRP-07 | The system shall prompt the user to choose between using the default example inputs and entering custom values in interactive environments, and fallback to the default example inputs (attendance=62, internal=58, assignment=70) in non-interactive environments to prevent blocking. [cite:1] |

### Sample specification logic

The predictor shall compute the score using the weighted formula below, where attendance contributes 30 percent, internal score contributes 40 percent, and assignment score contributes 30 percent. [cite:1]


the weighted score logic is implemented in the code sample and used only for instructional demonstration, not as a statistically validated academic risk model. [cite:1]

### Inputs

- Attendance: integer or float in the range 0 to 100. [cite:1]
- Internal score: integer or float in the range 0 to 100. [cite:1]
- Assignment score: integer or float in the range 0 to 100. [cite:1]
- Environment threshold: float between 0 and 1 from the execution environment. [cite:1]

### Outputs

- `environment`: current environment name such as `dev` or `test`. [cite:1]
- `score`: normalized weighted score. [cite:1]
- `threshold`: threshold value used for classification. [cite:1]
- `label`: `safe` or `at_risk`. [cite:1]

### Example behavior

When the input values are 62, 58, and 70, the normalized score is approximately 0.629, so the student may be classified as `safe` in DEV with threshold 0.5 and `at_risk` in TEST with threshold 0.7. [cite:1]

This difference is central to the teaching goal of the session. [cite:1]

## Use case 2: Academic FAQ Bot

### Use case summary

The Academic FAQ Bot is a simple NLP-based question-answer system that uses TF-IDF vectorization and cosine similarity to match a user query with a small FAQ knowledge base. [cite:1]

It is designed to show how environment-specific confidence settings affect system response behavior, particularly the difference between a permissive development environment and a stricter testing environment. [cite:1]

### Problem statement

AI and NLP applications often require decision thresholds to determine whether a response is trustworthy enough to present to the user. [cite:1]

This use case demonstrates how a confidence threshold can be changed between DEV and TEST so that the same query may produce an answer in one environment and a fallback message in another. [cite:1]

### Intended users

- Faculty teaching introductory NLP concepts. [cite:1]
- Learners exploring text similarity and retrieval-based QA systems. [cite:1]
- Demonstrators showing environment-specific AI safety behavior. [cite:1]

### Functional requirements

| ID | Requirement |
|---|---|
| FR-FAQ-01 | The system shall maintain a small FAQ dictionary of question-answer pairs. [cite:1] |
| FR-FAQ-02 | The system shall transform FAQ questions into TF-IDF vectors. [cite:1] |
| FR-FAQ-03 | The system shall transform the user query into a vector and compute cosine similarity against stored FAQ questions. [cite:1] |
| FR-FAQ-04 | The system shall return the answer with the highest similarity if it meets or exceeds `FAQ_CONFIDENCE`. [cite:1] |
| FR-FAQ-05 | The system shall return a fallback message when the confidence score is below the configured threshold. [cite:1] |
| FR-FAQ-06 | The system shall print the current environment and confidence threshold when run from the command line. [cite:1] |

### Inputs

- Query string from the user. [cite:1]
- FAQ confidence threshold from environment variable `FAQ_CONFIDENCE`. [cite:1]
- Environment name from environment variable `APP_ENV`. [cite:1]

### Outputs

- Printed environment name. [cite:1]
- Printed confidence threshold. [cite:1]
- Best matched answer or fallback text. [cite:1]

### Example behavior

In DEV, a lower threshold such as 0.20 allows the bot to answer borderline similarity matches for exploratory testing. [cite:1]

In TEST, a higher threshold such as 0.60 may prevent low-confidence answers and instead return a safe fallback response. [cite:1]

## Supporting module 1: Automated Test Suite

### Purpose

The automated test suite validates that the student risk predictor produces expected labels and score ranges for known inputs before the code is allowed to proceed through the simulated deployment pipeline. [cite:1]

### Functional requirements

| ID | Requirement |
|---|---|
| FR-TST-01 | The project shall include unit tests for at least one safe case and one at-risk case. [cite:1] |
| FR-TST-02 | The test suite shall verify that the computed score remains in the valid range from 0 to 1. [cite:1] |
| FR-TST-03 | The tests shall be executable using `pytest`. [cite:1] |
| FR-TST-04 | A failed test shall stop the simulated CI/CD pipeline. [cite:1] |

### Demonstration goal

This module exists primarily to demonstrate that CI begins with automated validation and that deployment should be blocked when expected behavior is violated. [cite:1]

## Supporting module 2: CI/CD Pipeline and Deployment Simulation

### Purpose

The pipeline module simulates a real CI/CD process locally by executing dependency installation, test execution, and deployment steps in sequence. [cite:1]

The deployment module simulates target-environment promotion by writing a deployment receipt as a JSON file. [cite:1]

### Functional requirements for `pipeline.py`

| ID | Requirement |
|---|---|
| FR-PIPE-01 | The pipeline shall define execution stages as ordered commands. [cite:1] |
| FR-PIPE-02 | The pipeline shall install TEST dependencies before validation. [cite:1] |
| FR-PIPE-03 | The pipeline shall execute pytest-based test cases. [cite:1] |
| FR-PIPE-04 | The pipeline shall call the deployment module after successful validation. [cite:1] |
| FR-PIPE-05 | The pipeline shall stop immediately if any stage returns a non-zero exit code. [cite:1] |
| FR-PIPE-06 | The pipeline shall print pass/fail feedback for each stage. [cite:1] |

### Functional requirements for `deploy.py`

| ID | Requirement |
|---|---|
| FR-DEP-01 | The deployment module shall accept a command-line target environment argument. [cite:1] |
| FR-DEP-02 | The deployment module shall construct a configuration object for the selected environment. [cite:1] |
| FR-DEP-03 | The deployment module shall write deployment output to a JSON file named according to the target environment. [cite:1] |
| FR-DEP-04 | The deployment module shall print deployment details to the console. [cite:1] |

### Example deployment artifact

The deployment artifact is a JSON file such as `deployed_test.json` that records environment, status, config, and timestamp. [cite:1]

This is not a real server deployment, but it is sufficient to model the idea of promotion to a tested target environment. [cite:1]

## Environment specification

### Operating environment

The primary operating environment is Windows 11 with Python 3.11 or newer installed locally, because that is the intended demonstration platform for the FDP session. [cite:1]

The project should also run on macOS or Linux with equivalent Python and pip commands, but Windows 11 is the reference platform for the specification. [cite:1]

### Development tools

- Python 3.11 or higher. [cite:1]
- pip package manager. [cite:1]
- Virtual environment support through `venv`. [cite:1]
- VS Code or equivalent text editor. [cite:1]
- Command Prompt or PowerShell for execution. [cite:1]
- Optional GitHub repository for demonstrating workflow automation. [cite:1]

### Dependency specification

Two dependency manifests are required. [cite:1]

| File | Purpose |
|---|---|
| `requirements-dev.txt` | Includes packages needed for exploration, plotting, notebooks, NLP, testing, and ML experimentation. [cite:1] |
| `requirements-test.txt` | Includes only the packages required for testing and deployment simulation. [cite:1] |

## Architecture overview

The demo solution uses a modular but intentionally lightweight folder structure to keep the session understandable for faculty participants while still reflecting industry-like organization. [cite:1]

| Folder/File | Responsibility |
|---|---|
| `app/` | Application logic, including predictor and FAQ bot. [cite:1] |
| `tests/` | Automated test cases for quality validation. [cite:1] |
| `pipeline.py` | Local CI/CD orchestrator. [cite:1] |
| `deploy.py` | Deployment simulation and JSON artifact creation. [cite:1] |
| `.github/workflows/` | Cloud-style CI/CD workflow definition. [cite:1] |
| `requirements-*.txt` | Environment dependency manifests. [cite:1] |

## Non-functional requirements

### Usability requirements

- The system must be understandable to faculty members with beginner-to-intermediate Python familiarity. [cite:1]
- The code must be short enough for live explanation within a half-day FDP session. [cite:1]
- The scripts must run from a terminal with minimal setup steps. [cite:1]

### Portability requirements

- The system must run on a personal laptop without cloud access. [cite:1]
- The system must not require Docker, Kubernetes, remote databases, or proprietary services for the core demonstration. [cite:1]
- The system must use only locally installable Python packages. [cite:1]

### Reliability requirements

- The predictor and FAQ bot must produce deterministic output for the same configuration and input values. [cite:1]
- The pipeline must stop on failure. [cite:1]
- The deployment simulation must always produce a machine-readable JSON artifact when successful. [cite:1]

### Maintainability requirements

- The project must use small, readable Python files. [cite:1]
- Variables and filenames should be descriptive and faculty-friendly. [cite:1]
- The codebase should be extendable into future student mini-projects. [cite:1]

## Assumptions and constraints

### Assumptions

- Participants have Python installed or can install it before the session. [cite:1]
- Participants can open a terminal and run basic command-line commands. [cite:1]
- Participants have internet access at least once for pip installation of packages. [cite:1]

### Constraints

- The session is limited to approximately 2.5 hours including break, so project complexity must remain intentionally low. [cite:1]
- The demonstration must prioritize concept clarity over enterprise completeness. [cite:1]
- The solution must use Python-first workflows and avoid heavy operational tooling during the live demonstration. [cite:1]

## Acceptance criteria

The project set shall be considered successful for FDP delivery when all the following conditions are met. [cite:1]

| ID | Acceptance criterion |
|---|---|
| AC-01 | A participant can create and activate DEV and TEST virtual environments on a local laptop. [cite:1] |
| AC-02 | The participant can run `predict.py` in DEV and TEST and observe different classification behavior. [cite:1] |
| AC-03 | The participant can run `faq_bot.py` with different confidence thresholds and observe different response behavior. [cite:1] |
| AC-04 | The participant can run `pytest` and observe all tests passing under the intended code state. [cite:1] |
| AC-05 | The participant can run `pipeline.py` and generate a successful deployment JSON artifact. [cite:1] |
| AC-06 | The participant can intentionally break a test and observe the pipeline stopping before deployment. [cite:1] |
| AC-07 | The participant can relate the local pipeline simulation to the GitHub Actions workflow file. [cite:1] |

## Extension roadmap

The current project specification intentionally keeps the scope small for FDP delivery, but the same project family can be extended in later sessions. [cite:1]

Possible extensions include:
- adding CSV input instead of hard-coded values to the predictor, [cite:1]
- building a small Streamlit user interface, [cite:1]
- adding logging and configuration files, [cite:1]
- exposing the predictor as a Flask or FastAPI endpoint, [cite:1]
- containerizing the application with Docker, and [cite:1]
- integrating model training notebooks or dashboard views. [cite:1]

## Conclusion

These project specifications define a compact but realistic AI engineering teaching setup in which faculty participants can experience the full path from isolated Python environments to testing, CI/CD simulation, and controlled deployment behavior. [cite:1]

Because the projects are grounded in familiar academic use cases and runnable on standard Windows 11 laptops, they are well suited for faculty training, student labs, and introductory AI software engineering demonstrations. [cite:1]
