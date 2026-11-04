---
title: "When Software Synchronization Makes Power Grids Oscillate Every 60 Seconds"
description: "A Nature Energy study connects one-minute grid-frequency patterns to synchronized control in UPS and battery systems. Its measured propagation is a warning about collective timing."
excerpt: "A routine control timer can create a repeated load pulse. When many devices align, a local software decision becomes visible in the wider electrical system."
pubDate: "2026-11-04"
status: "published"
canonical_id: "2026-11-04-one-minute-grid-synchronization"
tags: ["PowerGrids", "CyberPhysicalSystems", "DataCenters", "ControlEngineering", "TechMindHub"]
source_url: "https://www.nature.com/articles/s41560-026-02144-0"
cover_card: "https://media.techmindhub.cc/posts/one-minute-grid-synchronization-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/one-minute-grid-synchronization-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/one-minute-grid-synchronization-og-web-v1.jpg"
domain: "energy-environment"
topic: "Grid synchronization"
card_alt: "Conceptual UPS and battery cabinets send synchronized load pulses through a substation toward transmission lines."
cover_alt: "Conceptual sequence from clocked control in UPS and batteries to power pulses and a frequency response in the grid."
---

A [study published in *Nature Energy* on October 30, 2026](https://www.nature.com/articles/s41560-026-02144-0) examines a remarkably regular feature of power-system measurements: a frequency disturbance repeating at exactly one minute. The researchers identify a pattern in grid-frequency time series from power systems around the world. They also show, through measurements of digitally controlled equipment, that clock-synchronized actions in uninterruptible power supplies (UPSs) and battery energy storage systems can create periodic demand peaks. In their investigated setting, the signal propagates across voltage levels up to the transmission interface.

The result matters because the initiating action can be routine software behavior. A device controller may check status, change a charging state or perform a recurring operation on a clock boundary. One device has little effect. Many devices doing similar work at the same time can produce a coherent change in demand. The grid responds to the aggregate load, not to each device's benign intention.

## Why a minute is a clue

Grid frequency reflects the balance between electrical supply and demand. It can move for many reasons, including generation changes, load steps and control-system dynamics. A pattern locked to an exact wall-clock interval points toward an externally synchronized process. A free-running mechanical oscillation would not normally keep the same phase with civil time across long periods and disparate systems. That timing clue guided the authors' investigation of digital controllers.

The study distinguishes observation from mechanism. Frequency traces establish the recurring pattern. Equipment and voltage-level measurements show one concrete path from synchronized control to a grid-visible pulse. These observations support the proposed class of cyber-physical synchronization effects. They do not prove that every one-minute pattern everywhere has the same device population or that UPS self-checks alone explain the full contribution in all grids. The paper also discusses battery storage as a relevant digitally controlled system. This is not evidence of an attack.

The authors report that the pattern's amplitude has increased in several grids and discuss wear on hydropower systems and tighter control requirements. Those are system-level concerns, but a single publication does not translate into a universal failure probability for a particular data centre or utility. The practical question is how to identify synchronized load behavior before enough equipment shares the same timing to matter.

## Timing becomes an engineering parameter

Our assessment: periodic operations deserve the same design attention as their electrical magnitude. A controller specification may state the peak current of a test, charging transition or self-check, while omitting when many devices start that operation. In a large fleet, the phase distribution across devices can matter as much as the pulse of any one device.

Consider hundreds of UPS modules commissioned with identical software defaults. If each performs an action at the top of a minute, the demand steps can coincide. A fixed offset for the whole site merely moves the aggregate pulse to another second. A bounded random offset or deliberately distributed schedule can spread the actions, provided the maintenance and safety purpose of each operation still works. That mitigation should be tested for startup, restart and time resynchronization: a fleet can accidentally align again after a common event.

Operators should first measure. Record device-level power, site demand and grid frequency with clocks accurate enough to compare phase. Correlate peaks with controller logs and scheduled jobs, then change one timing policy in a controlled test and observe whether the site pulse changes. Keep other loads and operating states documented. Correlation alone can nominate a suspect; intervention and repeated measurement provide stronger evidence of the mechanism.

The interaction between facilities and utilities also matters. A data centre may have UPS and batteries managed by different vendors, each with its own clock, firmware and maintenance cycle. Procurement and commissioning should document recurring control actions and expose scheduling controls where available. Utilities evaluating a large new load can ask for the time profile of those actions alongside average and peak demand.

As power systems add digitally controlled storage, power electronics and large computing facilities, small timing choices can become collective electrical behavior. The study's useful lesson is specific: the researchers measured a pathway from synchronized controls to a grid-visible one-minute signal. Designing a fleet with intentionally distributed timing and measuring the result is a tractable way to investigate that risk.

## Avoid trading one synchronization problem for another

Randomizing a schedule is not as simple as adding an arbitrary delay to a safety check. Some checks must happen within a maximum interval, and some battery actions may be constrained by charge state or the facility's operating mode. A proposed policy should bound the delay, preserve required protective functions and coordinate with vendor support. It should also distinguish an action that changes power from a software-only status poll; changing a harmless timer will not reduce the electrical pulse.

Measurement has its own traps. A one-minute feature can appear in sampled telemetry because an instrument averages or reports at one-minute boundaries. Compare raw high-resolution electrical measurements with independent clocks before assigning a physical cause. Then examine whether the pulse precedes the frequency response, and whether its amplitude follows the number of active devices. A site-wide rescheduling test should be reversible and should preserve a record of normal load variation and grid conditions.

For a fleet spanning facilities, independent random offsets can reduce coincidence at one site without guaranteeing independence at the regional level. Common firmware defaults, a scheduled update or a synchronized restart could reintroduce alignment. Fleet observability should therefore include the distribution of action times, not merely a pass/fail status for each controller. The paper gives a reason to ask that question; a particular operator still needs evidence from its own equipment and grid connection.

## Source

- [*Nature Energy*: One-minute frequency disturbances](https://www.nature.com/articles/s41560-026-02144-0)
