* Import data
use "data/clean/cleaned_data.dta", clear

* Regression of household income and body height
reg hhincome height
reg ln_hhincome ln_height

* Regression of household income, body height and age
reg ln_hhincome ln_height age

* Regression of household income, body height, age and gender
reg ln_hhincome ln_height age female

* Graphical representation of the relationship between household income and body weight
graph twoway (scatter ln_hhincome ln_height, mcolor(blue)) ///
	(lfit ln_hhincome ln_height, lcolor(orange)), ///
	xtitle("Household Income") ytitle("Body height") ///
	title("Relationship between household income and body height", color(black)) ///
	note("Source: Health and Retirement Study, 2014, USA")
	

	

