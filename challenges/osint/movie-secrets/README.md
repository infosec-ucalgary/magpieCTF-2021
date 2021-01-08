# Movie Secrets
### Category: OSINT
### Author: Ethan Sengsavang (e-seng)

## Description
All the reviews from the film reviewer FibrousFilms was recently wiped.
Can you determine the password like the hacker did?

https://fibrousfilms.neocities.net

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
ordered list on the homepage (`index.html`).
 * This shows that the password to the site is likely FibrousFilms' 
pet name, followed by the name of their favourite movie, then their
favourite food, and lastly the hidden string underneath that. This string
is hidden with a paragraph set to 0 opacity.
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
7. They mention that the sometimes connect words together `inthismanner` on
their Reddit.
 * Thus, each peice can be connected in this way to form the password to 
`admin.html`.

# Flag
magpie{j0urn3y\_t0\_743\_c3ntr3\_of\_743\_n3t}
