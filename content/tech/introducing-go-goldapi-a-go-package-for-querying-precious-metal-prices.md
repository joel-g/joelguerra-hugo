---
title: "Introducing go-goldapi: a Go Package for Querying Precious Metal Prices"
date: 2020-11-04T17:33:09-08:00
draft: false
featured_image: "/img/introducing-go-goldapi-a-go-package-for-querying-precious-metal-prices/1.jpg"
tags: ["golang"]
---
_Photo by [Stanislaw Zarychta](https://unsplash.com/@stahooo) on [Unsplash](https://unsplash.com/)_

Would you like to have automation workflows or alerting related to current spot pricing of gold, silver, platinum or palladium? Of course you would! But first you need to grab the price…

Introducing `go-goldapi`, a Go package for querying current and historical precious metal prices from goldapi.io. Note: I am the author of the Go package ([https://github.com/joel-g/go-goldapi](https://github.com/joel-g/go-goldapi)) but I have no affiliation with [goldapi.io](https://www.goldapi.io).

This API and package can be used to query current and historical prices of gold, silver, platinum and palladium in the following currencies:

* USD — United States dollar

* AUD — Australian dollar

* GBP — British pound

* EUR — European Euro

* CHF — Swiss franc

* CAD — Canadian dollar

* JPY — Japanese yen

* INR — Indian rupee

* SGD — Singapore Dollar

* BTC — Bitcoin

* CZK — Czech Krona

* RUB — Russian Ruble

* PLN — Polish Złoty

* MYR — Malaysian Ringgit

* XAG — Gold/Silver Ratio

To start fetching spot prices with Go get your free API key [here](https://www.goldapi.io/) and then `import github.com/joel-g/go-goldapi` into your project.

Try this code sample after you replace “YOUR API KEY” with your API key from [goldapi.io](https://www.goldapi.io).

Then try replacing “USD” with any of the above currency codes.

Then try different metals using the following consts `goldapi.Gold`, `goldapi.Silver`, `goldapi.Platinum`, `goldapi.Palladium`.

Then try different dates in the YYMMDDD format for the third argument.

```go
package main

import (
	"fmt"
	"log"
	"os"

	"github.com/joel-g/go-goldapi/goldapi"
)

func main() {
	// Get your API key from https://www.goldapi.io
	api := goldapi.NewAPIClient("YOUR API KEY")

	// Use one of the 4 const Metals from goldapi package:
	// Must include currency in ISO 4217.
	// Date is optional but must be in YYYYMMDD format.
	// If date is left blank today's date will be used.

	silverReport, err := api.GetPrice(goldapi.Silver, "USD", "")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("The price of silver is %f\n",silverReport.Price)
	fmt.Printf("%+v", silverReport)

	// A report of your API usage
	stats, err := api.GetStats()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("\nYou have used %d requests this month", stats.RequestsMonth)
}
```

Have fun and as always, bother me on [Twitter](https://twitter.com/joelatwar).
