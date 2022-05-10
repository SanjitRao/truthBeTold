# TruthBeTold
TruthBeTold is a high-school student organization devoted to designing an algorithm that can combat misinformation online. Through this Github, we hope to present our approach and what work we believe still needs to be done. 

# Approach:
Our approach consists of understanding a given article as completely as possible and then trying to deduce veracity from that. This consists of looking at an article's sentiment, finding the author/publisher's bio (if one exists), checking for recency of information, finding supporting material in other articles, and many more. Taken and processed simultaneously in seperate 'feature-functions', this information represents our algorithm's comprehensive understanding of an article, which can then be compared to other articles like that to predict credibility overall. To minimize any aspects of an article that might get overlooked, we're looking to expand the range and capability of our feature-functions in the coming months.

## The Feature Functions
Here, we will detail each of our feature functions we currently have, as well as discuss what next steps we could implement in the future. 

### def relevancy_ff(keyword, news_source, API_KEY = api_key):
This feature function looks to figure out relevancy by comparing today's date with the date the given article was published. This function will simply return the number of days between these two dates. This function is definitely over-simplistic, as a breaking-news story on a developing issue might have different relevancy paramenters than a an old article on issue that's remained constant over decades, so in the future we believe we need to add some way to (...) 
### def Question_GAC(article_text, reference_texts):




## Notes for things to add in the future:
- [ ] in the Approach section, include a diagram of the TBT approach
- [ ] Have pictures of each of th feature functions
- [ ] Link our TBT USC Presentation + Blue Ocean 
- [ ] Add a direct link to the TBT website
![New People - Welcome!](https://user-images.githubusercontent.com/68609739/166170008-b2b34dce-b9ea-4f4b-bdf1-c3f5c100905a.png)
