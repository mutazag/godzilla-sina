
# Output Files

These are produced after apply additiona processing to raw entities. these files are meant to include additional information, for example, joining data, preserving the results of some analysis. 


|filename | description | columns | github link |
|:---:|:---|:---|:---|
|tags-tags.csv| edges represetnation of the tags networks <br>processed from the Posts entity, <br>includes weight for each time two tags appear in the same post | v1,v2: names of tags<br>weight: weight of edge | https://raw.githubusercontent.com/mutazag/godzilla-sina/master/data/outputs/tags-tags.csv |
|tags-with-wiki.csv| tags table joined with posts table for posts of type id 4 and 5 <br>these are the take short description and tag description wiki content <br> the text content is url encoded | TagId <br>TagName<br>Count<br>ExcerptPostId, WikiPostId<br> TagDescription_Qoute, TagExcerpt_Qoute: to decode <br>`df[TagDescription] = df.TagDescription_Qoute.apply(urllib.parse.unquote)`<br>`df[TagExcerpt] = df.TagExcerpt_Qoute.apply(urllib.parse.unquote)`| https://github.com/mutazag/godzilla-sina/raw/master/data/outputs/tags-with-wiki.csv | 

use URL decode functions for the any of the following columns `{'Body', 'Title', 'AboutMe', 'Text', 'Comment'}`

- [URLEncode/URLDecode in R](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/URLencode)

- `urllib.parse.unquote(value)` [in python](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse)

