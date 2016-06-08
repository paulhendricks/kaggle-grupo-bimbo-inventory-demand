library(dplyr)
library(ggplot2)

train_original <- read.csv("./data/prepped/train.csv", stringsAsFactors = FALSE)
test <- read.csv("./data/prepped/test.csv", stringsAsFactors = FALSE)
train <- subset(train_original, !(Semana %in% c(8, 9)))
validation <- subset(train_original, Semana %in% c(8, 9))

hist(train$Demanda_uni_equil)
g <- 
  ggplot(train, aes(x = Demanda_uni_equil)) + 
  geom_histogram()
print(g)

g + facet_wrap(~ Semana)
g + facet_wrap(~ Canal_ID)


s <- 
  train %>% 
  filter(Canal_ID == 1) %>% 
  filter(Agencia_ID == 1911) %>% 
  filter(Ruta_SAK == 1279) %>% 
  filter(Cliente_ID == 2016521) %>% 
  select(-Agencia_ID, -Canal_ID, -Ruta_SAK, -Cliente_ID)

ggplot(s, aes(x = Semana, y = Demanda_uni_equil, group = Producto_ID)) + 
  geom_line()

ggplot(s, aes(x = Demanda_uni_equil)) + 
  geom_histogram() + 
  facet_wrap(~ Semana)
