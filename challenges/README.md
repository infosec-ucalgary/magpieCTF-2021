## Challenges

### Overview
Contains source code and solutions for dynamic and static challenges for magpieCTF 2021. 

Challenges are organized into folders based on challenge type.

***
### Folder Organization
Each challenge folder should contain a `README.md` file that has the challenge description (as to be shown on CTFd), challenge solution, and flag.

There should also be a folder called `source/` which contains any source code/scripts that were used to create a challenge. If the challenge is dynamic (i.e. needs to be hosted) then the `source/` folder should contain the `Dockerfile` and any resources needed to build the docker image. Running `docker build` from the `source/` directory should correctly build the challenge's docker container.

There should also be a folder called `solve/` which contains the solve script for the challenge. If your challenge is static and does not need a solve script then this folder may be omitted.

If your challenge is static, then place the static challenge file in the challenge's root directory alongside the `README.md` file.

***
### Example Folder Structure
#### Dynamic Challenges
```
challenges
└── web-exploitation
    └── foo-bar
        ├── solve
        |   └── foo_bar_solve.py
        ├── source
        |   ├── app/
        |   └── Dockerfile
        └── README.md
  ...
```

#### Static Challenges
```
challenges
└── forensics
    └── foo-bar
        ├── foo-bar.png
        ├── source
        |   └── foo-bar.psd
        └── README.md
  ...
```

***
### Example README File
Below is an example template for how to format the `README.md` file for your challenge:

```markdown
# Foo Bar
### Category: Forensics
### Author: John Smith (jsmith123)

## Description
This is the challenge description!

## Hints
1. Here is hint 1!
2. Here is hint 2!

## Solution
This would be the solution to the challenge!

1. Do this first
    * Some more explanation
2. Then do this
3. Finally do this  

## Flag
magpie{example_flag}
```