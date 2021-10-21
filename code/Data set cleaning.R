## Owen Doyle ##
# Data-151 Cleaning #
library(tidyverse)
imdb <- read.csv("Documents/DATA-151/Project/IMDb movies.csv")
imdb2 <- subset(imdb, country == "USA" & language == "English" & votes >= 500)
imdb2$title[imdb2$title == ""] <- NA
imdb2$year[imdb2$year == ""] <- NA
imdb2$genre[imdb2$genre == ""] <- NA
imdb2$duration[imdb2$duration == ""] <- NA
imdb2$country[imdb2$country == ""] <- NA
imdb2$language[imdb2$language == ""] <- NA
imdb2$director[imdb2$director == ""] <- NA
imdb2$avg_vote[imdb2$avg_vote == ""] <- NA
imdb2$votes[imdb2$votes == ""] <- NA
imdb2$budget[imdb2$budget == ""] <- NA
imdb2$usa_gross_income[imdb2$usa_gross_income == ""] <- NA
imdb2$worlwide_gross_income[imdb2$worlwide_gross_income == ""] <- NA
imdb2$metascore[imdb2$metascore == ""] <- NA
imdb2$reviews_from_users[imdb2$reviews_from_users == ""] <- NA
imdb2$reviews_from_critics[imdb2$reviews_from_critics == ""] <- NA
imdb3 <- na.omit(imdb2)
imdb4 <- imdb3

imdb4$budget <- as.integer(imdb4$budget)
imdb4$usa_gross_income <- as.integer(imdb4$usa_gross_income)
imdb4$worlwide_gross_income <- as.integer(imdb4$worlwide_gross_income)
imdb4$year <- as.integer(imdb4$year)
imdb4 <- na.omit(imdb4)

imdb5 <- subset(imdb4, year > 1990)

imdb6 <- imdb5

imdb6$votecat <- cut(imdb6$avg_vote, seq(0, 10, 10/3), right = FALSE, labels=c('Low', 'Middle', 'High'))

write.csv(imdb6, file = "Documents/DATA-151/Project/IMDb_clean.csv")
