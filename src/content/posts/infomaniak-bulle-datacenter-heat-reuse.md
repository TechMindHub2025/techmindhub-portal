---
title: "When Data Center Waste Heat Becomes District Heating: Testing the 28 GWh Claim"
description: "Infomaniak's planned 2.5 MW data center in Bulle could supply district heating through heat pumps. Its 28 GWh forecast raises useful questions about system boundaries, seasonal demand and emissions."
excerpt: "A planned Swiss data center offers a test of what heat recovery really means. The first question is where the 28 GWh of delivered heat originates."
pubDate: "2026-11-15T04:00:00Z"
status: "published"
canonical_id: "2026-11-15-infomaniak-bulle-datacenter-heat-reuse"
tags: ["WasteHeat", "DistrictHeating", "HeatPumps", "EnergyEfficiency", "AIDatacenters", "TechMindHub"]
source_url: "https://www.presseportal.ch/fr/pm/100057093/100943576"
cover_card: "https://media.techmindhub.cc/posts/infomaniak-bulle-datacenter-heat-reuse-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/infomaniak-bulle-datacenter-heat-reuse-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/infomaniak-bulle-datacenter-heat-reuse-og-web-v1.jpg"
domain: "energy-environment"
topic: "Heat recovery and energy accounting"
card_alt: "Conceptual server building transfers a warm liquid loop to nearby homes under the phrase Heat Beyond the Rack."
cover_alt: "Conceptual district-heating energy balance showing server heat entering a heat pump, added electricity and useful heat delivered to the network."
---

Waste heat from a data center is not automatically useful heat. It has to exist at a recoverable temperature, reach a customer that needs it, and arrive through an economically workable network. The most difficult part of a heat-reuse project may therefore be outside the server room: the heat pumps, district-heating connection and year-round match between supply and demand.

