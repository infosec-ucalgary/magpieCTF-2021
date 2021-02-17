# Devo(ps)
### Category: Web Exploitation
### Author: Emily Baird (Analytical Engine)

## Description
Did you know that the guys in DEVO thought that humanity was getting stupider? Luckily, we here at Magpie Inc. are here to prove them wrong!

## Hint 
Github can be used for more than just storing code. The 'Actions' tab at the top of the repo might provide some insight.

## Solution
This challenge's exploit takes advantage of a misconfigured GitHub Actions build script.

1. The description mentions that this is a 'fully-automated release.' Instead of a link to a C binary, the challenge links us to a GitHub repo from a user named [Magpie Inc](https://github.com/magpie-inc/flag-checker)
2. The `magpie-inc` user seems to have a single public repo. The source code for the binary, `flagchecker.c`, is out here in the open. Looking closer at the source code, it appears that our Flag-Checker 9000 takes user input, hashes the input using MD5, and compares the result to a macro called `FLAG_HASH`.
3. As the hint mentions, there seems to be a lot of code here that isn't related to `flagchecker.c`. Perhaps the exploit isn't in the source code of Flag-Checker 9000 itself?
4. In the folder `.github/workflows`, we find a file called `build_flag_checker.yml`. It appears that this GitHub Action is the automated script responsible for packaging Flag-Checker 9000.
5. Reading the script `./build.sh` referenced in step 'Build Flag Checker Program' we can see that it uses the 1st command-line argument as the value assigned to the macro. `build_flag_checker.yml` is using the output of a previous step as the arg to the 'Build Flag Checker Program' step: "${{ steps.get_hash.outputs.HASH_VALUE }}"
6. The output of the 'Get hash' step is the result of a second bash script, `flaghash.sh`. This one appears to cURL an IP address, and then hashes the results using MD5. We know that `flagchecker.c` is converting the user's guess to an MD5 hash and tells us that our flag is right if our hash matches the value of `FLAG_HASH`. However, the value of the cookie 'auth' in the curl request is set to `${ secrets.FLAG_AUTH }` which doesn't seem to be accessible in any of the files. In the workflow runs (accessible under the 'actions' tab on the repo), the value of FLAG_AUTH is starred out.
7. The last thing to investigate is the commit history. We can see that there is a commit with the message 'Fix auth!!!' 
8. If we look at the changes made for the commit, we see that an earlier version was set up slightly differently, with the 'auth' cookie set in the code of `gethash.sh` itself.
9. Run `curl http://ipaddress/api.php --cookies 'auth=f4e53e561c6580d6d304f3f31e3102f5` for yourself, and the result is the flag!

## Flag
magpie{build_automation_genius}