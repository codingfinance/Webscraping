library(rvest)
library(tidyquant)
library(tidyverse)

st_df <- read_csv('Downloads/Master Report/rentals/All/rentIndex_All.csv')  

st_df %>%
  gather(Brooklyn:Queens,key = boro,value = idx) %>%
  ggplot(aes(x = Month, y = idx, color = boro)) +
  geom_line()

df_rent <- read_csv('Downloads/Master Report/rentals/All/medianAskingRent_All.csv')

clean_df <- df_rent %>%
  gather(`2010-01`:colnames(df_rent[ncol(df_rent)]),
         key = Month,
         value = rent) %>%
  separate(Month,sep = '-', into = c('year', 'month')) %>%
  mutate(day = 1) %>%
  mutate_at(.vars = c('year','month'),
            .funs = parse_number) %>%
  mutate(date = make_date(year = year,
                          month = month,
                          day = day)) %>%
  select(date,areaName,Borough,areaType,rent) 


