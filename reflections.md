# Reflections
Briefly answer the following questions. Point form and 1-2 sentences is fine.

## Why did you choose your selected dataset?

<!-- Mainly I'm just curious what interests people -->

1. we thought we could do some cool things with housing data like how prices vary due to certain factors
2. more features in the data so we could do more things
3. business partner that we could help (Zakie)

## What are some of your key observations from the data exploration process?

<!-- Refer to your notebook as desired -->
1. in all of Alberta, largest property density is shown to be in the middle (Calgary) and highest population
2. residenital, muliti-restidental and direct control district were the hightest valued land use
3. most properties have small land sizes
4. year of construction, more houses are being built later down the years as more people come to Calgary
5. Calgary has a weak negative correlation, suggests in Calgary, larger properties might not always have higher values 
6. could be due to zoning, location or other usage types

## Why did you choose to process the data the way you did?

<!-- Some reasonable justification here -->
1. We started with splitting our data into 80% training and 20% testing data
2. Remove the nulls from the two columns (land use and year of construction using imputer) 
3. Standard Scalar is prepared as we were thinking of implementing a Linear Regression where the data could skew our model but since we proceeded with Random Forest algorithm that is no longer really required. 

## What additional information do you wish you had?

<!-- The provided data is pretty limited. What information do you think would help you to make a more effective prediction? -->
1. median salary of people
2. if garage exists or not
3. neigbourhood amenities
4. number of bedrooms
5. house size 

## What was the hardest part of this assignment?

<!-- Anything goes! Tell me more about the challenges you faced -->

1. git... pull requests got messy and confusing so we decided to call and work on it in real time together
2. pipelines were a bit confusing at first in trying to figure out how they worked and the implementation
