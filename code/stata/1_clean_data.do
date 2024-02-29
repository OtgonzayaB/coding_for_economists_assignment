* Load data
import delimited using "data/raw/hrs_height_income.csv", clear

* Only keep relevant variables
keep age height hhincome female

* Summarize hhincome height age
summarize hhincome height age, detail

* Checking for missing values
misstable summarize

* Dropping missing values
drop if missing(height)

*Create logged variables
gen ln_hhincome = ln(hhincome)
gen ln_height = ln(height)

* Checking for outliers
hist ln_hhincome 
hist ln_height
hist age
hist female

* Save the cleaned data
save "data/clean/cleaned_data.dta", replace

