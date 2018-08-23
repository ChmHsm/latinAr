# latinAr
An extensive dataset for latin-written and arabic-written dialectal arabic.

# Quick JSON example
<b>One-to-one mapping:</b></br>
{<b>latin_ar_arabic</b>:"سير", <b>american_english</b>:"go"}</br>
{<b>latin_ar_french</b>:"sir", <b>american_english</b>:"go"}</br></br>
<b>One-to-many mapping:</b></br>
{<b>latin_ar_arabic</b>:"سير", <b>classical_arabic</b>:"إذهب", <b>american_english</b>:"go"}</br>
{<b>latin_ar_french</b>:"sir", <b>classical_arabic</b>:"إذهب", <b>american_english</b>:"go"}</br></br>
<b>Many-to-many mapping:</b></br>
{<b>latin_ar_arabic</b>:["سير","مشي"], <b>classical_arabic</b>:"إذهب", <b>american_english</b>:"go"}</br>
{<b>latin_ar_french</b>:["sir","mchi"], <b>classical_arabic</b>:"إذهب", <b>american_english</b>:"go"}</br>

# What is latin-written Arabic?
Latin-written dialectal Arabic is any text written in latin alphabet, mainly english or french, but which represents dialectal arabic words and expressions. Here are some examples:

# Examples 
The word "إذهب" (not dialectal, used here for clarity) is arabic for "Go" in English. And because most arabic-speaking countries don't use arabic keyboards for short and even long text messaging (i.e. chatting), it is written "Idhab" (Frenchly-pronounced) or "Edheb" (Englishly-prnonouced). </br>The ultimate goal from this repo is to provide a <b>latinAR-to-Classical-arabic mapping</b>, so for the word "إذهب", we'll have the following mapping: <b>{latin_ar: "Idhab", classical_arabic: "إذهب"}</b> for frenchly-pronouncing regions and <b>{latin_ar: "Edheb", classical_arabic: "إذهب"}</b> englishly-pronouncing regions.<br/><br/>
<b>A (real) dialectal example:</b> "sir" (frenchly) or "seer" (englishly), not the english "sir", but maghrebi-dialectal arabic for the word "إذهب". The mapping would consequently be <b>{latin_ar: "sir", classical_arabic: "إذهب", american_english:"go"}</b>. 

# The Goal
We aim with this repository to provide an as-extensive-as-possible dataset (<b>CSV/JSON</b> files actually) for latin written arabic, hence the name "latinAr". Specifically regions such as Morocco, Algeria and Tunisia, but also Egypt, Mauritania, Lybia, Middle-east and eventually more depending on adoption and/or need.

This repository is structured into regions (i.e. a batch of countries that have roughly the same language aspects), countries (i.e. Morocco, Algeria, Tunisia) and then country regions (i.e. northern, eastern etc... depending on language differences in the same country).
Thus, the data is structured as follows: <b>data/Regions/Countries/Country-regions/data-types</b>.
The data-type part of the repo structures data into words, phrases and sentences, paragraphs, then long texts.

# Why launch a latinAr dataset?!
Being a <b>deep learning driven team of individuals</b>, and being disappointed that there's a huge lack in structured latinAr data, we've realized that we could not perform anything deep learning-related for the dialectal arabic language! <b>So we've decided to create one. For the sake of AI</b>.

Want to contribute (we need you!)? or interested in any way? Have suggestions? Please let us know.

# What's this repo going to be used for anyway?
Mainly, this repo is intended to contain a training, validation and evaluation dataset for dialectal arabic RNN and CNN-related models:<br/>
Language modeling & generation<br/>
Word representation (word embeddings, Word2Vec,...)<br/>
Sentiment analysis<br/>
Machine translation<br/>
Text-to-speech (soon)<br/>
Speech-to-text (soon)<br/>
And others...

# Types of data you'll find in this repo
You'll find 3 sets of data in every region-directory (an example of a "region-directory": data\regions\Maghreb\Morocco\Northern -chamali):
- Raw data: data which didn't go through any sort of processing, directly created through a copy/paste operation from the original source.
- Pre-processed data : data which has been cleansed of irregularities. Basicaly, it's the raw data plus regular expressions.
- Plug-and-play data : JSON or CSV structured data. Ready for use.</br>
In the plug and play data you'll always find a "column" called:
- "latin_ar", containing the original word/phrase.
- The translations of the latin_ar word/phrase in the target language(s) (as of 01/08/2018, we're thinking classical arabic and english)
