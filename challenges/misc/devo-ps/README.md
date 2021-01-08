# Devo(ps)
### Category: Web Exploitation
### Author: Emily Baird (Analytical Engine)

## Description
Did you know that the band DEVO took their name from the idea of "de-evolution?" That's right, the guys in DEVO thought that humanity was getting stupider. Luckily, we here at Magpie Inc. are here to prove them wrong. Need an example? Look no further than our first fully-automated release, the Flag-Checker 9000!

Hint 1: This seems like a lot of effort for a simple flag checker. Added complexity means more opportunities for things to go wrong outside just the source code itself.

## Solution
This challenge's exploit takes advantage of a misconfigured GitHub Actions build script. The source files during the CTF were hosted on a dummy GitHub account, which can be found at [INSERT LINK HERE].

1. The description mentions that this is a 'fully-automated release.' Instead of a link to a C binary, the challenge links us to a GitHub Package from a user named [Magpie Inc](https://github.com/magpie-inc?tab=packages)
2. Running the binary from the package doesn't seem to do much. It asks for a flag, and tells us whether or not the flag is correct. Worse, the package is pre-compiled, meaning that we can't easily view the source code of the binary.
3. However, maybe if we go back to the GitHub account, we'll be able to find more.
4. Sure enough, the `magpie-inc` user seems to have a single public repo, and it looks like the correct one for the flag checker. The source code for the binary, `flagchecker.c`, is out here in the open. Looking closer at the source code, it appears that our Flag-Checker 9000 takes user input, hashes the input using MD5, and compares the result to a macro called `FLAG_HASH`.
5. As the hint mentions, there seems to be a lot of code here that isn't related to `flagchecker.c`. Perhaps the exploit isn't in the source code of Flag-Checker 9000 itself?
6. In the folder `.github/workflows`, we find a file called `build_flag_checker.yml`. It appears that this GitHub Action is the automated script responsible for packaging Flag-Checker 9000.
7. Reading the script `./build.sh` referenced in step 'Build Flag Checker Program' we can see that it uses the 1st command-line argument as the value assigned to the macro. `build_flag_checker.yml` is using the output of a previous step as the CL arg to the 'Build Flag Checker Program' step: "${{ steps.get_hash.outputs.HASH_VALUE }}"
8. The output of the 'Get hash' step is the result of a second bash script, `flaghash.sh`. This one appears to cURL an IP address, and then hashes the results using MD5. We know that `flagchecker.c` is converting the user's guess to an MD5 hash and tells us that our flag is right if our hash matches the value of `FLAG_HASH`. The post-hashing results from `flaghash.sh` are being used to set the value of `FLAG_HASH`, so it stands to reason that the IP address is giving out the un-hashed flag!
9. Run `curl http://ipaddress/api.php --header 'Authorization: token f4e53e561c6580d6d304f3f31e3102f5` for yourself, and the result is the flag!

## Flag
magpie{build_automation_genius}