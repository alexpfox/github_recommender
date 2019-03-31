# github_recommender

Recommends similar GitHub users and interesting projects you may not have seen/heard of before based on your starred list and follows.

[Blog post here.](https://alexandrafox.me)

I wanted a quick and easy way to dig through Github looking for inspiration for my next project, as I'm often overcome by a bit of analysis paralysis when trying to decide what to work on next. By limiting my sphere of influence I'm able to overcome that a bit. I can now wander through a list of GitHub users in order to traverse the field of sources of possible inspiration in a constructive way. 

GitHub offers a similar feature in their Explore tab, but doesn't offer a way to traverse similar users along any given path directly - their suggestions are most often repo based, which is simply too granular for my tastes. 

I utilize Singular Value Decomposition via [Surprise](http://surpriselib.com/) in order to compare users and offer the three most similar users in high-dimensional space, which represents the list of people that any given user is following. It would be great to include the list of people following someone as well, and the list of users' starred repos' owners. This would need to be limited to a highly dense subset of GitHub users to really work well, as one of the limiting factors when working with collaborative filtering techniques is the "cold start" problem - when the data is too sparse, the signal is too faint for the algorithm to pick up on in a sense.

<p align="center">
<img src="/assets/images/2019/3/github/usercomp2-2.png">
</p>

The Flask app is currently very simple, but it was not my goal to spend hours working on CSS for this project. I learned instead mostly about Surprise, SVD, matrix factorization techniques, MongoDB usage in a more significant sense, AWS and generating test data. I would love to add visualizations for traversing the username 'paths' through similarity in different ways through different developer communities and follow-clusters on GitHub, but there are a few things getting in the way currently. The list of users is a bit outdated, because it comes from an aged GHarchive via git-awards. I acquired the list of usernames from git-awards in order to preferentially select users who were active and interesting on GitHub, but this has the effect of being as out of date as their website is. I'd prefer to turn this into a streaming source of information in the future.

I had to test my pipeline using generated data - the data used from the GitHub Archive database is too outdated or the sparse matrix generated by the list of followed users only has the effect of making thr project impossible as it currently stands with the collected data. This is fine, as it was a great challenge to try to overcome, and in troubleshooting the issues I had I learned a great deal about Surprise, matrix factorization, and a few other implimentations of SVD from other libraries. Ultimately I may revisit this process later in order to try to gather a denser network of follows to map, and then add visualization of the network using D3.