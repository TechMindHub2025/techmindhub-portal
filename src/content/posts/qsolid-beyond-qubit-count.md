---
title: "QSolid: Scaling Quantum Computers Beyond the Qubit Count"
description: "QSolid's tested 10-qubit system and a 30-qubit system under testing show why packaging, cryogenic control and integration matter alongside processor size."
excerpt: "A larger chip is one milestone. Reliable connections, thermal control and repeatable system operation determine what the assembled machine can do."
pubDate: "2026-10-26"
status: "published"
canonical_id: "2026-10-26-qsolid-beyond-qubit-count"
tags: ["QuantumComputing", "Semiconductors", "AdvancedPackaging", "CryogenicElectronics", "Engineering", "TechMindHub"]
source_url: "https://www.ipms.fraunhofer.de/en/press-media/press/2026/QSolid-quantum-computer.html"
cover_card: "https://media.techmindhub.cc/posts/qsolid-beyond-qubit-count-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/qsolid-beyond-qubit-count-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/qsolid-beyond-qubit-count-og-web-v1.jpg"
domain: "photonics"
topic: "Quantum systems"
card_alt: "A conceptual processor package and adjacent control chip beneath the words Beyond the Qubit Count."
cover_alt: "Conceptual sequence from a quantum processor through interposer and control electronics to an integrated, repeatable machine; 10- and 30-qubit milestones are distinguished."
---

A qubit count describes one part of a quantum computer. The connections and electronics needed to make those qubits controllable are another part, and they become harder to overlook as systems grow. The QSolid consortium's latest report puts that integration work beside the more familiar processor milestone.

In an [October 23, 2026 announcement](https://www.ipms.fraunhofer.de/en/press-media/press/2026/QSolid-quantum-computer.html), Fraunhofer IPMS said QSolid's tested 10-qubit system is accessible to users, while the consortium is still testing a 30-qubit system. These are different stages: access to one tested demonstrator does not make the larger one a finished service. The announcement also describes demonstration applications, including modelling spin resonance processes, to examine hardware and software together. It does not establish a computational advantage over classical methods or a fault-tolerant quantum computer.

## The interface around the chip

Fraunhofer IPMS reports cryogenic characterization of CMOS circuits with GlobalFoundries and advanced packaging work with Fraunhofer IZM-ASSID. Its description says interposers connect the quantum chip and control chip in a compact arrangement. The central engineering tension is signal transmission without adding heat that harms sensitive quantum hardware. The work draws on industrial silicon manufacturing processes, but the announcement does not provide a full set of electrical, thermal or manufacturing-yield measurements for the assembled design.

An interposer is an intermediate structure that makes connections between components. It cannot be evaluated only by the density of those connections. A control path has to preserve the required signal behaviour at the operating temperature and within the heat budget of the device. Packaging changes can alter the route taken by signals and heat, and can affect assembly, testing and repair. Those effects belong to a system-level review rather than an attractive chip photograph.

Our assessment is that quantum scaling is best treated as an integration problem. More qubits increase the number and complexity of control, readout and calibration tasks. A component tested alone may behave differently after it is joined to control electronics, cooling hardware and software. The relevant result is therefore specific to the assembled system and the conditions under which it operated.

## What evidence would help

For an interconnect design, we would want measured signal integrity and thermal loading at the intended operating conditions, alongside repeatability after assembly and repeated cooling cycles. These are proposed evaluation criteria, not test results claimed by Fraunhofer. They help distinguish a promising packaging method from a demonstrated contribution to reliable machine operation.

For a complete demonstrator, ask which components were tested together, how the system was calibrated, and what workload ran through the actual control and software stack. A gate or component result, a processor benchmark and an application run answer different questions. State preparation, measurement, errors and uptime need enough context to compare experiments. Qubit count alone cannot supply that context.

Manufacturing adds another threshold. A laboratory assembly can demonstrate a principle without showing that units can be fabricated repeatedly to a consistent standard. Yield, interchangeability, rework and service access matter if the design is to move beyond a single specimen. Using an established semiconductor process may offer useful tools for repeatability, but it does not establish production readiness by itself.

The report describes a consortium bringing semiconductor processing, cryogenic control, connectors, software and application testing into common demonstrators. Its practical importance will depend on documented system operation as the larger device matures. The 10-qubit and 30-qubit statements should remain separately labelled until evidence supports a different conclusion.

Progress toward reproducible quantum machines will be clearer when results show what was assembled, what was measured, at which conditions and how consistently it worked.

When assessing a quantum-computing milestone, what would you want to know beyond the number of qubits?

## Source

- [Fraunhofer IPMS, QSolid consortium progress, October 23, 2026](https://www.ipms.fraunhofer.de/en/press-media/press/2026/QSolid-quantum-computer.html)
