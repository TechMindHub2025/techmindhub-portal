---
title: "A 4U Pump Is Not a Cooling Capacity: Reading the Gates ThermalCool 2100SS Specifications"
description: "Gates' compact 48 VDC ThermalCool 2100SS pump can circulate up to 200 L/min. Its value in a rack CDU depends on operating-point hydraulics, motor heat and validated N+1 behaviour."
excerpt: "The thermal capacity of a rack loop cannot be read from its pump's maximum flow alone. Gates' new 4U-compatible pump illustrates the system calculations that matter."
pubDate: "2026-11-15T05:00:00Z"
status: "published"
canonical_id: "2026-11-15-gates-thermalcool-2100ss-cdu-hydraulics"
tags: ["LiquidCooling", "CDU", "PumpEngineering", "RackInfrastructure", "AIDatacenters", "TechMindHub"]
source_url: "https://www.gates.com/us/en/about-us/news.one.122768.html"
cover_card: "https://media.techmindhub.cc/posts/gates-thermalcool-2100ss-cdu-hydraulics-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/gates-thermalcool-2100ss-cdu-hydraulics-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/gates-thermalcool-2100ss-cdu-hydraulics-og-web-v1.jpg"
domain: "infrastructure"
topic: "Rack liquid-cooling hydraulics"
card_alt: "A compact conceptual coolant pump and two pipes appear under the words Inside the Cooling Loop."
cover_alt: "Conceptual rack-cooling loop links pump flow and pressure, coolant heat transport, motor heat and parallel-pump resilience."
---

As liquid cooling moves into individual AI racks, the pump stops being a remote plant-room detail. It competes with compute hardware for space, draws electricity from the rack environment, creates its own heat and becomes part of the system's availability argument. A compact pump is valuable only if its operating curve matches the actual hydraulic circuit.

