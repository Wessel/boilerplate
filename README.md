<!---
To update:
  project.
    master        - The master org or user of the repo
    linter        - The linter used for the project
    name          - Project name
    lang          - The (primary) programming language used
    logo          - Project logo
    contact       - All ways to contact for any inqueries
    reviewers     - A list of users to auto-assign to issues and features
  info.
    toc           - Table of Contents of README
    desc          - Small project description
    badges        - Any extra badges
  setup.
    prerequisites - The prerequisites needed to run the project
    install       - Command for initial installation
    test          - Command for running tests
  tree.
    parts         - All individual parts of the project
--->
<img src="{{project.logo}}" align="left" width="192px" height="192px"/>
<img align="left" width="0" height="192px" hspace="10"/>

> {{project.name}}

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE) {{info.badges}}

{{info.desc}}

<br><br>

<!---
Example table of contents:
* header
  * sub header
--->
## Table of contents
{{info.toc}}

