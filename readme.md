## Purpose
The purpose of this project is to create a machine learning model that can identify stitches using an image input. I will begin by focusing on knitting stitches, building up the dataset by stitch and may eventually add crochet stitches. This project may aid those who come across heirloom clothing and wish to find out more details about its construction.

## Data
Data will be scraped from knitting dictionary sites that are public facing and do not disallow individual graphics scraping. Data will be in two forms: image and a stitch name.

Images ought to meet the following criteria:
    * Close up image
    * Only a single stitch is present in the image
    * Front view of the stitch (back view optional)

Stitch names will be saved in a CSV that corresponds to the image saved in the relevant folder (not uploaded)

Note that since stitch images are usually only uploaded as single images (or at most, a single front and a single back image), multiple sites will be scraped and the scrape_images file is only an example for a single site. These images may also be supplanted through synthetic means such as image rotation, or through the creator of the project's personal crafting stash.

## EDA
EDA will require an initial classification of the stitch files based on stitch names. This will simply be done by moving relevant images into separate classificatory folders per name of the stitch from relevant knitting dictionary sites as well as the creator's subject matter expertise (I really love knitting).

Stitch names will be made consistent by stripping extraneous words like the website name and by correcting possible spelling mistakes.

Images will be resized for consistency of modeling.

## Modeling
Transfer learning will be used to fine-tune a pre-existing model. Details to come!