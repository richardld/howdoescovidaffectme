# howdoescovidaffectme
A model for estimating live risk of COVID-19 infection.

## Introduction
While numbers on case data may tell an overall picture, it is hard for the individual to grasp the danger of COVID-19 in personal terms. How does COVID affect me? trys to solve this by creating a risk percentage calculation based on a model we created of COVID-19 spread.  

The website can be found at https://www.howdoescovidaffectme.com.

### Details

#### How was the risk of infection calculated?

The real risk of infection of a disease is impossible to calculate with perfect accuracy. Our risk of infection is calculate as a rough estimate based on current data on the virus. To calculate risk of infection, we took the proportion of state population tested positive for COVID-19 in the past day out of the entire state population.

Assuming (somewhat naively) that the number of infections in the next day would be the same as the number of infections in the previous day, we used this value to create a preliminary risk factor. This risk factor was scaled by 7.14 to reflect the disparity between tested cases and estimated cases (whether asymptomatic or untested). Sources suggest that possibly 6 out of 7 cases of COVID-19 are undetected, hence the data was scaled by around a factor of 7. The risk of infection also does not fall equally on all groups of the population. The risk factor assumes that those not social distancing make up most of the daily case count. The calculation also assumed that 90% of the population was obeying the current shelter in place orders/social distancing order. The preliminary proportion was scaled by 10x as a result to account for the majority of the risk falling on a small subset of the population.
#### What data was used in the calculation?

State level daily COVID-19 case data were sourced from the Coronavirus Tracker API.

County level daily COVID-19 case data were sourced from The COVID Tracking Project API.

County population data were sourced from the US Census Poplation Estimates API.

Location data were processed using the FCC Area API.
#### How accurate is this calculation?

The risk of infection calculation is not at all accurate as it is formed off of a large base of assumptions. The risk of infection calculation is not medical advice or information that should be strictly informative of any COVID-19 related decisions. Please do not place overly strong importance on this risk factor.

### Implementation
This website is written entirely from scratch. CSS themes were borrowed from Bootswatch. Created during hacknow 2020.
