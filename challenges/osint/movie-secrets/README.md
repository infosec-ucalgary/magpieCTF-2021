# Movie Secrets
### Category: OSINT
### Author: Ethan Sengsavang (Petiole)

## Description
All the reviews from the film reviewer FibrousFilms was recently wiped.
Can you determine the password like the hacker did?

https://fibrousfilms.netlify.app

## Hints
1. Connect ideas between websites
2. Where can you find FibrousFilms' birthday?

## Solution
1. Players must determine that FibrousFilms has a Twitter and a Reddit
 * Both of these social media sites are mentioned in different locations.
Twitter is mentioned on the website itself, where Reddit is mentioned on Twitter.
2. They then should notice the semi-hidden Admin Panel link on the footer
of the page (or by going to admin.html themselves)
3. Reading the html comment on `admin.html`, players should consider the
start to look for answers to security questions. 
4. The pet's name can be determined:
 * From Reddit, fibrousfilms writes:

`aww they really remind me of my kitten tim back at home. thanks for posting`
 * hinting that they have a kitten named tim.
 * From Twitter, they also write:

`i really like nicknames sometimes, like if i introduced someone to tim, no one would guess that's short for timbala`
 * showing that their kitten's name, tim, is short for timbala.
5. Their favourite movie can be determined:
 * From Twitter, their birthday is public, showing they were born on June 7th 1983
 * Their website states that their favourite movie came out on their second birthday
 * A Google search for movies released on June 7th, 1985 results with the 
Goonies, which is their favourite film.
6. Their favourite food can also be determined:
 * On Reddit, they mention that they want to post a photo of the lasagna they're
making with their roommate one day after they made that post (Posted on 
January 6th).
 * On Twitter, they state that they're making their favourite food "today"
(Posted on January 7th)
 * Noticing that the two days line up, their favourite food can be determined.
7. The hidden key is just that, hidden.
 * This should give a hint to point to the zero opacity string found on the
index page of fibrousfilms' website.

* NOTE: There is an intentional 404 page call if the players answer incorrectly,
but players may use any casing to stay fairly lenient.

# Flag
magpie{j0urn3y\_t0\_743\_c3ntr3\_of\_743\_n3t}
