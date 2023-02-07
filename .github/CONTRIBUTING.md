# Contributing

<!---
Used linters:
  [ESLint](https://eslint.org/)
  [EditorConfig](https://editorconfig.org)
--->

If you wish to contribute to {{project.name}}, feel free to fork the repository and submit a pull request.
{{project.linter}} is enforced to correct most typo's you make and keep the code style the same throughout the whole project,
so it would be much appreciated if you installed {{project.linter}} to your editor of choice

<!---
Prerequisites for Node.JS:

* [Node.JS V18.14.0](https://nodejs.org/en/)
* [Docker](https://www.docker.com)
* [ESLint](https://eslint.org)
* [(OPTIONAL) Yarn](https://yarnpkg.com)
--->
## Prerequisites
The following prerequisites must be met before installing {{project.name}}:
{{setup.prerequisites}}

<!---
Install commands:
  JavaScript/TypeScript: `yarn --dev` or `npm install --dev`
  Rust: `cargo run`
  C: `make clean install`

Run commands:
  JavaScript/TypeScript: `yarn test` or `npm run test`
  Rust: `cargo run`
  C: `make clean dev`
--->
## Setup
To get ready to work on the codebase, please do the following:

1. Fork & clone the repository, and make sure you are on the **master** branch
2. Run {{setup.install}}
4. Code your ideas and test them using {{setup.test}}
6. [Submit a pull request](https://github.com/{{project.master}}/{{project.name}}/compare)

## Testing
When creating any new functions, please also create unit tests for them in the `tests` directory.
Use the library associated with the project when creating such tests.

When modifying existing functions, make sure to test them before making a pull request, this will prevent
anything from breaking on the production environment.