library(tidyquant)
library(timetk)
library(tidyverse)
library(rvest)



raw_url <- read_html('https://finance.yahoo.com/currencies/')


txt <- raw_url %>%
  html_nodes("td") %>%
  html_text()

raw_df <- as.data.frame(matrix(txt, ncol = 7,
                               nrow = length(txt)/7,
                               byrow = TRUE), stringsAsFactors = FALSE) %>%
  tk_tbl()

tickers <- raw_df$V1


price_df <- tq_get(tickers,
                   from = '2006-1-1',
                   get = 'stock.prices')

price_df

price_df %>%
  filter(str_detect(symbol,pattern = '=X$')) %>%
  ggplot(aes(x = date, y = adjusted, color = symbol)) +
  geom_line() +
  facet_wrap(~symbol, scales = 'free_y')


