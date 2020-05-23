library(tidyquant)
library(tidyverse)
library(rvest)

my_url <- read_html("https://www.airbnb.com/s?query=milan&checkin=2020-04-16&checkout=2020-04-20")

text <- my_url %>%
  html_nodes("div._8ssblpx") %>%
  html_text()

text
