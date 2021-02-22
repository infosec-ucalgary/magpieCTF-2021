## Challenges

### Overview
Contains source code and solutions for dynamic and static challenges for magpieCTF 2021. 

Challenges are organized into folders based on challenge type.

***
### Starting a Docker Container

This will be a bare-bones guide on how to run one of our docker challenges locally. Go to [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/) for more information.

1. Install docker on your computer.
    * If you're running Windows, I recommend looking into installing Docker using WSL2.
2. Clone this repo to your local machine.
3. Change your directory to the `source/` folder for the challenge you want to run in a terminal.
4. Run `docker build -t <tag> .`
    * `<tag>` is a name of your choice (for example, `foobar`).
5. To start the docker container, run `docker run -p <external port>:<internal port> <tag>`.
    * `<external port>` is the external port you will bind to a port on your computer. It can be almost anything.
    * `<internal port>` is the internal port that will be mapped inside the container.
        * The internal port(s) differs for each challenge. See `Internal Ports` below. 
    * `<tag>` is the same tag that you used to build the challenge before.
    * You can use the `-p` flag multiple times to forward multiple ports to the container.

For example, to start Sweatin' in LaTeX:
1. `git clone https://github.com/infosec-ucalgary/magpieCTF-2021.git`
2. `cd magpieCTF-2021/challenges/web-exploitation/sweatin-in-latex/source`
3. `docker build -t latex .`
4. `docker run -p 8080:80 latex`
5. Go to `http://localhost:8080` in a web browser to connect!

Note: All dynamic challenges in the binary exploitation category need to be run with the `--privileged` flag.
* `docker run --privileged -p 31337:31337 foobar`

### Internal Ports


**Chain-my-song**
* `1982`

**Finger-in-the-shell**
* `6000`

**Flush**
* `31337`

**numwrite**
* `8754`

**Poly**
* `31337`

**Ret2jedi**
* `6600`

**Smash**
* `1996`

**Text Adventure 1**
* `1976`

**Data Encryption (non)Standard**
* `20000`

**Man-in-the-Mirror**
* `8080` 
* `1337`

**By Grace** 
* `80`

**Birdbuster Video** 
* `80`

**David Byrne Online Tailor**
* `80`

**Devo(ps)**
* `80`

**The Smurfs Cipher**
* `80`

**Sweatin' in LaTeX**
* `80`

***
### Folder Organization
Each challenge folder should contain a `README.md` file that has the challenge description (as to be shown on CTFd), challenge solution, and flag.

There should also be a folder called `source/` which contains any source code/scripts that were used to create a challenge. If the challenge is dynamic (i.e. needs to be hosted) then the `source/` folder should contain the `Dockerfile` and any resources needed to build the docker image. Running `docker build` from the `source/` directory should correctly build the challenge's docker container.

There should also be a folder called `solve/` which contains the solve script for the challenge. If your challenge is static and does not need a solve script then this folder may be omitted.

If your challenge is static, then place the static challenge file in the challenge's root directory alongside the `README.md` file. Any file that is not in a folder (i.e. alongside `README.md`) will be made public on CTFd.

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
### Example README.md File
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