On November 13, 2026, Swiss cloud provider Infomaniak and regional utility Gruyère Energie [announced a proposed data center in Bulle](https://www.presseportal.ch/fr/pm/100057093/100943576) and the opening of its public consultation process. The planned facility would accommodate **170 server racks** and **2.5 MW of IT power**, with commissioning targeted for **2028**, subject to permits and final agreements. It would use closed-loop liquid cooling for compute and AI servers and heat pumps operated by Gruyère Energie to transfer recovered energy into the existing district-heating system.

The companies forecast **approximately 28 GWh of heat delivered per year** and potential avoidance of **up to 7,500 tonnes of CO₂ annually relative to heating oil**. Both are projections for an unbuilt facility, not measurements of an operating plant.

## Start with the energy boundary

The 28 GWh forecast is interesting because it exceeds a simple annual energy calculation from the advertised IT power rating:

`2.5 MW × 8,760 hours/year = 21.9 GWh/year.`

That **21.9 GWh is a theoretical upper annual IT-energy figure** if the site continuously uses its full stated 2.5 MW IT power for every hour of a non-leap year. Real utilization may be lower or vary through a commissioning ramp. The figure is not total facility electricity, and it is not a forecast of delivered district heat.

Does the larger 28 GWh thermal forecast violate conservation of energy? No. A heat pump adds electricity while moving heat from a lower-temperature source to a hotter network. The heating-side balance is, in simplified annual terms:

`Q_delivered = Q_recovered + E_heat-pump`,

before any distribution losses, additional heat sources or other boundary effects are considered. Thus an output of 28 GWh can be consistent with a data center rated at 2.5 MW IT. But it **cannot be explained by IT electricity alone**, and the release does not publish the complete annual energy model.

Consider an intentionally extreme illustration: if all **21.9 GWh** of maximum annual IT input were recovered as usable source heat, with no other recovered facility heat and no relevant losses, then producing **28 GWh** of network heat would require **6.1 GWh** of heat-pump electricity. The implied annual heating coefficient of performance would be `28 / 6.1 ≈ 4.6`.

**This is not an Infomaniak performance claim, an equipment specification or an estimate of actual consumption.** It only shows why the heat pump must appear inside the accounting boundary. Lower IT utilization, additional facility heat, heat rejected elsewhere, distribution losses and a changing seasonal COP all change the equation. The companies have not provided sufficient data here to reconstruct their forecast.

The rack count does not solve the question. Dividing 2.5 MW equally by 170 racks gives about **14.7 kW per rack**, an arithmetic site average at full IT rating—not the density of individual AI racks or evidence that every rack operates continuously at that level.

## The temperature problem is as important as the energy total

A liquid-cooled server loop collects heat at a temperature determined by component cold plates, flow rates and permitted silicon temperatures. A district-heating network needs water at its own required delivery temperature. The larger the temperature lift, generally the more electricity a heat pump needs for a given useful heat output.

This creates a design trade-off. A warmer server-side coolant can make recovery more attractive, but it must remain within the allowable operating envelope of the IT equipment. A lower network supply-temperature requirement can reduce the lift, but must still serve customers and maintain its thermal service obligations. Neither side can be specified by a single annual gigawatt-hour number.

Seasonal demand adds another complication. A compute workload may produce heat in July, while the most valuable building-heating demand occurs in January. Storage, alternative sinks, network operation and the ability to reject heat when buyers cannot take it determine how much can actually be reused. A contract for heat capacity is not the same thing as a metered annual utilization rate.

The proposed Bulle site benefits from its location near electricity, fibre and the existing district-heating network, according to the release. That reduces a major barrier to heat recovery: a long new thermal pipe network could erode an otherwise attractive project. Yet the press release does not give detailed design temperatures, seasonal COP, thermal storage capacity, return temperatures or a full curtailment strategy.

## What do the water and carbon claims mean?

The companies say the building will use **closed internal cooling circuits without cooling towers, evaporation or cooling-water withdrawals**. That is a meaningful operational water-design choice. It does not mean no water is ever needed in construction, maintenance or the wider electricity supply chain, and it does not by itself prove a water footprint of zero.

The avoided-emissions forecast also needs the correct comparison. The stated **up to 7,500 tonnes of CO₂ per year** is explicitly *relative to heating oil*. Spread over 28 GWh of projected heat, that is roughly **0.27 tonnes of CO₂ per MWh delivered** as an implied comparison rate, not a measured reduction from the existing network.

That distinction is material because Gruyère Energie's district-heating system is already reported as **more than 95% renewable**. Adding recovered heat may diversify supply or accommodate future demand, but the real marginal emissions reduction depends on which fuel, plant and operating hours the new source displaces. Replacing hypothetical oil heating is a different claim from reducing emissions in an already predominantly renewable system. A credible emissions evaluation also needs the emissions associated with heat-pump electricity and the chosen accounting method.

## Publish the meters, not just the target

If this project reaches service in 2028, the most useful public evidence would be a set of consistently defined measurements:

- IT energy and total facility electricity, including the heat pumps, with clear organisational and meter boundaries.
- Heat captured from the IT/facility loops and heat actually injected into the district network, separately metered.
- Hourly source/sink temperatures, flow and heat-pump input, allowing calculation of operating and seasonal COP.
- Available recovered heat versus heat accepted by the network, including summer rejection and maintenance outages.
- Water withdrawals, makeup water and energy-source accounting using a stated reporting scope.
- Avoided emissions against a documented **marginal heating counterfactual**, not an unspecified comparison to fossil heating.

Infomaniak's prior Geneva data-center design may offer operational experience, but it does not establish the future performance of this different, larger Bulle project. The proposed integration is technically credible as a design direction and worth tracking through construction and commissioning. Its strongest eventual contribution would be transparent evidence that recovered IT heat can become *reliably useful* regional energy—not merely that a convincing annual total was announced before the plant existed.

## Source

- [Infomaniak and Gruyère Energie: Bulle data-center project announcement, November 13, 2026](https://www.presseportal.ch/fr/pm/100057093/100943576)
