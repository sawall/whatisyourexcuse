# Voting Excuse Generator

What is your excuse not to vote? We've got answers and information for everything you can
think of!

## Technical

The Voting Excuse Generator is built using static site generation with a `jinja2` template
in `python`. It requires a CSV file to reference data and images in order to build out all of
the site pages.

Meme images should be placed in /static/memes. Open Graph letterboxed versions of the
images should be generated in the same directory; e.g., use this command in `zsh`:

> for file in ./**/*(.); convert $file:t -resize 1200x630 -gravity center -background "rgb(255,255,255)" -extent 1200x630 $file:t:r_og.$file:e

The initial rev of the site was built using anchor tags and dynamic loading, but
unfortunately Facebook and Twitter don't play nicely with anchors. Not wanting to abuse
query strings led us to the current multi-page solution. However, further research shows
that the HTML5 History API may be a more appropriate solution so stay tuned.

See the example CSV file, `content.csv` to understand the expected format. It's a vanilla
csv download from Google Sheets. `generate_site.py` is used to generate the pages, using
the template at `templates/base.html`.

As an added bonus, the `hashgen.py` script here was used to generate random web-friendly
names for all of the images.

## Build process

1. Download CSV into `content.csv`.
2. Run `generate_site.py`
3. Push the `www` directory online 

# Credits:

* Audrey Maker: vision, product owner, and memes
* Anonymous Designer: user experience and design
* Scott Boone: code, project management, and design
* Mercedes Vaughn: writer and copy editor
* Delia Davila: copy editor and morale
* Monk: hexcolor resample process engineer

