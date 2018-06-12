# latinAr
An extensive dataset for latin-written dialectal arabic.

# What is latin-written Arabic?
Latin-written dialectal Arabic is any text written in latin alphabet, mainly english and french, but which represents dialectal arabic words and expressions. Here are some examples:

# Examples 
The word "إذهب" (not dialectal, used here for clarity) is arabic for "Go" in English. And because most arabic-speaking countries don't use arabic keyboards for short and even long text messaging (i.e. chatting), it is written "Idhab" (Frenchly-pronounced) or "Edheb" (Englishly-prnonouced). The ultimate goal behind this repo is to provide a <b>latinAR-to-Classical-arabic mapping</b>, so for the word "إذهب", we'll have the following mapping: <b>{Idhab: إذهب}</b> for frenchly-pronouncing regions and <b>{Edheb: إذهب}</b> englishly-pronouncing regions.<br/>
A dialectal example: "sir" (frenchly) or "seer" (englishly), not the english "sir", but maghrebi-dialectal arabic for the word "إذهب". The mapping would consequently be <b>{sir: إذهب}</b>. 

# The Goal
We aim with this repository to provide an as-extensive-as-possible dataset (CSV files actually) for latin written arabic, hence the name "latinAr". Specifically regions such as Morocco, Algeria and Tunisia, but also Egypt, Mauritania, Lybia, Middle-east and eventually more depending on adoption and/or need.

This repository is structured into regions (i.e. a batch of countries that have roughly the same language aspects), countries (i.e. Morocco, Algeria, Tunisia) and then country regions (i.e. northern, eastern etc... depending on language differences in the same country).
Thus, the repo is structured as follows: <b>Dataset/Regions/Countries/Country-regions/data-types</b>.
The data-type part of the repo structures data into words, phrases and sentences, paragraphs, then long texts.

# But why launch a latinAr dataset?!
Well, because being a <b>deep learning driven team of individuals</b>, and after being disappointed that there's a huge lack in structured latinAr data, we've realized that we could not perform anything deep learning-related for the dialectal arabic language! <b>So we've decided to create one. For the sake of AI democratization</b>.

Want to contribute (we need you!)? or interested in any way? Have suggestions? Please let us know.
