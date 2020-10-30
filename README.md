# Different Approaches to Name Matching - Fuzzy Match, NLP, Machine Learning

## The Problem

Name matching OR finding similar names is a tricky problem to solve at first place. There can be spelling mistakes, OCR errors, abbreviations, short names etc. For e.g. "Catherine Zeta-Jones", "Katherine Z Jones", "Catherine Jones" may all be referring to the same person OR they can be completely different persons. Another example is "Alaska Supreme Court" vs "Supreme Court of Alaska". In this case we are sure that the both refer to same name, but they are written differently. So when deciding to find similarity you need to be sure whether you need to go with model based prediction, accurate match OR percentage match (most common in fuzzy matching).

## Approaches

There are different approaches to solving this problem. In this tutorial, I am mainly exploring Fuzzy match, NLP and ML based approaches.
