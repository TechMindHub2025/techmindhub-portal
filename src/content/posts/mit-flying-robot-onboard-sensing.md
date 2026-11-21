---
title: "A Tiny Flying Robot Moves Its Senses Onboard, While Power Stays Offboard"
description: "MIT has integrated sensing and computation into a flapping-wing microrobot, reducing dependence on external motion capture. A tether still supplies energy."
excerpt: "The prototype can close its sensing and control loop onboard; it is not yet an untethered autonomous flyer."
pubDate: "2026-11-21T08:03:00Z"
status: "published"
canonical_id: "2026-11-21-mit-flying-robot-onboard-sensing"
tags: ["Microrobotics", "EmbeddedSystems", "FlightControl", "MIT", "TechMindHub"]
source_url: "https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118"
cover_card: "https://media.techmindhub.cc/posts/mit-flying-robot-onboard-sensing-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/mit-flying-robot-onboard-sensing-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/mit-flying-robot-onboard-sensing-og-web-v1.jpg"
domain: "robotics"
topic: "Onboard flight control"
card_alt: "A small winged robot over a flower carries visible electronics and a power tether."
cover_alt: "A cutaway labels onboard sensors and control electronics separately from the offboard power tether."
---

A flying microrobot that relies on a room full of tracking cameras has a narrow operating envelope outside the laboratory. MIT's [November 18 report](https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118) describes a flapping-wing prototype that carries its own sensing and computation. It can estimate and control its motion without depending on an external motion-capture system for every control update. The robot still receives **power through a tether**.

## The mass and feedback budget

At insect scale, sensors, processor, wiring and actuators compete for a very small mass allowance. The robot uses onboard measurements, including inertial and visual cues, to infer how it moves and to close the flight-control loop. That is a meaningful advance in autonomy because a local estimator can respond to conditions not covered by room-mounted cameras. It also creates familiar embedded-system problems in extreme form: vibration, limited compute, noisy optical flow and tightly coupled control and perception.

Experiments reported by the researchers include trajectory following and landing. These are demonstrations in controlled conditions; they do not establish robust flight in wind, rain, cluttered outdoor environments or rescue operations. The image above separates what is onboard from what remains outside the robot rather than depicting a freely operating field device.

## The remaining energy constraint

A tether changes possible range, maneuvers and deployment. Integrating batteries or another energy source without sacrificing lift and control margin is a separate challenge from moving sensing onboard. A fair comparison with an untethered flyer must state flight duration, mass, payload, environment and what computation happens on the vehicle.

Source: [MIT News, November 18, 2026](https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118).