On November 12, 2026, Gates [introduced the ThermalCool 2100SS](https://www.gates.com/us/en/about-us/news.one.122768.html), a stainless-steel pump designed for coolant distribution units (CDUs) in high-density data centers. The manufacturer describes it as compatible with a **4U rack arrangement** and suitable for parallel operation. Global availability is expected in **early 2027**. This is an announced component, not an independently validated production CDU.

The [manufacturer's technical datasheet](https://www.gates.com/content/dam/documents-library/flyers/thermalcool-data-centers-pumps-thermalcool-spec-sheet-2100ss-letter-na-en.pdf) lists **up to 200 L/min**, **3 bar** of differential pressure, **48 VDC** input, **2.1 kW** motor power and **44 A** maximum current. It also lists **7,000 rpm**, IP55 protection, a maximum coolant temperature of **65°C**, a maximum ambient temperature of **50°C**, and a **50,000-hour** pump-life rating. Communications options are CANBUS and MODBUS.

Those numbers describe important boundaries. They do not, by themselves, tell an engineer how many kilowatts of IT heat a finished rack system can reject.

## Flow and head must be paired at one duty point

The basic hydraulic relationship is:

`P_hydraulic = Δp × V̇`,

where `Δp` is the pressure rise across the pump and `V̇` is the volumetric flow. At an illustrative **200 L/min** and **3 bar**, the volume flow is approximately **0.00333 m³/s** and the ideal hydraulic power is about **1.0 kW**.

That is **not** a statement that the 2100SS simultaneously delivers its listed maximum flow and maximum differential pressure, or that it draws exactly 1.0 kW of electrical power. Centrifugal-pump head generally changes with flow and rotational speed; the actual duty point lies at the intersection of the selected pump curve and the system resistance curve. The Gates sheet includes a hydraulic-performance plot, but a rack designer needs the correct configured curve, fluid properties and measured or calculated pressure losses for the complete circuit.

Likewise, `48 V × 44 A ≈ 2.11 kW` is a useful electrical upper-end consistency check against the 2.1 kW motor rating. It is not a measured efficiency ratio at the hypothetical 200 L/min and 3 bar point. Combining separate nameplate maxima as if they were one certified test point would create a misleading pump efficiency claim.

## Cooling capacity comes from temperature rise

For a circulating fluid, the heat transported is approximately:

`Q_heat = mass flow × specific heat × temperature rise.`

If the loop carried **water** at 200 L/min, with density approximated as 1 kg/L and specific heat as 4.18 kJ/(kg·K), then a **5°C** return-to-supply temperature difference corresponds to about **70 kW** of heat transport. At **10°C**, the same flow corresponds to about **139 kW**. These are transparent *illustrations of the energy equation*, not rated ThermalCool 2100SS or CDU capacities.

Real applications may use a water-glycol blend, operate below the maximum flow, have different allowable cold-plate temperatures or rely on a heat exchanger with a nonzero approach temperature. Maximum pump flow is not the same as maximum usable IT cooling. To specify the complete CDU, one needs the server-side temperature budget, coolant chemistry, exchanger performance, pressure drop and facility-side heat-rejection capacity together.

The distinction becomes critical when comparing equipment suppliers: a pump's size and flow tell us about *circulation capability*, whereas a CDU's kW or MW rating describes thermal transfer under **specified boundary conditions**. The two headline numbers cannot be substituted for one another.

## Where the motor heat goes

The 2100SS has an integrated liquid-cooled motor rather than a separate air-cooling fan. Gates states that the arrangement can transfer **up to 95% of the heat generated by the motor** into the working fluid. The denominator is motor-generated heat—not 95% of the pump's 2.1 kW nameplate electrical power, and certainly not 95% of the cooling load.

Moving heat into the liquid can simplify an enclosed CDU where airflow is limited. But energy does not disappear: the loop and downstream heat exchanger must carry away the motor's rejected heat in addition to the IT heat it collects. This makes pump efficiency, motor operating point and thermal accounting relevant to total facility power usage. It also means a pump that is easy to package physically is not automatically low-overhead thermally.

## Redundancy is a system design, not a pump label

Gates describes parallel installation for **N+1** operation. Parallel-capable pumps make redundancy *possible*, but whether it is achieved depends on manifold design and duty sizing. A functional N+1 design must sustain required coolant flow after a duty pump fails, with the remaining pumps meeting the full circuit resistance curve.

Isolation valves, check valves, electrical feed separation, a controller that detects failure, safe sequencing and maintenance access all matter. If a stopped pump permits reverse flow or the common controller becomes the single point of failure, adding one spare pump may not deliver the intended availability. Transient temperatures at cold plates after a trip deserve explicit testing.

CANBUS and MODBUS provide paths for reporting and command, not proof of effortless integration with BMS or DCIM. Integration still needs a register map, alarm semantics, control authority, timeout handling, interoperability testing and a fail-safe mode for lost communications. The stated **50,000-hour life** is a manufacturer's rating, not a field-derived mean time between failures or a guarantee of five-plus years of uninterrupted service.

## An acceptance test for a rack CDU

For a real design review, the most defensible evaluation would request:

- A pump curve at the chosen speed and fluid temperature, with verified flow, head and electrical power at several duty points.
- System pressure loss through cold plates, manifolds, hoses, filters, couplings and exchanger, including fouling and operating tolerances.
- Supply/return temperatures and transferred heat at the CDU's declared IT and facility boundary conditions.
- Measured contribution of pump/motor heat to the coolant and to the total facility heat-rejection requirement.
- A failed-pump and recovered-pump test at full requested thermal load, including cold-plate temperature excursions.
- Controls and telemetry behaviour during network loss, sensor disagreement and maintenance isolation.

Gates' announcement is a useful sign of how rack-level liquid cooling is becoming a specialised component market. The engineering lesson is narrower and more useful: **200 L/min is a pump capability, not a cooling promise.** The quality of the eventual CDU will depend on the complete flow path, its temperature limits and its demonstrated behaviour when one component stops working.

## Sources

- [Gates: ThermalCool 2100SS product announcement, November 12, 2026](https://www.gates.com/us/en/about-us/news.one.122768.html)
- [Gates: ThermalCool 2100SS technical datasheet (PDF)](https://www.gates.com/content/dam/documents-library/flyers/thermalcool-data-centers-pumps-thermalcool-spec-sheet-2100ss-letter-na-en.pdf)
- [ASHRAE Handbook: Data Centers and Telecommunication Facilities](https://handbook.ashrae.org/handbooks/A23/SI/A23_Ch20/a23_ch20_si.aspx)
